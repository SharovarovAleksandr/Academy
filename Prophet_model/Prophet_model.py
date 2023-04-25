# Програма Prophet_model написана на базі моделі лінійної регресії Prophet (https://facebook.github.io/prophet/) для
# прогнозування курсів фінансових інструментів та працює в парі з торговим радником Prophet_Start на торговому терміналі
# МТ5 в режимі скрипта Python. Для її роботи необхідно установити програму в каталог скриптів торгового терміналу МТ5 та
# провести її запуск у середовищі MetaEditor, яке є невід`ємною частиною торгового терміналу МТ5. Після цього програма
# з`явиться у каталозі скриптів торгового терміналу з поміткою скрипт Python.
# Програма працює виключно на таймфреймі D1.
# За основу алгоритма прийнято три гіпотези для побудови прогнозів:
# 1. Модель ideal - коли реальні торгові дані перетворюються в ідеальний календар, який не містить пропусків даних, що
#    обумовлено вихідними та святковими днями, під час яких не проходять торги.
# 2. Модель normal - коли дані для моделі готуються з пустими значеннями, які припадають на вихідні та свята. При цьому
#    можуть враховуватися вихідні дні з розподіленим впливом на п`ятницю та понеділок методом holidays (window), описаним
#    в технічній документації моделі Prophet.
# 3. Модель Transform - яка проводить корегування даних та заповнює пусті значення плавно розподіленими середніми
#    значеннями між точками до свята та після свята.
# В якості додаткових регрессорів всі моделі можуть використовувати:
#   - вихідні дні офіційних свят, прийнятих для NYSE, або модель, коли всі незаповнені дні вважаються вихідними;
#   - використовувати фрактали Вільямса як точки changepoints згідно з документацією моделі Prophet;
#   - брати за основу два регресійних фактори Open-Close (ос) або ATR (atr) та додавати їх до обрахунків.
#  В результаті роботи програма створює файли прогнозів згідно зі стандартами обміну файлами між Prophet_model та Prophet_Start
#  Вхідний файл для програми - це останній (за часом)csv файл, створений у спеціальному середовищі терміналу MT5 в каталозі Files
#  В якості вихідних файлів програма формує кількість файлів у відповідності до кількості прогнозованих показників.
#  обраних у модулі Prophet_Start. Стандарт створення файлів Forecast─high─GBPCAD─2023-04-07.csv.
#  Де high - параметр предикції, може приймати значення (open,high,low,close,ma,atr).
#  GBPCAD - фінансовий інструмент, на якому буде проводитися предикція. Будь-який із доступних в терміналі.
#  2023-04-07 - дата у форматі YYYY-MM-DD, яка відповідає останній даті періоду навчання моделі.
#  З цієї дати буде проводиться предикція.
#
#
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from prophet import Prophet
import os
import holidays
import matplotlib.pyplot as plt
from prophet.plot import add_changepoints_to_plot
import MetaTrader5 as mt5
import warnings
warnings.filterwarnings("ignore")

# Процедура готує дані для моделі Ideal
def ideal(df1, ideal_mark, predict_num,  holiday_method, regression_method, changepoint_method):
    hol_day_method = None    # метод ideal не дозволяє використовувати свята в якості предиктора
    num_date = len(df1)
    ser_regress = pd.Series()    # Змінна, в якій буде створюватися додатковий регресійний фактор
    result = pd.DataFrame(columns=['ds', 'y'], index=pd.RangeIndex(0, num_date))    # результуючий датафрейм
# Цикл змінює реальні дати на ідеальний календар без вихідних та свят
    for ii in range(num_date):
        result['ds'][num_date - 1 - ii] = (df1['ds'][num_date - 1] - timedelta(days=ii))
# Формуємо дані та розраховуємо додатковий регресійний фактор
    if regression_method == "oc":
        result['y'] = df1['regression=oc'][:].values
        ser_regress = model_reg(result, predict_num)
    if regression_method == "atr":
        result['y'] = df1['regression=atr'][:].values
        ser_regress = model_reg(result, predict_num)
#  За необхідності формуємо changepoint_list з фракталів
    if changepoint_method == "fractals":
        result['up_fractal'] = df1['up_fractal'][:].values
        result['down_fractal'] = df1['down_fractal'][:].values
        cng_lst=changepoint(result)
    else:
        cng_lst = None
#  Формуємо стовбчик 'y' для предиції  згідно з документацією моделі  Prophet
    result['y'] = df1[ideal_mark][:].values
    if 'up_fractal' in result.columns:
        result.drop('up_fractal', axis=1, inplace=True)
    if 'down_fractal' in result.columns:
        result.drop('down_fractal', axis=1, inplace=True)
    return result, hol_day_method, ser_regress, cng_lst


# Процедура готує дані для моделі Normal
def normal(df1, normal_mark, predict_num,  holiday_method, regression_method, changepoint_method):
    result = pd.DataFrame(columns=['ds', 'y'])
    result['ds'] = df1['ds']
    ser_regress = pd.Series()
# Формуємо дані та розраховуємо додатковий регресійний фактор
    if regression_method == "oc":
        result['y'] = df1['regression=oc'][:].values
        ser_regress = model_reg(result, predict_num)
    if regression_method == "atr":
        result['y'] = df1['regression=atr'][:].values
        ser_regress = model_reg(result, predict_num)
#  За необхідності формуємо changepoint_list з фракталів
    if changepoint_method == "fractals":
        cng_lst = changepoint(df1)
    else:
        cng_lst = None
#  Формуємо стовбчик 'y' для предиції  згідно документації моделі  Prophet
    result['y'] = df1[normal_mark][:].values
#  За необхідності формуємо фактор свят
    if holiday_method == "country":
        hol_day_method = get_holiday_country(result, predict_num)
    elif holiday_method == "weekend":
        hol_day_method = get_holiday_weekend(result, predict_num, True)
    else:
        hol_day_method = None
    return result, hol_day_method, ser_regress, cng_lst


# Процедура трансформує данні та заповнює пробіли середніми значеннями для моделі Transform
def transform_mark(df1, trans_mk):
    start_tr = df1['ds'][0]           # Дата початку обрахунків
    end_tr = df1['ds'][len(df) - 1]   # Дата кінця обрахунків
    result = pd.DataFrame(columns=['ds', 'y'], index=pd.RangeIndex((end - start).days + 1))
# Генеруємо повний календар дат
    result['ds'] = pd.date_range(start_tr, end_tr, freq='d')
    jj = 0
    kk = 0
    ii = 0
    while ii < len(result):
        if result['ds'][ii] == df1['ds'][jj]:        # Заповнюємо існуючі дати
            result['y'][ii] = df1[trans_mk][jj]
            jj += 1
            ii += 1
        else:       # Заповнюємо не існуючі дати
            kk = (df1['ds'][jj] - df1['ds'][jj - 1]).days - 1  # Кількість вихідних днів
            delta = (df1[trans_mk][jj] - df1[trans_mk][jj - 1]) / (kk + 1)  # Денний приріст ціни у вихідний день
            new = df1[trans_mk][jj - 1]
            for mm in range(0, kk):
                result['y'][ii + mm] = new + delta * (mm + 1)
            ii = ii + kk
    return result


# Процедура готує дані безпосередньо для моделі Transform
def transform(df1, trans_mk, predict_num,  holiday_method, regression_method, changepoint_method):
    ser_regress = pd.Series()
    result = pd.DataFrame()
# Формуємо дані та розраховуємо додатковий регресійний фактор
    if regression_method == "oc":
        result = transform_mark(df1, 'regression=oc')
        ser_regress = model_reg(result, predict_num)
    if regression_method == "atr":
        result = transform_mark(df1, 'regression=atr')
        ser_regress = model_reg(result, predict_num)
#  За необхідности формуємо changepoint_list з фракталів
    if changepoint_method == "fractals":
        cng_lst = changepoint(df1)
    else:
        cng_lst = None
#  Формуємо стовбчик 'y' для предикції  згідно з документацією моделі Prophet
    result = transform_mark(df1, trans_mk)
#  За необхідності формуємо фактор свят
    if holiday_method == "country":
        hol_day_method = get_holiday_country(result, predict_num)
    elif holiday_method == "weekend":
        hol_day_method = get_holiday_weekend(result, predict_num)
    else:
        hol_day_method = None
    return result, hol_day_method, ser_regress, cng_lst


# Процедура готує дані про свята для моделі Transform, Normal
def get_holiday_weekend(df1, predict_n, window=False):
    start_hol = df1['ds'][0]                # Дата початку обрахунків
    end_hol = df1['ds'][len(df1) - 1]       # Дата кінця обрахунків
    end_predict = df1['ds'][len(df1) - 1] + pd.Timedelta(days=predict_n)   # Дата кінця предикції
# Створюємо новий повний календар
    predict_lst = pd.date_range(end_hol, end_predict, freq='d')
    df_hol_day = pd.DataFrame(columns=['ds', 'holiday'])
    df_hol_day['ds'] = pd.date_range(start_hol, end_hol, freq='d')
# Визначаємо співпадіння індексів
    idx = df_hol_day[df_hol_day['ds'].isin(df1['ds'])].index
    df_hol_day.drop(idx, inplace=True)
    df_hol_day.reset_index(drop=True, inplace=True)
    end_index = len(df_hol_day)
# Отримуємо святкові дні за розкладом NYSE
    nyse_holiday = holidays.NYSE(years=[end_hol.year, end_predict.year], observed=True)
# Перевіряємо співпадіння дат зі святами та заповнюємо значення згідно з вимогами моделі Prophet
    for ii in range(1, predict_n + 1):
        if predict_lst[ii].day_of_week == 5 or predict_lst[ii].day_of_week == 6 or predict_lst[ii] in nyse_holiday:
            df_hol_day.loc[end_index] = [predict_lst[ii], 'weekend']
            end_index += 1
    df_hol_day['holiday'] = 'weekend'
# Заповнюємо значення  lower_window та upper_window згідно з вимогами моделі Prophet
    if window:
        df_hol_day['lower_window'] = -1
        df_hol_day['upper_window'] = 1
    return df_hol_day

# Процедура готує дані про робочі дні NYSE для моделі Transform, Normal
def get_holiday_country(df1, predict_n):
    start_hol=df1['ds'][0]
    end_hol=df1['ds'][len(df1)-1]
    year_list = [ii for ii in range(start_hol.year, end_hol.year + 1, 1)]
    nyse_holidays = holidays.NYSE(years=year_list, observed=True)
    df_hol_day = pd.DataFrame(nyse_holidays.items(), columns=['ds', 'holiday'])
    df_hol_day['ds'] = pd.to_datetime(df_hol_day['ds'])
    return df_hol_day

# Процедура здійснює пошук та ліквідацію хибних фракталів, а також готує changepoint list для роботи моделі
def changepoint(df1):
    change_lst = []
    jj = 0
    ii = 0
    while ii <= len(df1) - 1 or jj <= len(df1) - 1:  # цикл проходу по історії фракталів
# Додаємо у лист верхні не хибні фрактали
        if df1['up_fractal'][ii] > 0 and not df1['down_fractal'][ii] > 0:
            temp_lst_up = []  # створюємо тимчасовий лист для збереження up фракталів
            jj = ii
            temp_lst_up.append([ii, df1['up_fractal'][ii]])
            while not df1['down_fractal'][jj] > 0:
                jj += 1
                if jj >= len(df1):
                    break
                if df1['up_fractal'][jj] > 0:
                    temp_lst_up.append([jj, df1['up_fractal'][jj]])
            if jj >= len(df1):
                change_lst.append(df1['ds'][ii])
                break
            if df1['up_fractal'][jj] > 0:
                temp_lst_up.append([jj, df1['up_fractal'][jj]])

            if len(temp_lst_up) == 1:
                change_lst.append(df1['ds'][ii])
                ii += 1
                continue
            else:
                max_up = temp_lst_up[0][1]
                indx = temp_lst_up[0][0]
                for mm in temp_lst_up:
                    if mm[1] > max_up:
                        max_up = mm[1]
                        indx = mm[0]
                for mm in temp_lst_up:
                    if mm[0] != indx:
                        df1.loc[mm[0], 'up_fractal'] = np.NaN

                    else:
                        change_lst.append(df1['ds'][indx])
            ii = jj
            continue
# Додаємо у лист нижні не хибні фрактали
        if df1['down_fractal'][ii] > 0 and not df1['up_fractal'][ii] > 0:
            temp_lst_down = []   # створюємо тимчасовий лист для збереження down фракталів
            jj = ii
            temp_lst_down.append([ii, df1['down_fractal'][ii]])
            while not df1['up_fractal'][jj] > 0:
                jj += 1
                if jj >= len(df1):
                    break
                if df1['down_fractal'][jj] > 0:
                    temp_lst_down.append([jj, df1['down_fractal'][jj]])
            if jj >= len(df1):
                change_lst.append(df1['ds'][ii])
                break
            if df1['down_fractal'][jj] > 0:
                temp_lst_down.append([jj, df1['down_fractal'][jj]])

            if len(temp_lst_down) == 1:
                change_lst.append(df1['ds'][ii])
                ii += 1
                continue
            else:
                min_dn = temp_lst_down[0][1]
                indx = temp_lst_down[0][0]
                for mm in temp_lst_down:
                    if mm[1] < min_dn:
                        min_dn = mm[1]
                        indx = mm[0]
                for mm in temp_lst_down:
                    if mm[0] != indx:
                        df1.loc[mm[0], 'down_fractal'] = np.NaN
                    else:
                        change_lst.append(df1['ds'][indx])
            ii = jj
            continue
#  Заповнюємо датафрейм значеннями фракталів
        if df1['down_fractal'][ii] > 0 and df1['up_fractal'][ii] > 0:
            jj = ii
            while not (df1['down_fractal'][jj + 1] > 0) and not (df1['up_fractal'][jj + 1] > 0):
                jj += 1
                if jj >= len(df1):
                    break
            jj += 1
            if jj >= len(df1):
                change_lst.append(df1['ds'][ii])
                break
            if df1['down_fractal'][jj] > 0 and not df1['up_fractal'][jj] > 0:
                df1.loc[ii, 'down_fractal'] = np.NaN

            if df1['up_fractal'][jj] > 0 and not df1['down_fractal'][jj] > 0:
                df1.loc[ii, 'up_fractal'] = np.NaN

            if df1['down_fractal'][jj] > 0 and df1['up_fractal'][jj] > 0:

                if df1['down_fractal'][ii] < df1['down_fractal'][jj] and df1['up_fractal'][ii] > df1['up_fractal'][jj]:
                    df1.loc[jj, 'down_fractal'] = np.NaN
                    df1.loc[jj, 'up_fractal'] = np.NaN

                if df1['down_fractal'][ii] > df1['down_fractal'][jj] and df1['up_fractal'][ii] < df1['up_fractal'][jj]:
                    df1.loc[ii, 'down_fractal'] = np.NaN
                    df1.loc[ii, 'up_fractal'] = np.NaN

                if df1['down_fractal'][ii] < df1['down_fractal'][jj] and df1['up_fractal'][ii] < df1['up_fractal'][jj]:
                    df1.loc[ii, 'up_fractal'] = np.NaN

                if df1['down_fractal'][ii] > df1['down_fractal'][jj] and df1['up_fractal'][ii] > df1['up_fractal'][jj]:
                    df1.loc[ii, 'down_fractal'] = np.NaN

            continue
        ii += 1
# Приводимо список до вимог моделі Prophet
    change_lst = set(change_lst)
    change_lst = list(change_lst)
    change_lst.sort()
    return change_lst

# Функція видаляє вихідні дні у предикшен періоді для моделі normal
def result_processing(df1, predict_n):
    nn=len(df1)-1
    for ii in range(predict_n):
        if df1['ds'][nn-ii].weekday() == 5 or df1['ds'][nn-ii].weekday() == 6:
            df1=df1.drop(nn-ii)
    df1.reset_index(drop=True, inplace=True)
    return df1

# Функція будує регрессійний фактор на базі моделі
def model_reg(df_reg, predict_num):
    m = Prophet(holidays=None,
               holidays_prior_scale=10,
               changepoint_range=0.95,
               changepoint_prior_scale=0.1,
               yearly_seasonality='auto',
               weekly_seasonality='auto',
               daily_seasonality=0,
               growth='linear',
               n_changepoints=100,
               seasonality_mode='additive',
               seasonality_prior_scale=10,
               mcmc_samples=0,
               interval_width=0.1,
               uncertainty_samples=1000,
               stan_backend=None)

    m.fit(df_reg)
    m_future = m.make_future_dataframe(periods=predict_num)
    m_forecast = m.predict(m_future)
    return m_forecast['yhat']



# Ініціалізуємо бібліотеку mt5
mt5.initialize()

# Знаходимо останній змінений файл
path = 'C:\\Users\\Александр\\AppData\\Roaming\\MetaQuotes\\Terminal\\550A9E6B699B2474CBE17711F34DD758\\MQL5\\Files\\'
files = os.listdir(path)
max_date = os.path.getmtime(path + files[0])
n = 0
for i in range(len(files)):
    if os.path.getmtime(path + files[i]) > max_date:
        max_date = os.path.getmtime(path + files[i])
        n = i
# Отримуємо ім'я фінансового інструмента
ticker = files[n][4:10]

# Читаємо файл
df = pd.read_csv(path + files[n], delimiter=';')

# Перетворюємо дати у формат datetime
df['ds'] = pd.to_datetime(df['ds'])

# Визначаємо точку старту обрахунків
start = df['ds'][0]

# Визначаємо точку кінця обрахунків
end = df['ds'][len(df) - 1]

print("Prophet_model start calculation on file ", files[n], "  Instrument : ", ticker, "  Period : ", start.strftime("%Y-%m-%d"), "-", end.strftime("%Y-%m-%d"))

# Із заголовка файлу отримуємо інформацію стосовно методів та параметрів моделі
columns = df.columns
mark = []
holiday_method = "None"
regression_method = "None"
changepoint_method = "None"
predict_num = int(columns[-1].split("=")[1])
method = columns[-2].split("=")[1]
for i in columns:
    if len(i.split("=")) > 1:
        if i.split("=")[0] == "holidays":
            holiday_method = i.split("=")[1]
        if i.split("=")[0] == "regression":
            regression_method = i.split("=")[1]
        if i.split("=")[0] == "changepoint":
            changepoint_method = i.split("=")[1]
        if i.split("=")[0] == "ma":
            ma_num = int(i.split("=")[1])
            mark.append(i.split("=")[0])
            df = df.rename(columns={i: 'ma'})
    if i == "up_fractal":
        changepoint_method = "fractals"
    if i == 'open':
        mark.append(i)
    if i == 'high':
        mark.append(i)
    if i == 'low':
        mark.append(i)
    if i == 'close':
        mark.append(i)
    if i == 'atr':
        mark.append(i)

# Формуємо необхідні параметри моделі
hol_prior_scale=10
n_changepoint=25
chang_range=0.95
chang_prior_scale=0.05
year_seasonality='auto'
week_seasonality='auto'
day_seasonality=0
growth_ln='linear'
season_mode='additive'
season_prior_scale=10
mcmc=0
interval=0.05
samples=1000
stan=None
hol_day_method = None
changepoint_lst = None

# Відкриваємо файл журналу
file_jr = open('C:\\Users\\Александр\\AppData\\Roaming\\MetaQuotes\\Terminal\\550A9E6B699B2474CBE17711F34DD758\\MQL5\\Files\\prophet_journal.csv', 'a')

# Починаємо розрахунки за кожною змінною та результати кожного передбачення зберігаємо у файл 
df_rab = pd.DataFrame()
series_regress = pd.Series()

for i in mark:
# Відпрацьовуємо метод Ideal
    if method == "ideal":
        df_rab, hol_day_method, series_regress, changepoint_lst = ideal(df, i, predict_num,  holiday_method, regression_method, changepoint_method)
        if regression_method == "oc" or regression_method == "atr":
            df_rab['regress'] = series_regress
# Відпрацьовуэмо метод Normal
    if method == "normal":
        df_rab, hol_day_method, series_regress, changepoint_lst = normal(df, i, predict_num,  holiday_method, regression_method, changepoint_method)
        if regression_method == "oc" or regression_method == "atr":
            df_rab['regress'] = series_regress
# Відпрацьовуэмо метод Transform
    if method == "transform":
        df_rab, hol_day_method, series_regress, changepoint_lst = transform(df, i, predict_num,  holiday_method, regression_method, changepoint_method)
        if regression_method == "oc" or regression_method == "atr":
            df_rab['regress'] = series_regress
         
# Запускаємо модель на розрахунок
    model = Prophet(holidays=hol_day_method,
                    holidays_prior_scale=hol_prior_scale,
                    changepoints=changepoint_lst,
                    n_changepoints=n_changepoint,
                    changepoint_range=chang_range,
                    changepoint_prior_scale=chang_prior_scale,
                    yearly_seasonality=year_seasonality,
                    weekly_seasonality=week_seasonality,
                    daily_seasonality=day_seasonality,
                    growth=growth_ln,
                    seasonality_mode=season_mode,
                    seasonality_prior_scale=season_prior_scale,
                    mcmc_samples=mcmc,
                    interval_width=interval,
                    uncertainty_samples=samples,
                    stan_backend=stan)

# За необхідності додаємо до моделі регресійний фактор
    if regression_method == "oc" or regression_method == "atr":
        model.add_regressor('regress')
# Навчання моделі
    model.fit(df_rab)
# Підготовка даних майбутніх періодів
    future_new = model.make_future_dataframe(periods=predict_num)
# При застосуванні регресійних факторів додаємо регресійні фактори майбутніх періодів
    if regression_method == "oc" or regression_method == "atr":
        future_new['regress'] = series_regress
# Робимо передбачення
    forecast_new = model.predict(future_new)
    
# Зберігаємо файл з даними передбачення
    file_forecast = "Forecast─" + i + "─" + ticker + "─" + end.strftime("%Y─%m─%d")+".csv"
    forecast_new.rename(columns={'yhat': i}, inplace=True)
    forecast_new[['ds', i, 'yhat_lower', 'yhat_upper']].to_csv('C:\\Users\\Александр\\AppData\\Roaming\\MetaQuotes\\Terminal\\550A9E6B699B2474CBE17711F34DD758\\MQL5\\Files\\' + file_forecast)   

# Зберігаємо дані роботи в журнал. Для цього необхідно обрахувати МАЕ
# Перевіряємо, чи є необхідність в обрахунку МАЕ 
    mae = None
    if end+timedelta(days=predict_num+1) < datetime.today():
     # Визначаємо періоди обрахунку МАЕ   
        first_day_predict = end+timedelta(days=1)
        end_day_predict = end+timedelta(days=predict_num)
        calc_day=first_day_predict
        num_weekend=0
     # Додаємо вихідні дні у період розрахунку
        while calc_day < end+timedelta(days=predict_num+1):
            if calc_day.weekday() == 5:
                num_weekend +=2
            calc_day = calc_day + timedelta(days=1)
        end_day_predict += timedelta(days=num_weekend)
        
     # Завантажуємо дані з терміналу
        mae_period = pd.DataFrame(mt5.copy_rates_from(ticker, mt5.TIMEFRAME_D1, end_day_predict, predict_num))
        mae_period['time']=pd.to_datetime(mae_period['time'], unit='s')
        mae_period['atr']=mae_period['high']-mae_period['low']
        
     # Вираховуємо МАЕ  
        if i != "ma":
            mae=0
            for q in range(predict_num):
                mae += abs(mae_period[i][q] - forecast_new[i][len(forecast_new)-predict_num+q])
            mae=mae/predict_num                
                
# Готуємо дані для запису в журнал
    journal_str=str(mae)+";"+start.strftime('%Y-%m-%d')+";"+end.strftime('%Y-%m-%d')+";"+i+";"+method+";"+str(predict_num)+";"
    journal_str+=str(changepoint_method)+";"+str(holiday_method)+";"+str(regression_method)+";"+str(chang_range)+";"
    journal_str+=str(chang_prior_scale)+";"+str(hol_prior_scale)+";"+str(year_seasonality)+";"+str(week_seasonality)+";"
    journal_str+=str(day_seasonality)+";"+str(growth_ln)+";"+str(n_changepoint)+";"+str(season_mode)+";"
    journal_str+=str(season_prior_scale)+";"+str(mcmc)+";"+str(interval)+";"+str(samples)+";"+str(stan)+"\n"
   
# Записуємо строку в журнал
    file_jr.write(journal_str)
    
# Завершення роботи скрипта
# Закриваємо журнал
file_jr.close()
# Розриваємо зв`язок із терміналом
mt5.shutdown()
print("Prophet_model completed successfully!")  
    
# Цей розділ закоментованого коду є виключно технічним та слугує для вивчення поведінки моделі
# Корекція методу  normal – це службовий модуль, викликаний тим, що модель Prophet видає неадекватно великий викид даних
# при предикції моделі normal у вихідні дні, особливо на короткому проміжку навчання.
            # Для методу normal викидаємо з виборки передбачення вихідні дні
            #    print(forecast_new)
            #    if method == "normal":
            #        forecast_new = result_processing(forecast_new, predict_num)
            #        print(forecast_new)
               # Залишаємо технічну можливість при необхідності візуалізувати вплив гіперпараметрів моделі   
            #    fig = model.plot(forecast_new) 
            #    from prophet.plot import add_changepoints_to_plot
            #    a = add_changepoints_to_plot(fig.gca(), model_regres, forecast_new)       
            #    fig.show()
            #    plt.show()
                    
            # Зберігаємо повний файл для аналізу з даними передбачення
            #    file_forecast = "Forecast─" + i + "─" + ticker + "─" + end.strftime("%Y─%m─%d") + "-full.csv"
            #    forecast_new.to_csv('C:\\Users\\Александр\\AppData\\Roaming\\MetaQuotes\\Terminal\\550A9E6B699B2474CBE17711F34DD758\\MQL5\\Files\\' + file_forecast)
   

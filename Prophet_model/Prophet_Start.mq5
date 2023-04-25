//+------------------------------------------------------------------+
//|                                                        Test3.mq5 |
//|                                  Copyright 2023, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+

#property copyright "Copyright 2023"
#property link      "https://facebook.github.io/prophet/"
#property version   "1.00"
#property description "Model-Prophet used Facebook Prophet metod for building chart of prediction price instrument. Author - Sharovarov Aleksandr sharovarovaleksandr@gmail.com"

// Формуємо заголовок для введення даних та визначення методу розрахунку
#property script_show_inputs
enum marks
  {
   sd0=0,  // None
   sd1=1,  // Open
   sd2=2,  // High
   sd3=3,  // Low
   sd4=4,  // Close
   sd5=5,  // MA
   sd6=6,  // ATR
  };
enum metod
  {
   md0=0,   // Ideal
   md1=1,   // Normal
   md2=2,   // Transform
  };
enum regres
  {
   rg0=0,   // None
   rg1=1,   // Open-Close
   rg2=2,   // ATR
  };
enum chang
  {
   ch0=0,   // Auto
   ch1=1,   // Fractals_method
  };
enum holi
  {
   hd0=0,   // None
   hd1=1,   // Country_Holidays
   hd2=2,   // Weekends=Holidays
  };
// Ввод констант заголовку
input string   Start_Date_YYYY─MM─DD = "Last_History_Day";
input string   End_Date_YYYY─MM─DD = "2023-04-20";
input int      Pridiction_Period = 5;
input metod    Metod_Processing_Data = md2;
input regres   Regression_Metod=rg0;
input chang    Changepoint_Metod=ch0;
input holi     Holiday_Metod=hd0;
input marks    Prediction_Mark_1 = sd2;
input marks    Prediction_Mark_2 = sd3;
input marks    Prediction_Mark_3 = sd0;


//Блок оголошення змінних
datetime Start, End, tim, testdata, testdata_new, load_time[20000]; //Виходимо з гіпотези що кількість барів в історії не перевищує 20000 (75 років)
bool Calc_MAE, Change_Prophet, Today, files_ready, graph_ready;
string filename, name, first_str, next_str, Start_Date_YYYY─MM─DD1,End_Date_YYYY─MM─DD1, File_forecast_name, mk[3], rab_str, str_result[5];
int i, j, k, l, num_bar, num_mk, m, n1, fil, IMA1, IFRAC1, IATR1, bar_shift, result_shift, ima_day, last_bar;
double open, high, low, close, up_fractal[], down_fractal[], ma[], atr[], regres_oc, regers_atr, load_data[3][3][20000], MAE, XMAE;
string mark_array[6]= {"open","high","low","close","ma","atr"};
string obj_name, name_graph[3], obj_name_ma;

MqlDateTime strt, ennd, loc_time, bar_time;
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
   Print("Prophet starts to work. Your Starts day - ", Start_Date_YYYY─MM─DD,"  End day - ",End_Date_YYYY─MM─DD);

   Change_Prophet=false; // Змінна буде визначати чи потрібна корекція графіка якщо End_Day=Weekend, Holiday
   Today=false;          // Змінна визначає день в якій проходять розрахунки
   files_ready=true;     // Змінна яка перевіряє чи існують файли з даними
   graph_ready=true;     // Змінна яка перевіряє чи побудовані вже графіки
   TimeLocal(loc_time);  // Зчитуємо час сервера
   Calc_MAE=true;        // Змінна буде визначати це тестовий розрахунок чи реальний прогноз (розраховувати MAE чи ні)
   name = Symbol();      // Визначаемо символ на якому будемо проводити розрахунок

// Перевіримо відповідність графіків таймфрейму
   if(PERIOD_D1 != Period())
     {
      Print("Script works only D1 timeframe. Please try again!");
      PlaySound("alert2");
      ExpertRemove();
     }

// Перетворюємо дати у формат datetime та аналізуємо їх на можkиві помилки
   if(Start_Date_YYYY─MM─DD == "Last_History_Day")
     {
      Start=iTime(name,PERIOD_CURRENT,Bars(Symbol(),PERIOD_CURRENT)-1);
     }
   else
     {
      Start=StringToTime(Start_Date_YYYY─MM─DD);
     }
   if(End_Date_YYYY─MM─DD == "Current_Day")
     {
      End=TimeCurrent();
      Calc_MAE=false;
      Today=true;
     }
   else
     {
      End=StringToTime(End_Date_YYYY─MM─DD);
      if(End == iTime(name,PERIOD_CURRENT,0))
        {
         End=TimeCurrent();
         Calc_MAE=false;
         Today=true;
        }
     }

// Перевірка введених дат на послідовніть
   if(Start >= End)
     {
      Print("Error rise the End_Date<=Start_Date");
      PlaySound("alert2");
      ExpertRemove();
     }

// Перевірка Start_Date на відповідність історії
   if(Start < iTime(name,PERIOD_CURRENT,Bars(Symbol(),PERIOD_CURRENT)-1))
     {
      Start=iTime(name,PERIOD_CURRENT,Bars(Symbol(),PERIOD_CURRENT)-1);
      Print(" The Start_Date is less then last history day and will be changed at ", Start);
     }
// Перевірка та корегування Start_Date на відповідність робочим дням
   n1=Bars(Symbol(),PERIOD_CURRENT,Start,TimeCurrent())-1;
   testdata=iTime(Symbol(),PERIOD_CURRENT,n1);
   if(Start != testdata)
     {
      Start=testdata;
      Print("Your Start_Date falls on a Weekend or Holiday and will be changed to ",Start);
     }

// Перевірка та корегування End_Date на відповідність останньому дню історії графіка
   if(End > TimeCurrent())
     {
      End=TimeCurrent();
      Calc_MAE=false;
      Today=true;
      Print("Your End_Date is later or equal than today's date end will be changed at ", End);
     }

// 6 та 0 - службові константи структури day_of_week - Субота та Неділя відповідно
   if(loc_time.day_of_week == 6 || loc_time.day_of_week == 0 || (loc_time.day_of_week == 1 && Today))
     {
      result_shift=2;
      Change_Prophet=true;
     }

// Перевірка чи випадає End_Date на вихідні та корекція дати
   if(!Today)
     {
      n1=Bars(Symbol(),PERIOD_D1,End,TimeCurrent())-1;
      testdata=iTime(Symbol(),PERIOD_D1,n1);
      TimeToStruct(testdata,strt);
      if(strt.day_of_week==5)
        {
         result_shift=2;
         Change_Prophet=true;
        }
      if(End != testdata)
        {
         Change_Prophet=true;
         n1=Bars(Symbol(),PERIOD_D1,End,TimeCurrent());
         testdata_new=iTime(Symbol(),PERIOD_D1,n1);
         TimeToStruct(testdata_new,ennd);
         result_shift=strt.day-ennd.day-1;
         End=testdata_new;
         Print("Your End_Date falls on a Weekend or Holiday and will be changed to ",End);
         Print("Don't worry, we remember this and will fix the results!");
        }
     }

// Визначаємо необхідність розрахунку MAE
   if(Bars(Symbol(),PERIOD_D1,End,TimeCurrent())-1<Pridiction_Period)
     {
      Calc_MAE=false;
     }

// Визначаємо наявну кількість барів в історії
   num_bar = Bars(Symbol(),PERIOD_CURRENT,Start,End)-1;

// Визначаємо номер бара який приходиться на точку Start
   bar_shift=iBarShift(Symbol(),PERIOD_CURRENT,Start);


// Відкриваємо файл у форматі csv для формування вихідних даних
   filename="Prop"+name+TimeToString(TimeCurrent(),TIME_DATE)+".csv";
   fil=FileOpen(filename, FILE_WRITE|FILE_CSV|FILE_ANSI);

// Перевіряємо чи визначені параметри для роботи радника
   if(Prediction_Mark_1 == sd0 && Prediction_Mark_2 == sd0 && Prediction_Mark_3 == sd0)
     {
      Print("No <Prediction_Mark> parameter  defined for the script operation. Please try again!");
      PlaySound("alert2");
      ExpertRemove();
     }

// Перевіряємо чи не задвоюються параметри
   if(((Prediction_Mark_1 == Prediction_Mark_2) && Prediction_Mark_1 != sd0) ||
      ((Prediction_Mark_1 == Prediction_Mark_3) && Prediction_Mark_1 != sd0) ||
      ((Prediction_Mark_2 == Prediction_Mark_3) && Prediction_Mark_2 != sd0))
     {
      Print("Parameters <Prediction_Mark> are match. Please try again!");
      PlaySound("alert2");
      ExpertRemove();
     }

// Перевіримо необхідність створення хендлів для індикаторів та завантажемо необхідні дані індикатору МА
   if(Prediction_Mark_1 == sd5  || Prediction_Mark_2 == sd5 ||Prediction_Mark_3 == sd5)
     {
      ima_day=5;  // змінна визначає період створення МА прийнята з розрахунку 5-денної робочої неділі
      IMA1=iMA(name,PERIOD_CURRENT,ima_day,0,MODE_LWMA,PRICE_WEIGHTED);
      ArraySetAsSeries(ma,false); // ma массив для зберігання значень MA
      if(CopyBuffer(IMA1,0,Start,End,ma) < 0)
        {
         Print("CopyBuffer IMA1 error =",GetLastError());
        }

      //  Якщо ми запросили МА за період який передує Start date то перші  ima_day елементів масиву ma будуть заповнені числами 1.0Е+378
      //  У такомі випадку видати попередження, запросити переініціалізувати радника з правильною  Start date
      for(i=0; i<=ima_day; i++)
        {
         if(ma[i]>100000000)  // виходимо із гіпотези що реально не існує інструменту із ціною більше 100000000$
           {
            Print("We use the MA=",ima_day,"(day) parameter.");
            Print("The Start date must differ by at least ",ima_day," days from the last date in the history.");
            Print("Please change the Start date and try again.");
            PlaySound("alert2");
            ExpertRemove();
           }
        }

     }

// Перевіримо необхідність завантаження та завантажемо значення  up_fracta, down_fractal з графіка
   if(Changepoint_Metod == ch1)
     {
      IFRAC1=iFractals(name,PERIOD_CURRENT);
      ArraySetAsSeries(up_fractal,false);
      ArraySetAsSeries(down_fractal,false);
      if(CopyBuffer(IFRAC1,0,Start,End,up_fractal) < 0)
        {
         Print("CopyBuffer IFRAC1 error =",GetLastError());
        }
      if(CopyBuffer(IFRAC1,1,Start,End,down_fractal) < 0)
        {
         Print("CopyBuffer IFRAC2 error =",GetLastError());
        }
     }

// Перевіримо необхідність створення хендлів для індикаторів та завантажемо необхідні дані індикатору ATR
   if(Regression_Metod == rg2 || Prediction_Mark_1 == sd6 || Prediction_Mark_2 == sd6|| Prediction_Mark_3 == sd6)
     {
      IATR1=iATR(name,PERIOD_CURRENT,1);
      ArraySetAsSeries(atr,false);
      if(CopyBuffer(IATR1,0,Start,End,atr) < 0)
        {
         Print("CopyBuffer ATR1 error =",GetLastError());
        }
     }

// Формуємо заголовок датафрейму у якості строки first_str, для цього додаємо до строки ті колонки які війдуть у вихідний файл даних
// Колонки майбутнього датафрейму будуть мати назви відповідно до доданих текстових значень
   first_str="ds;";
   switch(Prediction_Mark_1)
     {
      case sd0:
         break;
      case sd1:
         first_str=first_str+mark_array[0]+";";
         break;
      case sd2:
         first_str=first_str+mark_array[1]+";";
         break;
      case sd3:
         first_str=first_str+mark_array[2]+";";
         break;
      case sd4:
         first_str=first_str+mark_array[3]+";";
         break;
      case sd5:
         first_str=first_str+mark_array[4]+"="+IntegerToString(ima_day)+";";
         break; // До назви колонки МА додається період створення ima_day
      case sd6:
         first_str=first_str+mark_array[5]+";";
         break;
     }

   switch(Prediction_Mark_2)
     {
      case sd0:
         break;
      case sd1:
         first_str=first_str+mark_array[0]+";";
         break;
      case sd2:
         first_str=first_str+mark_array[1]+";";
         break;
      case sd3:
         first_str=first_str+mark_array[2]+";";
         break;
      case sd4:
         first_str=first_str+mark_array[3]+";";
         break;
      case sd5:
         first_str=first_str+mark_array[4]+"="+IntegerToString(ima_day)+";";
         break;
      case sd6:
         first_str=first_str+mark_array[5]+";";
         break;
     }

   switch(Prediction_Mark_3)
     {
      case sd0:
         break;
      case sd1:
         first_str=first_str+mark_array[0]+";";
         break;
      case sd2:
         first_str=first_str+mark_array[1]+";";
         break;
      case sd3:
         first_str=first_str+mark_array[2]+";";
         break;
      case sd4:
         first_str=first_str+mark_array[3]+";";
         break;
      case sd5:
         first_str=first_str+mark_array[4]+"="+IntegerToString(ima_day)+";";
         break;
      case sd6:
         first_str=first_str+mark_array[5]+";";
         break;
     }

   switch(Changepoint_Metod)
     {
      case ch0:
         break;
      case ch1:
         first_str=first_str+"up_fractal;down_fractal;";
         break;
     }
   switch(Regression_Metod)
     {
      case rg0:
         break;
      case rg1:
         first_str=first_str+"regression=oc;";
         break;
      case rg2:
         first_str=first_str+"regression=atr;";
         break;
     }
   switch(Holiday_Metod)
     {
      case hd0:
         break;
      case hd1:
         first_str=first_str+"holidays=country;";
         break;
      case hd2:
         first_str=first_str+"holidays=weekend;";
         break;
     }
   switch(Metod_Processing_Data)
     {
      case md0:
         first_str=first_str+"metod=ideal;";
         break;
      case md1:
         first_str=first_str+"metod=normal;";
         break;
      case md2:
         first_str=first_str+"metod=transform;";
         break;
     }
   first_str=first_str+"pred="+IntegerToString(Pridiction_Period,3,' ');

// записуємо першу строку датафрейму
   FileWrite(fil,first_str);

// У випадку якщо сьогодні торговий день проведемо корегування кількості барів в історіі
   if(Today)
      num_bar=num_bar-1;

// Запускаємо цикл який построчно буде формувати данні у змінній next_str та записувати цю строку у файл датафрейму
   for(j=0; j<=num_bar; j++)
     {
      i = bar_shift-j;
      next_str=TimeToString(iTime(name,PERIOD_CURRENT,i),TIME_DATE)+";";
      switch(Prediction_Mark_1)
        {
         case sd0:
            break;
         case sd1:
            next_str=next_str+DoubleToString(iOpen(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd2:
            next_str=next_str+DoubleToString(iHigh(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd3:
            next_str=next_str+DoubleToString(iLow(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd4:
            next_str=next_str+DoubleToString(iClose(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd5:
            next_str=next_str+DoubleToString(ma[j],5)+";";
            break; // 5 - кількість знаків після коми
         case sd6:
            next_str=next_str+DoubleToString(atr[j],5)+";";
            break;
        }

      switch(Prediction_Mark_2)
        {
         case sd0:
            break;
         case sd1:
            next_str=next_str+DoubleToString(iOpen(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd2:
            next_str=next_str+DoubleToString(iHigh(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd3:
            next_str=next_str+DoubleToString(iLow(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd4:
            next_str=next_str+DoubleToString(iClose(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd5:
            next_str=next_str+DoubleToString(ma[j],5)+";";
            break;
         case sd6:
            next_str=next_str+DoubleToString(atr[j],5)+";";
            break;
        }

      switch(Prediction_Mark_3)
        {
         case sd0:
            break;
         case sd1:
            next_str=next_str+DoubleToString(iOpen(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd2:
            next_str=next_str+DoubleToString(iHigh(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd3:
            next_str=next_str+DoubleToString(iLow(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd4:
            next_str=next_str+DoubleToString(iClose(name,PERIOD_CURRENT,i),5)+";";
            break;
         case sd5:
            next_str=next_str+DoubleToString(ma[j],5)+";";
            break;
         case sd6:
            next_str=next_str+DoubleToString(atr[j],5)+";";
            break;
        }

      switch(Changepoint_Metod)
        {
         case ch0:
            break; // виходимо із гіпотези що реально не існує інструменту із ціною більше 10000000$
         case ch1:
           {
            if(up_fractal[j]<10000000 && down_fractal[j]>10000000)
              {
               next_str=next_str+DoubleToString(up_fractal[j],5)+";;";
              }
            if(up_fractal[j]>10000000 && down_fractal[j]<10000000)
              {
               next_str=next_str+";"+DoubleToString(down_fractal[j],5)+";";
              }
            if(up_fractal[j]<10000000 && down_fractal[j]<10000000)
              {
               next_str=next_str+DoubleToString(up_fractal[j],5)+";"+DoubleToString(down_fractal[j],5)+";";
              }
            if(up_fractal[j]>10000000 && down_fractal[j]>10000000)
              {
               next_str=next_str+";;";
              }
            break;
           }
        }
      switch(Regression_Metod)
        {
         case rg0:
            break;
         case rg1:
            next_str=next_str+DoubleToString(iOpen(name,PERIOD_CURRENT,i)-iClose(name,PERIOD_CURRENT,i),5)+";";
            break;
         case rg2:
            next_str=next_str+DoubleToString(atr[j],5)+";";
            break;
        }
      switch(Holiday_Metod)
        {
         case hd0:
            break;
         case hd1:
            next_str=next_str+";";
            break;
         case hd2:
            next_str=next_str+";";
            break;
        }

      FileWrite(fil,next_str);     // Записуємо строку у файл
     }

// Закриваємо сформованиий файл
   FileClose(fil);

// Виводимо в журнал радника повідомлення про те що файл із даними сформовано
   Print("The program has generated a data file ",filename);
   Print("Now you need to run the script Prophet_model.");

// З метою уникнення конфліктів якщо Prediction_Mark=atr та regression=atr проведемо коригування строки яка формувала заголовок датафрейму
// Аналогічно для normal та ma
   StringReplace(first_str,"regression=atr","regression");
   StringReplace(first_str,"normal","norm");

//  Формуємо назви файлів у яких будуть перевірятися передбачення для цього створемо масив mk у якому зберігаються реальні стовбчики датафрейму
   num_mk=0;  // Кількість елементів масиву mk
   for(i=0; i<6; i++)
     {
      if(StringFind(first_str,mark_array[i])>0)
        {
         mk[num_mk]=mark_array[i];
         num_mk++;
        }
     };

// Перетворимо дату End у структуру для отримання компонент дати
   TimeToStruct(End,ennd);

// Перетворюємо масив з назвами стовбчиків по яких було проведено передбачення у массив із назвами відповідних файлів які сформував Prophet_model
   for(i=0; i<num_mk; i++)
     {
      mk[i]="Forecast"+"─"+mk[i]+"─"+name+"─"+StringFormat("%04d",ennd.year)+"-"+StringFormat("%02d",ennd.mon)+"-"+StringFormat("%02d",ennd.day)+".csv";
     }

// Зупиняємо процес виконання програми до того моменту поки  Prophet_model не сформує файли прогнозів для їх подальшої відмальовки
// Перевіряємо чи всі файли створені, якщо ні чекаємо  1000 мілісекунд та повторюємо процес
   while(true)
     {
      j=0;
      for(i=0; i<num_mk; i++)
        {
         if(FileIsExist(mk[i],0))
            j++;
        }
      Sleep(1000);
      if(j==num_mk)
         break;
     };

//  Формуємо сповіщення що файли передбачення створені
   Print("Prediction files are ready. Now create charts.");

// Починаємо відмальовувати графіки по кожному Prediction_Mark
   for(i=0; i<num_mk; i++)   // i<num_mk; поменять
     {
      // Відкриваємо відповідний файл
      fil=FileOpen(mk[i],FILE_READ|FILE_CSV|FILE_ANSI);

      // Зчитуємо першу строчку файлу в якій міститься інформація про назву Prediction_Mark та МАЕ
      rab_str=FileReadString(fil);

      // Розділяємо строку на масив
      StringSplit(rab_str,StringGetCharacter(",",0),str_result);

      // Змінна назви графіку
      name_graph[i]=str_result[2];

      // Завантажуємо данні з файлу та приводимо іх до відповідного формату закриваємо файл
      k=0;
      while(!FileIsEnding(fil))
        {
         rab_str=FileReadString(fil);
         StringSplit(rab_str,StringGetCharacter(",",0),str_result);
         load_time[k]=StringToTime(str_result[1]);
         load_data[i][0][k]=StringToDouble(str_result[2]);
         load_data[i][1][k]=StringToDouble(str_result[3]);
         load_data[i][2][k]=StringToDouble(str_result[4]);
         k++;
        }
      FileClose(fil);

      // В змінній k знаходиться кількість точок для малювання
      // Проведемо корекцію дат у відповідності до прогнозу, якщо прогноз випадає на субботу чи неділю просто зміщуємо прогнозні данні на 2 дні

      for(m=k-Pridiction_Period-1; m<k; m++)
        {
         TimeToStruct(load_time[m],ennd);
         if(ennd.day_of_week == 5)
           {
            for(l=m+1; l<k; l++)
              {
               TimeToStruct(load_time[l],bar_time);
               bar_time.day+=2;
               load_time[l]=StructToTime(bar_time);
              }
           }
        }

     }
// Встановлюємо час реакції таймера 1с.
   EventSetTimer(1);

   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
//|                                                                  |
//+------------------------------------------------------------------+
void OnTimer()
  {
// Визначаємо номер бара який попадає на точку End
   bar_shift=iBarShift(Symbol(),PERIOD_CURRENT,End);

// Створюємо ім'я для графічного об'єкту МАЕ
   obj_name_ma="MAE:\n";

// Починаємо створювати графічні об'єкти по кожній компоненті
   for(i=0; i<num_mk; i++)   // i<num_mk; поменять
     {
      // При необхідності обраховуємо значення МАЕ
      if(Calc_MAE)
        {
         //Отримаємо значення MA на період предикції
         if(name_graph[i]=="ma")
           {
            if(CopyBuffer(IMA1,0,End,load_time[k-1],ma) < 0)
              {
               Print("CopyBuffer IMA1 error =",GetLastError());
              }
           }
         MAE=0;
         l=0;
         // Проводимо обрахунок МАЕ по кожному параметру окремо
         for(m=k-Pridiction_Period; m<k; m++)
           {
            if(name_graph[i]=="open")
               MAE=MAE+MathAbs(iOpen(name,PERIOD_CURRENT,bar_shift-l-1)-load_data[i][0][m]);
            if(name_graph[i]=="high")
               MAE=MAE+MathAbs(iHigh(name,PERIOD_CURRENT,bar_shift-l-1)-load_data[i][0][m]);
            if(name_graph[i]=="low")
               MAE=MAE+MathAbs(iLow(name,PERIOD_CURRENT,bar_shift-l-1)-load_data[i][0][m]);
            if(name_graph[i]=="close")
               MAE=MAE+MathAbs(iClose(name,PERIOD_CURRENT,bar_shift-l-1)-load_data[i][0][m]);
            if(name_graph[i]=="ma")
               MAE=MAE+MathAbs(ma[l+1]-load_data[i][0][m]);
            if(name_graph[i]=="atr")
               MAE=MAE+MathAbs((iHigh(name,PERIOD_CURRENT,bar_shift-l-1)-iLow(name,PERIOD_CURRENT,bar_shift-l-1))-load_data[i][0][m]);
            l++;
           }
         // Перераховуємо значення МАЕ у пункти та вираховуємо середнє значення
         MAE=MAE*pow(10,Digits())/Pridiction_Period;

         // Готуємо ім'я графічного об'єкту МАЕ для виводу
         obj_name_ma+=name_graph[i]+" : "+DoubleToString(MAE,0)+" \n";
        }

      // Створюємо графік у основному вікні терміналу
      for(m=0; m<k-1; m++)
        {
         if(name_graph[i]=="atr")
           {
            // Запускаємо нове вікно індикатора ATR
            ChartIndicatorAdd(0,1,IATR1);
            // Створюємо ім'я графічного об'єкту
            obj_name="ATR-"+TimeToString(load_time[m],TIME_DATE)+" "+DoubleToString(load_data[i][0][m],5)+"  ↑"+DoubleToString(load_data[i][2][m],5)+" ↓"+ DoubleToString(load_data[i][1][m],5);
            // Малюємо об'єкт
            if(!ObjectCreate(0,obj_name,OBJ_TREND,1,load_time[m],load_data[i][0][m],load_time[m+1],load_data[i][0][m+1]))
              {
               Print("Error creation object : ", obj_name, " code #",GetLastError());
              }
           }
         else
           {
            // Створюємо ім'я графічного об'єкту основного графіку
            obj_name=name_graph[i]+"-"+TimeToString(load_time[m],TIME_DATE)+" "+DoubleToString(load_data[i][0][m],5)+"  ↑"+DoubleToString(load_data[i][2][m],5)+" ↓"+ DoubleToString(load_data[i][1][m],5);
            // Малюємо об'єкт
            if(!ObjectCreate(0,obj_name,OBJ_TREND,0,load_time[m],load_data[i][0][m],load_time[m+1],load_data[i][0][m+1]))
              {
               Print("Error creation object : ", obj_name, " code #",GetLastError());
              }
           }
         // Міняєм колір у періоді передбачення
         if(m<k-Pridiction_Period-1)
            ObjectSetInteger(0, obj_name, OBJPROP_COLOR, clrFloralWhite);
         else
            ObjectSetInteger(0, obj_name, OBJPROP_COLOR, clrMagenta);
        }

      // Виводимо графіки на екран
      ChartRedraw();
     }
// Якщо потрібно виводимо графік на екран
   if(Calc_MAE)
     {
      // Розраховуємо точку виводу графічного об'єкту МАЕ
      XMAE = iHigh(name,PERIOD_CURRENT,0);

      // Створюємо графічний об'єкт
      ObjectCreate(0, obj_name_ma, OBJ_TEXT,0,load_time[k-1],XMAE);

      // Встановлюємо його властивості
      ObjectSetInteger(0, obj_name_ma, OBJPROP_ANCHOR, ANCHOR_LEFT_UPPER);
      ObjectSetString(0, obj_name_ma, OBJPROP_TEXT, "MAE");
      ObjectSetString(0, obj_name_ma, OBJPROP_FONT, "Arial");
      ObjectSetInteger(0, obj_name_ma, OBJPROP_FONTSIZE,15);
      ObjectSetInteger(0, obj_name_ma, OBJPROP_COLOR, clrRed);
      ObjectSetInteger(0, obj_name_ma, OBJPROP_SELECTABLE, true);

      // Виводимо об'єкт на екран
      ChartRedraw();
     }
// Змінюємо час таймеру для того щоб графіки не перебудовувалися раніше ніж 5 хвилин
   EventSetTimer(300);
  }

//+------------------------------------------------------------------+
void OnTick()
  {
//---
  }

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
// Прибираємо всі графіки з екрану
   ObjectsDeleteAll(0,0,-1);
   if(!FileDelete(filename))
     {
      Print("Error of deleting file ",filename);
     }
   for(i=0; i<num_mk; i++)
     {
      if(name_graph[i]=="atr")
        {
         ObjectsDeleteAll(0,1,-1);
        }
      if(!FileDelete(mk[i]))
        {
         Print("Error of deleting file ",mk[i]);
        }
     }
// Ліквідуємо таймер
   EventKillTimer();
   Print("Prophet_Start process completed successfull!");
  }
//+------------------------------------------------------------------+

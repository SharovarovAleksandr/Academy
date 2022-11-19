class TextProcessor():

    set_punctuation = (".", ",", ":", ";", "!", "?", "-")

    # def __init__(self,__text_processor):
    #     self.__text_processor=text_processor

# Варіант 1  Коли приватний метод классу __is_punctuation повертає приватний аргумент True/False
    @classmethod
    def get_clean_string(cls,s):
        s1=""
        for i in list(s):
            if TextProcessor.__is_punctuation(i,False):
                continue
            else:
                s1 += i
        return s1

    @classmethod
    def __is_punctuation(cls, s, b):
        if s in TextProcessor.set_punctuation:
            b= True
        else:
            b= False
        return b

#Ваіант 2 Коли приватний метод класу __is_punctuation обробляє запрос True/False всередині класу
    # @classmethod
    # def get_clean_string(cls,s):
    #     s1=""
    #     for i in list(s):
    #         if TextProcessor.__is_punctuation(i):
    #             continue
    #         else:
    #             s1 += i
    #     return s1
    #
    # @classmethod
    # def __is_punctuation(cls, s):
    #     if s in TextProcessor.set_punctuation:
    #         return  True
    #     else:
    #         return  False

# class TextLoader(TextProcessor):
#
#     def __init__(self,__clean_string):
#         self.__clean_string=__clean_string
#
#     @classmethod
#     def set_clean_text(cls,text_processor):




st=" Ну, як можливо це зрозуміти? Тут повинен бути - знак, який я повинен видалити !"
print(st)
print(TextProcessor.get_clean_string(st))


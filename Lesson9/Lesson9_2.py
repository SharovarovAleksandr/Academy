class TextProcessor():

    set_punctuation = (".", ",", ":", ";", "!", "?", "-")

    def __init__(self,text_processor):
        self.text_processor=text_processor

# Варіант 1  Коли приватний метод классу __is_punctuation повертає приватний аргумент True/False
    @classmethod
    def get_clean_string(cls,s):
        s1=""
        for i in list(s):
            if TextProcessor.__is_punctuation(i):
                continue
            else:
                s1 += i
        return s1

    @classmethod
    def __is_punctuation(cls, s):
        if s in TextProcessor.set_punctuation:
            b= True
        else:
            b= False
        return b

#

class TextLoader(TextProcessor):

    def __init__(self,text_processor,clean_string):
        self.__text_processor=TextProcessor.text_processor
        self.__clean_string=clean_string

    @property
    def text_processor(self):
        return self.__text_processor

    @text_processor.setter
    def text_processor(self,value):
        self.__text_processor=value

    @property
    def clean_string(self):
        return self.__clean_string

    @property
    def clean_string(self):
        print("Виводимо  текст очищений від знаків пуктуації")
        return

    @clean_string.setter
    def clean_string(self, value):
        self.__clean_string = value


    @classmethod
    def set_clean_text(cls):
        return text_processor()

class DataInterface(TextLoader):
    # def __init__(self,atribut):
    #     self.__atribut=

    @classmethod
    def processor_texts(cls,lst):
        for i in lst:
            print(TextProcessor.get_clean_string(i))
        return




# st=" Ну, як можливо це зрозуміти? Тут повинен бути - знак, який я повинен видалити !"
# print(st)
# print(TextProcessor.get_clean_string(st))

lst=[" Ну, як можливо це зрозуміти? Тут повинен бути - знак, який я повинен видалити !",
     " Це друге, вже вдруге, речення для тесту!?",
     " А, може бути, ще одно речення!! "]

DataInterface.processor_texts(lst)

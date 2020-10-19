import os, random


class Uncommon:

    __DATA_PATH = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), 'data', 'words' + '.txt'
        )
    )
    __word_list = []

    def __init__(self, separator='-', count=3):
        self.count = count
        self.separator = separator

    def __load_words(self):
        with open(self.__DATA_PATH, 'r') as file:
            for item in file.readlines():
                self.__word_list.append(item.strip())

    def get(self):
        return_list = []
        if not self.__word_list:
            self.__load_words()
        for i in range(self.count):
            return_list.append(random.choice(self.__word_list))
        return f'{self.separator}'.join([x for x in return_list])

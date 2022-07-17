import re
from typing import List


class DataPreprocessing:
    """

    """

    def __init__(self):
        a = 0

    def create_filtered_file(self, path_load: str, path_save: str):
        """
        Create a filtered file
        :param path_load: path load unfiltered file
        :param path_save: path to save filtered file
        """
        list_load_strings = self.load_txt_file(path_load)
        filtered_strings = self.filtered_list_stings(list_load_strings)
        self.save_txt_file(path_save, filtered_strings)
        print(f"Save file path {path_save}")

    def filtered_list_stings(self, list_strings: List[str]) -> List[str]:
        """
        Filtering rows from a list
        :param list_strings: list of lines
        :return: filtered list of lines
        """
        filtered_strings = []
        for i in list_strings:
            if self.special_match(i) and len(i) > 10:
                filtered_strings.append(i)

        print(f"The number of non-coming lines  {len(list_strings) - len(filtered_strings)}")

        return filtered_strings

    @staticmethod
    def load_txt_file(path_: str) -> List[str]:
        """
        loading data from a text file
        :param path_: the path to the text file
        :return: list of lines from a text file
        """
        with open(fr'{path_}', 'r') as f:
            list_strings = f.read().splitlines()
            f.close()
        return list_strings

    @staticmethod
    def save_txt_file(path_: str, list_data: List[str]):
        with open(path_, 'w') as f:
            for line in list_data:
                f.write("%s\n" % line)

    @staticmethod
    def special_match(strg: str, search=re.compile(r'[^TCGA]').search):
        """
        Boolean value by character presence
        :param strg: строка для проверки
        :param search: regex
        :return: True or False
        """
        return not bool(search(strg))


if __name__ == '__main__':
    a = 0

def write_file(data: str, file_name: str) -> str:
    '''
    Открывает указанный файл для записи не затирая предыдущие данные
    :param data: принемает строку с данными
    :param file_name: принемает имя и путь к файлу
    :return: записывает данные в файл
    '''
    with open(file_name, 'a', encoding='utf-8') as file:
        return file.writelines(data)


def read_data(file_name: str) -> list:
    '''
    Считывает все данные из файла
    :param file_name: принемает имя и путь к файлу
    :return: строки с данными
    '''
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.readlines()
        return data


if __name__ == '__main__':
    pass

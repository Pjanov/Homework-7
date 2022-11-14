file_name_export = 'export.csv'
file_name_import = 'import.csv'
telephone_directory = 'telephone_directory'


def data_entry():
    '''
    Запрос данных у пользователя
    :return: строку с данными
    '''
    print('ДАННЫЕ:')
    data = [
    input('Введите Фамилию: '),
    input('Введите Имя: '),
    input('Введите Телефон: '),
    input('Введите Описание: ')
]
    res = ','.join(data)
    return res + '\n'


if __name__ == '__main__':
    print(data_entry())

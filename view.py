file_name_export = 'export.csv'
file_name_import = 'import.csv'
telephone_directory = 'telephone_directory'


def data_entry():
    '''
    Запрос данных у пользователя
    :return: строку с данными
    '''
    data = []
    print('ДАННЫЕ:')
    data.append(input('Введите Фамилию: '))
    data.append(input('Введите Имя: '))
    data.append(input('Введите Телефон: '))
    data.append(input('Введите Описание: '))
    res = ','.join(data)
    return res + '\n'


if __name__ == '__main__':
    pass

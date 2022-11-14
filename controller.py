import view as vw
import model as md


def add_record() -> str:
    '''
    Добавить запись в телефонный справочник
    :return: строку с данными
    '''
    res = md.write_file(vw.data_entry(), vw.telephone_directory)
    return res


def export_data() -> str:
    '''
    Экспорт данных из телефонного справочника в файл
    :return: строки с данными
    '''
    data = md.read_data(vw.telephone_directory)
    res = md.write_file(data, vw.file_name_export)
    return res


def import_data() -> str:
    '''
    Импорт из файла в телефонный справочник
    :return: строки с данными
    '''
    data = md.read_data(vw.file_name_import)
    res = md.write_file(data, vw.telephone_directory)
    return res


def menu():
    exit = 1
    while exit == 1:
        print()
        print('МЕНЮ ПРИЛОЖЕНИЯ')
        print('1 => Добавить запись в телефонный справочник')
        print('2 => Импорт данных в телефонный справочник')
        print('3 => Экспорт данных из телефонного справочника')

        num = int(input('ВЫБЕРЕТЕ ПУНКТ ИЗ МЕНЮ: '))
        if num == 1:
            add_record()
        elif num == 2:
            import_data()
        elif num == 3:
            export_data()
        else:
            print('нет такого пункта')
            continue
        print()
        exit = int(input('ХОТИТЕ ПРОДОЛЖИТЬ? (1 => да, 0 => нет): '))


if __name__ == '__main__':
    pass

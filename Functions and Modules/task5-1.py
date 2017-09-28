# -*- coding: utf-8 -*-
import psutil
import datetime
import time
import configparser


def settingsfile():
    config = configparser.ConfigParser()
    config.read('config5-1.cfg')
    interval = config.get("interval", "interval")
    result = {"interval": interval}
    return result


def get_info():
    # Показывает текущую дату и время
    now = datetime.datetime.now()
    # Возвращает количество логических процессоров в системе
    a = psutil.cpu_count()
    # Возвращает уровень нагрузки процессора в процентах
    b = psutil.cpu_percent(interval=3)
    # Возвращает время работы центрального процессора
    c = psutil.cpu_times(percpu=False)
    # Возвращает данные в байтах об использовании системной памяти
    d = psutil.virtual_memory()
    # Возвращает список именованных кортежей всех смонтированных разделов диска
    e = psutil.disk_partitions(all=False)
    # Возвращает данных о вводе/выводе#
    f = psutil.disk_io_counters(perdisk=False)
    # Возвращает глобальные данный сетевого ввода/вывода
    g = psutil.net_io_counters(pernic=False)

    results = {
        "time": now,
        "cpu_count": a,
        "cpu_percent": b,
        "cpu_times": c,
        "virtual_memory": d,
        "disk_partitions": e,
        "disk_io_counters": f,
        "net_io_counters": g
    }
    return results


def write_log():
    parametrs = get_info()
    my_file = open('log.txt', 'a')
    my_file.writelines(
        "{0}{1}\n".format(
            "Текущее время: ", str(parametrs["time"])
            )
    )
    my_file.writelines("{0}{1}\n".format(
        "Kоличество логических процессоров в системе: ",
        str(parametrs["cpu_count"])
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Уровень нагрузки процессора : ", str(parametrs["cpu_percent"])
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Время работы центрального процессора: ",
            str(parametrs["cpu_times"].user)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Использование системной памяти в байтах: ",
            str(parametrs["virtual_memory"].used)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Список всех смонтированных разделов диска: ",
            str(parametrs["disk_partitions"])
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Данных о вводе/выводе: ",
            str(parametrs["disk_io_counters"].read_count)+"/"+str(
                    parametrs["disk_io_counters"].write_count)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Данные сетевого ввода/вывода: ", str(
                    parametrs["net_io_counters"].bytes_sent)+"/"+str(
                    parametrs["net_io_counters"].bytes_recv)
            )
    )
    my_file.close()


def main():
    while True:
        write_log()
        time.sleep(int(settingsfile()["interval"]))
        settingsfile()
main()

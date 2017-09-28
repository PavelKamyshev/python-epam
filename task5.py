# -*- coding: utf-8 -*-
import psutil
import datetime
import time
while True:
    time.sleep(60)
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

    my_file = open('log.txt', 'a')
    my_file.writelines(
        "{0}{1}\n".format(
            "Текущеее время: ", str(now)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Kоличество логических процессоров в системе: ", str(a)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Уровень нагрузки процессора : ", str(b)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Время работы центрального процессора: ", str(c.user)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Использование системной памяти в байтах: ", str(d.used)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Список всех смонтированных разделов диска: ", str(e)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Данных о вводе/выводе: ", str(f.read_count)+"/"+str(f.write_count)
            )
    )
    my_file.writelines(
        "{0}{1}\n".format(
            "Данные сетевого ввода/вывода: ", str(g.bytes_sent)+"/"+str(
                g.bytes_recv)
            )
    )
    my_file.close()

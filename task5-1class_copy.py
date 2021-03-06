# -*- coding: utf-8 -*-
import psutil
import datetime
import time
import configparser


class Monitoring:
        def __init__(self):
            self.getInform()

        def getInform(self):
            # Показывает текущую дату и время
            self.now = datetime.datetime.now()
            # Возвращает количество логических процессоров в системе
            self.a = psutil.cpu_count()
            # Возвращает уровень нагрузки процессора в процентах
            self.b = psutil.cpu_percent(interval=3)
            # Возвращает время работы центрального процессора
            self.c = psutil.cpu_times(percpu=False)
            # Возвращает данные в байтах об использовании системной памяти
            self.d = psutil.virtual_memory()
            # Cписок именованных кортежей всех смонтированных разделов диска
            self.e = psutil.disk_partitions(all=False)
            # Возвращает данных о вводе/выводе#
            self.f = psutil.disk_io_counters(perdisk=False)
            # Возвращает глобальные данный сетевого ввода/вывода
            self.g = psutil.net_io_counters(pernic=False)


class Writer(Monitoring):
    def __init__(self):
        super().__init__()
        self.run()

    def write_log(self):

        my_file = open('log.txt', 'a')
        my_file.writelines(
            "{0}{1}\n".format("Текущее время: ", str(self.now))
        )
        my_file.writelines("{0}{1}\n".format(
            "Kоличество логических процессоров в системе: ",
            str(self.a))
        )
        my_file.writelines(
            "{0}{1}\n".format("Уровень нагрузки процессора : ", str(self.b))
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Время работы центрального процессора: ", str(self.c))
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Использование системной памяти в байтах: ", str(self.d))
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Список всех смонтированных разделов диска: ", str(self.e))
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Данных о вводе/выводе: ",
                str(self.f.read_count)+"/"+str(self.f.write_count))
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Данные сетевого ввода/вывода: ", str(
                        self.g.bytes_sent)+"/"+str(
                        self.g.bytes_recv)
                )
        )
        my_file.close()

    def settingsfile(self):
        config = configparser.ConfigParser()
        config.read('config5-1.cfg')
        interval = config.get("interval", "interval")
        result = {"interval": interval}
        return result

    def run(self):
        while True:
            self.getInform()
            self.write_log()
            time.sleep(int(self.settingsfile()["interval"]))
            self.settingsfile()

wr = Writer()

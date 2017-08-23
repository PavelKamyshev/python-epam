# -*- coding: utf-8 -*-
import psutil
import datetime
import time

class get_monitoring:
        def get_info(self):
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
            # Возвращает список именованных кортежей всех смонтированных разделов диска
            self.e = psutil.disk_partitions(all=False)
            # Возвращает данных о вводе/выводе#
            self.f = psutil.disk_io_counters(perdisk=False)
            # Возвращает глобальные данный сетевого ввода/вывода
            self.g = psutil.net_io_counters(pernic=False)

            results = {
                "time": self.now,
                "cpu_count": self.a,
                "cpu_percent": self.b,
                "cpu_times": self.c,
                "virtual_memory": self.d,
                "disk_partitions": self.e,
                "disk_io_counters": self.f,
                "net_io_counters": self.g
            }
            return results

gm = get_monitoring()
r = gm.get_info()
print(r["time"])


"""def write_log():
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
write_log()

while True:
    time.sleep(30)
    write_log()


def main():
    write_log()
main()"""

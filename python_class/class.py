# class Time:
#
#     hour = ""
#     minute = ""
#     second = ""
#
#     def add_time(self, t1, t2):
#         self.hour = t1.hour + t2.hour
#         self.minute = t1.minute + t2.minute
#         self.second = t1.second + t2.second
#
#         return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
#
# start = Time()
# start.hour = 9
# start.minute = 45
# start.second = 0
#
# duration = Time()
# duration.hour = 1
# duration.minute = 35
# duration.second = 0
#
# done = Time()
# print(done.add_time(start, duration))


class Time:
    def __init__(self, hour, minute, sec):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def __str__(self):

        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.sec)

    def mul_time(self, num):
        self.hour = self.hour * num
        self.minute = self.minute * num
        self.sec = self.sec * num

        return str(self.hour) + ":" + str(self.minute) + ":" + str(self.sec)

    def avg_pace(self, time, distance):
        self.minute = self.minute / 60
        self.sec = self.minute / 60
        self.hour = self.hour + self.minute + self.sec

        avg = distance/ self.hour
        return avg


t1 = Time(9, 9, 9)
result = t1.mul_time(2)
print(t1.avg_pace(result, 100))









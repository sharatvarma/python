from datetime import datetime, date


# def date_time():
#     d = date.today()
#     if d.isoweekday() == 1:
#         print("Monday")
#     elif d.isoweekday() == 2:
#         print("Tuesday")
#     elif d.isoweekday() == 3:
#         print("Wednesday")
#     elif d.isoweekday() == 4:
#         print("Thursday")
#     elif d.isoweekday() == 5:
#         print("Friday")
#     elif d.isoweekday() == 6:
#         print("Saturday")
#     elif d.isoweekday() == 7:
#         print("Sunday")
#     else:
#         print("No day")
#
# date_time()

def birthday(month, day):
    d = date.today()
    next_birthday = date(d.year, month, day)

    if d > next_birthday:
        next_birthday = date(d.year + 1, month, day)
    delta = next_birthday - d
    return delta


final = birthday(2, 16)
print(final)

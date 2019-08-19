import datetime

def wrap_calc(func):
    def result_func(x, y):
        x = x**2
        y = y**2

        return func(x, y)
    return result_func


def wrap_message(func):
    def result_func(text):
        print("Добрый день!")
        func(text)
        print("Спасибо, что пишите нам")
        date = datetime.datetime.today()
        print(date.strftime("%d-%m-%Y %H:%M:%S"))
    return result_func

from wrap import wrap_message, wrap_calc

@wrap_calc
def calc(x, y):
    return x + y

@wrap_calc
def render(x, y):
    print(x, y)

@wrap_calc
def pow(x, y):
    return x**y

@wrap_message
def message(text):
    print(text)

if __name__ == "__main__":
    print(render(4, 5))

    message("Здравствуйте, это декораторы")

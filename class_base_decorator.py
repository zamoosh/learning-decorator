class Decorator:
    def __init__(self, function):
        print("starting the decorator")
        self.function = function

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

        return self.function(*args, **kwargs)


@Decorator
def ali(name: str):
    if name:
        return name + " ali ali ali"
    return 'ali ali ali'


print(ali(name="no"))

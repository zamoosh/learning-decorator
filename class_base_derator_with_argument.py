class Decorator:
    def __init__(self, *args, **kwargs):
        print("starting the decorator")
        self._args = args
        self._kwargs = kwargs

    def __call__(self, function):
        self.function = function

        def decorator(*args, **kwargs):
            print(self.function(*args, **kwargs))
            print(args)
            print(kwargs)
            return self.function(*args, **kwargs)

        return decorator


@Decorator(preson=45)
def ali(name: str):
    if name:
        return name + " ali ali ali"
    return 'ali ali ali'


# @Decorator()
# def mohammad():
#     print("mohammad")


print(ali(name="no"))
# mohammad()

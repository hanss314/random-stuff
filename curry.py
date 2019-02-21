import re


class CurriedFunction(object):
    def __init__(self, f, args=None, kwargs=None, regex=None):
        self.function = f
        self._args = args or []
        self._kwargs = kwargs or {}
        self.regex = regex or re.compile(
            r"{}\(\) missing \d+? required (positional|keyword-only) argument".format(self.function.__name__)
        )

    def __call__(self, *args, **kwargs):
        new = self.__class__(self.function, self._args, self._kwargs, self.regex)
        try:
            return new.attempt_call(args, kwargs)
        except TypeError as e:
            if self.regex.match(e.args[0]):
                new._args.extend(args)
                new._kwargs.update(kwargs)
                return new
            else:
                raise e

    def attempt_call(self, args, kwargs):
        new_args, new_kwargs = self._args.copy(), self._kwargs.copy()
        new_args.extend(args)
        new_kwargs.update(kwargs)
        return self.function(*new_args, **new_kwargs)


@CurriedFunction
def addweird(*, a, b):
    return a + b


add3 = addweird(b=3)
print(add3(a=1), add3(a=3))

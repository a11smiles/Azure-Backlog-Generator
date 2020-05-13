
class Noniterable_str(str):
    def __iter__(self):
        yield self
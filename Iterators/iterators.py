"""
iterator protocol: objects that support the __iter and __next dunder methods automatically work with the for-in loops
"""

"""class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    def __init__(self, source):
        self.source = source
        self.source.value = "samet"

    def __next__(self):
        return self.source.value"""


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > 10:
            return None
        self.value += 1
        return self.value


repeater = Repeater(1)
for item in repeater:
    print(item)

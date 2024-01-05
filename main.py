class Test:
    def __str__(self):
        return "str"

    def __repr__(self):
        return "info"

obj = Test()
print(obj)

print(repr(obj))



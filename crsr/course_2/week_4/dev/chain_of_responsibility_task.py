class Someobject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type_):
        self.type_ = type_


class EventSet:
    def __init__(self, value):
        self.value = value


class NullHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, obj, event):
        if self.successor:
            return self.successor.handle(obj, event)
        # return None


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and (event.type_ is int):
            return obj.integer_field
        elif isinstance(event, EventSet) and isinstance(event.value, int):
            obj.integer_field = event.value
            return

        return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and (event.type_ is float):
                return obj.float_field
        elif isinstance(event, EventSet) and isinstance(event.value, float):
                obj.float_field = event.value
                return

        return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and (event.type_ is str):
            return obj.string_field
        elif isinstance(event, EventSet) and isinstance(event.value, str):
            obj.string_field = event.value
            return

        return super().handle(obj, event)


if __name__ == "__main__":
    obj = Someobject()
    chain = FloatHandler(IntHandler(StrHandler(NullHandler())))
    chain.handle(obj, EventSet(1))
    chain.handle(obj, EventSet(1.5))
    chain.handle(obj, EventSet("str"))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))

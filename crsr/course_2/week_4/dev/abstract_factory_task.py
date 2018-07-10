
class AbstractLevel:
    @classmethod
    def get_map(Class):
        return Class.Map()

    @classmethod
    def get_objects(Class):
        return Class.Objects()


class EasyLevel(AbstractLevel):
    pass


class MediumLevel(AbstractLevel):
    pass

class HardLevel(AbstractLevel):
    pass





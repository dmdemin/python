import random
from abc import ABC
import yaml


class AbstractLevel(yaml.YAMLObject):
    @classmethod
    def from_yaml(cls, loader, node):
        data = loader.construct_mapping(node, True)

        map = cls.get_map()
        obj = cls.get_objects()
        obj.config = data

        return {'map': map, 'obj': obj}

    @classmethod
    def get_map(Class):
        return Class.Map()

    @classmethod
    def get_objects(Class):
        return Class.Objects()

    class Map(ABC):
        pass

    class Objects(ABC):
        pass


class EasyLevel(AbstractLevel):
    yaml_tag = u'!easy_level'

    class Map:
        def __init__(self):
            self.map = [[0 for j in range(5)] for i in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        self.map[j][i] = -1  # граница карты
                    else:
                        # случайная характеристика области
                        self.map[j][i] = random.randint(0, 2)

        def get_map(self):
            return self.map


    class Objects:

        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (2, 2))]

        def get_objects(self, map):
            # размещаем противников
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects


class MediumLevel(AbstractLevel):
    yaml_tag = u'!medium_level'

    class Map:

        def __init__(self):
            self.map = [[0 for j in range(8)] for i in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        self.map[j][i] = -1  # граница карты
                    else:
                        # случайная характеристика области
                        self.map[j][i] = random.randint(0, 2)

        def get_map(self):
            return self.map

    class Objects:

        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (4, 4))]

        def get_objects(self, map):
            # размещаем врагов
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))

                self.objects.append((obj_name, coord))

            return self.objects


class HardLevel(AbstractLevel):
    yaml_tag = u'!hard_level'

    class Map:

        def __init__(self):
            self.map = [[0 for j in range(10)] for i in range(10)]
            for i in range(10):
                for j in range(10):
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        # граница карты
                        self.map[j][i] = -1
                    else:
                        # характеристика области (-1 для непроходимой обл.)
                        self.map[j][i] = random.randint(-1, 8)

        def get_map(self):
            return self.map

    class Objects:

        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (5, 5))]

        def get_objects(self, map):
            # размещаем врагов
            for obj_name in ['rat', 'snake']:
                coord = (random.randint(1, 8), random.randint(1, 8))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    if map[coord[0]][coord[1]] == -1:
                        intersect = True
                        coord = (random.randint(1, 8), random.randint(1, 8))
                        continue
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 8), random.randint(1, 8))

                self.objects.append((obj_name, coord))

            return self.objects


Levels = '''levels:
  - !easy_level {}
  - !medium_level
    enemy: ['rat', 'dog']
  - !hard_level
    enemy:
    - rat
    - snake
    - dragon
    enemy_count: 10'''

levels = yaml.load(Levels)
print(levels)
#
# Levels = {'levels':[]}
# _map = EasyLevel.Map()
# _obj = EasyLevel.Objects()
# Levels['levels'].append({'map': _map, 'obj': _obj})
#
# _map = MediumLevel.Map()
# _obj = MediumLevel.Objects()
# _obj.config = {'enemy':['rat']}
# Levels['levels'].append({'map': _map, 'obj': _obj})
#
# _map = HardLevel.Map()
# _obj = HardLevel.Objects()
# _obj.config = {'enemy': ['rat', 'snake', 'dragon'], 'enemy_count': 10}
# Levels['levels'].append({'map': _map, 'obj': _obj})
# print(Levels)
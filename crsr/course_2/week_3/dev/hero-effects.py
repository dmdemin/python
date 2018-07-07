from abc import ABC, abstractmethod


HP_name = "HP"
MP_name = "MP"
SP_name = "SP"

Strength_name = "Strength"
Perception_name = "Perception"
Endurance_name = "Endurance"
Charisma_name = "Charisma"
Intelligence_name = "Intelligence"
Agility_name = "Agility"
Luck_name = "Luck"

class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            HP_name: 128,
            MP_name: 42,
            SP_name: 100,

            Strength_name: 15,
            Perception_name: 4,
            Endurance_name: 8,
            Charisma_name: 2,
            Intelligence_name: 3,
            Agility_name: 8,
            Luck_name: 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def apply_effect(self):
        pass

    def get_stats(self):  # returns final states
        return self.apply_effect()

    def get_positive_effects(self):
        return self.base.get_positive_effects() + [self.__class__.__name__]
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects() + [self.__class__.__name__]


class AbstractPositive(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects() + [self.__class__.__name__]

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    POSITIVE_POINTS = 7
    NEGATIVE_POINTS = 3
    HP_POSITIVE_POINTS = 50

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy[Strength_name] += self.POSITIVE_POINTS
        stats_copy[Endurance_name] += self.POSITIVE_POINTS
        stats_copy[Agility_name] += self.POSITIVE_POINTS
        stats_copy[Luck_name] += self.POSITIVE_POINTS

        stats_copy[Perception_name] -= self.NEGATIVE_POINTS
        stats_copy[Charisma_name] -= self.NEGATIVE_POINTS
        stats_copy[Intelligence_name] -= self.NEGATIVE_POINTS

        stats_copy[HP_name] += self.HP_POSITIVE_POINTS

        return stats_copy


class Blessing(AbstractPositive):
    POSITIVE_POINTS = 2

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy[Strength_name] += self.POSITIVE_POINTS
        stats_copy[Endurance_name] += self.POSITIVE_POINTS
        stats_copy[Agility_name] += self.POSITIVE_POINTS
        stats_copy[Luck_name] += self.POSITIVE_POINTS
        stats_copy[Perception_name] += self.POSITIVE_POINTS
        stats_copy[Charisma_name] += self.POSITIVE_POINTS
        stats_copy[Intelligence_name] += self.POSITIVE_POINTS

        return stats_copy


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects() + [self.__class__.__name__]


class Weakness(AbstractNegative):
    NEGATIVE_POINTS = 4

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy[Strength_name] -= self.NEGATIVE_POINTS
        stats_copy[Endurance_name] -= self.NEGATIVE_POINTS
        stats_copy[Agility_name] -= self.NEGATIVE_POINTS

        return stats_copy


class EvilEye(AbstractNegative):
    NEGATIVE_POINTS = 10

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy[Luck_name] -= self.NEGATIVE_POINTS
        return stats_copy


class Curse(AbstractNegative):
    NEGATIVE_POINTS = 2

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy[Strength_name] -= self.NEGATIVE_POINTS
        stats_copy[Endurance_name] -= self.NEGATIVE_POINTS
        stats_copy[Agility_name] -= self.NEGATIVE_POINTS
        stats_copy[Luck_name] -= self.NEGATIVE_POINTS
        stats_copy[Perception_name] -= self.NEGATIVE_POINTS
        stats_copy[Charisma_name] -= self.NEGATIVE_POINTS
        stats_copy[Intelligence_name] -= self.NEGATIVE_POINTS

        return stats_copy


if __name__ == "__main__":
    hero = Hero()
    berserk = Weakness(Berserk(Curse(Blessing(EvilEye(Berserk(hero))))))
    print(hero)
    print(berserk.get_positive_effects())
    print(berserk.get_negative_effects())
    print(berserk.get_stats())
    print("----------------------")

    # delete the 2nd Berserk decorator
    # berserk.base = berserk.base.base

    # delete Blessing decorator
    # berserk.base.base.base = berserk.base.base.base.base

    # delete the 1st Berserk decorator
    # berserk.base.base.base.base.base = berserk.base.base.base.base.base.base

    print(berserk.get_positive_effects())
    print(berserk.get_negative_effects())
    print(berserk.get_stats())

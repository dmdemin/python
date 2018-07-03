from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
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

    def get_stats(self):  # Возвращает итоговые хараетеристики
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
        # return super().get_positive_effects()
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    POSITIVE_POINTS = 7
    NEGATIVE_POINTS = 3
    HP_NEGATIVE_POINTS = 50

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy["Strength"] += self.POSITIVE_POINTS
        stats_copy["Endurance"] += self.POSITIVE_POINTS
        stats_copy["Agility"] += self.POSITIVE_POINTS
        stats_copy["Luck"] += self.POSITIVE_POINTS

        stats_copy["Perception"] -= self.NEGATIVE_POINTS
        stats_copy["Charisma"] -= self.NEGATIVE_POINTS
        stats_copy["Intelligence"] -= self.NEGATIVE_POINTS

        stats_copy["HP"] -= self.HP_NEGATIVE_POINTS

        return stats_copy


class Blessing(AbstractPositive):
    POSITIVE_POINTS = 2

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy["Strength"] += self.POSITIVE_POINTS
        stats_copy["Endurance"] += self.POSITIVE_POINTS
        stats_copy["Agility"] += self.POSITIVE_POINTS
        stats_copy["Luck"] += self.POSITIVE_POINTS
        stats_copy["Perception"] += self.POSITIVE_POINTS
        stats_copy["Charisma"] += self.POSITIVE_POINTS
        stats_copy["Intelligence"] += self.POSITIVE_POINTS

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
        stats_copy["Strength"] -= self.NEGATIVE_POINTS
        stats_copy["Endurance"] -= self.NEGATIVE_POINTS
        stats_copy["Agility"] -= self.NEGATIVE_POINTS

        return stats_copy


class EvilEye(AbstractNegative):
    NEGATIVE_POINTS = 10;

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy["Luck"] -= self.NEGATIVE_POINTS
        return stats_copy


class Curse(AbstractNegative):
    NEGATIVE_POINTS = 2

    def apply_effect(self):
        stats_copy = self.base.get_stats()
        stats_copy["Strength"] -= self.NEGATIVE_POINTS
        stats_copy["Endurance"] -= self.NEGATIVE_POINTS
        stats_copy["Agility"] -= self.NEGATIVE_POINTS
        stats_copy["Luck"] -= self.NEGATIVE_POINTS
        stats_copy["Perception"] -= self.NEGATIVE_POINTS
        stats_copy["Charisma"] -= self.NEGATIVE_POINTS
        stats_copy["Intelligence"] -= self.NEGATIVE_POINTS

        return stats_copy


if __name__ == "__main__":
    hero = Hero()
    berserk = Weakness(Berserk(Curse(Blessing(EvilEye(Berserk(hero))))))
    print(hero)
    print(berserk.get_positive_effects())
    print(berserk.get_negative_effects())
    print(berserk.get_stats())
    print("----------------------")

    # delete 2nd Berserk decorator
    # berserk.base = berserk.base.base

    # delete Blessing decorator
    berserk.base.base.base = berserk.base.base.base.base

    print(berserk.get_positive_effects())
    print(berserk.get_negative_effects())
    print(berserk.get_stats())

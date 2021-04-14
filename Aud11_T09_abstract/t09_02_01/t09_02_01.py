

from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):

    @abstractmethod
    def visit_general_staff(self, general_staff):
        pass

    @abstractmethod
    def visit_military_base(self, military_base):
        pass


class MilitaryObject(metaclass=ABCMeta):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def accept(self, spy: Spy):
        pass


class GeneralStaff(MilitaryObject):

    def __init__(self, title, generals, secret_papers):
        super().__init__(title)
        self.generals = generals
        self.secret_papers = secret_papers

    def __str__(self):
        return ("Генеральний штаб \"{}\" має {} генералів та {}"
                " секретних паперів"
                .format(self.title, self.generals, self.secret_papers))

    def accept(self, spy: Spy):
        spy.visit_general_staff(self)


class MilitaryBase(MilitaryObject):

    def __init__(self, title, soldiers, officers, tanks):
        super().__init__(title)
        self.soldiers = soldiers
        self.officers = officers
        self.tanks = tanks

    def __str__(self):
        return ("Військова база \"{}\" містить {} солдат, {} офіцерів та"
                " {} танків"
                .format(self.title, self.soldiers, self.officers, self.tanks))

    def accept(self, spy: Spy):
        spy.visit_military_base(self)


class SecretAgent(Spy):

    def __init__(self):
        self.stolen_info = ""

    def __str__(self):
        return self.stolen_info

    def visit_general_staff(self, general_staff):
        secret_papers = general_staff.secret_papers
        self.stolen_info = "Вкрадено {} секретних паперів. ".format(secret_papers)
        general_staff.secret_papers = 0
        self.stolen_info += "Отримана інформація: " + str(general_staff)

    def visit_military_base(self, military_base):
        self.stolen_info = "Отримана інформація: " + str(military_base)


class Saboteur(Spy):

    def __init__(self):
        self.destroyed_info = ""

    def __str__(self):
        return self.destroyed_info

    def visit_general_staff(self, general_staff):
        generals = general_staff.generals
        secret_papers = general_staff.secret_papers
        self.destroyed_info = ("Знищено {} генералів та {} секретних паперів."
                               .format(generals, secret_papers))
        general_staff.generals = 0
        general_staff.secret_papers = 0

    def visit_military_base(self, military_base):
        soldiers = military_base.soldiers
        officers = military_base.officers
        tanks = military_base.tanks
        self.destroyed_info = ("Знищено {} солдатів, {} офіцерів та {} танків."
                               .format(soldiers, officers, tanks))
        military_base.soldiers = 0
        military_base.officers = 0
        military_base.tanks = 0


if __name__ == '__main__':
    general_staff = GeneralStaff("99", 10, 100)
    military_base = MilitaryBase("101", 1000, 100, 20)

    print(general_staff)
    print(military_base)
    print()

    secret_agent = SecretAgent()
    general_staff.accept(secret_agent)
    print(secret_agent)
    print(general_staff)
    print()

    military_base.accept(secret_agent)
    print(secret_agent)
    print(military_base)
    print()

    saboteur = Saboteur()
    general_staff.accept(saboteur)
    print(saboteur)
    print(general_staff)
    print()

    military_base.accept(saboteur)
    print(saboteur)
    print(military_base)
    print()


class Shohoku:
    def __init__(self, name):
        self.name = name
        self.exp = 0
        self.lesson = 0

    def Hello(self):
        print('Hello ! my name is {}'.format(self.name))

    def coding(self):
        print('{} is coding'.format(self.name))
        self.exp += 10
        self.lesson += 1

    def showexp(self):
        print('{} have {} exp \nhave {} lessons.'.format(
            self.name, self.exp, self.lesson))

    def addexp(self, score):
        self.exp += score
        self.lesson += 1


class NYC(Shohoku):
    def __init__(self, name, player):
        super().__init__(name)
        self.player = player
        Team = ['Nets', 'Knicks']
        if player in Team:
            self.exp += 100

    def addexp(self, score):
        self.exp += score * 3
        self.lesson += 1

    def askexp(self, score=10):
        print('Extra point for NBA players {} EXP'.format(score))
        self.addexp(score)


if __name__ == '__main__':
    print('-----1 Jan 2021 -------')
    player1 = NYC('Kevin Durant', 'Nets')
    player1.askexp()
    player1.showexp()
    student1 = Shohoku('Rukawa')
    print(student1.name)
    student1.Hello()
    student2 = Shohoku('Akagi')
    print(student2.name)
    student2.Hello()

    print('-----2 Jan 2021 -------')
    print('Who want to traing basketball today for 10 exp ? ')
    print(student1.name, ' : Me !')
    student1.addexp(10)

    print('-----3 Jan 2021 -------')
    print('Total individul exp : ')
    student1.name = 'Rukawa Kaede'
    print(student1.name, student1.exp)
    print(student2.name, student2.exp)

    print('-----4 Jan 2021 -------')
    for i in range(5):
        student2.coding()
    student1.showexp()
    student2.showexp()

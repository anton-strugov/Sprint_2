class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def number_of_wins(self):
        print(f'Футбольных побед: {self.victories}')

    def number_of_draws(self):
        print(f'Футбольных ничьих: {self.victories}')

    def number_of_losses(self):
        print(f'Футбольных поражений: {self.victories}')

    def total_points(self):
        print(f'Общее количество очков: {2 * self.victories + self.draws}')


class Hockey(Results):
    def number_of_wins(self):
        print(f'Хоккейных побед: {self.victories}')

    def number_of_draws(self):
        print(f'Хоккейных ничьих: {self.victories}')

    def number_of_losses(self):
        print(f'Хоккейных поражений: {self.victories}')

    def total_points(self):
        print(f'Общее количество очков: {2 * self.victories + self.draws}')


foolball_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)
for team in (foolball_team, hockey_team):
    team.number_of_wins()
    team.number_of_draws()
    team.number_of_losses()
    team.total_points()

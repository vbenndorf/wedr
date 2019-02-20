from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency
)
import random, string, json, time

doc = """
a.k.a. Keynesian beauty contest.

Players all guess a number; whoever guesses closest to
2/3 of the average wins.

See https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    name_in_url = 'encrypt_js'

    letters_per_word = 3

    use_timeout = True
    seconds_per_period = 60

class Subsession(BaseSubsession):
    dictionary = models.StringField()

    def creating_session(self):
        # Create dictionary
        letters = list(string.ascii_uppercase)
        random.shuffle(letters)
        numbers = []
        N = list(range(100, 1000))
        for i in range(27):
            choice = random.choice(N)
            N.remove(choice)
            numbers.append(choice)
        d = [letters, numbers]
        dictionary = dict([(d[0][i], d[1][i]) for i in range(26)])
        self.dictionary = json.dumps(dictionary)



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    performance = models.IntegerField(initial=0, blank=True)
    mistakes = models.IntegerField(initial=0, blank=True)


from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    send_B = models.IntegerField(label='Si fueras el jugador A, ¿Cuánto enviarías al jugador B?', choices=[
                                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    send_A_if_3 = models.IntegerField(
        label='Si fueras el jugador B y recibieras 3 puntos, ¿Cuánto enviarías al jugador A?', choices=[1, 2, 3])
    send_A_if_6 = models.IntegerField(
        label='Si fueras el jugador B y recibieras 6 puntos, ¿Cuánto enviarías al jugador A?', choices=[1, 2, 3, 4, 5, 6])
    send_A_if_9 = models.IntegerField(
        label='Si fueras el jugador B y recibieras 9 puntos, ¿Cuánto enviarías al jugador A?', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9])


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['send_B', 'send_A_if_3', 'send_A_if_6', 'send_A_if_9']

page_sequence = [Demographics]

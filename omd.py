from random import choice
# Guido van Rossum <guido@python.org>


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    def step2_umbrella():
        print(
            'Настроение отличное!'
            'Ночь будет веселой:)'
        )

    def step2_no_umbrella():
        cases = [
                'Дождик не пошел, поэтому один шот и иду домой!:)',
                'Я промокла и у меня нет настроения пить - иду домой:('
        ]
        print(choice([cases[0], cases[1]]))

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()

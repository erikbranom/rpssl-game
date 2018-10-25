import random

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""


def choice_to_number(choice):
    return{'rock': 0, 'paper': 1, 'scissors': 2, 'spock': 3, 'lizard': 4}[choice]


def number_to_choice(number):
    return{0: 'rock', 1: 'paper', 2: 'scissors', 3: 'spock', 4: 'lizard'}[number]


def random_computer_choice():
    return{'rock', 'paper', 'scissors', 'spock', 'lizard'}


def choice_result(human_move, computer_move):

    global COMPUTER_SCORE
    global HUMAN_SCORE

    human_choice_number = choice_to_number(human_move)
    computer_choice_number = choice_to_number(computer_move)
    if (computer_choice_number - human_choice_number) % 5 == [1, 3]:
        print("Human Wins!")
        HUMAN_SCORE += 1
    elif (human_choice_number - computer_choice_number) % 5 == {2, 4}:
        print("Computer wins!")
        COMPUTER_SCORE += 1
    elif computer_choice_number == human_choice_number:
        print("Uh oh, its a tie")


def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
    assert choice_to_number('spock') == 3
    assert choice_to_number('lizard') == 4


def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'
    assert number_to_choice(3) == 'spock'
    assert number_to_choice(4) == 'lizard'


def test_computer_choice():
    choice = random_computer_choice()
    assert choice in ['rock', 'paper', 'scissors', 'spock', 'lizard']
    assert 0 <= choice_to_number(choice) <= 4


def test_all():
    test_choice_to_number()
    test_number_to_choice()
    test_computer_choice()


def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)


def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)


def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)


def spock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'spock'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)


def lizard():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE

    human_choice = 'lizard'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)


def greet():
    print('Welcome to the game of RPSSL')
    print('Commands: (r)ock\n' +
          '          (p)aper\n' +
          '          (s)cissors\n' +
          '          sp(o)ck\n' +
          '          (l)izard\n' +
          '          (q)uit\n')


def get_user_input():
    valid = False
    while not valid:
        print('Please, make a choice: ', end='')
        s = input().strip().lower()
        if len(s) == 0 or len(s) > 1 or s not in 'rpsolq':
            print('Invalid input. Valid inputs are {r, p, s, o, l, q}.')
            continue
        else:
            return s


def play_rps():
    global HUMAN_SCORE, COMPUTER_SCORE

    moves = {'r': rock,
             'p': paper,
             's': scissors,
             'o': spock,
             'l': lizard}
    greet()
    while True:
        user_input = get_user_input()
        if user_input == 'q':
            print('Final score: Human {} : Computer {}'.format(HUMAN_SCORE, COMPUTER_SCORE))
            print('Thanks for playing. Good bye!')
            break
        else:
            move = moves.get(user_input)
            assert move is not None
            move()
            print('Score: Human {} : Computer {}'.format(HUMAN_SCORE, COMPUTER_SCORE))


if __name__ == '__main__':

    play_rps()

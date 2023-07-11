from microbit import *
from random import randint


A_Z = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z'
]


def blink(char):
    for x in range(5):
        display.clear()
        sleep(700)
        display.show(char)
        sleep(700)


def shuffle(obj):
    shuffled_lst = obj
    length = len(shuffled_lst)

    for word_index in range(length - 1, 0, -1):
        place = randint(0, word_index)

        shuffled_lst[word_index], shuffled_lst[place] = shuffled_lst[place], shuffled_lst[word_index]

    return shuffled_lst


def alph_input():
    counter = 0
    display.clear()
    while True:
        if button_b.was_pressed():
            counter += 1
            if counter == 26:
                counter = 0

        if button_a.was_pressed():
            return A_Z[counter]

        display.clear()
        display.show(A_Z[counter])
        sleep(200)

FRAMES = [
    Image('55555:'
          '50000:'
          '50000:'
          '50000:'
          '55000'),
    Image('55599:'
          '50099:'
          '50000:'
          '50000:'
          '55000'),
    Image('55599:'
          '50099:'
          '50700:'
          '50000:'
          '55000'),
    Image('55599:'
          '50099:'
          '50707:'
          '50000:'
          '55000'),
    Image('55599:'
          '50099:'
          '50797:'
          '50090:'
          '55090'),
]

WORDS = [
    "Bliss", "Grape",
    "Pixel", "Oasis",
    "Tidal", "Knife",
    "Dingo", "Zebra",
    "Folly", "Mirth",
    "Mound", "Fluke",
    "Fetch", "Gloat",
    "Latch", "Quirk",
    "Thump", "Stork",
    "Yacht", "Fjord"
]
WORDS = shuffle(WORDS)

GAME = True
while GAME:
    computer_word = WORDS.pop().upper()
    random_hint = randint(0, len(computer_word)-1)
    display_word_raw = (len(computer_word)) * '*'

    display_word = display_word_raw[:random_hint]
    display_word += computer_word[random_hint]
    display_word += display_word_raw[random_hint+1:]
    used_letters = []

    counter = 0

    while True:
        text = ""
        for index, letter in enumerate(display_word):
            index = str(index)
            text += index + letter + " "
        for x in range(3):
            sleep(1000)
            display.show(text)

        while True:
            display.show(FRAMES[counter])
            if button_a.was_pressed():
                break

        next_letter = alph_input()

        if next_letter in used_letters:
            counter += 1
            if counter == 4:
                display.show(FRAMES[counter])
                sleep(1500)
                GAME = False
                blink('X')
                display.show("GAME Over!")
                break
        else:
            used_letters.append(next_letter)
        
        if next_letter in computer_word:
            temp = display_word
            display_word = ""
            for x in range(len(computer_word)):
                if next_letter == computer_word[x]:
                    display_word += next_letter
                else:
                    display_word += temp[x]
        else:
            counter += 1
            if counter == 4:
                GAME = False
                blink('X')
                display.show("GAME Over!")
                break

        if '*' not in display_word:
            display.show("Complete, next word")
            break

    if len(WORDS) == 0 and GAME:
        display.show("GAME OVER! YOU'VE WON!")
        break
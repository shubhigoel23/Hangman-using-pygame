import string
import pygame.freetype
from typing import Text
from words import choose_word
from pygame.locals import *
import pygame
pygame.init()
# initializes the display module

clock = pygame.time.Clock()
screen = pygame.display.set_mode([1300, 700], pygame.RESIZABLE)
# display screen's width and heigth are set and it is resizable
pygame.display.set_caption('Hangman')
# sets the caption of the display screen

# define the RGB values for different colors
blue = (0, 0, 128)
white = (255, 255, 255)
yellow = (255, 255, 0)
dark_green = (34, 177, 76)
green = (0, 255, 255)
orange = (255, 100, 0)
saddle_brown = (139, 69, 19)
black = (0, 0, 0)
red = (255, 0, 0)
maroon = (102, 0, 51)
orange_red = (255, 69, 0)
lightred = (255, 165, 145)
darklightred = (255, 95, 81)


subFont = pygame.font.SysFont('freesansbold', 36)
message = subFont.render('Welcome to the game, Hangman!',
                         True, blue, (135, 206, 235))
# create a rectangular object for the
# text surface object
messageRect = message.get_rect()
# set the center of the rectangular object.
messageRect.center = (650, 150)

DEFAULT_IMAGE_SIZE = (100, 100)
# Take image as input
img = pygame.image.load('Hangman-Game.ico')

# Set image as icon
pygame.display.set_icon(img)
image = pygame.image.load('hangman2.ico')
image1 = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# setting the pygame font style(1st parameter), size of font(2nd parameter)and for bold pass true else false
mainFont = pygame.font.SysFont('timesnewroman', 40, True)
mainFont1 = pygame.font.SysFont('Bahnschrift', 40, True)
mainFont2 = pygame.font.SysFont('Segoe Script', 37, True)

# Split the text into letters
# 3rd parameter is font colour and
# 4th parameter is Font background
letter1 = mainFont.render("H", False, orange, yellow)
letter2 = mainFont.render("A", False, orange, green)
letter3 = mainFont.render("N", False, orange, yellow)
letter4 = mainFont.render("G", False, orange, green)
letter5 = mainFont.render("M", False, orange, yellow)
letter6 = mainFont.render("A", False, orange, green)
letter7 = mainFont.render("N", False, orange, yellow)
letter8 = mainFont.render(" ", False, orange, white)
letter9 = mainFont.render("W", False, orange, yellow)
letter10 = mainFont.render("O", False, orange, green)
letter11 = mainFont.render("R", False, orange, yellow)
letter12 = mainFont.render("D", False, orange, green)
letter13 = mainFont.render(" ", False, orange, white)
letter14 = mainFont.render("G", False, orange, green)
letter15 = mainFont.render("A", False, orange, yellow)
letter16 = mainFont.render("M", False, orange, green)
letter17 = mainFont.render("E", False, orange, yellow)
background_image = pygame.image.load("backgroundastheticRESIZED1.jpg")


nrmlBodyFont = pygame.font.SysFont('caveat.ttf', 30, False)
about1 = nrmlBodyFont.render(
    "Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one  letter at a time. ", True, saddle_brown, white)
about2 = nrmlBodyFont.render(
    "After a certain number of incorrect guesses, the game ends and the player loses.", True, saddle_brown, white)
# if we want the text to be strong then  pass true else false as an parameter
subFont2 = pygame.font.SysFont('chalkduster.ttf', 35, False)
# set_underline function underlines the text if 1 is pass and its intensity increses with increase in number and if 0 no underline
subFont2.set_underline(1)
instructions = subFont2.render(
    "INSTRUCTIONS:", True, black, white)
instruction1 = nrmlBodyFont.render(
    "1. You will get 8 chances to guess a word.", True, saddle_brown, white)
instruction2 = nrmlBodyFont.render(
    "2. When you guess the wrong character your chance will be reduced by one.", True, saddle_brown, white)
instruction3 = nrmlBodyFont.render(
    "3. Only single hint will be provided to you. ", True, saddle_brown, white)

# intiall state of the word
secret_word = choose_word()
s_lenth = len(secret_word)
word_g = ""
# adding spaces after each letter
for i in range(0, s_lenth):
    word_g = word_g+"_   "
guessed_word = mainFont.render(
    word_g, True, maroon, white)
guessed_wordCen = guessed_word.get_rect()
guessed_wordCen.center = (650, 520)


letters_guessed = []
chances = 8


def hint(secret_word, letters_guessed):
    # hint function
    # if a letter of secret word not present in letters guessed then adds that letter to letters_guessed
    for ch in secret_word:
        if ch not in letters_guessed:
            letters_guessed.append(ch)
            break
    g_word = get_guessed_word(secret_word, letters_guessed)
    printFunction(g_word)


def button(word, x, y, w, h, ic, ac, action=None):
    '''buttons structure'''
    # ic stands for inactive color (original state of button) and ac means active color (when mouse is hovered over the button)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        # if the position of the mouse is within the button then change color
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            # if there is a left click  and action provided is not null
            # basically initially click returns (0,0,0) means no clicks
            # (1,0,0) means left click
            # (0,1,0) means center click
            # (0,0,1) means right click
            action()
    else:
        # without mouse position  over the button
        pygame.draw.rect(screen, ic, (x, y, w, h))

    buttonText = pygame.font.Font("freesansbold.ttf", 20)
    buttonTextSurf = buttonText.render(word, True, white)
    buttonTextRect = buttonTextSurf.get_rect()
    buttonTextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(buttonTextSurf, buttonTextRect)
    clock.tick(30)
    # changes 30 frames per second


def printFunction(g_word):
    # Using join() + list comprehension
    # Insert character after every character pair
    if(g_word != ("")):
        res = '    '.join(g_word[i:i + 1]
                          for i in range(0, len(g_word), 1))
        guessed_word = mainFont1.render(
            res, True, maroon, white)
        guessed_wordCen = guessed_word.get_rect()
        guessed_wordCen.center = (650, 520)
        screen.blit(guessed_word, guessed_wordCen)
        pygame.display.update()
        pygame.time.wait(1000)
# updates the screen and waiting time is 1000 miliseconds


alertFont = pygame.font.SysFont('Comic Sans MS', 34)


def input_check(guess):
    # checks for correct input
    if len(guess) != 1 or not guess.isalpha():
        return False
    else:
        return True


def is_word_guessed(secret_word, letters_guessed):
    # tests whether the word has been correctly guessed or not
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    count = 0
    for ch in letters_guessed:
        if ch in secret_word:
            count += 1
    if len(set(secret_word)) == count:
        return True
    else:
        return False
# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''

    letters_left = string.ascii_lowercase
    for ch in letters_guessed:
        letters_left = letters_left.replace(ch, "")
    return letters_left


def printChances(chances):
    # prints chances left
    chance = subFont2.render("Chances: {}".format(
        chances), True, dark_green)
    subFont2.set_underline(0)
    chanceCen = chance.get_rect()
    chanceCen.center = (975, 443)
    screen.blit(chance, chanceCen)
    pygame.display.update()


def printImage(chances):
    # prints corresponding figure for every number of chances left
    if chances == 7:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
    elif chances == 6:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
    elif chances == 5:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
        pygame.draw.line(screen, black, [1100, 300], [1280, 300], 8)
    elif chances == 4:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
        pygame.draw.line(screen, black, [1100, 300], [1280, 300], 8)
        pygame.draw.line(screen, black, [1200, 300], [1200, 350], 8)
    elif chances == 3:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
        pygame.draw.line(screen, black, [1100, 300], [1280, 300], 8)
        pygame.draw.line(screen, black, [1200, 300], [1200, 350], 8)
        pygame.draw.circle(screen, black, [1200, 350], 30)
    elif chances == 2:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
        pygame.draw.line(screen, black, [1100, 300], [1280, 300], 8)
        pygame.draw.line(screen, black, [1200, 300], [1200, 350], 8)
        pygame.draw.circle(screen, black, [1200, 350], 30)
        pygame.draw.line(screen, black, [1200, 350], [1200, 500], 8)
    elif chances == 1:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
        pygame.draw.line(screen, black, [1100, 300], [1280, 300], 8)
        pygame.draw.line(screen, black, [1200, 300], [1200, 350], 8)
        pygame.draw.circle(screen, black, [1200, 350], 30)
        pygame.draw.line(screen, black, [1200, 350], [1200, 500], 8)
        pygame.draw.line(screen, black, [1150, 450], [1200, 430], 8)
        pygame.draw.line(screen, black, [1200, 430], [1250, 450], 8)
    elif chances == 0:
        pygame.draw.rect(screen, black, [1000, 650, 250, 100])
        pygame.draw.line(screen, black, [1100, 650], [1100, 300], 8)
        pygame.draw.line(screen, black, [1100, 300], [1280, 300], 8)
        pygame.draw.line(screen, black, [1200, 300], [1200, 350], 8)
        pygame.draw.circle(screen, black, [1200, 350], 30)
        pygame.draw.line(screen, black, [1200, 350], [1200, 500], 8)
        pygame.draw.line(screen, black, [1150, 450], [1200, 430], 8)
        pygame.draw.line(screen, black, [1200, 430], [1250, 450], 8)
        pygame.draw.line(screen, black, [1150, 520], [1200, 500], 8)
        pygame.draw.line(screen, black, [1200, 500], [1250, 520], 8)
    pygame.display.update()
    pygame.time.delay(1000)


global g_word
g_word = ""
# global declaration of pygame.Surface
global Text3
hint_used = True
running = True
while running:
    # setting a background image
    screen.blit(background_image, [0, 0])
    screen.blit(image1, (0, 0))
    screen.blit(letter1, (125, 20))
    screen.blit(letter2, (156, 20))
    screen.blit(letter3, (187, 20))
    screen.blit(letter4, (218, 20))
    screen.blit(letter5, (250, 20))
    screen.blit(letter6, (281, 20))
    screen.blit(letter7, (313, 20))
    screen.blit(letter8, (344, 20))
    screen.blit(letter9, (373, 20))
    screen.blit(letter10, (413, 20))
    screen.blit(letter11, (443, 20))
    screen.blit(letter12, (470, 20))
    screen.blit(letter13, (495, 20))
    screen.blit(letter14, (528, 20))
    screen.blit(letter15, (559, 20))
    screen.blit(letter16, (590, 20))
    screen.blit(letter17, (628, 20))
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    screen.blit(message, messageRect)

    screen.blit(about1, (0, 200))
    screen.blit(about2, (0, 230))

    screen.blit(instructions, (0, 260))
    screen.blit(instruction1, (0, 300))
    screen.blit(instruction2, (0, 340))
    screen.blit(instruction3, (0, 380))
    screen.blit(guessed_word, guessed_wordCen)

    button("Hint", 300, 420, 100, 50,
           darklightred, lightred)
    pygame.draw.rect(screen, yellow, [900, 420, 150, 50])
    printChances(chances)
    available_letters = get_available_letters(letters_guessed)
    Text3 = subFont.render(
        "Available letters: {} ".format(available_letters), True, black, white)
    screen.blit(Text3, (100, 640))
    printFunction(g_word)
    printImage(chances)
    pygame.display.update()
    pygame.time.delay(1000)
    # updates the screen and delay time is 1000 miliseconds

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            # recognizes a keyboard event
            pressed_key = pygame.key.name(event.key)
# recognizes which key has been pressed
            guess = str(pressed_key)
            letter = guess.lower()
#  converts that to str and lower case
            if not input_check(pressed_key):
                Text = alertFont.render(
                    "Wrong Input!!", True, red, yellow)
                screen.blit(Text, (528, 575))
                pygame.display.update()
                pygame.time.delay(1000)
                continue
            letters_guessed.append(letter)
            available_letters = get_available_letters(letters_guessed)

            if letter in secret_word:

                g_word = get_guessed_word(secret_word, letters_guessed)
                printFunction(g_word)
                Text = alertFont.render(
                    "Good Guess", True, red, yellow)
                screen.blit(Text, (528, 575))
                pygame.display.update()
                pygame.time.delay(1000)

                if is_word_guessed(secret_word, letters_guessed) == True:
                    Text = mainFont2.render(
                        " * * Congratulations, you won! * *", True, orange_red, white)
                    screen.blit(Text, (350, 575))
                    pygame.display.update()
                    pygame.time.delay(100)
                    pygame.quit()
            else:
                Text = alertFont.render(
                    "Oops! That letter is not in my word!! ", True, red, yellow)
                screen.blit(Text, (328, 575))
                letters_guessed.append(letter)
                chances -= 1
                pygame.display.update()
                pygame.time.delay(1000)

            if chances == 0:
                Text = mainFont2.render(
                    "You Lose", True, orange_red, white)
                screen.blit(Text, (528, 620))
                printFunction(secret_word)
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.quit()

        if ((event.type == pygame.MOUSEBUTTONDOWN) and (hint_used == True)):
            # recognises the mouse events
            hint_used = False
            hint(secret_word, letters_guessed)
            if is_word_guessed(secret_word, letters_guessed) == True:
                Text = mainFont2.render(
                    " * * Congratulations, you won! * *", True, orange_red, white)
                screen.blit(Text, (350, 570))
                pygame.display.update()
                pygame.time.delay(1000)
                pygame.quit()
            pygame.display.update()
            # pygame.time.delay(1000)
            clock.tick(300)
        elif ((event.type == pygame.MOUSEBUTTONDOWN) and (hint_used != True)):
            # recognises the mouse events
            # if one hint has been provided already prints an alert
            Text = alertFont.render(
                "No more hints available ", True, red, yellow)
            screen.blit(Text, (450, 575))
            pygame.display.update()
            pygame.time.delay(1000)
    pygame.display.flip()
    # It allows only a portion of the screen to updated, instead of the entire area. If no argument is passed it updates the entire Surface area like pygame. display. flip() .
    clock.tick(30)


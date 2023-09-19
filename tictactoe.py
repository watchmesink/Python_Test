import pprint
# define the board
theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
    'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
    }
# draw the board
def drawBoard(x):
    print(x['top-L'] + '|' + x['top-M'] + '|' + x['top-R'])
    print('-+-+-')
    print(x['mid-L'] + '|' + x['mid-M'] + '|' + x['mid-R'])
    print('-+-+-')
    print(x['low-L'] + '|' + x['low-M'] + '|' + x['low-R'])

# decide who goes first
def definePlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('choose X or Y')
        letter = input().upper()
    if letter  == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

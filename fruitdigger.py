# 10 mango id 1
# 8 apple id 2
# 4 watermelon id 3
# 4 pomgranate id 4
# 3 coconut id 5
# 2 Cherry id 6
# 2 durian id 7
# 1 dragonfruit id 8
# 15 bombs id 9
# 5 rum id 10

import random
import os
import pygame as pyg
import sys

WIN = pyg.display.set_mode((0, 0), pyg.FULLSCREEN)
WIDTH, HEIGHT = pyg.display.get_surface().get_size()
first_cherry = True
next_bomb = True
pyg.display.set_caption("Fruit Digger")
pyg.font.init()
applepng = pyg.image.load(os.path.join("fruit", "apple.png")).convert_alpha()
bombpng = pyg.image.load(os.path.join("fruit", "bomb.png")).convert_alpha()
cherrypng = pyg.image.load(os.path.join("fruit", "cherry.png")).convert_alpha()
coconutpng = pyg.image.load(os.path.join("fruit",
                                         "coconut.png")).convert_alpha()
dragonfruitpng = pyg.image.load(os.path.join(
    "fruit", "dragonfruit.png")).convert_alpha()
durianpng = pyg.image.load(os.path.join("fruit", "durian.png")).convert_alpha()
mangopng = pyg.image.load(os.path.join("fruit", "mango.png")).convert_alpha()
pomegranatepng = pyg.image.load(os.path.join(
    "fruit", "pomegranate.png")).convert_alpha()
rumpng = pyg.image.load(os.path.join("fruit", "rum.png")).convert_alpha()
watermelonpng = pyg.image.load(os.path.join("fruit",
                                            "watermelon.png")).convert_alpha()
sandpng = pyg.image.load(os.path.join("fruit", "sand.jpg")).convert_alpha()
sandstonepng = pyg.image.load(os.path.join("fruit",
                                           "sandstone.png")).convert_alpha()
applepng = pyg.transform.smoothscale(applepng, (120, 120))
bombpng = pyg.transform.smoothscale(bombpng, (120, 120))
cherrypng = pyg.transform.smoothscale(cherrypng, (120, 120))
coconutpng = pyg.transform.smoothscale(coconutpng, (120, 120))
dragonfruitpng = pyg.transform.smoothscale(dragonfruitpng, (120, 120))
durianpng = pyg.transform.smoothscale(durianpng, (120, 120))
mangopng = pyg.transform.smoothscale(mangopng, (120, 120))
pomegranatepng = pyg.transform.smoothscale(pomegranatepng, (120, 120))
rumpng = pyg.transform.smoothscale(rumpng, (120, 120))
watermelonpng = pyg.transform.smoothscale(watermelonpng, (120, 120))
sandpng = pyg.transform.smoothscale(sandpng, (120, 120))
sandstonepng = pyg.transform.smoothscale(sandstonepng, (120, 120))

bigfont = pyg.font.SysFont('arial', 70)

points = 0
moves = 15
duglist = []
mult = 1


def shuffle_board():
    unshuffled = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4,
        4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        9
    ]
    print(len(unshuffled))
    tempcase = 0
    for x in range(0, 10000):
        firstnum = random.randint(0, len(unshuffled) - 1)
        secondnum = random.randint(0, len(unshuffled) - 1)
        tempcase = unshuffled[secondnum]
        unshuffled[secondnum] = unshuffled[firstnum]
        unshuffled[firstnum] = tempcase

    for x in range(0, 5):
        unshuffled[random.randint(0, 48)] = 10

    return unshuffled


def split_list_board(slist):
    table = []
    for x in range(0, 7):
        row = []
        for y in range(0, 7):
            row.append(slist[y + (x * 7)])
            #print(y+(x*7))
        table.append(row)
    return table


def display_board(list):
    for x in range(0, 7):
        row = []
        for y in range(0, 7):
            row.append(list[y + (x * 7)])
            #print(y+(x*7))
        print(row)


shlist = shuffle_board()
table = []
table = split_list_board(shlist)
display_board(shlist)


def spot_checker(x, y, table):
    scan_spots = []
    if y == 0 or y == 6 or x == 0 or x == 6:
        #top left corner
        if y == 0 and x == 0:
            scan_spots = [[table[y][x + 1], x + 1, y],
                          [table[y + 1][x], x, y + 1],
                          [table[y + 1][x + 1], x + 1, y + 1]]
        #top border
        elif y == 0 and x != 0 and x != 6:
            scan_spots = [[table[y][x - 1], x - 1, y],
                          [table[y][x + 1], x + 1, y],
                          [table[y + 1][x - 1], x - 1, y + 1],
                          [table[y + 1][x], x, y + 1],
                          [table[y + 1][x + 1], x + 1, y + 1]]
        #top right corner
        elif y == 0 and x == 6:
            scan_spots = [[table[y][x - 1], x - 1, y],
                          [table[y + 1][x - 1], x - 1, y + 1],
                          [table[y + 1][x], x, y + 1]]
        #left border
        elif y != 0 and y != 6 and x == 0:
            scan_spots = [[table[y - 1][x], x, y - 1],
                          [table[y - 1][x + 1], x + 1, y - 1],
                          [table[y][x + 1], x + 1, y],
                          [table[y + 1][x], x, y + 1],
                          [table[y + 1][x + 1], x + 1, y + 1]]
        #right border
        elif y != 0 and y != 6 and x == 6:
            scan_spots = [[table[y - 1][x - 1], x - 1, y - 1],
                          [table[y - 1][x], x, y - 1],
                          [table[y][x - 1], x - 1, y],
                          [table[y + 1][x - 1], x - 1, y + 1],
                          [table[y + 1][x], x, y + 1]]
        #bottom border
        elif y == 6 and x != 0 and x != 6:
            scan_spots = [[table[y - 1][x - 1], x - 1, y - 1],
                          [table[y - 1][x], x, y - 1],
                          [table[y - 1][x + 1], x + 1, y - 1],
                          [table[y][x - 1], x - 1, y],
                          [table[y][x + 1], x + 1, y]]
        #bottom left corner
        elif y == 6 and x == 0:
            scan_spots = [[table[y - 1][x], x, y - 1],
                          [table[y - 1][x + 1], x + 1, y - 1],
                          [table[y][x + 1], x + 1, y]]
        #bottom right corner
        elif y == 6 and x == 6:
            scan_spots = [[table[y - 1][x - 1], x - 1, y - 1],
                          [table[y - 1][x], x, y - 1],
                          [table[y][x - 1], x - 1, y]]
    else:
        scan_spots = [[table[y - 1][x - 1], x - 1, y - 1],
                      [table[y - 1][x], x, y - 1],
                      [table[y - 1][x + 1], x + 1, y - 1],
                      [table[y][x - 1], x - 1, y], [table[y][x + 1], x + 1, y],
                      [table[y + 1][x - 1], x - 1, y + 1],
                      [table[y + 1][x], x, y + 1],
                      [table[y + 1][x + 1], x + 1, y + 1]]

    scan_spots = board.check_normal(scan_spots)

    return scan_spots


def bomb(x, y, table):
    global next_bomb
    destroyedamount = random.randint(1, 2)
    if next_bomb == True:
        if destroyedamount == 1:
            scan_spots = spot_checker(x, y, table)
            print(scan_spots)
            if (len(scan_spots)) > 0:
                print("ITS NOT TRUE")
                spot = random.randint(0, len(scan_spots))-1
                bombedspot = [scan_spots[spot][1], scan_spots[spot][2]]
                board.destroy(bombedspot[0], bombedspot[1])

        elif destroyedamount == 2:
            scan_spots = spot_checker(x, y, table)
            print(len(scan_spots))
            if (len(scan_spots)) > 0:
                spot = random.randint(0, len(scan_spots))-1
                bombedspot = [scan_spots[spot][1], scan_spots[spot][2]]
                board.destroy(bombedspot[0], bombedspot[1])
    next_bomb = True


# 10 mango id 1
# 8 apple id 2
# 4 watermelon id 3
# 4 pomgranate id 4
# 3 coconut id 5
# 2 Cherry id 6
# 2 durian id 7
# 1 dragonfruit id 8
# 15 bombs id 9
# 5 rum id 10
def mango(x, y, table):
    global points, mult
    points += 300*mult
    mult = 1


def apple(x, y, table):
    global points, mult
    applecount = 0
    for x in duglist:
        if x == 2:
            applecount += 1
    points += (applecount * 100)*mult
    mult = 1


def watermelon(x, y, table):
    global points, mult
    scan_spots = spot_checker(x, y, table)
    goodscan_spots = []
    points+=100*mult
    mult = 1
    for obj in scan_spots:
        if obj[0] == 1 or obj[0] == 2 or obj[0] == 3 or obj[0] == 4 or obj[
                0] == 5 or obj[0] == 6 or obj[0] == 7 or obj[0] == 8:
            goodscan_spots.append(obj)
    if len(goodscan_spots) > 0:
        spot = random.randint(0, len(goodscan_spots))-1
        bombedspot = [scan_spots[spot][1], scan_spots[spot][2]]
        board.watermelonpop(bombedspot[0], bombedspot[1])
    

    #table[bombedspot[1], bombedspot[0]]
def pomegranate(x, y, table):
    global points, mult
    points += 200 * mult
    mult = 1.5
    


def coconut(x, y, table):
    global points, mult, next_bomb
    points += 200*mult
    next_bomb = False


def cherry(x, y, table):
    global points, mult, first_cherry
    if first_cherry == True:
        points += 200*mult
        first_cherry = False
    else:
        points += 500*mult

def durian(x, y, table):
    global points, mult
    points += 800 * mult
    mult = .5


def dragonfruit(x, y, table):
    global points, mult
    points += 1200


def rum(x, y, table):
    pass


digdict = {
    1: mango,
    2: apple,
    3: watermelon,
    4: pomegranate,
    5: coconut,
    6: cherry,
    7: durian,
    8: dragonfruit,
    9: bomb,
    10: rum
}
pngdict = {
    1: mangopng,
    2: applepng,
    3: watermelonpng,
    4: pomegranatepng,
    5: coconutpng,
    6: cherrypng,
    7: durianpng,
    8: dragonfruitpng,
    9: bombpng,
    10: rumpng
}
# pointdict = {
#     1:300,
#     2:apple,
#     3:watermelon,
#     4:pomegranate,
#     5:coconut,
#     6:cherry,
#     7:durian,
#     8:dragonfruit,
#     9:bomb,
#     10:rum
# }


class Spot(pyg.sprite.Sprite):

    def __init__(self, x, y, id, group, icon):
        super().__init__(group)
        self.x = x
        self.y = y
        self.id = id
        self.image = sandpng
        self.broken = sandstonepng
        self.under = icon
        self.normal = True
        self.flipped = False
        self.scanned = False
        self.cracked = False


class Board(pyg.sprite.Group):

    def __init__(self):
        super().__init__()

    def draw(self):
        for sprite in self.sprites():
            if sprite.flipped == True:
                WIN.blit(sprite.under,
                         (playarea / 7 * sprite.x, HEIGHT / 7 * sprite.y))
            elif sprite.cracked == True:
                WIN.blit(sprite.broken,
                         (playarea / 7 * sprite.x, HEIGHT / 7 * sprite.y))
            elif sprite.scanned == True:
                WIN.blit(sprite.image,
                         (playarea / 7 * sprite.x, HEIGHT / 7 * sprite.y))
                WIN.blit(sprite.under,
                         (playarea / 7 * sprite.x, HEIGHT / 7 * sprite.y))
            else:
                WIN.blit(sprite.image,
                         (playarea / 7 * sprite.x, HEIGHT / 7 * sprite.y))

    def watermelonpop(self, spotx, spoty):
        for sprite in self.sprites():
            #print(f"{spotx} bombed x")
            #print(f"{sprite.x} checked x")
            #print(f"{spoty} bombed y")
            #print(f"{sprite.y} checked y")
            if spotx == sprite.x and spoty == sprite.y:
                sprite.flipped = True
                sprite.normal = False
                digdict[sprite.id](sprite.x, sprite.y, table)
        print("AGGG")

    def check_normal(self, scan_spots):
        cleaned_spots = []
        for sprite in self.sprites():
            for obj in scan_spots:
                if sprite.x == obj[1] and sprite.y == obj[2]:
                    if sprite.normal == True:
                        cleaned_spots.append(obj)

        return cleaned_spots

    def clickcheck(self, mouse):
        for sprite in self.sprites():
            if sprite.normal == True:
                #print(f"{playarea/7*sprite.x} to {(playarea/7*sprite.x)+120}\n{HEIGHT/7*sprite.y} to {(HEIGHT/7*sprite.y)+120}\nmouse is {mouse}")
                #print(f"{mouse[0]} >= {playarea/7*sprite.x}")
                if mouse[0] >= playarea / 7 * sprite.x and mouse[0] <= (
                        playarea / 7 * sprite.x
                ) + 120 and mouse[1] >= HEIGHT / 7 * sprite.y and mouse[
                        1] <= HEIGHT / 7 * sprite.y + 120:
                    sprite.flipped = True
                    sprite.normal = False
                    sprite.scanned = False
                    duglist.append(sprite.id)
                    digdict[sprite.id](sprite.x, sprite.y, table)

    def destroy(self, spotx, spoty):
        for sprite in self.sprites():
            #print(f"{spotx} bombed x")
            #print(f"{sprite.x} checked x")
            #print(f"{spoty} bombed y")
            #print(f"{sprite.y} checked y")
            if spotx == sprite.x and spoty == sprite.y:
                sprite.cracked = True
                sprite.normal = False
                print("ASDHASDK")
        print("AGGG")


def mine(x, y, table, mode):
    pass


def bomb_dowse(x, y, table):
    bombcount = 0
    scan_spots = spot_checker(x, y, table)
    for x in scan_spots:
        if x[0] == 9:
            bombcount += 1
    return bombcount

def lowestfruit_dowse(x,y,table):
    pointoptions = []
    lowestpoint = []
    scan_spots = spot_checker(x,y,table)
    print(scan_spots)
    for x in scan_spots:
        pointoptions.append([pointdict[x[0]], x])
    for x in range(0,len(pointoptions)-1):
        if pointoptions[x][0] < pointoptions[x+1][0] and pointoptions[x][0] <10000:
            lowestpoint = pointoptions[x][1]
        
    return lowestpoint



pointdict = {
    1: 300,
    2: 0,
    3: 100,
    4: 200,
    5: 200,
    6: 200,
    7: 800,
    8: 1200,
    9: 100000,
    10: 1000000,
}
# for y in range(0, 7):
#     for x in range(0,7):
#         print(f"There are {bomb_dowse(x,y,table)} bombs nearby at pos ({x}, {y})")
#print(bomb_dowse(0,0,table))

#bomb(1,1,table)
#bomb(1,1,table)
#bomb(1,1,table)
WIN.fill((94, 128, 87))
playarea = WIDTH - 200
board = Board()
pyg.display.update()

run = True
for y in range(0, 7):
    for x in range(0, 7):
        #WIN.blit(sandpng,(playarea/7*x, HEIGHT/7*y) )
        Spot(x, y, table[y][x], board, pngdict[table[y][x]])
lowestfruit_dowse(1,1,table)
while run == True:
    mouse = pyg.event.get()
    mouse = pyg.mouse.get_pos()
    WIN.fill((94, 128, 87))
    counter = bigfont.render(f'{points}', True, (255,255,255))
    WIN.blit(counter, (playarea, 20))
    board.draw()
    pyg.display.update()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
            pyg.quit()
            sys.exit()
        if event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE:
            run = False
            pyg.quit()
            sys.exit()
        if event.type == pyg.MOUSEBUTTONDOWN:
            board.clickcheck(mouse)

pyg.quit()

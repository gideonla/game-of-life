import pygame
import random
import collections
import pdb
import numpy as np
import time


BLOCK_SIZE = 50


def check_overlap(list1, val):
    '''
    Check if val is close by upto 5 to any number in list1. if so return True
    :param list1: list of numbers
    :param val: value to assess
    :return: True/False
    '''
    for x in list1:
        if (val > (x - BLOCK_SIZE) and val < x):
            return True
        else:
            return False
    return False  # if list is empty then obviously nothing is in the list


def draw_blocks(num_of_blocks):
    for i in range(0, num_of_blocks):
        # pdb.set_trace()
        x_rand_location = coordinate_list[
            random.randint(0, len(coordinate_list) - 1)]
        y_rand_location = coordinate_list[
            random.randint(0, len(coordinate_list) - 1)]
        # check if new block overlaps over existing block
        while check_overlap(x_block_locs, x_rand_location):
            x_rand_location = coordinate_list[
                random.randint(0, len(coordinate_list) - 1)]  # it's 495 and not 500 b/c the block size is 5
        while check_overlap(y_block_locs, y_rand_location):
            y_rand_location = coordinate_list[
                random.randint(0, len(coordinate_list) - 1)]  # it's 495 and not 500 b/c the block size is 5
        pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                         (x_rand_location, y_rand_location, BLOCK_SIZE, BLOCK_SIZE))
        # pop the first block if list is full
        x_block_locs.append(x_rand_location)
        y_block_locs.append(y_rand_location)
        board[int(x_rand_location/BLOCK_SIZE),int(y_rand_location/BLOCK_SIZE)]=True


def check_neighbours(listx, listy, x, y):
    '''
    Check if val is close by upto 5 to any number in list1. if so return True
    :param listx: list of x coordinates of squares
    :param listy: list of y coordinates of squares
    :param x: square x coor
    :param y: square y coor
    :return: True/False
    '''
    num__of_neighbours = 0
    for i in range(0, len(listx)):
        #pdb.set_trace()
        if (x - BLOCK_SIZE == listx[i] or x + BLOCK_SIZE == listx[i]) and (y == listy[i] or (y + BLOCK_SIZE ) == listy[i] or (y - BLOCK_SIZE) == listy[i]): #neiboughr is to the right/left of current block
            num__of_neighbours = num__of_neighbours+1
        if (x==listx[i]) and (y==listy[i]-BLOCK_SIZE) or (y==listy[i]+BLOCK_SIZE):
            num__of_neighbours = num__of_neighbours + 1
    return num__of_neighbours  # if list is empty then obviously nothing is in the list

def check_neighbours2(input_board, x, y):
    '''

    '''
    num__of_neighbours = 0
    mod = len(coordinate_list)
    if input_board[(x+1)%mod,y]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[(x-1)%mod,y]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[(x+1)%mod,(y+1)%mod]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[(x+1)%mod,(y-1)%mod]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[x,(y+1)%mod]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[x,(y-1)%mod]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[(x-1)%mod,(y-1)%mod]:
        num__of_neighbours=num__of_neighbours+1
    if input_board[(x-1)%mod,(y+1)%mod]:
        num__of_neighbours=num__of_neighbours+1

    return num__of_neighbours  # if list is empty then obviously nothing is in the list


# parameter block
(width, height) = (500, 500)
coordinate_list = [x for x in range(0, width, BLOCK_SIZE)]
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('game of life')
pygame.display.set_mode((width, height))
board = np.zeros((int(height/BLOCK_SIZE),int(height/BLOCK_SIZE)), dtype=bool)

# set up a random ititial state
number_of_blocks = random.randint(15, 15)
x_block_locs = collections.deque(number_of_blocks * [0], number_of_blocks)
y_block_locs = collections.deque(number_of_blocks * [0], number_of_blocks)
screen.fill((255, 255, 255))

draw_blocks(number_of_blocks)
# pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
#                          (0, 0, BLOCK_SIZE, BLOCK_SIZE))
# pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
#                          (0, 50, BLOCK_SIZE, BLOCK_SIZE))
# x_block_locs = collections.deque([0, 0], maxlen=2)
# y_block_locs = collections.deque([0,50], maxlen=2)
pygame.display.flip()

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #print(pygame.mouse.get_pos())
    screen.fill((255, 255, 255))
    for i in range(0, len(coordinate_list)):
        for j in range(0, len(coordinate_list)):
            res=(check_neighbours2(board,i,j))
            print (i,j,res)
            if res<2:
                board[i, j] = board[i,j] and False
            if 2<=res <=3:
                board[i, j] = board[i, j] and True
            if res >3:
                board[i, j] = board[i, j] and False
            if res == 3 and not board[i, j]:
                board[i, j] = True
            if board[i,j]:
                pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                                 (i*BLOCK_SIZE, j*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    #time.sleep(2)


    # pygame.draw.rect(screen, (0,0,0), (200, 150, 10, 10))
    pygame.display.flip()

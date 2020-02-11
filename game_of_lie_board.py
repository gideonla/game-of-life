import pygame
import random
import numpy as np
import pdb

BLOCK_SIZE = 50
x_block_locs = []
y_block_locs = []

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
        #pop the first block if list is full
        if (len(x_block_locs)>=num_of_blocks):
            x_tmp=x_block_locs[1:]
            x_block_locs=x_tmp
            bla = y_block_locs[1:]
        x_block_locs.append(x_rand_location)
        y_block_locs.append(y_rand_location)


# def check_neighbours(listx,listy, x,y):
#     '''
#     Check if val is close by upto 5 to any number in list1. if so return True
#     :param listx: list of x coordinates of squares
#     :param listy: list of y coordinates of squares
#     :param x: square x coor
#     :param y: square y coor
#     :return: True/False
#     '''
#     num__of_neighbours=0
#     for i in range(0,listx):
#         if x+BLOCK_SIZE+1==listx[i] and y>=listy[i] and y <=
#
#
#             return True
#         else:
#             return False
#     return False  # if list is empty then obviously nothing is in the list


# parameter block
(width, height) = (500, 500)
coordinate_list = [x for x in range(0, 500, BLOCK_SIZE)]
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('game of life')
pygame.display.set_mode((width, height))

# set up a random ititial state
number_of_blocks = random.randint(40, 40)
print(number_of_blocks)
screen.fill((255, 255, 255))

draw_blocks(number_of_blocks)
pygame.display.flip()
pdb.set_trace()

running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(pygame.mouse.get_pos())
    screen.fill((255, 255, 255))
    for i in range(0, len(x_block_locs)):
        pdb.set_trace()
        draw_blocks(number_of_blocks)
    # pygame.draw.rect(screen, (0,0,0), (200, 150, 10, 10))
    pygame.display.flip()

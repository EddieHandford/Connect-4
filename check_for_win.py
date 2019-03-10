# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:43:44 2019

@author: Eddie
"""
import numpy as np
    

#takes current board state
#height and width of board
#player number who just moved


#improvements to make :
#derive height and width from board shape


#bugs known:
#none


def check_for_win(board , height , width , player):

    # check horizontal spaces
    for y in range(height):
        for x in range(width - 4):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True

    # check vertical spaces
    for y in range(width):
        for x in range(height - 4):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                return True

    # check / diagonal spaces
    for y in range(width - 4):
        for x in range(4 - height):
            if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True

    # check \ diagonal spaces
    for y in range(width - 4):
        for x in range(height - 4):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True

    return False
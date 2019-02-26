# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:36:22 2019

@author: kulka
"""

from IPython.display import clear_output
import random
import sys

marker_player1='X'
marker_player2='O'
player2_win = False
player1_win = False
board = ['_','_','_','_','_','_','_','_','_']
def display_board(board):
    for pos in range(0,9,3):
        if len(board) > 9 or len(board) < 9:
            print("Enter 9 values")
        else:
            print(board[pos],board[pos+1],board[pos+2])
def player_input():
        marker_player1 = input("Player 1 Please pick a marker 'X' or 'O'\n")
        if marker_player1.upper() == 'X':
            marker_player1 ='X'
            marker_player2 ='O'
            print("Player 1 , your marker is X")
            print("Player 2 , your marker is O")
            ref_board()
            display_board(board)
            return (marker_player1, marker_player2)
            
        elif marker_player1.upper() == 'O':
            marker_player1 ='O'
            marker_player2 ='X'
            print("Player 1 , your marker is O")
            print("Player 2 , your marker is X")
            ref_board()
            display_board(board)
            return (marker_player1, marker_player2)
        else:
            print("Please select either X or O")
            player_input()
        return (marker_player1, marker_player2)

        
    

def accept_position_1():
        x1 = int(input("Player 1 Enter position\n"))
        x1 = change_pos(x1)
        if x1<1 or x1>9:
            print("Please choose a number between 1 and 9\n")
            accept_position_1()
        if board[x1-1] != 'X' and board[x1-1] != 'O':
            place_marker(board,marker_player1,x1-1)
        else:
            print("Position already used,please choose a new position\n")
            accept_position_1()
        ref_board()
        display_board(board)
        win_check(board,marker_player1)
        return board

def accept_position_2():

        x2 = int(input("Player 2 Enter position\n"))
        x2 = change_pos(x2)
        if x2<1 or x2>9:
            print("Please choose a number between 1 and 9\n")
            accept_position_2()
        if board[x2-1] != 'X' and board[x2-1] != 'O':
            place_marker(board,marker_player2,x2-1)
        else:
            print("Position already used,please choose a new position\n")
            accept_position_2()
        ref_board()
        display_board(board)
        win_check(board,marker_player2)
        return board

def change_pos(pos1):
    if pos1 == 1:
        pos2=7
    if pos1 == 2:
        pos2=8
    if pos1 == 3:
        pos2=9
    if pos1 == 7:
        pos2=1
    if pos1 == 8:
        pos2=2
    if pos1 == 9:
        pos2=3
    if pos1 == 5:
        pos2 = 5
    if pos1 == 6:
        pos2 = 6
    if pos1 == 4:
        pos2 = 4
    return pos2

def place_marker(board, marker, position):
    board[position]= marker
    return board

def win_check(board, mark):
    player1_win = False
    player2_win = False
    if (board[0]==mark and board[1] == mark and board[2] ==mark) or (board[3]==mark and board[4] ==mark and board[5] ==mark):
        if mark=='X' and marker_player1=='X':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        elif mark=='O' and marker_player1=='O':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        else:
            print("Player 2 wins!\n")
            player2_win = True
            player1_win = False
            sys.exit(0)
    if (board[6]==mark and board[7] == mark and board[8] ==mark) or (board[0]==mark and board[3] ==mark and board[6] ==mark):
        if mark=='X' and marker_player1=='X':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        elif mark=='O' and marker_player1=='O':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        else:
            print("Player 2 wins!\n")
            player2_win = True
            player1_win = False
            sys.exit(0)
    if (board[1]==mark and board[4] == mark and board[7] ==mark) or (board[2]==mark and board[5] ==mark and board[8] ==mark):
        if mark=='X' and marker_player1=='X':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        elif mark=='O' and marker_player1=='O':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        else:
            print("Player 2 wins!\n")
            player2_win = True
            player1_win = False
            sys.exit(0)
    if (board[0]==mark and board[4] == mark and board[8] ==mark) or (board[2]==mark and board[4] ==mark and board[6] ==mark):
        if mark=='X' and marker_player1=='X':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        elif mark=='O' and marker_player1=='O':
            print("Player 1 wins!\n")
            player1_win = True
            player2_win = False
            sys.exit(0)
        else:
            print("Player 2 wins!\n")
            player2_win = True
            player1_win = False
            sys.exit(0)
    return(player1_win,player2_win)


    
print('Welcome to Tic Tac Toe!')

def ref_board():
    print("Please note board positions")
    board_dis = ['7','8','9','4','5','6','1','2','3']
    for pos in range(0, 9, 3):
        print(board_dis[pos], board_dis[pos + 1], board_dis[pos + 2])
    print("\n")
[marker_player1,marker_player2]=player_input()
toss = random.randint(1,101)
if toss % 2 == 0:
        accept_position_2()
        accept_position_1()
        accept_position_2()
        accept_position_1()
        accept_position_2()
        accept_position_1()
        accept_position_2()
        accept_position_1()
        accept_position_2()

else:
        accept_position_1()
        accept_position_2()
        accept_position_1()
        accept_position_2()
        accept_position_1()
        accept_position_2()
        accept_position_1()
        accept_position_2()
        accept_position_1()
if player1_win == False and player2_win == False:
    print("It's a tie!")


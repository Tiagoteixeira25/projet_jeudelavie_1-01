# -*- coding: utf-8 -*-


from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 

from jdlv_data import * 
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid

def make_diamond (grid, i, j, colors):
    try:
        grid = clean_grid(grid)
        cases = grid.cases
        cases[i] [j] ['s'] = life_status
        cases[i] [j] ['c'] = colors
    except:
        pass
    return grid

def make_figure_figee (grid, i, j, colors):
    try:
        
        cases = grid.cases
        cases [i + 5] [j + 60] ['s'] = life_status
        cases [i + 5] [j + 60] ['c'] = colors
        cases [i + 4] [j + 61] ['s'] = life_status
        cases [i + 4] [j + 61] ['c'] = colors
        cases [i + 4] [j + 62] ['s'] = life_status
        cases [i + 4] [j + 62] ['c'] = colors
        cases [i + 4] [j + 63] ['s'] = life_status
        cases [i + 4] [j + 63] ['c'] = colors
        cases [i + 4] [j + 64] ['s'] = life_status
        cases [i + 4] [j + 64] ['c'] = colors
        cases [i + 4] [j + 65] ['s'] = life_status
        cases [i + 4] [j + 65] ['c'] = colors
        cases [i + 6] [j + 62] ['s'] = life_status
        cases [i + 6] [j + 62] ['c'] = colors
        cases [i + 6] [j + 60] ['s'] = life_status
        cases [i + 6] [j + 60] ['c'] = colors
        cases [i + 7] [j + 60] ['s'] = life_status
        cases [i + 7] [j + 60] ['c'] = colors
        cases [i + 8] [j + 60] ['s'] = life_status
        cases [i + 8] [j + 60] ['c'] = colors
        cases [i + 9] [j + 61] ['s'] = life_status
        cases [i + 9] [j + 61] ['c'] = colors
        cases [i + 10] [j + 62] ['s'] = life_status
        cases [i + 10] [j + 62] ['c'] = colors
        cases [i + 11] [j + 63] ['s'] = life_status
        cases [i + 11] [j + 63] ['c'] = colors
        cases [i + 12] [j + 62] ['s'] = life_status
        cases [i + 12] [j + 62] ['c'] = colors
        cases [i + 13] [j + 61] ['s'] = life_status
        cases [i + 13] [j + 61] ['c'] = colors
        cases [i + 14] [j + 60] ['s'] = life_status
        cases [i + 14] [j + 60] ['c'] = colors
        cases [i + 15] [j + 60] ['s'] = life_status 
        cases [i + 15] [j + 60] ['c'] = colors
        cases [i + 16] [j + 60] ['s'] = life_status
        cases [i + 16] [j + 60] ['c'] = colors
        cases [i + 17] [j + 60] ['s'] = life_status
        cases [i + 17] [j + 60] ['c'] = colors
        cases [i + 17] [j + 59] ['s'] = life_status
        cases [i + 17] [j + 59] ['c'] = colors
        cases [i + 17] [j + 58] ['s'] = life_status
        cases [i + 17] [j + 58] ['c'] = colors
        cases [i + 17] [j + 57] ['s'] = life_status
        cases [i + 17] [j + 57] ['c'] = colors
        cases [i + 16] [j + 56] ['s'] = life_status
        cases [i + 16] [j + 56] ['c'] = colors
        cases [i + 18] [j + 56] ['s'] = life_status
        cases [i + 18] [j + 56] ['c'] = colors
        cases [i + 18] [j + 60] ['s'] = life_status
        cases [i + 18] [j + 60] ['c'] = colors
        cases [i + 19] [j + 60] ['s'] = life_status
        cases [i + 19] [j + 60] ['c'] = colors
        cases [i + 20] [j + 60] ['s'] = life_status
        cases [i + 20] [j + 60] ['c'] = colors
        cases [i + 21] [j + 60] ['s'] = life_status
        cases [i + 21] [j + 60] ['c'] = colors
        cases [i + 22] [j + 60] ['s'] = life_status
        cases [i + 22] [j + 60] ['c'] = colors
        cases [i + 23] [j + 60] ['s'] = life_status
        cases [i + 23] [j + 60] ['c'] = colors
        cases [i + 24] [j + 60] ['s'] = life_status
        cases [i + 24] [j + 60] ['c'] = colors
        cases [i + 25] [j + 60] ['s'] = life_status
        cases [i + 25] [j + 60] ['c'] = colors
        cases [i + 26] [j + 60] ['s'] = life_status
        cases [i + 26] [j + 60] ['c'] = colors
        cases [i + 27] [j + 60] ['s'] = life_status
        cases [i + 27] [j + 60] ['c'] = colors
        cases [i + 28] [j + 60] ['s'] = life_status
        cases [i + 28] [j + 60] ['c'] = colors
        cases [i + 29] [j + 60] ['s'] = life_status
        cases [i + 29] [j + 60] ['c'] = colors
        cases [i + 30] [j + 60] ['s'] = life_status
        cases [i + 30] [j + 60] ['c'] = colors
        cases [i + 31] [j + 60] ['s'] = life_status
        cases [i + 31] [j + 60] ['c'] = colors
        cases [i + 32] [j + 60] ['s'] = life_status
        cases [i + 32] [j + 60] ['c'] = colors
        cases [i + 32] [j + 59] ['s'] = life_status
        cases [i + 32] [j + 59] ['c'] = colors
        cases [i + 32] [j + 58] ['s'] = life_status
        cases [i + 32] [j + 58] ['c'] = colors
        cases [i + 5] [j + 66] ['s'] = life_status
        cases [i + 5] [j + 66] ['c'] = colors
        cases [i + 6] [j + 66] ['s'] = life_status
        cases [i + 6] [j + 66] ['c'] = colors
        cases [i + 7] [j + 66] ['s'] = life_status
        cases [i + 7] [j + 66] ['c'] = colors
        cases [i + 8] [j + 66] ['s'] = life_status
        cases [i + 8] [j + 66] ['c'] = colors
        cases [i + 9] [j + 66] ['s'] = life_status
        cases [i + 9] [j + 66] ['c'] = colors
        cases [i + 10] [j + 66] ['s'] = life_status
        cases [i + 10] [j + 66] ['c'] = colors
        cases [i + 11] [j + 66] ['s'] = life_status
        cases [i + 11] [j + 66] ['c'] = colors
        cases [i + 12] [j + 66] ['s'] = life_status
        cases [i + 12] [j + 66] ['c'] = colors
        cases [i + 13] [j + 66] ['s'] = life_status
        cases [i + 13] [j + 66] ['c'] = colors
        cases [i + 14] [j + 66] ['s'] = life_status
        cases [i + 14] [j + 66] ['c'] = colors
        cases [i + 32] [j + 66] ['s'] = life_status
        cases [i + 32] [j + 66] ['c'] = colors
        cases [i + 32] [j + 65] ['s'] = life_status
        cases [i + 32] [j + 65] ['c'] = colors
        cases [i + 32] [j + 64] ['s'] = life_status
        cases [i + 32] [j + 64] ['c'] = colors
        cases [i + 28] [j + 66] ['s'] = life_status
        cases [i + 28] [j + 66] ['c'] = colors
        cases [i + 29] [j + 66] ['s'] = life_status
        cases [i + 29] [j + 66] ['c'] = colors
        cases [i + 30] [j + 66] ['s'] = life_status
        cases [i + 30] [j + 66] ['c'] = colors
        cases [i + 31] [j + 66] ['s'] = life_status
        cases [i + 31] [j + 66] ['c'] = colors
        cases [i + 27] [j + 66] ['s'] = life_status
        cases [i + 27] [j + 66] ['c'] = colors
        cases [i + 27] [j + 65] ['s'] = life_status
        cases [i + 27] [j + 65] ['c'] = colors
        cases [i + 27] [j + 64] ['s'] = life_status
        cases [i + 27] [j + 64] ['c'] = colors
        cases [i + 27] [j + 63] ['s'] = life_status
        cases [i + 27] [j + 63] ['c'] = colors
        cases [i + 27] [j + 62] ['s'] = life_status
        cases [i + 27] [j + 62] ['c'] = colors
        cases [i + 27] [j + 61] ['s'] = life_status
        cases [i + 27] [j + 61] ['c'] = colors
        cases [i + 27] [j + 67] ['s'] = life_status
        cases [i + 27] [j + 67] ['c'] = colors
        cases [i + 27] [j + 68] ['s'] = life_status
        cases [i + 27] [j + 68] ['c'] = colors
        cases [i + 27] [j + 69] ['s'] = life_status
        cases [i + 27] [j + 69] ['c'] = colors
        cases [i + 27] [j + 70] ['s'] = life_status
        cases [i + 27] [j + 70] ['c'] = colors
        cases [i + 27] [j + 71] ['s'] = life_status
        cases [i + 27] [j + 71] ['c'] = colors
        cases [i + 26] [j + 72] ['s'] = life_status
        cases [i + 26] [j + 72] ['c'] = colors
        cases [i + 25] [j + 73] ['s'] = life_status
        cases [i + 25] [j + 73] ['c'] = colors
        cases [i + 24] [j + 74] ['s'] = life_status
        cases [i + 24] [j + 74] ['c'] = colors
        cases [i + 23] [j + 75] ['s'] = life_status
        cases [i + 23] [j + 75] ['c'] = colors
        cases [i + 22] [j + 75] ['s'] = life_status
        cases [i + 22] [j + 75] ['c'] = colors
        cases [i + 21] [j + 75] ['s'] = life_status
        cases [i + 21] [j + 75] ['c'] = colors
        cases [i + 20] [j + 75] ['s'] = life_status
        cases [i + 20] [j + 75] ['c'] = colors
        cases [i + 19] [j + 75] ['s'] = life_status
        cases [i + 19] [j + 75] ['c'] = colors
        cases [i + 18] [j + 75] ['s'] = life_status
        cases [i + 18] [j + 75] ['c'] = colors
        cases [i + 17] [j + 75] ['s'] = life_status
        cases [i + 17] [j + 75] ['c'] = colors
        cases [i + 16] [j + 75] ['s'] = life_status
        cases [i + 16] [j + 75] ['c'] = colors
        cases [i + 15] [j + 75] ['s'] = life_status
        cases [i + 15] [j + 75] ['c'] = colors
        cases [i + 14] [j + 75] ['s'] = life_status
        cases [i + 14] [j + 75] ['c'] = colors
        cases [i + 13] [j + 75] ['s'] = life_status
        cases [i + 13] [j + 75] ['c'] = colors
        cases [i + 12] [j + 75] ['s'] = life_status
        cases [i + 12] [j + 75] ['c'] = colors
        cases [i + 11] [j + 74] ['s'] = life_status
        cases [i + 11] [j + 74] ['c'] = colors
        cases [i + 10] [j + 73] ['s'] = life_status
        cases [i + 10] [j + 73] ['c'] = colors
        cases [i + 9] [j + 72] ['s'] = life_status
        cases [i + 9] [j + 72] ['c'] = colors
        cases [i + 10] [j + 72] ['s'] = life_status
        cases [i + 10] [j + 72] ['c'] = colors
        cases [i + 11] [j + 72] ['s'] = life_status
        cases [i + 11] [j + 72] ['c'] = colors
        cases [i + 12] [j + 72] ['s'] = death_status
        cases [i + 12] [j + 72] ['c'] = colors
        cases [i + 13] [j + 72] ['s'] = life_status
        cases [i + 13] [j + 72] ['c'] = colors
        cases [i + 14] [j + 72] ['s'] = life_status
        cases [i + 14] [j + 72] ['c'] = colors
        cases [i + 14] [j + 71] ['s'] = life_status
        cases [i + 14] [j + 71] ['c'] = colors
        cases [i + 14] [j + 70] ['s'] = life_status
        cases [i + 14] [j + 70] ['c'] = colors
        cases [i + 14] [j + 69] ['s'] = life_status
        cases [i + 14] [j + 69] ['c'] = colors
        cases [i + 14] [j + 68] ['s'] = life_status
        cases [i + 14] [j + 68] ['c'] = colors
        cases [i + 14] [j + 67] ['s'] = life_status
        cases [i + 14] [j + 67] ['c'] = colors
        cases [i + 32] [j + 5] ['s'] = life_status
        cases [i + 32] [j + 5] ['c'] = colors
        cases [i + 32] [j + 7] ['s'] = life_status
        cases [i + 32] [j + 7] ['c'] = colors
        cases [i + 31] [j + 5] ['s'] = life_status
        cases [i + 31] [j + 5] ['c'] = colors
        cases [i + 31] [j + 7] ['s'] = life_status
        cases [i + 31] [j + 7] ['c'] = colors
        cases [i + 30] [j + 6] ['s'] = life_status
        cases [i + 30] [j + 6] ['c'] = colors
        cases [i + 30] [j + 5] ['s'] = life_status
        cases [i + 30] [j + 5] ['c'] = colors
        cases [i + 30] [j + 7] ['s'] = life_status
        cases [i + 30] [j + 7] ['c'] = colors
        cases [i + 29] [j + 5] ['s'] = life_status
        cases [i + 29] [j + 5] ['c'] = colors
        cases [i + 29] [j + 7] ['s'] = life_status
        cases [i + 29] [j + 7] ['c'] = colors
        cases [i + 28] [j + 5] ['s'] = life_status
        cases [i + 28] [j + 5] ['c'] = colors
        cases [i + 28] [j + 7] ['s'] = life_status
        cases [i + 28] [j + 7] ['c'] = colors
        cases [i + 28] [j + 6] ['s'] = life_status
        cases [i + 28] [j + 6] ['c'] = colors
        cases [i + 29] [j + 6] ['s'] = life_status
        cases [i + 29] [j + 6] ['c'] = colors
        cases [i + 28] [j + 8] ['s'] = life_status
        cases [i + 28] [j + 8] ['c'] = colors
        cases [i + 28] [j + 9] ['s'] = life_status
        cases [i + 28] [j + 9] ['c'] = colors
        cases [i + 27] [j + 10] ['s'] = life_status
        cases [i + 27] [j + 10] ['c'] = colors
        cases [i + 27] [j + 9] ['s'] = life_status
        cases [i + 27] [j + 9] ['c'] = colors
        cases [i + 25] [j + 5] ['s'] = life_status
        cases [i + 25] [j + 5] ['c'] = colors
        cases [i + 25] [j + 7] ['s'] = life_status
        cases [i + 25] [j + 7] ['c'] = colors
        cases [i + 25] [j + 6] ['s'] = life_status
        cases [i + 25] [j + 6] ['c'] = colors
        cases [i + 26] [j + 5] ['s'] = life_status
        cases [i + 26] [j + 5] ['c'] = colors
        cases [i + 26] [j + 7] ['s'] = life_status
        cases [i + 26] [j + 7] ['c'] = colors
        cases [i + 26] [j + 6] ['s'] = life_status
        cases [i + 26] [j + 6] ['c'] = colors
        cases [i + 27] [j + 6] ['s'] = life_status
        cases [i + 27] [j + 6] ['c'] = colors
    except:
        pass
    return grid

def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def apply_rules (grid, cpt):
     if (cpt  + 1) % 20 != 0:
         print ("CPT % 11  is  0")
         next_grid = \
             make_figure_figee (grid, cpt + 4, cpt + 4, 'black') 
         grid.cases [4] [cpt + 4] = \
             revive_case (grid.cases [4] [cpt + 4])
         grid.cases [cpt + 4] [20 + 4] = \
             revive_case (grid.cases [cpt + 4] [20 + 4])
         next_grid = grid
     else:
         cpt = cpt
         print ("CPT % 11 is NOT 0")
         time.sleep (0.2)
         #next_grid = apply_game_of_life_rules (grid)
         grid.cases [cpt - (cpt  + 1) % 20 + 4] [4] = \
             revive_case (grid.cases [cpt - (cpt  + 1) % 20 + 4] [4])
         next_grid = grid
         next_grid = apply_game_of_life_rules (grid)
         return next_grid
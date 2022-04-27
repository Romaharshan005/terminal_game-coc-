from builtins import print
from select import select
from shutil import which
from matplotlib.pyplot import flag
import numpy as np
import time
# from hut import Hut
from src.heroes import *
from src.input import *
from colorama import Fore, Back, Style
from src.building import *
# from hut import Hut
# from cannon import Cannon
from src.walls import *
from src.troops import *
import sys

m = 33
n = 17
mid_x = (n - 1)/2
mid_y = (m - 1)/2
last_ks = 0
last_bs = 0
last_as = 0
last_ls = 0
t_0 = time.time()
rage_start = 0
level = 0
level_flag = 0

the_king_damage = 75
the_king_health = 300
the_king_health_init = the_king_health
th_health = 500
th_health_init = th_health
hut_health = 200
hut_health_init = hut_health
cannon_health = 250
cannon_health_init = cannon_health
barbarian_health = 50
barbarian_init_health = barbarian_health
barbarian_damage = 25
archers_health = barbarian_health/2
archers_init_health = archers_health
archers_damage = barbarian_damage/2
balloon_health = barbarian_health
balloon_init_health = balloon_health
balloon_damage = 2*barbarian_damage
cannon_damage = 2
cannon_range = 5
archer_range = 6
queen_x_factor = 0
queen_attack_time = 0
spawn_king = 0
barb_spawn = 0
arch_spawn = 0
loon_spawn = 0
wall_health = 100
wall_health_init = wall_health
time_interval_barb = 0.6
samayam_barb = time_interval_barb
time_interval_arch = time_interval_barb/2
samayam_arch = time_interval_arch
time_interval_loon = time_interval_barb/2
samayam_loon = time_interval_loon
rage_flag = 0

rage_flag_1 = 0
heal_flag = 0
heal_flag_1 = 0
heal_start = 0
the_hero = King(mid_x - 4,mid_y, the_king_health, the_king_health_init, the_king_damage, spawn_king)

buildings = []
result = []
cannon_list = []
wizz = []
barbs = []
huts = []
walls = []
arch = []
loons = []
troops = []
defences = []
wiz_target = []
which_hero = ""
play = ""

the_th = TownHall(mid_x, mid_y, th_health, th_health_init)

def select_hero(p):
    hero_flag = 0
    global which_hero
    print("You can choose only one hero:")
    print("Press (K/k) for king and (Q/q) for queen")
    while(1):
        hero = p
        if(hero == "king"):
            the_hero = King(mid_x - 7,mid_y - 15, the_king_health, the_king_health_init, the_king_damage, spawn_king)
            which_hero = 'k'
            break
        elif(hero == "queen"):
            the_hero = Queen(mid_x - 7,mid_y - 15, the_king_health, the_king_health_init, the_king_damage, spawn_king)
            which_hero = 'q'
            break

def build_village():
    if(level == 1):
        buildings.append(the_th)
        result.append(the_th)

        the_cannon_1 = Cannon(mid_x, mid_y - 8, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_1)
        cannon_list.append(the_cannon_1)
        defences.append(the_cannon_1)
        buildings.append(the_cannon_1)
        the_cannon_2 = Cannon(mid_x, mid_y + 8, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_2)
        defences.append(the_cannon_2)
        cannon_list.append(the_cannon_2)
        buildings.append(the_cannon_2)

        the_wiztower_1 = WizardTower(mid_x - 6, mid_y, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_1)
        wizz.append(the_wiztower_1)
        defences.append(the_wiztower_1)
        buildings.append(the_wiztower_1)
        the_wiztower_2 = WizardTower(mid_x + 6, mid_y, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_2)
        wizz.append(the_wiztower_2)
        defences.append(the_wiztower_2)
        buildings.append(the_wiztower_2)

        the_hut_1 = Hut(mid_x - 7,mid_y - 10, hut_health, hut_health_init)
        buildings.append(the_hut_1)
        huts.append(the_hut_1)
        result.append(the_hut_1)
        the_hut_2 = Hut(mid_x + 7,mid_y + 10, hut_health, hut_health_init)
        buildings.append(the_hut_2)
        huts.append(the_hut_2)
        result.append(the_hut_2)
        the_hut_3 = Hut(mid_x - 7,mid_y + 10, hut_health, hut_health_init)
        buildings.append(the_hut_3)
        result.append(the_hut_3)
        huts.append(the_hut_3)
        the_hut_4 = Hut(mid_x + 7,mid_y - 10, hut_health, hut_health_init)
        buildings.append(the_hut_4)
        result.append(the_hut_4)
        huts.append(the_hut_4)

        the_barbarian_1 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_1)
        the_barbarian_2 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_2)
        the_barbarian_3 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_3)
        the_barbarian_4 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_4)
        the_barbarian_5 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_5)
        the_barbarian_6 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_6)

        the_archers_1 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_1)
        the_archers_2 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_2)
        the_archers_3 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_3)
        the_archers_4 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_4)
        the_archers_5 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_5)
        the_archers_6 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_6)

        the_balloon_1 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_1)
        the_balloon_2 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_2)
        the_balloon_3 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_3)

        the_wall_1 = Wall(mid_x - 2, mid_y - 1, wall_health, wall_health_init)
        buildings.append(the_wall_1)
        walls.append(the_wall_1)
        the_wall_2 = Wall(mid_x - 2, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_2)
        walls.append(the_wall_2)
        the_wall_3 = Wall(mid_x - 2, mid_y + 1, wall_health, wall_health_init)
        buildings.append(the_wall_3)
        walls.append(the_wall_3)
        the_wall_4 = Wall(mid_x - 2, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_4)
        walls.append(the_wall_4)
        the_wall_5 = Wall(mid_x - 1, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_5)
        walls.append(the_wall_5)
        the_wall_6 = Wall(mid_x - 1, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_6)
        walls.append(the_wall_6)
        the_wall_7 = Wall(mid_x, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_7)
        walls.append(the_wall_7)
        the_wall_8 = Wall(mid_x, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_8)
        walls.append(the_wall_8)
        the_wall_9 = Wall(mid_x + 1, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_9)
        walls.append(the_wall_9)
        the_wall_10 = Wall(mid_x + 1, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_10)
        walls.append(the_wall_10)
        the_wall_11 = Wall(mid_x + 2, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_11)
        walls.append(the_wall_11)
        the_wall_12 = Wall(mid_x + 2, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_12)
        walls.append(the_wall_12)
        the_wall_13 = Wall(mid_x + 3, mid_y, wall_health, wall_health_init)
        buildings.append(the_wall_13)
        walls.append(the_wall_13)
        the_wall_14 = Wall(mid_x + 3, mid_y + 1, wall_health, wall_health_init)
        buildings.append(the_wall_14)
        walls.append(the_wall_14)
        the_wall_15 = Wall(mid_x + 3, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_15)
        walls.append(the_wall_15)
        the_wall_16 = Wall(mid_x + 3, mid_y - 1, wall_health, wall_health_init)
        buildings.append(the_wall_16)
        walls.append(the_wall_16)
        the_wall_17 = Wall(mid_x + 3, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_17)
        walls.append(the_wall_17)
        the_wall_18 = Wall(mid_x - 2, mid_y, wall_health, wall_health_init)
        buildings.append(the_wall_18)
        walls.append(the_wall_18)

    if(level == 2):
        buildings.append(the_th)
        result.append(the_th)

        the_cannon_1 = Cannon(mid_x - 4, mid_y - 8, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_1)
        cannon_list.append(the_cannon_1)
        defences.append(the_cannon_1)
        buildings.append(the_cannon_1)
        the_cannon_2 = Cannon(mid_x - 4, mid_y + 8, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_2)
        defences.append(the_cannon_2)
        cannon_list.append(the_cannon_2)
        buildings.append(the_cannon_2)
        the_cannon_3 = Cannon(mid_x + 8, mid_y, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_3)
        defences.append(the_cannon_3)
        cannon_list.append(the_cannon_3)
        buildings.append(the_cannon_3)

        the_wiztower_1 = WizardTower(mid_x + 4, mid_y - 9, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_1)
        wizz.append(the_wiztower_1)
        defences.append(the_wiztower_1)
        buildings.append(the_wiztower_1)
        the_wiztower_2 = WizardTower(mid_x + 4, mid_y + 9, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_2)
        defences.append(the_wiztower_2)
        wizz.append(the_wiztower_2)
        buildings.append(the_wiztower_2)
        the_wiztower_3 = WizardTower(mid_x - 7, mid_y, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_3)
        wizz.append(the_wiztower_3)
        defences.append(the_wiztower_3)
        buildings.append(the_wiztower_3)

        the_hut_1 = Hut(mid_x - 7,mid_y - 10, hut_health, hut_health_init)
        buildings.append(the_hut_1)
        huts.append(the_hut_1)
        result.append(the_hut_1)
        the_hut_2 = Hut(mid_x + 7,mid_y + 10, hut_health, hut_health_init)
        buildings.append(the_hut_2)
        huts.append(the_hut_2)
        result.append(the_hut_2)
        the_hut_3 = Hut(mid_x - 7,mid_y + 10, hut_health, hut_health_init)
        buildings.append(the_hut_3)
        result.append(the_hut_3)
        huts.append(the_hut_3)
        the_hut_4 = Hut(mid_x + 7,mid_y - 10, hut_health, hut_health_init)
        buildings.append(the_hut_4)
        result.append(the_hut_4)
        huts.append(the_hut_4)

        the_barbarian_1 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_1)
        the_barbarian_2 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_2)
        the_barbarian_3 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_3)
        the_barbarian_4 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_4)
        the_barbarian_5 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_5)
        the_barbarian_6 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_6)

        the_archers_1 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_1)
        the_archers_2 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_2)
        the_archers_3 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_3)
        the_archers_4 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_4)
        the_archers_5 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_5)
        the_archers_6 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_6)

        the_balloon_1 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_1)
        the_balloon_2 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_2)
        the_balloon_3 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_3)

        the_wall_1 = Wall(mid_x - 2, mid_y - 1, wall_health, wall_health_init)
        buildings.append(the_wall_1)
        walls.append(the_wall_1)
        the_wall_2 = Wall(mid_x - 2, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_2)
        walls.append(the_wall_2)
        the_wall_3 = Wall(mid_x - 2, mid_y + 1, wall_health, wall_health_init)
        buildings.append(the_wall_3)
        walls.append(the_wall_3)
        the_wall_4 = Wall(mid_x - 2, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_4)
        walls.append(the_wall_4)
        the_wall_5 = Wall(mid_x - 1, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_5)
        walls.append(the_wall_5)
        the_wall_6 = Wall(mid_x - 1, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_6)
        walls.append(the_wall_6)
        the_wall_7 = Wall(mid_x, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_7)
        walls.append(the_wall_7)
        the_wall_8 = Wall(mid_x, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_8)
        walls.append(the_wall_8)
        the_wall_9 = Wall(mid_x + 1, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_9)
        walls.append(the_wall_9)
        the_wall_10 = Wall(mid_x + 1, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_10)
        walls.append(the_wall_10)
        the_wall_11 = Wall(mid_x + 2, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_11)
        walls.append(the_wall_11)
        the_wall_12 = Wall(mid_x + 2, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_12)
        walls.append(the_wall_12)
        the_wall_13 = Wall(mid_x + 3, mid_y, wall_health, wall_health_init)
        buildings.append(the_wall_13)
        walls.append(the_wall_13)
        the_wall_14 = Wall(mid_x + 3, mid_y + 1, wall_health, wall_health_init)
        buildings.append(the_wall_14)
        walls.append(the_wall_14)
        the_wall_15 = Wall(mid_x + 3, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_15)
        walls.append(the_wall_15)
        the_wall_16 = Wall(mid_x + 3, mid_y - 1, wall_health, wall_health_init)
        buildings.append(the_wall_16)
        walls.append(the_wall_16)
        the_wall_17 = Wall(mid_x + 3, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_17)
        walls.append(the_wall_17)
        the_wall_18 = Wall(mid_x - 2, mid_y, wall_health, wall_health_init)
        buildings.append(the_wall_18)
        walls.append(the_wall_18)

    if(level == 3):
        buildings.append(the_th)
        result.append(the_th)

        the_cannon_1 = Cannon(mid_x - 4, mid_y - 7, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_1)
        cannon_list.append(the_cannon_1)
        defences.append(the_cannon_1)
        buildings.append(the_cannon_1)
        the_cannon_2 = Cannon(mid_x - 4, mid_y + 7, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_2)
        defences.append(the_cannon_2)
        cannon_list.append(the_cannon_2)
        buildings.append(the_cannon_2)
        the_cannon_3 = Cannon(mid_x + 4, mid_y - 7, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_3)
        defences.append(the_cannon_3)
        cannon_list.append(the_cannon_3)
        buildings.append(the_cannon_3)
        the_cannon_4 = Cannon(mid_x + 4, mid_y + 7, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_cannon_4)
        defences.append(the_cannon_4)
        cannon_list.append(the_cannon_4)
        buildings.append(the_cannon_4)

        the_wiztower_1 = WizardTower(mid_x, mid_y - 9, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_1)
        defences.append(the_wiztower_1)
        wizz.append(the_wiztower_1)
        buildings.append(the_wiztower_1)
        the_wiztower_2 = WizardTower(mid_x, mid_y + 9, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_2)
        defences.append(the_wiztower_2)
        wizz.append(the_wiztower_2)
        buildings.append(the_wiztower_2)
        the_wiztower_3 = WizardTower(mid_x - 7, mid_y, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_3)
        defences.append(the_wiztower_3)
        wizz.append(the_wiztower_3)
        buildings.append(the_wiztower_3)
        the_wiztower_4 = WizardTower(mid_x + 7, mid_y, cannon_health, cannon_health_init, cannon_damage, cannon_range)
        result.append(the_wiztower_4)
        defences.append(the_wiztower_4)
        wizz.append(the_wiztower_4)
        buildings.append(the_wiztower_4)

        the_hut_1 = Hut(mid_x - 7,mid_y - 10, hut_health, hut_health_init)
        buildings.append(the_hut_1)
        huts.append(the_hut_1)
        result.append(the_hut_1)
        the_hut_2 = Hut(mid_x + 7,mid_y + 10, hut_health, hut_health_init)
        buildings.append(the_hut_2)
        huts.append(the_hut_2)
        result.append(the_hut_2)
        the_hut_3 = Hut(mid_x - 7,mid_y + 10, hut_health, hut_health_init)
        buildings.append(the_hut_3)
        result.append(the_hut_3)
        huts.append(the_hut_3)
        the_hut_4 = Hut(mid_x + 7,mid_y - 10, hut_health, hut_health_init)
        buildings.append(the_hut_4)
        result.append(the_hut_4)
        huts.append(the_hut_4)

        the_barbarian_1 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_1)
        the_barbarian_2 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_2)
        the_barbarian_3 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_3)
        the_barbarian_4 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_4)
        the_barbarian_5 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_5)
        the_barbarian_6 = Barbarian(mid_x, mid_y, barbarian_health, barbarian_init_health, barbarian_damage, barb_spawn)
        barbs.append(the_barbarian_6)

        the_archers_1 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_1)
        the_archers_2 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_2)
        the_archers_3 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_3)
        the_archers_4 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_4)
        the_archers_5 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_5)
        the_archers_6 = Archers(mid_x, mid_y, archers_health, archers_init_health, archers_damage, arch_spawn, archer_range)
        arch.append(the_archers_6)

        the_balloon_1 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_1)
        the_balloon_2 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_2)
        the_balloon_3 = Balloons(mid_x, mid_y, balloon_health, balloon_init_health, balloon_damage, loon_spawn)
        loons.append(the_balloon_3)

        the_wall_1 = Wall(mid_x - 2, mid_y - 1, wall_health, wall_health_init)
        buildings.append(the_wall_1)
        walls.append(the_wall_1)
        the_wall_2 = Wall(mid_x - 2, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_2)
        walls.append(the_wall_2)
        the_wall_3 = Wall(mid_x - 2, mid_y + 1, wall_health, wall_health_init)
        buildings.append(the_wall_3)
        walls.append(the_wall_3)
        the_wall_4 = Wall(mid_x - 2, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_4)
        walls.append(the_wall_4)
        the_wall_5 = Wall(mid_x - 1, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_5)
        walls.append(the_wall_5)
        the_wall_6 = Wall(mid_x - 1, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_6)
        walls.append(the_wall_6)
        the_wall_7 = Wall(mid_x, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_7)
        walls.append(the_wall_7)
        the_wall_8 = Wall(mid_x, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_8)
        walls.append(the_wall_8)
        the_wall_9 = Wall(mid_x + 1, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_9)
        walls.append(the_wall_9)
        the_wall_10 = Wall(mid_x + 1, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_10)
        walls.append(the_wall_10)
        the_wall_11 = Wall(mid_x + 2, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_11)
        walls.append(the_wall_11)
        the_wall_12 = Wall(mid_x + 2, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_12)
        walls.append(the_wall_12)
        the_wall_13 = Wall(mid_x + 3, mid_y, wall_health, wall_health_init)
        buildings.append(the_wall_13)
        walls.append(the_wall_13)
        the_wall_14 = Wall(mid_x + 3, mid_y + 1, wall_health, wall_health_init)
        buildings.append(the_wall_14)
        walls.append(the_wall_14)
        the_wall_15 = Wall(mid_x + 3, mid_y + 2, wall_health, wall_health_init)
        buildings.append(the_wall_15)
        walls.append(the_wall_15)
        the_wall_16 = Wall(mid_x + 3, mid_y - 1, wall_health, wall_health_init)
        buildings.append(the_wall_16)
        walls.append(the_wall_16)
        the_wall_17 = Wall(mid_x + 3, mid_y - 2, wall_health, wall_health_init)
        buildings.append(the_wall_17)
        walls.append(the_wall_17)
        the_wall_18 = Wall(mid_x - 2, mid_y, wall_health, wall_health_init)
        buildings.append(the_wall_18)
        walls.append(the_wall_18)

def set_target(barbarian, buildings):
    min = 10000
    for i in buildings:
        if(abs(barbarian.pos_x - i.pos_x) + abs(barbarian.pos_y - i.pos_y) < min):
            min = abs(barbarian.pos_x - i.pos_x) + abs(barbarian.pos_y - i.pos_y)
            barbarian.target = i

def attack_queen(x, y, last_move):
    if(last_move == 's' or last_move == 'S'):
        x = x + 8
        for i in buildings:
            if(abs(x - i.pos_x) <= 2 and abs(y - i.pos_y) <= 2 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage
    if(last_move == 'w' or last_move == 'W'):
        x = x - 8
        for i in buildings:
            if(abs(x - i.pos_x) <= 2 and abs(y - i.pos_y) <= 2 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage

    if(last_move == 'a' or last_move == 'A'):
        y = y - 8
        for i in buildings:
            if(abs(x - i.pos_x) <= 2 and abs(y - i.pos_y) <= 2 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage

    if(last_move == 'd' or last_move == 'D'):
        y = y + 8
        for i in buildings:
            if(abs(x - i.pos_x) <= 2 and abs(y - i.pos_y) <= 2 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage

def queen_bonus(x, y, last_move):
    if(last_move == 's' or last_move == 'S'):
        x = x + 16
        for i in buildings:
            if(abs(x - i.pos_x) <= 4 and abs(y - i.pos_y) <= 4 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage
    if(last_move == 'w' or last_move == 'W'):
        x = x - 16
        for i in buildings:
            if(abs(x - i.pos_x) <= 4 and abs(y - i.pos_y) <= 4 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage

    if(last_move == 'a' or last_move == 'A'):
        y = y - 16
        for i in buildings:
            if(abs(x - i.pos_x) <= 4 and abs(y - i.pos_y) <= 4 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage

    if(last_move == 'd' or last_move == 'D'):
        y = y + 16
        for i in buildings:
            if(abs(x - i.pos_x) <= 4 and abs(y - i.pos_y) <= 4 and the_hero.health > 0 and i.health > 0):
                i.health = i.health - the_hero.damage

def attack_hut_king(x, y, last_move):
    for hu in huts: 
        if (x == hu.pos_x - 1 and y == hu.pos_y and hu.health > 0 and (last_move == 's' or last_move == 'S')):
            hu.health = hu.health - the_hero.damage
        elif (x == hu.pos_x + 1 and y == hu.pos_y and hu.health > 0 and (last_move == 'w' or last_move == 'W')):
            hu.health = hu.health - the_hero.damage
        elif (x == hu.pos_x and y == hu.pos_y - 1 and hu.health > 0 and (last_move == 'd' or last_move == 'D')):
            hu.health = hu.health - the_hero.damage
        elif (x == hu.pos_x and y == hu.pos_y + 1 and hu.health > 0 and (last_move == 'a' or last_move == 'A')):
            hu.health = hu.health - the_hero.damage

def area_slash(x, y, buildings):
    for i in buildings:
        if(abs(x - i.pos_x) <= 3 and abs(y - i.pos_y) <= 3 and the_hero.health > 0 and i.health > 0):
            i.health = i.health - the_hero.damage

def attack_cannon_king(x, y, last_move):
    for can in cannon_list:    
        if (x == can.pos_x - 1 and y == can.pos_y and can.health > 0 and (last_move == 's' or last_move == 'S')):
            can.health = can.health - the_hero.damage
        elif (x == can.pos_x + 1 and y == can.pos_y and can.health > 0 and (last_move == 'w' or last_move == 'W')):
            can.health = can.health - the_hero.damage
        elif (x == can.pos_x and y == can.pos_y - 1 and can.health > 0 and (last_move == 'd' or last_move == 'D')):
            can.health = can.health - the_hero.damage
        elif (x == can.pos_x and y == can.pos_y + 1 and can.health > 0  and (last_move == 'a' or last_move == 'A')):
            can.health = can.health - the_hero.damage

def attack_wizzy_king(x, y, last_move):
    for wizzy in wizz:    
        if (x == wizzy.pos_x - 1 and y == wizzy.pos_y and wizzy.health > 0 and (last_move == 's' or last_move == 'S')):
            wizzy.health = wizzy.health - the_hero.damage
        elif (x == wizzy.pos_x + 1 and y == wizzy.pos_y and wizzy.health > 0 and (last_move == 'w' or last_move == 'W')):
            wizzy.health = wizzy.health - the_hero.damage
        elif (x == wizzy.pos_x and y == wizzy.pos_y - 1 and wizzy.health > 0 and (last_move == 'd' or last_move == 'D')):
            wizzy.health = wizzy.health - the_hero.damage
        elif (x == wizzy.pos_x and y == wizzy.pos_y + 1 and wizzy.health > 0  and (last_move == 'a' or last_move == 'A')):
            wizzy.health = wizzy.health - the_hero.damage

def loon_attack(loon, target):
    if(loon.pos_x == target.pos_x and loon.pos_y == target.pos_y):
        target.health = target.health - loon.damage

def archer_attack(archer, target, last_move):
    x = abs(archer.pos_x - target.pos_x)
    y = abs(archer.pos_y - target.pos_y)
    if(x <= archer.range and y <= archer.range and x*x + y*y <= 36 and archer.health > 0 and target.health > 0):
        target.health = target.health - archer.damage
    
    for i in buildings: 
        if (x == i.pos_x - 1 and y == i.pos_y and i.health > 0 and (last_move == 's' or last_move == 'S')):
            i.health = i.health - archer.damage
        elif (x == i.pos_x + 1 and y == i.pos_y and i.health > 0 and (last_move == 'w' or last_move == 'W')):
            i.health = i.health - archer.damage
        elif (x == i.pos_x and y == i.pos_y - 1 and i.health > 0 and (last_move == 'd' or last_move == 'D')):
            i.health = i.health - archer.damage
        elif (x == i.pos_x and y == i.pos_y + 1 and i.health > 0 and (last_move == 'a' or last_move == 'A')):
            i.health = i.health - archer.damage

def cannons_attack(x,y,z,h):
    xa = abs(x - the_hero.pos_x)
    ya = abs(y - the_hero.pos_y)
    if( xa*xa + ya*ya <= cannon_range*cannon_range and h > 0 and the_hero.health > 0):
        the_hero.health = the_hero.health - z
    for bars in barbs:
        if(xa*xa + ya*ya <= cannon_range*cannon_range and h > 0 and bars.health > 0):
            bars.health = bars.health - z
    for arc in arch:
        if(xa*xa + ya*ya <= cannon_range*cannon_range and h > 0 and arc.health > 0):
            arc.health = arc.health - z

def wizard_attack(obj,x,y,z,h):
    for i in troops:
        xa = abs(x - i.pos_x)
        ya = abs(y - i.pos_y)
        if(xa*xa + ya*ya <= cannon_range*cannon_range and h > 0 and i.health > 0):
            wiz_target.append(i)
    for i in wiz_target:
        xa = abs(x - i.pos_x)
        ya = abs(y - i.pos_y)
        if(xa*xa + ya*ya > cannon_range*cannon_range or i.health <= 0 or h <= 0):
            wiz_target.remove(i)
    min = 10000
    for j in wiz_target:
        xa = abs(x - j.pos_x)
        ya = abs(y - j.pos_y)
        if(xa*xa + ya*ya <= cannon_range*cannon_range and abs(x - j.pos_x) + abs(y - j.pos_y) < min):
            min = abs(x - j.pos_x) + abs(y - j.pos_y)
            obj.target = j
    if(obj.target):
        x = obj.target.pos_x 
        y = obj.target.pos_y
        for i in troops:
            if(abs(x - i.pos_x) <= 1 and abs(y - i.pos_y) <= 1 and obj.health > 0 and i.health > 0):
                i.health = i.health - obj.damage

def attack_th_king(x,y,last_move):
    if (x == the_th.pos_x - 2 and y == the_th.pos_y and the_th.health > 0 and (last_move == 's' or last_move == 'S')):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x and y == the_th.pos_y - 2 and the_th.health > 0 and (last_move == 'd' or last_move == 'D')):
        the_th.health = the_th.health - the_hero.damage
    if ((x == the_th.pos_x - 2 and y == the_th.pos_y - 1 and the_th.health > 0 and (last_move == 's' or last_move == 'S')) or (x == the_th.pos_x - 1 and y == the_th.pos_y - 2 and (last_move == 'd' or last_move == 'D'))):
        the_th.health = the_th.health - the_hero.damage
    if ((x == the_th.pos_x - 2 and y == the_th.pos_y + 1 and the_th.health > 0 and (last_move == 's' or last_move == 'S')) or (x == the_th.pos_x - 1 and y == the_th.pos_y + 2 and (last_move == 'a' or last_move == 'A'))):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x + 1 and y == the_th.pos_y - 2 and the_th.health > 0 and (last_move == 'd' or last_move == 'D')):
        the_th.health = the_th.health - the_hero.damage
    if ((x == the_th.pos_x + 2 and y == the_th.pos_y - 2 and the_th.health > 0 and (last_move == 'd' or last_move == 'D')) or (x == the_th.pos_x + 3 and y == the_th.pos_y - 1 and (last_move == 'w' or last_move == 'W'))):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x + 1 and y == the_th.pos_y + 2 and the_th.health > 0 and (last_move == 'a' or last_move == 'A')):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x + 2 and y == the_th.pos_y + 2 and the_th.health > 0 and (last_move == 'a' or last_move == 'A')):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x + 3 and y == the_th.pos_y + 1 and the_th.health > 0 and (last_move == 'w' or last_move == 'W')):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x and y == the_th.pos_y + 2 and the_th.health > 0 and (last_move == 'a' or last_move == 'A')):
        the_th.health = the_th.health - the_hero.damage
    if (x == the_th.pos_x + 3 and y == the_th.pos_y and the_th.health > 0 and (last_move == 'w' or last_move == 'W')):
        the_th.health = the_th.health - the_hero.damage

def attack_wall_king(x,y,last_move):
    for wal in walls:    
        if (x == wal.pos_x - 1 and y == wal.pos_y and wal.health > 0 and (last_move == 's' or last_move == 'S')):
            wal.health = wal.health - the_hero.damage
        elif (x == wal.pos_x + 1 and y == wal.pos_y and wal.health > 0 and (last_move == 'w' or last_move == 'W')):
            wal.health = wal.health - the_hero.damage
        elif (x == wal.pos_x and y == wal.pos_y - 1 and wal.health > 0 and (last_move == 'd' or last_move == 'D')):
            wal.health = wal.health - the_hero.damage
        elif (x == wal.pos_x and y == wal.pos_y + 1 and wal.health > 0 and (last_move == 'a' or last_move == 'A')):
            wal.health = wal.health - the_hero.damage

def movement_func_w(x,y,move_w):
    for hu in huts:
        if (x == hu.pos_x + 1 and y == hu.pos_y and hu.health > 0):
            move_w = move_w + 1
    for can in cannon_list:
        if (x == can.pos_x + 1 and y == can.pos_y and can.health > 0):
            move_w = move_w + 1
    for wizzy in wizz:
        if (x == wizzy.pos_x + 1 and y == wizzy.pos_y and wizzy.health > 0):
            move_w = move_w + 1
    for wal in walls:
        if (x == wal.pos_x + 1 and y == wal.pos_y and wal.health > 0):
            move_w = move_w + 1
    if (x == the_th.pos_x + 3 and the_th.health > 0):
        if(y == the_th.pos_y or y == the_th.pos_y - 1 or y == the_th.pos_y + 1):
            move_w = move_w + 1
    return move_w

def movement_func_a(x,y,move_a):
    for hu in huts:
        if (x == hu.pos_x and y == hu.pos_y + 1 and hu.health > 0):
            move_a = move_a + 1
    for can in cannon_list:
        if (x == can.pos_x and y == can.pos_y + 1 and can.health > 0):
            move_a = move_a + 1
    for wizzy in wizz:
        if (x == wizzy.pos_x and y == wizzy.pos_y + 1 and wizzy.health > 0):
            move_a = move_a + 1
    for wal in walls:
        if (x == wal.pos_x and y == wal.pos_y + 1 and wal.health > 0):
            move_a = move_a + 1
    if (y == the_th.pos_y + 2 and the_th.health > 0):
        if(x == the_th.pos_x or x == the_th.pos_x - 1 or x == the_th.pos_x + 1 or x == the_th.pos_x + 2):
            move_a = move_a + 1
    return move_a

def movement_func_s(x,y,move_s):
    for hu in huts:
        if (x == hu.pos_x - 1 and y == hu.pos_y and hu.health > 0):
            move_s = move_s + 1
    for can in cannon_list:
        if (x == can.pos_x - 1 and y == can.pos_y and can.health > 0):
            move_s = move_s + 1
    for wizzy in wizz:
        if (x == wizzy.pos_x - 1 and y == wizzy.pos_y and wizzy.health > 0):
            move_s = move_s + 1
    for wal in walls:
        if (x == wal.pos_x - 1 and y == wal.pos_y and wal.health > 0):
            move_s = move_s + 1
    if (x == the_th.pos_x - 2 and the_th.health > 0):
        if(y == the_th.pos_y or y == the_th.pos_y - 1 or y == the_th.pos_y + 1):
            move_s = move_s + 1
    return move_s

def movement_func_d(x,y,move_d):
    for hu in huts:
        if (x == hu.pos_x and y == hu.pos_y - 1 and hu.health > 0):
            move_d = move_d + 1
    for can in cannon_list:
        if (x == can.pos_x and y == can.pos_y - 1 and can.health > 0):
            move_d = move_d + 1
    for wizzy in wizz:
        if (x == wizzy.pos_x and y == wizzy.pos_y - 1 and wizzy.health > 0):
            move_d = move_d + 1
    for wal in walls:
        if (x == wal.pos_x and y == wal.pos_y - 1 and wal.health > 0):
            move_d = move_d + 1
    if (y == the_th.pos_y - 2 and the_th.health > 0):
        if(x == the_th.pos_x or x == the_th.pos_x - 1 or x == the_th.pos_x + 1 or x == the_th.pos_x + 2):
            move_d = move_d + 1
    return move_d

def display():
    f = 1
    print(chr(27) + "[2J")

    for i in range(n):
        for k in range(m):
            if(f==1):
                print(' _____', end="")
        print()
        f+=1
        for l in range(m):
            print('|     ', end="")
        print('|')
        for c in range(m):
            flag = 0

            for l in loons:
                if (i == l.pos_x and c == l.pos_y and l.spawn == 1 and l.health > 0 and (last_ls == 'b' or last_ls == 'n' or last_ls == 'm' or last_ls == 'L' or last_ls == 'M' or last_ls == 'N')):
                    print('|  ', end="")
                    flag = 1
                    if(l.health > l.health_init/2):
                        print(Back.GREEN + 'L',end="")
                    elif(l.health <= l.health_init/2 and l.health > l.health_init/4):
                        print(Back.YELLOW + 'L',end="")
                    elif(l.health <= l.health_init/4 and l.health > 0):
                        print(Back.RED + 'L',end="")
                            
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
                    break
            if(flag == 1):
                flag = 0
                continue  

            for b in barbs:
                if (i == b.pos_x and c == b.pos_y and b.spawn == 1 and b.health > 0 and (last_bs == 'i' or last_bs == 'o' or last_bs == 'p' or last_bs == 'I' or last_bs == 'O' or last_bs == 'P')):
                    print('|  ', end="")
                    flag = 1
                    if(b.health > b.health_init/2):
                        print(Back.GREEN + 'B',end="")
                    elif(b.health <= b.health_init/2 and b.health > b.health_init/4):
                        print(Back.YELLOW + 'B',end="")
                    elif(b.health <= b.health_init/4 and b.health > 0):
                        print(Back.RED + 'B',end="")
                            
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
                    break
            if(flag == 1):
                flag = 0
                continue  

            for a in arch:
                if (i == a.pos_x and c == a.pos_y and a.spawn == 1 and a.health > 0 and (last_as == 'f' or last_as == 'g' or last_as == 'h' or last_as == 'F' or last_as == 'G' or last_as == 'H')):
                    print('|  ', end="")
                    flag = 1
                    if(a.health > a.health_init/2):
                        print(Back.GREEN + 'A',end="")
                    elif(a.health <= a.health_init/2 and a.health > a.health_init/4):
                        print(Back.YELLOW + 'A',end="")
                    elif(a.health <= a.health_init/4 and a.health > 0):
                        print(Back.RED + 'A',end="")
                            
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
                    break
            if(flag == 1):
                flag = 0
                continue  

            for can in cannon_list:
                if (i == can.pos_x  and c == can.pos_y and can.health > 0):
                    print('|  ', end="")
                    flag = 1
                    if(can.health > can.health_init/2):
                        print(Back.GREEN + 'C',end="")
                    elif(can.health <= can.health_init/2 and can.health > can.health_init/4):
                        print(Back.YELLOW + 'C',end="")
                    elif(can.health <= can.health_init/4 and can.health > 0):
                        print(Back.RED + 'C',end="")
                            
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
            if (flag == 1):
                flag = 0
                continue

            for wizzy in wizz:
                if (i == wizzy.pos_x  and c == wizzy.pos_y and wizzy.health > 0):
                    print('|  ', end="")
                    flag = 1
                    if(wizzy.health > wizzy.health_init/2):
                        print(Back.GREEN + 'Z',end="")
                    elif(wizzy.health <= wizzy.health_init/2 and wizzy.health > wizzy.health_init/4):
                        print(Back.YELLOW + 'Z',end="")
                    elif(wizzy.health <= wizzy.health_init/4 and wizzy.health > 0):
                        print(Back.RED + 'Z',end="")
                            
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
            if (flag == 1):
                flag = 0
                continue

            for wal in walls:
                if(i == wal.pos_x and c == wal.pos_y and wal.health > 0):
                    print('|  ', end="")
                    flag = 1               
                    if(wal.health > wal.health_init/2):
                        print(Back.GREEN + 'W',end="")
                    elif(wal.health <= wal.health_init/2 and wal.health > wal.health_init/4):
                        print(Back.YELLOW + 'W',end="")
                    elif(wal.health <= wal.health_init/4 and wal.health > 0):
                        print(Back.RED + 'W',end="")
                
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
            if(flag == 1):
                flag = 0
                continue

            for hu in huts:
                if(i == hu.pos_x and c == hu.pos_y and hu.health > 0):
                    print('|  ', end="")
                    flag = 1                
                    if(hu.health > hu.health_init/2):
                        print(Back.GREEN + 'H',end="")
                    elif(hu.health <= hu.health_init/2 and hu.health > hu.health_init/4):
                        print(Back.YELLOW + 'H',end="")
                    elif(hu.health <= hu.health_init/4 and hu.health > 0):
                        print(Back.RED + 'H',end="")
                            
                    print(Style.RESET_ALL, end="")
                    print('  ', end="")
            if(flag == 1):
                flag = 0
                continue

            if (i == the_hero.pos_x and c == the_hero.pos_y and the_hero.spawn == 1 and the_hero.health > 0 and (last_ks == 'j' or last_ks == 'k' or last_ks == 'l' or last_ks == 'J' or last_ks == 'K' or last_ks == 'L')):
                print('|  ', end="")
            
                if(the_hero.health > the_hero.health_init/2):
                    if(which_hero == 'K' or which_hero == 'k'):
                        print(Back.GREEN + 'K',end="")
                    elif(which_hero == 'Q' or which_hero == 'q'):
                        print(Back.GREEN + 'Q',end="")
                elif(the_hero.health <= the_hero.health_init/2 and the_hero.health > the_hero.health_init/4):
                    if(which_hero == 'K' or which_hero == 'k'):
                        print(Back.YELLOW + 'K',end="")
                    elif(which_hero == 'Q' or which_hero == 'q'):
                        print(Back.YELLOW + 'Q',end="")
                elif(the_hero.health <= the_hero.health_init/4 and the_hero.health > 0):
                    if(which_hero == 'K' or which_hero == 'k'):
                        print(Back.RED + 'K',end="")
                    elif(which_hero == 'Q' or which_hero == 'q'):
                        print(Back.RED + 'Q',end="")
                        
                print(Style.RESET_ALL, end="")
                print('  ', end="")     

            elif( (i == the_th.pos_x - 1 and c == the_th.pos_y) or (i == the_th.pos_x and c == the_th.pos_y-1) or (i == the_th.pos_x - 1 and c == the_th.pos_y - 1) or (i == the_th.pos_x - 1 and c == the_th.pos_y + 1) or (i == the_th.pos_x + 1 and c == the_th.pos_y-1) or (i == the_th.pos_x + 2 and c == the_th.pos_y-1) or (i == the_th.pos_x + 1 and c == the_th.pos_y+1) or (i == the_th.pos_x + 2 and c == the_th.pos_y+1) or (i == the_th.pos_x and c == the_th.pos_y + 1) or (i == the_th.pos_x + 2 and c == the_th.pos_y)):
                print('|  ', end="")
            
                if(the_th.health > the_th.health_init/2):
                    print(Back.GREEN + 'T',end="")
                elif(the_th.health <= the_th.health_init/2 and the_th.health > the_th.health_init/4):
                    print(Back.YELLOW + 'T',end="")
                elif(the_th.health <= the_th.health_init/4 and the_th.health > 0):
                    print(Back.RED + 'T',end="")
                elif(the_th.health <=0):
                    print(' ', end="")
                        
                print(Style.RESET_ALL, end="")
                print('  ', end="")

            else:
                print('|     ', end="")
        print('|')
        for z in range(m):
            print('|_____', end="")
        print('|', end="")
    print()
    if(which_hero == 'K' or which_hero == 'k'):
        print("King's health: |", end="")
    elif(which_hero == 'Q' or which_hero == 'q'):
        print("Queen's health: |", end="")
    for i in range(25):
        if(i<=the_hero.health/the_hero.health_init * 25):
            print(Back.GREEN + ' ',end="")
            print(Style.RESET_ALL, end="")
        else:
            print(" ", end="")
    print('|')
    # print(time.time())
    # print(samayam_barb)

flag_hero = 0

path = input()
print(path)

replay = open("replays/"+str(path)+".txt", "r")

input_list = []
time_list = []

cur_move = 0

cmd = replay.readlines()
for i in cmd:
    col = i.split(" ")
    if(len(col)==3):
        input_list.append(" ")
        end = col[2].rstrip("\n")
        time_list.append(float(end))
    else:
        end = col[1].rstrip("\n")
        input_list.append(col[0])
        time_list.append(float(end))

while(1):
    time.sleep(0.025)
    move_w = 0
    move_a = 0
    move_s = 0
    move_d = 0
    spawn_1 = 0
    last_barb = 0

    cur_time = time.time() - t_0

    p = "u"

    if(cur_move >= len(input_list) or cur_time < time_list[cur_move]):
        p = "u"
    elif(cur_move < len(input_list)):
        p = input_list[cur_move]
        cur_move = cur_move + 1

    if(p == "king" or p == "queen"):
        select_hero(p)


    if(p == "yes"):
        play = 'y'
    elif(p == "no"):
        play = 'n'

    # print(level)
    # print(level_flag)
    # # time.sleep(0.5)
    # if(flag_hero == 0):
    #     flag_hero = flag_hero + 1 
    #     select_hero()

    if((len(result) == 0 or (len(troops) == 0 and the_hero.health <= 0)) and level_flag == 0):
        level = level + 1

    if(level > 0 and level_flag == 0):
        build_village()
        level_flag = 1
 
    display()
    time.sleep(0.05)

    # if(p != None):
    #     replay.write("{} {}\n".format(p, cur_time))

    if( (p == 'r' or p == 'R') and rage_flag == 0):
        rage_start = time.time()
        time_interval_barb = time_interval_barb / 2
        time_interval_arch = time_interval_arch / 2
        time_interval_loon = time_interval_loon / 2
        rage_flag = rage_flag + 1
        the_hero.damage = the_hero.damage*2
    
    if( rage_flag == 1 and time.time() - rage_start > 3 and rage_flag_1 == 0):
        rage_flag_1 = 1
        time_interval_barb = 2*time_interval_barb
        time_interval_arch = 2*time_interval_arch
        time_interval_loon = 2*time_interval_loon
        the_hero.damage = the_hero.damage/2

    if( (p == 'h' or p == 'H') and heal_flag < 3):
        heal_start = time.time()
        heal_flag = heal_flag + 1
        the_hero.health = the_hero.health * (3/2)
        if (the_hero.health > the_hero.health_init):
            the_hero.health = the_hero.health_init
        for i in troops:
            if(i.spawn == 1 and i.health > 0):
                i.health = i.health * (3/2)
                if (i.health > i.health_init):
                    i.health = i.health_init

    for i in buildings:
        if(i.health <= 0):
            buildings.remove(i)

    for i in defences:
        if(i.health <= 0):
            defences.remove(i)
    
    for i in result:
        if(i.health <= 0):
            result.remove(i)

    for i in barbs:
        if(i.target == 0 and i.spawn == 1):
            set_target(i, result)
        elif(i.spawn == 1 and i.target.health <= 0):
            set_target(i, result)

    for i in arch:
        if(i.target == 0 and i.spawn == 1):
            set_target(i, result)
        elif(i.spawn == 1 and i.target.health <= 0):
            set_target(i, result)

    for i in loons:
        if(len(defences)):
            if(i.target == 0 and i.spawn == 1):
                set_target(i, defences)
            elif(i.spawn == 1 and i.target.health <= 0):
                set_target(i, defences)
        else:    
            if(i.target == 0 and i.spawn == 1):
                set_target(i, result)
            elif(i.spawn == 1 and i.target.health <= 0):
                set_target(i, result)

    for i in barbs:
        if(i.health <= 0):
            barbs.remove(i)
    
    for i in arch:
        if(i.health <= 0):
            arch.remove(i)

    for i in loons:
        if(i.health <= 0):
            loons.remove(i)

    if (len(troops) == 0 and the_hero.health <= 0):
        print()
        print()
        print('\033[1m'  'Defeat'  '\033[0m')
        print()
        level_flag = 0
        if(level == 3):
            print()
            print("You have played all three levels")
            print()
            print('\033[1m'  'THE END'  '\033[0m')
            print()
            print()
            break
    
        print("If you want to play the next level press (Y/y) else press (N/n) and then press enter when you are ready to play")
        while(1):
            if(play == 'y' or play == 'Y' or play == 'n' or play == 'N'):
                break

            cur_time = time.time() - t_0
            
            if(cur_move >= len(input_list) or cur_time < time_list[cur_move]):
                p = "u"
            elif(cur_move < len(input_list)):
                p = input_list[cur_move]
                cur_move = cur_move + 1
            if(p == "yes"):
                play = 'y'
            elif(p == "no"):
                play = 'n'
            else:
                play = ""

        if(play == 'Y' or play == 'y'):
            buildings = []
            defences = []
            result = []
            cannon_list = []
            wizz = []
            barbs = []
            arch = []
            loons = []
            huts = []
            walls = []
            flag_hero = 0
            if(which_hero == 'k' or which_hero == 'K'):
                the_hero = King(mid_x - 4,mid_y, the_king_health, the_king_health_init, the_king_damage, spawn_king)
            elif(which_hero == 'q' or which_hero == 'Q'):
                the_hero = Queen(mid_x - 4,mid_y, the_king_health, the_king_health_init, the_king_damage, spawn_king)
            the_th = TownHall(mid_x, mid_y, th_health, th_health_init)
            continue
        elif (play == 'N' or play == 'n'):
            break

    elif (len(result) == 0):
        print()
        print()
        print('\033[1m'  'Victory'  '\033[0m')
        print()
        level_flag = 0
        if(level == 3):
            print()
            print("You have played all three levels")
            print()
            print('\033[1m'  'THE END'  '\033[0m')
            print()
            print()
            break

        print("If you want to play the next level press (Y/y) else press (N/n) and then press enter when you are ready to play")

        while(1):
            if(play == 'y' or play == 'Y' or play == 'n' or play == 'N'):
                break

            cur_time = time.time() - t_0
            
            if(cur_move >= len(input_list) or cur_time < time_list[cur_move]):
                p = "u"
            elif(cur_move < len(input_list)):
                p = input_list[cur_move]
                cur_move = cur_move + 1
            if(p == "yes"):
                play = 'y'
            elif(p == "no"):
                play = 'n'
            else:
                play = ""

        if(play == 'Y' or play == 'y'):
            buildings = []
            result = []
            cannon_list = []
            defences = []
            wizz = []
            barbs = []
            arch = []
            loons = []
            huts = []
            walls = []
            flag_hero = 0
            if(which_hero == 'k' or which_hero == 'K'):
                the_hero = King(mid_x - 4,mid_y, the_king_health, the_king_health_init, the_king_damage, spawn_king)
            elif(which_hero == 'q' or which_hero == 'Q'):
                the_hero = Queen(mid_x - 4,mid_y, the_king_health, the_king_health_init, the_king_damage, spawn_king)
            the_th = TownHall(mid_x, mid_y, th_health, th_health_init)
            continue
        elif (play == 'N' or play == 'n'):
            break

    inputs = []
    inputs.append(p)

    if (p == 'W' or p == 'w' or p == 'S' or p == 's' or p == 'd' or p == 'D' or p == 'a' or p == 'A'):
        last = p

    if(the_hero.spawn == 0):
        if(p == 'j' or p == 'k' or p == 'l' or p == 'J' or p == 'K' or p == 'L'):
            last_ks = p

    for bars in barbs:
        if(bars.spawn == 0):
            if(p == 'i' or p == 'o' or p == 'p' or p == 'I' or p == 'O' or p == 'P'):
                last_bs = p  

    for a in arch:
        if(a.spawn == 0):
            if(p == 'f' or p == 'h' or p == 'g' or p == 'F' or p == 'G' or p == 'H'):
                last_as = p  

    for l in loons:
        if(l.spawn == 0):
            if(p == 'b' or p == 'n' or p == 'm' or p == 'B' or p == 'N' or p == 'M'):
                last_ls = p  
    
    for wizs in wizz:
        wizs.target = 0
        wizard_attack(wizs, wizs.pos_x, wizs.pos_y, wizs.damage, wizs.health)

    for cans in cannon_list:
        cannons_attack(cans.pos_x, cans.pos_y, cans.damage, cans.health)  

    if(time.time() - t_0 > samayam_barb):
        samayam_barb = time.time() + time_interval_barb - t_0
        for i in barbs:
            if(i.spawn == 1):
                if(i.pos_x > i.target.pos_x):
                    pb = 'w' 
                elif(i.pos_x < i.target.pos_x):
                    pb = 's'
                elif(i.pos_y > i.target.pos_y):
                    pb = 'a'
                elif(i.pos_y < i.target.pos_y):
                    pb = 'd'
                if ((pb == 'W' or pb == 'w') and (i.pos_x > 0)):
                    move_w = movement_func_w(i.pos_x, i.pos_y,move_w)
                    if (move_w == 0):
                        i.pos_x = i.pos_x - 1
                elif ((pb == 'S' or pb == 's') and i.pos_x < n-1):
                    move_s = movement_func_s(i.pos_x, i.pos_y,move_s)
                    if (move_s == 0):
                        i.pos_x = i.pos_x + 1
                elif ((pb == 'a' or pb == 'A') and i.pos_y > 0):
                    move_a = movement_func_a(i.pos_x, i.pos_y,move_a)
                    if (move_a == 0):
                        i.pos_y = i.pos_y - 1
                elif((pb == 'd' or pb == 'D') and i.pos_y < m-1):
                    move_d = movement_func_d(i.pos_x, i.pos_y,move_d)
                    if (move_d == 0):
                        i.pos_y = i.pos_y + 1
                
                attack_hut_king(i.pos_x, i.pos_y, pb)
                attack_cannon_king(i.pos_x, i.pos_y, pb)
                attack_wizzy_king(i.pos_x, i.pos_y, pb)
                attack_th_king(i.pos_x, i.pos_y, pb)
                attack_wall_king(i.pos_x, i.pos_y, pb)
                    
    if(time.time() - t_0 > samayam_arch):
        samayam_arch = time.time() + time_interval_arch - t_0
        for i in arch:
            if(i.spawn == 1):
                if(i.pos_x > i.target.pos_x):
                    xa = abs(i.pos_x - i.target.pos_x)
                    ya = abs(i.pos_y - i.target.pos_y)
                    if(xa*xa + ya*ya > 36):
                        pa = 'w'
                    else:
                        pa = '' 
                elif(i.pos_x < i.target.pos_x):
                    xa = abs(i.pos_x - i.target.pos_x)
                    ya = abs(i.pos_y - i.target.pos_y)
                    if(xa*xa + ya*ya > 36):
                        pa = 's'
                    else:
                        pa = ''
                elif(i.pos_y > i.target.pos_y):
                    xa = abs(i.pos_x - i.target.pos_x)
                    ya = abs(i.pos_y - i.target.pos_y)
                    if(xa*xa + ya*ya > 36):
                        pa = 'a'
                    else:
                        pa = ''
                elif(i.pos_y < i.target.pos_y):
                    xa = abs(i.pos_x - i.target.pos_x)
                    ya = abs(i.pos_y - i.target.pos_y)
                    if(xa*xa + ya*ya > 36):
                        pa = 'd'
                    else:
                        pa = ''
                if ((pa == 'W' or pa == 'w') and (i.pos_x > 0)):
                    i.pos_x = i.pos_x - 1
                elif ((pa == 'S' or pa == 's') and i.pos_x < n-1):
                    i.pos_x = i.pos_x + 1
                elif ((pa == 'a' or pa == 'A') and i.pos_y > 0):
                    i.pos_y = i.pos_y - 1
                elif((pa == 'd' or pa == 'D') and i.pos_y < m-1):
                    i.pos_y = i.pos_y + 1
                archer_attack(i, i.target, pa)

    if(time.time() - t_0 > samayam_loon):
            samayam_loon = time.time() + time_interval_loon - t_0
            for i in loons:
                pl = ''
                if(i.spawn == 1):
                    if(i.pos_x > i.target.pos_x):
                        pl = 'w' 
                    elif(i.pos_x < i.target.pos_x):
                        pl = 's'
                    elif(i.pos_y > i.target.pos_y):
                        pl = 'a'
                    elif(i.pos_y < i.target.pos_y):
                        pl = 'd'
                    if ((pl == 'W' or pl == 'w') and (i.pos_x > 0)):
                        i.pos_x = i.pos_x - 1
                    elif ((pl == 'S' or pl == 's') and i.pos_x < n-1):
                        i.pos_x = i.pos_x + 1
                    elif ((pl == 'a' or pl == 'A') and i.pos_y > 0):
                        i.pos_y = i.pos_y - 1
                    elif((pl == 'd' or pl == 'D') and i.pos_y < m-1):
                        i.pos_y = i.pos_y + 1

                    loon_attack(i, i.target)

    if ((p == 'W' or p == 'w') and (the_hero.pos_x > 0)):
        move_w = movement_func_w(the_hero.pos_x, the_hero.pos_y,move_w)
        if (move_w == 0):
           the_hero.pos_x = the_hero.pos_x - 1
    elif ((p == 'S' or p == 's') and the_hero.pos_x < n-1):
        move_s = movement_func_s(the_hero.pos_x, the_hero.pos_y,move_s)
        if (move_s == 0):
            the_hero.pos_x = the_hero.pos_x + 1
    elif ((p == 'a' or p == 'A') and the_hero.pos_y > 0):
        move_a = movement_func_a(the_hero.pos_x, the_hero.pos_y,move_a)
        if (move_a == 0):
            the_hero.pos_y = the_hero.pos_y - 1
    elif((p == 'd' or p == 'D') and the_hero.pos_y < m-1):
        move_d = movement_func_d(the_hero.pos_x, the_hero.pos_y,move_d)
        if (move_d == 0):
            the_hero.pos_y = the_hero.pos_y + 1
    elif((p == ' ') and the_hero.health > 0):
        if(which_hero == 'k' or which_hero == 'K'):
            attack_hut_king(the_hero.pos_x, the_hero.pos_y, last)
            attack_cannon_king(the_hero.pos_x, the_hero.pos_y, last)
            attack_wizzy_king(the_hero.pos_x, the_hero.pos_y, last)
            attack_th_king(the_hero.pos_x, the_hero.pos_y, last)
            attack_wall_king(the_hero.pos_x, the_hero.pos_y, last)
        elif(which_hero == 'q' or which_hero == 'Q'):
            attack_queen(the_hero.pos_x, the_hero.pos_y, last)

    elif(p == 'q' or p == 'Q'):
        break
    
    elif( (p == 'j' or p == 'J') and the_hero.spawn == 0):
        the_hero.spawn = the_hero.spawn + 1
        troops.append(the_hero)
        the_hero.pos_x = mid_x - 4
        the_hero.pos_y = mid_y
    
    elif( (p == 'k' or p == 'K') and the_hero.spawn == 0):
        the_hero.spawn = the_hero.spawn + 1
        troops.append(the_hero)
        the_hero.pos_x = mid_x + 7
        the_hero.pos_y = mid_y - 7
    
    elif( (p == 'l' or p == 'L') and the_hero.spawn == 0):
        the_hero.spawn = the_hero.spawn + 1
        troops.append(the_hero)
        the_hero.pos_x = mid_x + 7
        the_hero.pos_y = mid_y + 7

    elif(p == 'i' or p == 'I'):
        for i in barbs:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x - 5
                i.pos_y = mid_y
                break
    
    elif(p == 'f' or p == 'F'):
        for i in arch:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x - 5
                i.pos_y = mid_y
                break
    
    elif(p == 'B' or p == 'b'):
        for i in loons:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x - 5
                i.pos_y = mid_y
                break

    elif( p == 'o' or p == 'O'):
        for i in barbs:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x + 7
                i.pos_y = mid_y - 7
                break
    
    elif(p == 'g' or p == 'G'):
        for i in arch:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x + 7
                i.pos_y = mid_y - 7
                break
    
    elif(p == 'N' or p == 'n'):
        for i in loons:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x + 7
                i.pos_y = mid_y - 7
                break

    elif(p == 'p' or p == 'P'):
        for i in barbs:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x + 7
                i.pos_y = mid_y + 7
                break
    
    elif(p == 'h' or p == 'H'):
        for i in arch:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x + 7
                i.pos_y = mid_y + 7
                break
    
    elif(p == 'M' or p == 'm'):
        for i in loons:
            if(i.spawn == 0):
                i.spawn = 1
                troops.append(i)
                i.pos_x = mid_x + 7
                i.pos_y = mid_y + 7
                break
                
    elif(p == 'x' or p == 'X'):
        if(which_hero == 'k' or which_hero == 'K'):
            area_slash(the_hero.pos_x, the_hero.pos_y, buildings)
        elif(which_hero == 'q' or which_hero == 'Q'):
            queen_attack_time = time.time()
            queen_x_factor = 1
            
    if(queen_x_factor):
        if(time.time() - queen_attack_time > 1):
            queen_x_factor = 0
            queen_bonus(the_hero.pos_x, the_hero.pos_y, last)
            
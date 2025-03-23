# Pac_Man_Try
 
## Project done in 11th for fun.

## Overview:

An endless arcade game made for chasing high scores. Uses Tkinter and Turtle to give a cute and fun retro arcade game like interface with blinking hearts as you lose and score counters. Fun, engaging game play with each level getting increasingly harder with no limits thanks to procedural level generation. 

## Game:

Player can use arrow keys or WAS keys to move forward and turn left/right. The game starts off with 4 "ghosts" to avoid. 1 life out of 3 total is lost each time player is in contact with a ghost. There are also procedurally generated walls the player must traverse through.
The player must collect apples that appear at random places in the screen lasting a few seconds each time. There is also a blue and a red pellet that allows the player to go through a wall and destroy a "ghost" respectively.

## Progression:

Goal of the game is to eat as many apples as possible.
The levels increase as you eat more apples in multiples of 5.
As the levels increase:
    1. Number of apples needed to progress to next level increases.
    2. Number or pellets needed to break 1 wall/destroy 1 ghost increases.
    3. Time the pellets and apples last before randomly generating elsewhere reduces.
    4. Number of walls increases.
    5. Number of "ghosts" and speed of each "ghost" increases.

Hence increasing the difficulty of the game.

## Issues:
It is possible to glitch through walls by holding forward and moving faster than the tick speed. This is less of an issue with faster computers running the game.

There is no leader board option.

## How to play:
To play, download this folder and run the pac man try.py file (Preferably with IDLE)
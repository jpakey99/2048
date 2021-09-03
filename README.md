# 2048

# Project Statement
This project will not only provide users with the ability to play the game, but also simulate a game of 2048 using an algorithm.  2048 is played on a square 4x4 grid in which each cell either is empty or filled.  A filled cell contains a power of 2 (2,4,8,16,32,64,128,256,512,1024,2048...).  The moves of the game are in the form of swipes in the cardinal directions (north [up], south [down], west [left], or east [right]).  The swipe moves all filled cells in that direction as far as possible while keeping the sqaure space and not taking up the same cell.  All cells that were once filled will becomde empty if that filled cell can move in the direction of the swipe.  Filled cells with the same number will combine into a new filled cell of the next power of 2.  The goal of the game is to eventually reach 2048.  The algorthms players can simulate will be defined later.

# Features
- Ability for Users to type commands in command promt to control the game
- Ability to swipe on a graphical user interface that control the game
- Correct movement of cells during a move (combination not apart)
- Combining of cells works

# Domain Diagram
![Domain Model](https://user-images.githubusercontent.com/15817820/132010793-20a92f36-72d5-43cd-9ae1-a8831cc83135.PNG)

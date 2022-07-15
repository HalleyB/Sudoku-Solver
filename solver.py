#suduko solver
import sys, pygame as pg, numpy as np
pg.font.init()


#fonts used in this code
myfont = pg.font.SysFont('Comin Sans MS', 35)
myfont2 = pg.font.SysFont('Comin Sans MS', 75)

#the background color for the puzzle
bg_color= 'white'


#solves the sudoku puzzle array
def solve(bo):
    #finds the empty square, returns as a tuple
    find = find_empty(bo)
    if not find:
        return True
    else:
        #returns the pos of the empty square
        row, col = find



    #checks all the numbers through the valid function
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0

    return False

#checks to see if the number is valid
def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0]!= i:
            return False

    #check cube
    #we divide the pos of the box by 3 so we know what cube we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #by multiplying the box by 3, we get a clear answer for the cube.
    #for instance, if we are doing arr pos[4], 4 // 3 = 1, 1*3 = 3,
    #3, 3+3 will loop us through arr[3]-arr[5]
    for i in range(box_y *3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    #if it passes all the tests, returns true
    return True

#finds and empty square
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    #returns none if there are no empty squares
    return None

#checks the board for invalid input
def check(bo, win):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if valid(bo, bo[i][j], (i, j)) == False and bo[i][j] != 0:
                drawNumber(str(bo[i][j]), 'red', i, j, win)
                return False

#draws the lines for the puzzle
def drawBackground(win):
    for i in range(0, 10):
        if (i %3 ==0):
            pg.draw.line(win, 'black', (50*i, 0), (50*i, 450), 4)
            pg.draw.line(win, 'black', (0,50*i), (450,50*i), 4)

        pg.draw.line(win, 'black', (50*i, 0), (50*i, 450), 2)
        pg.draw.line(win, 'black', (0,50*i), (450,50*i), 2)

    pg.display.update()
    bg_color= 'white'

#draws any buttons
def drawButton(win, color, textColor, rect, text):
    rectangle = pg.Rect(rect[0], rect[1], rect[2], rect[3])
    pg.draw.rect(win, color, rectangle)
    displayText = myfont2.render(text, False, textColor)
    win.blit(displayText, (rect[0]+22, rect[1]+18))

#draws the numbers inside the puzzle
def drawNumber(text, color, pos1, pos2, win):
    number = myfont.render(text, False, color)
    win.blit(number, (pos1*50 + 20, pos2*50 + 20))
    pg.display.update()

def badInput(bo, uBo, win):
    noSol = pg.Rect(50, 175, 350, 80)
    drawButton(win, 'black', 'white', noSol, 'Invalid Input')
    pg.display.update()
    pg.time.wait(1500)
    reset(bo, win)
    #redraws the user board, for convinience
    for i in range(len(uBo)):
        for j in range(len(uBo[0])):
            uNum = uBo[i][j]
            if uNum == 1:
                drawNumber('1', 'black', j, i, win)
            if uNum == 2:
                drawNumber('2', 'black', j, i, win)
            if uNum == 3:
                drawNumber('3', 'black', j, i, win)
            if uNum == 4:
                drawNumber('4', 'black', j, i, win)
            if uNum == 5:
                drawNumber('5', 'black', j, i, win)
            if uNum == 6:
                drawNumber('6', 'black', j, i, win)
            if uNum == 7:
                drawNumber('7', 'black', j, i, win)
            if uNum == 8:
                drawNumber('8', 'black', j, i, win)
            if uNum == 9:
                drawNumber('9', 'black', j, i, win)
    #keeps the bad number red
    check(uBo, win)
    

#puts the user input on screen
def number(bo, event, win, i, j):
    if event.key == pg.K_1:
        bo[i][j] = 1
        drawNumber('1', 'black', j, i, win)
    if event.key == pg.K_2:
        bo[i][j] = 2
        drawNumber('2', 'black', j, i, win)
    if event.key == pg.K_3:
        bo[i][j] = 3
        drawNumber('3', 'black', j, i, win)
    if event.key == pg.K_4:
        bo[i][j] = 4
        drawNumber('4', 'black', j, i, win)
    if event.key == pg.K_5:
        bo[i][j] = 5
        drawNumber('5', 'black', j, i, win)
    if event.key == pg.K_6:
        bo[i][j] = 6
        drawNumber('6', 'black', j, i, win)
    if event.key == pg.K_7:
        bo[i][j] = 7
        drawNumber('7', 'black', j, i, win)
    if event.key == pg.K_8:
        bo[i][j] = 8
        drawNumber('8', 'black', j, i, win)
    if event.key == pg.K_9:
        bo[i][j] = 9
        drawNumber('9', 'black', j, i, win)
    if event.key == pg.K_0:
        bo[i][j] = 0
        eraser = pg.Rect(j*50+5, i*50+5, 40, 40)
        pg.draw.rect(win, 'white', eraser)
        pg.display.update()

#resets the board  and the array
def reset(bo, win):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            bo[i][j] = 0

    win.fill(bg_color)
    drawBackground(win)

#prints the board
def print_board(bo):
    for i in range(len(bo)):
        if (i % 3 ==0) and (i != 0):
            print('- - - - - - - - - - - - - -')
        for j in range(len(bo[0])):
            if (j % 3 == 0) and (j != 0):
                print(" | ", end="")

            if (j==8):
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end='')

#prints the array on the window
def print_win(bo, uBo, win):          
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            curNum = bo[i][j]
            uNum = uBo[i][j]
            if curNum != uNum:            
                if curNum == 1:
                    drawNumber('1', 'blue', j, i, win)
                if curNum == 2:
                    drawNumber('2', 'blue', j, i, win)
                if curNum == 3:
                    drawNumber('3', 'blue', j, i, win)
                if curNum == 4:
                    drawNumber('4', 'blue', j, i, win)
                if curNum == 5:
                    drawNumber('5', 'blue', j, i, win)
                if curNum == 6:
                    drawNumber('6', 'blue', j, i, win)
                if curNum == 7:
                    drawNumber('7', 'blue', j, i, win)
                if curNum == 8:
                    drawNumber('8', 'blue', j, i, win)
                if curNum == 9:
                    drawNumber('9', 'blue', j, i, win)
                #pauses for number of miliseconds, for aestetics
                pg.time.wait(150)

#runs the program    
def main():
    #creating the window
    win = pg.display.set_mode((452, 550))
    pg.display.set_caption('Sudoku')
    win.fill(bg_color)

    #the buttons
    solveRect = [25, 460, 188, 80]
    resetRect = [238, 460, 188, 80]

    #draws the buttons and the puzzle lines
    drawBackground(win)
    drawButton(win, 'black', 'white', solveRect, 'Solve')
    drawButton(win, 'black', 'white', resetRect, 'Reset')
    pg.display.update()

    #empty board to get user input
    board = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]

    #loop that runs the program                    
    while 1:
        pos = pg.mouse.get_pos()
        i,j = pos[1], pos[0]
        i = i //50
        j = j //50
        for event in pg.event.get():
            #changes the color to grey if the mouse hovers over the solve button
            if ((213 > pos[0] > 25) and (540 > pos[1] > 460)):
                drawButton(win, 'grey', 'white', solveRect, 'Solve')
                pg.display.update()
                
            elif((213 < pos[0] or pos[0] < 25) or (540 < pos[1] or pos[1] < 460)):
                drawButton(win, 'black', 'white', solveRect, 'Solve')
                pg.display.update()

            #changes the color to grey if the mouse hovers over the reset button
            if ((426 > pos[0] > 238) and (540 > pos[1] > 460)):
                drawButton(win, 'grey', 'white', resetRect, 'Reset')
                pg.display.update()
                
            elif((426 < pos[0] or pos[0] < 238) or (540 < pos[1] or pos[1] < 460)):
                drawButton(win, 'black', 'white', resetRect, 'Reset')
                pg.display.update()

            #closes the program
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                quit()

            elif event.type == pg.MOUSEBUTTONUP and event.button ==1:
                #runs solve if the solve button is clicked
                if ((213 > pos[0] > 25) and (540 > pos[1] > 460)):
                    #same board to draw in the user board after
                    userBoard = np.copy(board)
                    if check(userBoard, win) != False:
                        solve(board)
                        print_win(board, userBoard, win)
                    #if check fails, resets the board
                    else:
                        badInput(board, userBoard, win)
                        board = np.copy(userBoard)

                #runs reset if the rest button is clicked
                if ((426 > pos[0] > 238) and (540 > pos[1] > 460)):
                    reset(board, win)
                    
            #adds numbers to the board and on screen
            elif event.type == pg.KEYDOWN:
                #ensures that the pos is within range
                if (i < 9 and j < 9):
                    number(board, event, win, i, j)


main()

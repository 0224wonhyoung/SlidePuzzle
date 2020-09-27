from bangtal import *
import random

width = 4
height = 4

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("슬라이드퍼즐", "Images/배경.jpg")

arr = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def addInRange(x, y, f, t):
    s = x+y
    if f<=s and s<=t:
        return s
    return -1

def piece_onMouseAction(object, x, y, action):
    objNum = -1
    for i in range(0, width*height):
        if piece[i].pieceObj == object:
            objNum = i
            piece

def printArr():
    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[3])
    for i in range(0,16):
        if piece[i].hidden == True:
            print(str(i)+" is hide")




class Piece:

    def __init__(self, width, height, n):
        self.pieceObj = Object("Images/in"+str(n+1)+".jpg")
        self.x = n % width
        self.y = int(n/height)
        self.num = n
        
        self.locate(self.x, self.y)
        self.show()
        
        self.pieceObj.onMouseActionDefault = piece_onMouseAction

    def hide(self):
        self.pieceObj.hide()
        self.hidden = True

    def show(self):
        self.pieceObj.show()
        self.hidden = False

    def locate(self, x, y):
        self.pieceObj.locate(scene, 340 + 150*self.x, 510 - 150*self.y)

    def try_swap(self):
        #near = False
        flag = False
        for i in range(0, 4):
            tx = self.x + dx[i]
            ty = self.y + dy[i]
            if -1 < tx and tx < width and -1 < ty and ty < height and flag == False:
                if piece[arr[ty][tx]].hidden == True:
                    flag = True
                    near = True                    
                    hideNum = arr[ty][tx]                    
                    #print("Hide Num : "+str(hideNum))

                    piece[hideNum].x = self.x
                    piece[hideNum].y = self.y
                    piece[hideNum].locate(self.x, self.y)
                    arr[self.y][self.x] = hideNum

                    self.x = tx
                    self.y = ty
                    self.locate(tx, ty)
                    arr[ty][tx] = self.num 
            #else:
                #print("check")
           
             
        #if near == False :
            #print("NO HIDDEN NEAR")
           

                

piece = []
for i in range(0, width*height):
    piece.append(Piece(width, height, i))


piece[random.randint(0,width*height-1)].hide()

def piece_onMouseAction(object, x, y, action):
    objNum = -1
    for i in range(0, width*height):
        if piece[i].pieceObj == object:
            objNum = i
            piece[i].try_swap()
    #printArr()

Object.onMouseActionDefault = piece_onMouseAction 

#for i in range(0, width*height):
#    piece[i].pieceObj.onMouseActionDefault = piece_onMouseAction





startGame(scene)



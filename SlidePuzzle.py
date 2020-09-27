from bangtal import *
import random

shuffleNum = 10
stageNum = 1
width = [3, 4, 5]
height = [3, 4, 5]
piece_width = [200, 150, 120]
piece_height = [200, 150, 120]
hiddenPiece = 0
inGame = False
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
setGameOption(GameOption.ROOM_TITLE, False)
scene = [Scene("3X3", "Images/stage1/배경1.jpg"), Scene("4X4", "Images/stage2/배경2.jpg"), Scene("5x5", "Images/stage3/배경3.jpg")]
scene_menu = Scene("SlidePuzzle","Images/stage1/배경1.jpg")
arr =[[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16,17, 18, 19], [20, 21, 22, 23, 24]] ]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def printStageNum():
    print(stageNum)

def checkFin():
    for i in range(0, width[stageNum]*height[stageNum]):
        cpiece = piece[stageNum][i]
        if cpiece.x != (cpiece.num % width[stageNum]) or cpiece.y != int(cpiece.num/height[stageNum]):
            return False
    return True

def piece_onMouseAction(object, x, y, action):
    global stageNum
    global inGame
    for i in range(0, width[stageNum]*height[stageNum]):
        if piece[stageNum][i].pieceObj == object:            
            piece[stageNum][i].try_swap()
            if inGame == True and checkFin():                
                inGame = False
                piece[stageNum][hiddenPiece].show()
                showMessage("ClEAR!")
                startButton[stageNum].show()
            return
    for i in range(0, 3):
        if object == stageButton[i]:
            stageNum = i
            initStage()
            scene[i].enter()
            printStageNum()
            return
    for i in range(0, 3):
        if object == startButton[i]:            
            shuffle()
            startButton[i].hide()            
            inGame = True
            return
    for i in range(0, 3):
        if object == menuButton[i]:
            inGame = False
            scene_menu.enter()
            return
    
def initStage():    
    global stageNum
    for i in range(0, width[stageNum]*height[stageNum]):        
        piece[stageNum][i].backToInit()
    startButton[stageNum].show()

def shuffle():
    global hiddenPiece
    global stageNum
    
    initStage()
    
    hNum = random.randint(0,width[stageNum]*height[stageNum]-1)
    piece[stageNum][hNum].hide()
    hiddenPiece = hNum
    #print(hiddenPiece)    
    
    for i in range(0, shuffleNum):
        
        randN = random.randint(0,3)        
        piece[stageNum][hNum].swap(randN)



class Piece:
    
    def __init__(self, n, sn):
               
        self.pieceObj = Object("Images/stage"+str(sn+1)+"/in"+str(n+1)+".jpg")
        self.x = n % width[sn]
        self.y = int(n/height[sn])
        self.num = n
        self.stageNum = sn
        
        self.locate(self.x, self.y)
        self.show()
        
        self.pieceObj.onMouseActionDefault = piece_onMouseAction

    def backToInit(self):
        self.x = self.num % width[self.stageNum]
        self.y = int(self.num/height[self.stageNum])
        self.locate(self.x, self.y)
        self.show()
        arr[self.stageNum][self.y][self.x] = self.num

    def hide(self):
        self.pieceObj.hide()
        self.hidden = True

    def show(self):
        self.pieceObj.show()
        self.hidden = False

    def locate(self, x, y):
        self.pieceObj.locate(scene[self.stageNum], 340 + piece_width[self.stageNum]*self.x, 660 - piece_height[self.stageNum]*(self.y+1))

    def swap(self, dir):      
        
        tx = self.x + dx[dir]
        ty = self.y + dy[dir]        
        if -1 < tx and tx < width[self.stageNum] and -1 < ty and ty < height[self.stageNum] :
            tn = arr[self.stageNum][ty][tx]
            
            piece[self.stageNum][tn].x = self.x
            piece[self.stageNum][tn].y = self.y
            piece[self.stageNum][tn].locate(self.x, self.y)
            arr[self.stageNum][self.y][self.x] = tn

            self.x = tx
            self.y = ty
            self.locate(tx, ty)
            arr[self.stageNum][ty][tx] = self.num 

    def try_swap(self):        
        #near = False
        flag = False
        for i in range(0, 4):
            tx = self.x + dx[i]
            ty = self.y + dy[i]
            if -1 < tx and tx < width[self.stageNum] and -1 < ty and ty < height[self.stageNum] and flag == False:
                if piece[self.stageNum][arr[self.stageNum][ty][tx]].hidden == True:
                    flag = True
                    near = True                    
                    hideNum = arr[self.stageNum][ty][tx]                    
                    #print("Hide Num : "+str(hideNum))

                    piece[self.stageNum][hideNum].x = self.x
                    piece[self.stageNum][hideNum].y = self.y
                    piece[self.stageNum][hideNum].locate(self.x, self.y)
                    arr[self.stageNum][self.y][self.x] = hideNum

                    self.x = tx
                    self.y = ty
                    self.locate(tx, ty)
                    arr[self.stageNum][ty][tx] = self.num 
            #else:
                #print("check")
           
             
        #if near == False :
            #print("NO HIDDEN NEAR")
           

                
piece = []

piece0 = []
for i in range(0, width[0]*height[0]):
    piece0.append(Piece(i, 0))
piece.append(piece0)

piece1 = []
for i in range(0, width[1]*height[1]):
    piece1.append(Piece(i, 1))
piece.append(piece1)

piece2 = []
for i in range(0, width[2]*height[2]):
    piece2.append(Piece(i, 2))
piece.append(piece2)

Object.onMouseActionDefault = piece_onMouseAction 

startButton = []
for i in range(0, 3):
    startButton.append(Object("Images/start.png"))
    startButton[i].locate(scene[i], 590, 10)
    startButton[i].show()


stageButton = []
sbX=[0, 427, 853]
for i in range(0, 3):
    stageButton.append(Object("Images/m"+str(i)+".jpg"))
    stageButton[i].locate(scene_menu, sbX[i], 0)
    stageButton[i].show()

menuButton = []
for i in range(0, 3):
    menuButton.append(Object("Images/menu.png"))
    menuButton[i].locate(scene[i], 50, 650)
    menuButton[i].show()


#for i in range(0, width*height):
#    piece[i].pieceObj.onMouseActionDefault = piece_onMouseAction


startGame(scene_menu)



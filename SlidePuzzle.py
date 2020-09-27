from bangtal import *

width = 4
height = 4

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("슬라이드퍼즐", "Images/배경.jpg")

class Piece:

    def __init__(self, width, height, n):
        self.pieceObj = Object("Images/in"+str(n+1)+".jpg")
        self.x = n % width
        self.y = int(n/height)
        self.pieceObj.locate(scene, 340 + 150*self.x, 510 - 150*self.y)
        self.pieceObj.show()

    def hide(self):
        self.pieceObj.hide()


        

piece = []
for i in range(0, width*height):
    piece.append(Piece(width, height, i))
piece[5].hide()

startGame(scene)



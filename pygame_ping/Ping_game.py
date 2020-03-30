import turtle

class Shape(turtle.Turtle):

    def __init__(self, goto):
        
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(goto,0)

class Player(Shape):

    def __init__(self, goto):
        
        Shape.__init__(self,goto)
        self.shapesize(6,0.7)

    def comUp(self):

        self.sety(self.ycor() + 20)

    def comDown(self):

        self.sety(self.ycor() - 20)
        
class Bola(Shape):

    def __init__(self, goto):

        Shape.__init__(self,goto)
        self.vx = 2.5
        self.vy = 2.5
        
    def update(self):
        
        self.colisao()
        self.setx(self.xcor() + self.vx)
        self.sety(self.ycor() + self.vy)

    def colisao(self):
        
        if(self.ycor() > 290):
            self.sety(290)
            self.vy *= -1

        elif(self.ycor() < -290):
            self.sety(-290)
            self.vy *= -1

#        elif(self.xcor() > 350):
#            self.setx(350)
#            self.vx *= -1
#
#        elif(self.xcor() > 350):
#            self.setx(-350)
#            self.vx *= 1
            
        
jogadorA = Player(-350)
jogadorB = Player(350)
bola = Bola(0)

janela = turtle.Screen()
janela.title("Ping Game")
janela.bgcolor("black")
janela.setup(width = 800, height = 600)
janela.listen()
janela.onkeypress(jogadorA.comUp, "w")
janela.onkeypress(jogadorA.comDown, "s")
janela.onkeypress(jogadorB.comUp, "Up")
janela.onkeypress(jogadorB.comDown, "Down")

while(True):
    
    janela.update()
    bola.update()















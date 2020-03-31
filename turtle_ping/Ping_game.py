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
        self.vx = 0.3
        self.vy = 0.3
        
    def update(self,jogadorA,jogadorB):
        
        self.colisao(jogadorA,jogadorB)
        self.setx(self.xcor() + self.vx)
        self.sety(self.ycor() + self.vy)

    def colisao(self,jogadorA,jogadorB):
        
        if(self.ycor() > 290):
            self.sety(290)
            self.vy *= -1

        elif(self.ycor() < -290):
            self.sety(-290)
            self.vy *= -1

        if(self.xcor() < -340 and self.diff(jogadorA)):
            self.vx *= -1
            
        if(self.xcor() > 340 and self.diff(jogadorB)):
            self.vx *= -1
            
    def diff(self, player):
        return self.ycor() < player.ycor() + 60 and self.ycor() > player.ycor() - 60

class Score(Shape):

    def __init__(self, goto):
        
        Shape.__init__(self, goto)
        self.goto(0, goto)
        self.score_um = 0 
        self.score_dois = 0
        self.hideturtle()
        self.desenhar()

    def update(self, ball):
        
        if(ball.xcor() > 350):
            self.score_um += 1
            self.clear()
            self.desenhar()
            ball.goto(0,0)

        elif(ball.xcor() < -350):
            self.score_dois += 1
            self.clear()
            self.desenhar()
            ball.goto(0,0)
       
    def desenhar(self):

        self.write("Jogador 1: {}  Jogador 2: {}".format(self.score_um, self.score_dois),
                   font = ("Arial", 22, "normal"), align = "center")
        
jogadorA = Player(-350)
jogadorB = Player(350)
bola = Bola(0)
placar = Score(250)

janela = turtle.Screen()
janela.title("Ping Game")
janela.bgcolor("black")
janela.setup(width = 800, height = 600)
janela.tracer(0,0)
janela.listen()
janela.onkeypress(jogadorA.comUp, "w")
janela.onkeypress(jogadorA.comDown, "s")
janela.onkeypress(jogadorB.comUp, "Up")
janela.onkeypress(jogadorB.comDown, "Down")

while(True):
    
    janela.update()
    bola.update(jogadorA,jogadorB)
    placar.update(bola)
    

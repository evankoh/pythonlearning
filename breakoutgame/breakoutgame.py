#To import tkinter library
import tkinter as tk

#Define Game class
class Game(tk.Frame):
    def __init__(self,master):
        super(Game,self).__init__(master)
        self.lives=3
        self.width=610
        self.height=400
        self.canvas=tk.Canvas(self,bg='#aaaaff',width=self.width,height=self.height)
        self.canvas.pack()
        self.pack()

#Define GameObject class to create assets in game
class GameObject(object):
    def __init__(self,canvas,item):
        self.canvas=canvas
        self.item=item
        
    def get_position(self):
        return self.canvas.coords(self.item)
        
    def move(self,x,y):
        self.canvas.move(self.item,x,y)
    
    def delete(self):
        self.canvas.delete(self.item)
        
#Define Ball class to create ball in game
class Ball(GameObject):
    def __init__(self,canvas,x,y):
        self.radius=10
        self.direction=[1,-1]
        self.speed=10
        item=canvas.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill='white')
        super(Ball,self).__init__(canvas,item)

#Define Paddle class to create paddle in game
class Paddle(GameObject):
    def __init__(self,canvas,x,y):
        self.width=80
        self.height=10
        self.ball=None
        item=canvas.create_rectangle(x-self.width/2,y-self.height/2,x+self.width/2,y+self.height/2,fill='blue')
        super(Paddle,self).__init__(canvas,item)
    
    def set_ball(self,ball):
        self.ball=ball
        
    def move(self,offset):
        coords=self.get_position()
        width=self.canvas.winfo_width()
        if coords[0]+offset>=0 and coords[2] + offset <= width:
            super(Paddle,self).move(offset,0)
            if self.ball is not None:
                self.ball.move(offset,0)

#Define Brick class to create bricks in game
class Brick(GameObject):
    COLORS={1:'#999999',2:'#555555',3:'222222'}
    
    def __init__(self,canvas,x,y,hits):
        self.width=75
        self.height=20
        self.hits=hits
        color=Brick.COLORS[hits]
        item=canvas.create_rectangle(x-self.width/2,y-self.height/2,x+self.width/2,y+self.height/2,fill=color,tags='brick')
        super(Brick,self).__init__(canvas,item)
    
    def hit(self):
        self.hits=-1
        if self.hits==0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item,fill=Brick.COLORS[self.hits])
    

if __name__=='__main__':
    root=tk.Tk()
    root.title('Hello, Pong!')
    game=Game(root)
    game.mainloop()

#item = canvas.create_rectangle(10,10,100,80,fill='green')
#game_object=GameObject(canvas,item)

#print(game_object.get_position())
#[10,10,100,80]
#game_object.move(20,-10)
#print(game_object.get_position())
#[30,0,120,70]
#game_object.delete()
from tkinter import *
import random

#VARIABLES

GAME_NAME = "Snake";
WIDTH = 700;
HEIGHT = 700;
BACKGROUND_COLOR = "#000000"
SQUARE_SIZE = 50
SNAKECOLOR = "#FF00DD"
SNAKEPARTS = 3
SPEED = 500
window = Tk();
canva = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH);


# CLASSES

class Snake:

	def __init__(self):
		self.bodyParts = SNAKEPARTS;
		self.squares = [];
		self.coordinates = []
  
		for i in range(0, self.bodyParts):
			self.coordinates.append([0, 0]);

		for x,y in self.coordinates:
			square = canva.create_rectangle(x, y, x+SQUARE_SIZE, y+SQUARE_SIZE, fill=SNAKECOLOR);
			self.squares.append(square);
			
class Food:
	COLOR = "#00FF00"
	def __init__(self):
		x = random.randint(0, int(WIDTH / SQUARE_SIZE) - 1) * SQUARE_SIZE
		y = random.randint(0, int(HEIGHT / SQUARE_SIZE)-1) * SQUARE_SIZE
		self.coordinates = [x, y];
		self.food = canva.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=self.COLOR)

# FUNTIONS

def change_direction(nextDirection):
	global direction
	if (nextDirection == "left"):
		if(direction != "right"):
			direction = nextDirection;

	elif (nextDirection == "right"):
		if(direction != "left"):
			direction = nextDirection;

	elif (nextDirection == "down"):
		if(direction != "up"):
			direction = nextDirection;

	elif (nextDirection == "up"):
		if(direction != "dowm"):
			direction = nextDirection;

def next_turn(Snake, food):
	x, y = Snake.coordinates[0];
	if (direction == "up"):
		y -= SQUARE_SIZE;
	elif (direction == "down"):
		y += SQUARE_SIZE;
	elif (direction == "left"):
		x -= SQUARE_SIZE;
	elif (direction == "right"):
		x += SQUARE_SIZE;


	Snake.coordinates.insert(0, [x, y]);
	square = canva.create_rectangle(x, y, x + SQUARE_SIZE, y+SQUARE_SIZE, fill=SNAKECOLOR);
	Snake.squares.insert(0, square);
	check_collision(Snake);

	if (x==food.coordinates[0] and y == food.coordinates[1]):
		global score
		score += 1;
		label.config(text='score= {}'.format(score));
		canva.delete(food.food)
		food = Food()
	else:
		del snake.coordinates[-1]
		canva.delete(Snake.squares[-1])
		del snake.squares[-1]
	if (check_collision(Snake)):
		game_over()
	else:
		window.after(SPEED, next_turn, Snake, food) 

def check_collision(snake):
	x, y = snake.coordinates[0];
	if(x >= WIDTH or x < 0):
		return True;
	if(y >= HEIGHT or y < 0):
		return True;

    		
	return False;

def game_over():
	print("GAME OVER")
	canva.delete(ALL)
	canva.create_text(canva.winfo_width() / 2, canva.winfo_height() / 2, text="GAME OVER", fill="red", font=("consolas", 70))

snake = Snake();
food = Food();
score = 0
direction = 'down'

window.title(GAME_NAME);
window.resizable(False, False);

next_turn(snake, food)
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Escape>", lambda event: 	window.quit())

label = Label(window, text='score= {}'.format(score), font=('consolas', 40));
label.pack();

canva.pack();


window.mainloop();


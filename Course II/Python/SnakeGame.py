import tkinter as tk
from random import randint, choice
from PIL import Image, ImageTk


INCREMENT_STEP = 20
MOVES_PER_SECOND = 7
GAME_SPEED = 1000 // MOVES_PER_SECOND

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=640, background="black", highlightthickness=0)
        # highlightthickness убираем белые края canvas
        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_pos()
        # Изначальное направление вправо
        self.direction = "Right"
        self.score = 0
        self.food_list = []
        self.keys_history = ["Right"]*3
        self.load_imgs()
        self.create_objects()
        self.pack()

        self.bind_all("<KeyPress>", self.action)
        self.after(GAME_SPEED, self.main_process)

    def load_imgs(self):
        """Загрузка картинок с каталога"""
        try:
            self.snake_body_image = Image.open("./imgs/snake.png")
            self.snake_head_image = Image.open("./imgs/snake_head.png")
            self.apple_image = Image.open("./imgs/apple.png")
            self.grape_image = Image.open("./imgs/grape.png")
            self.snake_tail = Image.open("./imgs/snake_tail.png")

            self.tail_0 = ImageTk.PhotoImage(self.snake_tail)
            self.tail_90 = ImageTk.PhotoImage(self.snake_tail.transpose(Image.ROTATE_90))
            self.tail_180 = ImageTk.PhotoImage(self.snake_tail.transpose(Image.ROTATE_180))
            self.tail_270 = ImageTk.PhotoImage(self.snake_tail.transpose(Image.ROTATE_270))
            
            self.snake_horizontal = self.snake_head_image.transpose(Image.ROTATE_90)
            self.snake_vertical = self.snake_head_image

            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
            self.snake_head = ImageTk.PhotoImage(self.snake_horizontal)
            
            self.snake_head_horizontal = ImageTk.PhotoImage(self.snake_horizontal)
            self.snake_head_vertical = ImageTk.PhotoImage(self.snake_vertical)
            
            
            self.apple = ImageTk.PhotoImage(self.apple_image)
            self.grape = ImageTk.PhotoImage(self.grape_image)
            self.food_list.append(self.apple)
            self.food_list.append(self.grape)
            self.food = choice(self.food_list)

        except IOError:
            root.destroy()

    def create_objects(self):
        """
Создание объектов
    \nObjects:
    Score: text
    Speed: text
    Snake_head: image
    Snake_body: image
    Snake_tail: image
    Food: image
    Rectangle: square {Границы игрового поля}
        """

        self.create_text(
            50, 15, text=f"Score: {self.score}", tag="score", fill="#fff", font=("Arial", 14))

        self.create_text(
            550, 15, text=f"Speed: {MOVES_PER_SECOND}", tag="speed", fill="#fff", font=("Arial", 14))
        for x_position, y_position in self.snake_positions[:1]:
            self.head_pos = self.create_image(x_position, y_position, image=self.snake_head, tag="snake")
        

        for x_position, y_position in self.snake_positions[1:]:
            self.create_image(
                x_position, y_position, image=self.snake_body, tag="snake"
            )
        self.tail_pos = self.create_image(self.snake_positions[-1][0], self.snake_positions[-1][1], image=self.tail_270, tag="tail")
        
        self.create_image(*self.food_position, image=self.food, tag="food")
        self.create_rectangle(7, 27, 600-7, 640-7, outline="red")

    def check_head_pos(self):
        """
        Проверка позиции головы змеи:
            1)Проверка на выход за границы игрового поля
            2)Проверка на пересечение своего тела
        """
        head_x_pos, head_y_pos = self.snake_positions[0]
        # не понятно, как считается диапазон head_y_pos in (19, 640)/head_y_pos in (21, 640) дают интересный результат
        return (head_x_pos in (0, 600) or head_y_pos in (20, 640) or (head_x_pos, head_y_pos) in self.snake_positions[1:])

    def check_food_pos(self):
        """
        Добавляем змее доп. ячейку при нахождении в ячейке с едой

        Изменяем позицию еды

        Изменяем счет игры
        """
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])
            self.create_image(*self.snake_positions[-1], image=self.snake_body, tag="snake")

            self.delete("food")
            self.food_position = self.set_new_food_pos()
            food = choice(self.food_list)
            self.create_image(*self.food_position, image=food, tag="food")
            self.coords(self.find_withtag("food"), *self.food_position)

            score = self.find_withtag("score")
            self.itemconfig(score, text=f"Score: {self.score}", tag="score")

    def end_game(self):
        """
        Завершение игры:
        \nУдаление всех полей tkinter
        \nВывод текста об окончании игры
        """
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game over! You scored {self.score}!",
            fill="#fff",
            font=("Arial", 30)
        )

    def move_snake(self):
        head_x_pos, head_y_pos = self.snake_positions[0]
        self.delete("head")
        self.delete("tail")
        
        if self.direction == "Left":
            self.keys_history.append("Left")
            head_pos = self.snake_head_horizontal
            new_head_position = (head_x_pos - INCREMENT_STEP, head_y_pos)
        elif self.direction == "Right":
            self.keys_history.append("Right")
            head_pos = self.snake_head_horizontal
            new_head_position = (head_x_pos + INCREMENT_STEP, head_y_pos)
        elif self.direction == "Down":
            self.keys_history.append("Down")
            head_pos = self.snake_head_vertical
            new_head_position = (head_x_pos, head_y_pos + INCREMENT_STEP)
        elif self.direction == "Up":
            self.keys_history.append("Up")
            head_pos = self.snake_head_vertical
            new_head_position = (head_x_pos, head_y_pos - INCREMENT_STEP)
        
        self.snake_positions = [new_head_position] + self.snake_positions[:-1]
        #print(self.keys_history)
        tail_ACTION = self.keys_history[len(self.keys_history)-len(self.snake_positions)+1]
        if tail_ACTION == "Left":
            tail_pos = self.tail_90
        elif tail_ACTION == "Right":
            tail_pos = self.tail_270
        elif tail_ACTION == "Down":
            tail_pos = self.tail_180
        elif tail_ACTION == "Up":
            tail_pos = self.tail_0

        
        
        self.create_image(self.snake_positions[-1][0], self.snake_positions[-1][1], image=tail_pos, tag="tail")

        self.create_image(new_head_position[0], new_head_position[1], image=head_pos, tag="head")
        # print(self.keys_history)
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)
            
        

    def action(self, event):
        """
        Считываем нажатие символа с клавиатуры
        Задаем направление движения змеи
        """
        new_direction = event.keysym
        all_directions = ("Up", "Down", "Left", "Right")
        #Проверка на противоположное направление
        opposites = ({"Up", "Down"}, {"Left", "Right"})
        if new_direction in all_directions and {new_direction, self.direction} not in opposites:
            self.direction = new_direction

    def main_process(self):
        if self.check_head_pos():
            self.end_game()
        else:
            self.check_food_pos()
            self.move_snake()
            self.after(GAME_SPEED, self.main_process)

    def set_new_food_pos(self):
        """
        Установка новых позиций для еды;
        Содержится проверка на вхождение в змею
        """
        while True:
            # временно
            x_position = randint(1, 29) * INCREMENT_STEP
            y_position = randint(3, 31) * INCREMENT_STEP
            food_position = (x_position, y_position)

            if food_position not in self.snake_positions:
                return food_position


root = tk.Tk()
root.title("Snake")
root.resizable(False, False)
Game = Snake()

root.mainloop()
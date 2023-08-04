class Chandrayaan:

    def __init__(self, x, y, z, direction) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction
    
    def move_forward(self) -> None:
        if self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "Up":
            self.z += 1
        elif self.direction == "Down":
            self.z -= 1

    def move_backward(self) -> None:
        if self.direction == "E":
            self.x -= 1
        elif self.direction == "W":
            self.x += 1
        elif self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "Up":
            self.z -= 1
        elif self.direction == "Down":
            self.z += 1
    
    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "Up":
            self.direction = "W"
        elif self.direction == "Down":
            self.direction = "E"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"
        elif self.direction == "Up":
            self.direction = "E"
        elif self.direction == "Down":
            self.direction = "W"
    
    def turn_up(self):
        if self.direction in ["N", "W", "E", "S"]:
            self.direction = "Up"
        elif self.direction == "Up":
            self.direction = "W"
        elif self.direction == "Down":
            self.direction = "N"
    
    def turn_down(self):
        if self.direction in ["N", "W", "E", "S"]:
            self.direction = "Down"
        elif self.direction == "Up":
            self.direction = "N"
        elif self.direction == "Down":
            self.direction = "W"
    
    def execute_command(self, command):
        if command == "f":
            self.move_forward()
        elif command == "b":
            self.move_backward()
        elif command == "u":
            self.turn_up()
        elif command == "d":
            self.turn_down()
        elif command == "l":
            self.turn_left()
        elif command == "r":
            self.turn_right()

obj = Chandrayaan(0, 0, 0, "N")

commands = ["f", "u", "u", "d", "u", "f"]

for command in commands:
    obj.execute_command(command)

print("(x, y, z) = ",obj.x, obj.y, obj.z)
print(obj.direction)
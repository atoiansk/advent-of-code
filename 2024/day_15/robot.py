class Robot:
    moves_map = {
        '<': (-1, 0),
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1)
    }

    def __init__(self, position, walls, boxes):
        self.position = position
        self.walls = walls
        self.boxes = boxes

    def move(self, move):
        dx, dy = self.moves_map[move]

        new_position = (self.position[0] + dx, self.position[1] + dy)

        if new_position in self.walls:
            return

        if new_position in self.boxes:
            box_position = self.move_box(new_position, (dx, dy))
            new_position = (box_position[0] - dx, box_position[1] - dy)

        self.position = new_position

    def move_box(self, box_position, move):
        dx, dy = move

        new_box_position = (box_position[0] + dx, box_position[1] + dy)

        if new_box_position in self.walls:
            return box_position

        if new_box_position in self.boxes:
            next_box_position = self.move_box(new_box_position, move)
            new_box_position = (next_box_position[0] - dx, next_box_position[1] - dy)

        self.boxes.remove(box_position)
        self.boxes.add(new_box_position)

        return new_box_position

    def print_map(self):
        x = max(self.walls, key=lambda x: x[0])[0]
        y = max(self.walls, key=lambda x: x[1])[1]

        for i in range(y + 1):
            for j in range(x + 1):
                if (j, i) in self.walls:
                    print("#", end="")
                elif (j, i) in self.boxes:
                    print("O", end="")
                elif (j, i) == self.position:
                    print("@", end="")
                else:
                    print(".", end="")
            print()

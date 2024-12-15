from robot import Robot

class Robot2(Robot):
    def __init__(self, position, walls, boxes):
        # Initialize parent class
        super().__init__(position, walls, set())  # Pass empty set for boxes since we handle them differently
        # Store box pairs in self.boxes
        self.boxes = boxes

    def move(self, move):
        dx, dy = self.moves_map[move]
        new_position = (self.position[0] + dx, self.position[1] + dy)

        if new_position in self.walls:
            return

        if any(new_position in box for box in self.boxes):
            box_position = self.move_box(new_position, (dx, dy))
            new_position = (box_position[0] - dx, box_position[1] - dy)

        self.position = new_position

    def move_box(self, box_position, move):
        dx, dy = move

        box_start, box_end = next((pair for pair in self.boxes if box_position in pair), None)

        new_box_start = (box_start[0] + dx, box_start[1] + dy)
        new_box_end = (box_end[0] + dx, box_end[1] + dy)

        if new_box_start in self.walls or new_box_end in self.walls:
            return box_position

        boxes_copy = self.boxes.copy()
        boxes_copy.remove((box_start, box_end))

        if any(new_box_start == by for _, by in boxes_copy) and any(new_box_end == bx for bx, _ in boxes_copy):
            valid_box_1_move = self.validate_box_move(new_box_start, move)
            valid_box_2_move = self.validate_box_move(new_box_end, move)

            if valid_box_1_move and valid_box_2_move:
                new_box_1_position = self.move_box(new_box_start, move)
                self.move_box(new_box_end, move)
                new_box_start = (new_box_1_position[0] - dx, new_box_1_position[1] - dy)
                new_box_end = (new_box_start[0] + 1, new_box_start[1])
            else:
                return box_position
        elif any(new_box_start in box for box in boxes_copy):
            next_box_position = self.move_box(new_box_start, move)
            new_box_start = (next_box_position[0] - dx, next_box_position[1] - dy)
            new_box_end = (new_box_start[0] + 1, new_box_start[1])
        elif any(new_box_end in box for box in boxes_copy):
            next_box_position = self.move_box(new_box_end, move)
            new_box_end = (next_box_position[0] - dx, next_box_position[1] - dy)
            new_box_start = (new_box_end[0] - 1, new_box_end[1])

        self.boxes.remove((box_start, box_end))
        self.boxes.add((new_box_start, new_box_end))

        if box_start == box_position:
            return new_box_start
        else:
            return new_box_end

    def validate_box_move(self, box_position, move):
        dx, dy = move

        box_start, box_end = next((pair for pair in self.boxes if box_position in pair), None)

        new_box_start = (box_start[0] + dx, box_start[1] + dy)
        new_box_end = (box_end[0] + dx, box_end[1] + dy)

        if new_box_start in self.walls or new_box_end in self.walls:
            return False

        boxes_copy = self.boxes.copy()
        boxes_copy.remove((box_start, box_end))

        if any(new_box_start in box for box in boxes_copy) and any(new_box_end in box for box in boxes_copy):
            return self.validate_box_move(new_box_start, move) and self.validate_box_move(new_box_end, move)
        elif any(new_box_start in box for box in boxes_copy):
            return self.validate_box_move(new_box_start, move)
        elif any(new_box_end in box for box in boxes_copy):
            return self.validate_box_move(new_box_end, move)

        return True

    def print_map(self):
        x = max(self.walls, key=lambda x: x[0])[0]
        y = max(self.walls, key=lambda x: x[1])[1]

        for i in range(y + 1):
            for j in range(x + 1):
                if (j, i) in self.walls:
                    print("#", end="")
                elif any(box_start == (j, i) for box_start, _ in self.boxes):
                    print("[", end="")
                elif any(box_end == (j, i) for _, box_end in self.boxes):
                    print("]", end="")
                elif (j, i) == self.position:
                    print("@", end="")
                else:
                    print(".", end="")
            print()

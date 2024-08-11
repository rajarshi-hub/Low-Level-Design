class Board:
    snake_and_ladder = {}
    size = 0

    def __init__(self, snake_and_ladder, size):
        self.size = size
        # TODO: Checks on ladder and snakes
        for position in snake_and_ladder:
            self.snake_and_ladder[position[0]] = position[1]

    def get_final_position(self, cur_pos, die_roll):
        new_pos = cur_pos+die_roll
        if new_pos > self.size :
            return cur_pos
        return self.snake_and_ladder.get(new_pos, new_pos)



class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # store current position, and traverse the entire commands array to find all the potential positions that we can reach
        # at each command, before we move, we should check whether the position is being blocked by an obstacle
        
        direction = 0
        obstacle_map = {tuple(o) for o in obstacles}
    
        # direction takes 3 values: 0 (not moving), 1 (positive), -1(negative)
        horizontal_direction = 0
        vertical_direction = 1 
        max_distance_so_far = 0

        def move(curr_position, command):
            nonlocal  horizontal_direction, vertical_direction, max_distance_so_far
            if command == -1:
                if vertical_direction == 1:
                    vertical_direction = 0
                    horizontal_direction = 1
                elif vertical_direction == -1:
                    vertical_direction = 0
                    horizontal_direction = -1
                elif horizontal_direction == 1:
                    horizontal_direction = 0
                    vertical_direction = -1
                elif horizontal_direction == -1:
                    horizontal_direction = 0
                    vertical_direction = 1
                return curr_position
            elif command == -2:
                if vertical_direction == 1:
                    vertical_direction = 0
                    horizontal_direction = -1
                elif vertical_direction == -1:
                    vertical_direction = 0
                    horizontal_direction = 1
                elif horizontal_direction == 1:
                    horizontal_direction = 0
                    vertical_direction = 1
                elif horizontal_direction == -1:
                    horizontal_direction = 0
                    vertical_direction = -1
                return curr_position
            else:
                x,y = curr_position
                for _ in range(command):
                    x,y = x + horizontal_direction, y + vertical_direction
                    if (x,y) in obstacle_map:
                        x,y =  x - horizontal_direction, y - vertical_direction
                        break
                max_distance_so_far = max(max_distance_so_far, x ** 2 + y ** 2)
                return (x,y)

        curr_position = (0,0)
        for command in commands:
            curr_position = move(curr_position,command)
        
        return max_distance_so_far
            
        
                        
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x, self.y = 0, 0
        self.cur_dir = 0
        self.directions = [("East",1,0),("North",0,1),("West",-1,0),("South",0,-1)]
        self.cycle = 2 * (width + height) - 4
        

    def step(self, num: int) -> None:
        if self.cycle > 0:
            num %= self.cycle
            if num == 0:
                num = self.cycle

        i = 0
        while i < num:
            _, dx, dy = self.directions[self.cur_dir]

            if (0 <= self.x + dx < self.width) and (0 <= self.y + dy < self.height):
                self.x += dx
                self.y += dy
                i += 1
            else:
                self.cur_dir = (self.cur_dir + 1) % 4
                
    def getPos(self) -> List[int]:
        return [self.x,self.y]
        

    def getDir(self) -> str:
        return self.directions[self.cur_dir][0]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
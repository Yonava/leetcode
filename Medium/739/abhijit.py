class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        current_stack = [] 
        output = []
        Data = namedtuple('Data',['value','index'])
        for i in range(len(temperatures)):
            while len(current_stack)  > 0 and current_stack[-1].value < temperatures[i]:
                val = current_stack.pop()
                output[val.index] = i - output[val.index]
            
            d = Data(temperatures[i],i)
            output.append(i) # place current index in output
            current_stack.append(d)

        while len(current_stack):
            val = current_stack.pop()
            output[val.index] = 0


        return output
   
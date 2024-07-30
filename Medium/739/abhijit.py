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
   
def dailyTemperatures(self, T):
    #initialize the result array with all '0's considering when there is no bigger temperature
    ans = [0]*len(T) 
    stack = []
    
    for i,v in enumerate(T):
        #check whether current val is greater than the last appended stack value.  We will pop all the elements which is lesser than the current temp
        while stack and stack[-1][1] < v:
            index,value = stack.pop()
            ans[index] = i - index # we are checking how many indices we have crossed since we last have a lesser temperature
        #Remember since we are comparing all the stack elements before inserting,all the stack elements will have temperatures greater than the current value	
        stack.append([i,v])      
    
    return ans
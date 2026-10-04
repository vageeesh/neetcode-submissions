class MinStack:

    def __init__(self):
        # only time a min can change is during add/pop
        # idea is to keep seperate list of min only and update it when each new number added/poped: at each time interval it will also update
        self.min_list = []
        self.li = []
        
    def push(self, val: int) -> None:
        self.li.append(val)

        # update min value for each new item added
        # check the top and find the minimum
        # check top in min_list not the other one as this list always have min on top
        self.min_list.append(min(self.min_list[-1] if self.min_list else val, val))

    def pop(self) -> None:
        self.li.pop()
        
        # also delete form min list
        self.min_list.pop()

    def top(self) -> int:
        return self.li[-1]

    def getMin(self) -> int:
        # find-out current min value at current time
        # get top val and check corresponding min
        return self.min_list[-1]
        

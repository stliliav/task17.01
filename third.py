class Counter():
    def __init__(self, value):
        self.value = value
    def incr(self):
        self.value += 1
        return (self.value)
    def decr(self):
        self.value -= 1
        return self.value
    def reset(self):
        self.value = 0
        return self.value
q = Counter(0)
i = int(input("What do u want to do with your value?\nPress 1 to increase\nPress 2 to dicrease \nPress 3 to reset\n"))
while i!=0:
    if i == 1:
        print(f"New count:{q.incr()}")
    elif i ==2:
        print(f"New count:{q.decr()}")
    else:
        print(f"New count:{q.reset()}")
    i = int(input())

    

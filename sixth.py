class Store():
    def __init__(self, name, items):
        self.name = name
        self.items = items
    def add(self, item):
        self.items.append(item)
        return "Successfully added!"
    def remove(self, remov):
        self.items.remove(remov)
        return "Successfuly removed"
    def show(self):
        return f'Items: {self.items}'
q = Store("Gold apple", [])
i = int(input("What do u want to do?\nPress 1 to add item\nPress 2 to remove item\nPress 3 to see the current items list\n"))
while i!=0: 
    if i == 1: 
        s = (input("Choose the item:\n"))
        print(q.add(s))
    elif i ==2:  
        s = (input("Choose the item:\n"))
        print(q.remove(s))
    else:
        print(f"{q.show()}")
    i = int(input())



class Stack():
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    

class StackTwo():
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        # 列表头部为栈的顶端
        self.items.insert(0, item)

    def pop(self):
        # 列表头部为栈的顶端 return self.items[0] def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
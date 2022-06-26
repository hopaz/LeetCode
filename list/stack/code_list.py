from nis import match
from stack import Stack

def parChecker(symbolString):
    # "()"括号匹配，输入字符串，返回字符串中括号是否匹配
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False

def parCheckerMulti(symbolString):
    # "()[]{}"多种括号匹配，输入字符串，返回字符串中的各种括号是否匹配
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(opener, closer):
    openers = "([{"
    closers = ")]}"
    
    return openers.index(opener) == closers.index(closer)


def devideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        remstack.push(decNumber % 2)
        decNumber = decNumber // 2
    
    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString








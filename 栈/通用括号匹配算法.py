from Stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index =0
    while index <len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced =False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,colse):
    opens = "([{"
    colses = ")]}"
    return opens.index(open) == colses.index(colse)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
print(parChecker('{}'))
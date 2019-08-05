from test3 import Deque

def palchecker(str):
    char = Deque()
    for ch in str:
        char.addRear(ch)
    equal = True
    while char.size()>1 and equal:
        first = char.removeFront()
        last = char.removeRear()
        if first != last:
            equal = False
    return equal
print(palchecker("ashfkjaskfha"))
print(palchecker("toxot"))

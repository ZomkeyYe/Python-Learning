# 水壶问题
import copy
def x1tox2(lis):
    if lis[0] == 0:
        return False
    temp = 5 - lis[1]
    if lis[1] == 5:
        return False
    elif lis[0] >= temp:
        lis[0] = lis[0] - temp
        lis[1] = lis[1] + temp
    elif lis[0] < temp:
        lis[0],lis[1] = 0,(lis[1] + lis[0])
    xx = copy.deepcopy(lis)
    if xx in his:
        return False
    else:
        way.append(xx)
        his.append(xx)
        return True
def x1tox3(lis):
    if lis[0] == 0:
        return False
    temp = 3 - lis[2]
    if lis[2] == 3:
        return False
    elif lis[0] >= temp:
        lis[0] = lis[0] - temp
        lis[2] = lis[2] + temp
    elif lis[0] < temp:
        lis[0],lis[2] = 0,(lis[2] + lis[0])
    xx = copy.deepcopy(lis)
    if xx in his:
        return False
    else:
        way.append(xx)
        his.append(xx)
        return True
def x2tox3(lis):
    if lis[1] == 0:
        return False
    temp = 3 - lis[2]
    if lis[2] == 3:
        return False
    elif lis[1] >= temp:
        lis[1] = lis[1] - temp
        lis[2] = lis[2] + temp
    elif lis[1] < temp:
        lis[1],lis[2] = 0,(lis[2] + lis[1])
    xx = copy.deepcopy(lis)
    if xx in his:
        return False
    else:
        way.append(xx)
        his.append(xx)
        return True
def x3tox2(lis):
    if lis[2] == 0:
        return False
    temp = 5 - lis[1]
    if lis[1] == 5:
        return False
    elif lis[2] >= temp:
        lis[2] = lis[2] - temp
        lis[1] = lis[1] + temp
    elif lis[2] < temp:
        lis[2],lis[1] = 0,(lis[1] + lis[2])
    xx = copy.deepcopy(lis)
    if xx in his:
        return False
    else:
        way.append(xx)
        his.append(xx)
        return True
def x3tox1(lis):
    if lis[2] == 0:
        return False
    else:
        lis[2],lis[0] = 0,(lis[0] + lis[2])
    xx = copy.deepcopy(lis)
    if xx in his:
        return False
    else:
        way.append(xx)
        his.append(xx)
        return True
def x2tox1(lis):
    if lis[1] == 0:
        return False
    else:
        lis[1],lis[0] = 0,(lis[0] + lis[1])
    xx = copy.deepcopy(lis)
    if xx in his:
        return False
    else:
        way.append(xx)
        his.append(xx)
        return True
def judge(way):
    flag = False
    for x in way:
        if 4 in x:
            flag = True
    return flag
if __name__ == '__main__':
    while True:
        try:
            lis = [8,0,0]
            way = [[8,0,0]]
            his = [[8,0,0]]
            # print(his)
            # x1tox3(lis)
            # print(way)
            # x1tox2(lis)
            # x2tox3(lis)
            # print(way)
            # x3tox2(lis)
            # print(way)
            # x1tox3(lis)
            # print(way)
            # print(his)
            while (not judge(way)):
                # print(lis)
                print(way,"---",his)
                if x1tox2(lis):
                    print("1")
                    lis = copy.deepcopy(way[-1])
                    continue
                if x2tox3(lis):
                    print("3")
                    lis = copy.deepcopy(way[-1])
                    continue
                if x1tox3(lis):
                    print("2")
                    lis = copy.deepcopy(way[-1])
                    continue
                if x3tox1(lis):
                    print("6")
                    lis = copy.deepcopy(way[-1])
                    continue  
                if x2tox3(lis):
                    print("3")
                    lis = copy.deepcopy(way[-1])
                    continue  
                if x2tox1(lis):
                    print("4")
                    lis = copy.deepcopy(way[-1])
                    continue
                if x3tox2(lis):
                    print("5")
                    lis = copy.deepcopy(way[-1])
                    continue
                                    
                if way != []:
                    way.pop()
                if way:
                    lis = copy.deepcopy(way[-1])
            print(way)
            break
        except:
            break

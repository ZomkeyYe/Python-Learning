# 复杂迷宫问题
def up(i,j,N,M):
    #横坐标为0，无法再向上走
    if i <= 0:
        return False
    else:
        new_location = [i-1,j]
        #已经尝试过的点不会尝试第二次
        if new_location in route_history:
            return False
        #碰到墙不走
        elif source[new_location[0]][new_location[1]] == 0:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
def down(i,j,N,M):
    if i >= N-1:
        return False
    else:
        new_location = [i+1,j]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 0:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
def left(i,j,N,M):
    if j <= 0:
        return False
    else:
        new_location = [i,j-1]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 0:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True 
def right(i,j,N,M):
    if j >= M-1:
        return False
    else:
        new_location = [i,j+1]
        if new_location in route_history:
            return False
        elif source[new_location[0]][new_location[1]] == 0:
            return False
        else:
            route_stack.append(new_location)
            route_history.append(new_location)
            return True
if __name__ == '__main__':
    while True:
        try:
            flag = True
            source = []
            N = int(input())
            M = int(input())
            for i in range(N):
                source.append(list(map(int,input().split())))
            route_stack = [[0,0]]
            route_history = [[0,0]]
            i,j = 0,0
            if source[0][0] == 0:
                flag = False
                break
            while source[i][j] != 9:
                if up(i,j,N,M):
                    i,j = route_stack[-1][0],route_stack[-1][1]
                    continue
                if down(i,j,N,M):
                    i,j = route_stack[-1][0],route_stack[-1][1]
                    continue
                if left(i,j,N,M):
                    i,j = route_stack[-1][0],route_stack[-1][1]
                    continue
                if right(i,j,N,M):
                    i,j = route_stack[-1][0],route_stack[-1][1]
                    continue
                route_stack.pop()
                if route_stack:            
                    i,j = route_stack[-1][0],route_stack[-1][1]
                elif not route_stack:
                    flag = False
                    break
            if route_stack:
                flag = True
            elif not route_stack:
                flag = False
            if flag == True:
                print("1")
            elif flag == False:
                print("0")
        except:
            break
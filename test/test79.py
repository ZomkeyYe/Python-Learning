# 剪刀石头布游戏
def jcb(N):
    win, lose, tie = 0, 0, 0
    Jia, Yi = [0, 0, 0], [0, 0, 0] 
    for i in range(N):
        str = input()
        if str == "C J":
            win += 1
            Jia[1] += 1
        elif str == "J C":
            lose += 1
            Yi[1] += 1
        elif str == "C B":
            lose += 1
            Yi[0] += 1
        elif str == "B C":
            win += 1
            Jia[0] += 2
        elif str == "B J":
            lose += 1
            Yi[2] += 1
        elif str == "J B":
            win += 1
            Jia[2] += 1
        else:  # there is a tie
            tie += 1
    print(win, tie, lose)
    print(lose, tie, win)
    print("BCJ"[Jia.index(max(Jia))], "BCJ"[Yi.index(max(Yi))])
if __name__ == '__main__':
    N = int(input())
    jcb(N)

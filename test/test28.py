def InputFunc():
    a = int(input())
    data = []
    for i in range(a):
        data.append(list(map(int, input().split())))
    return a, data
def main():
    n, data = InputFunc()
    result = []
    data = sorted(data)
    result.append(data[0])
    for i in range(1, len(data)):
        if (data[i][0] > result[-1][1]):  #不重叠
            result.append(data[i])
        else:
            result[-1][1] = max(result[-1][1], data[i][1])
    for value in result:
        print(value[0], value[1])
 
 
if __name__ == "__main__":
    main()
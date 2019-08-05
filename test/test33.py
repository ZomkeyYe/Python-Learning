def cnm(N):
    n = 1024 - N
    count_1 = n//64
    n_1 = n%64
    count_2 = n_1//16
    n_2 = n_1%16
    count_3 = n_2//4
    n_3 = n_2%4
    count_4 = n_3
    return count_1+count_2+count_3+count_4
if __name__ == "__main__":
    print(cnm(int(input())))


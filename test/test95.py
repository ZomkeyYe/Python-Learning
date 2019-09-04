# 动态规划问题
def LD(str1, str2):                         #LD:Levenshtein distance
    lenstr1 = len(str1) + 1
    lenstr2 = len(str2) + 1
    # create 2D-matrix
    matrix = [([0] * lenstr1) for j in range(lenstr2)]
    # init matrix[0][:]
    for i in range(lenstr1): matrix[0][i]=i
    # init matrxi[:][j]
    for j in range(lenstr2): matrix[j][0]=j
    # assign values to the matrix
    for i in range(lenstr1 - 1):
        for j in range(lenstr2 - 1):
            if str1[i] == str2[j]: const = 0
            else: const = 1
            matrix[j + 1][i + 1] = min(matrix[j][i] + const, matrix[j + 1][i] + 1,matrix[j][i + 1] + 1)
    return matrix[-1][-1]           
if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(LD(str1, str2))
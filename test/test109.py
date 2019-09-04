if __name__ == '__main__':
    while True:
        try:
            count_1 = 0
            count_2 = 0
            count_3 = 0
            count_4 = 0
            s = input()
            for i in s:
                if i == "[":
                    count_1 += 1
                if i == "]":
                    count_1 -= 1
                if i =="{":
                    count_2 += 1
                if i == "}":
                    count_2 -= 1
                if i =="\"":
                    count_3 += 1
                

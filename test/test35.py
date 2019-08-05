def handle(num):
    result = 0;  
    i = num;
    while (i !=0 ) :  
        i = i/10*10;  
        result = result * 10 + num - i;  
        i = i /10;  
        num = num/10;  
    return result   
if __name__ == "__main__":
    print(handle(12354))
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
#initialize three variables that form the lists to be printed and place a condition as asked in the question
print(list([a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n))

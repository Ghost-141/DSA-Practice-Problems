def tow_set(n:int):
    a = set()
    b = set()
    sum = int(n*(n+1)/2)
    temp = int(sum/2)
    if(sum%2==0):
        for i in range(n, 0, -1):
            if(temp>=i):
                temp = temp - i
                a.add(i)
            else:
                b.add(i) 
        print("YES")
                
        print(len(a), end="\n")
        a_sorted=list(a)
        a_sorted.sort()
        print(*a_sorted)
        print(len(b), end="\n")
        b_sorted=list(b)
        b_sorted.sort()
        print(*b_sorted)        
    else:
        print("NO")
n = int(input())   
tow_set(n)     
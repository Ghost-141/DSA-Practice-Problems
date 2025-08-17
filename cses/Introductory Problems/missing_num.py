def missing_number(n, ar:[]):
    ip_total = sum(ar)
    sum_n = (n*(n+1))//2
    num = sum_n - ip_total
    return num

n = int(input())
arr = list(map(int, input().split()))
res=missing_number(n, arr)    
print(res)
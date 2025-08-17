ar = str(input())
def repetitions(ar:str):
    count = 1
    max_count = 1
    i = int(1)
    while i<len(ar):
        if(ar[i]==ar[i-1]):
            count+=1
            i+=1
        else:
            if(max_count<count):
                max_count=count
            count=1
            i+=1
    if(count>max_count):
        max_count=count
    return print(max_count)
repetitions(ar)  
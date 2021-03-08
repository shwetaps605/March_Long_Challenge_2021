from sys import stdin, stdout 

    
n,h,x =list(map(int, stdin.readline().strip().split()))
#print(n,h,x)

t = list(map(int, stdin.readline().strip().split()))
#print(t)

m = max(t)

if m + x < h:
    print("NO")
elif m + x == h:
    print("YES")
else:
    diff = h - x
    if diff in t:
        print("YES")
    else:
        print("NO")





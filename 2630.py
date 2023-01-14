#Greyscale
T = int(input())
for i in range(T):
    oper = input()
    R,G,B = map(int,input().split())
    if oper == "min":
      print(f"Caso #1: {min(R,G,B)}")
    elif oper == "mean":
      print(f"Caso #2: {int((R+G+B)/3)}")
    else:
      print(f"Caso #3: {int(.30*R+.59*G+.11*B)}")
      
      #note: I am having 10% Wrong ans:
    
    #you can use the code below:
    t = int(input())
I = 1
while t:
    str = input()
    a = list(map(float, input().split()))
    if str[0] == 'e':
        a[0] = (a[0]*30)/100
        a[1] = (a[1]*59)/100
        a[2] = (a[2]*11)/100
        a[0] = a[0] + a[1] + a[2]
        f = int(a[0])
        print("Caso #{}: {}".format(I, f))
    elif len(str) == 4:
        m = int((a[0] + a[1] + a[2]) / 3)
        print("Caso #{}: {}".format(I, m))
    else:
        a.sort()
        if str[1] == 'i':
            f = int(a[0])
            print("Caso #{}: {}".format(I, f))
        else:
            f = int(a[2])
            print("Caso #{}: {}".format(I, f))
    t -= 1
    I += 1

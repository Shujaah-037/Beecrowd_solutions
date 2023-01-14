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

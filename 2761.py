#Input and Output of Various Types
a = int(input())
b = float(input())
c = input()
d = input()

print(str(a) + str(b) + c + d)
print(str(a) + '\t' + str(b) + '\t' + c + '\t' + d)
print(str(a).rjust(10) + str(b).rjust(10) + c.rjust(10) + d.rjust(10))

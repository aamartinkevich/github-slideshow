a = input()
s = a.find("h")
k = a.rfind("h")

print(a[:s] + a[k+1:])
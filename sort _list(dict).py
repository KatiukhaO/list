
n = int(input('Input n :'))
d = {}
for i in range(n):
    key, d[key] = map(str, input().split())
    d[key] = int(d[key])
    
print(sorted(d,key=d.get, reverse=True))



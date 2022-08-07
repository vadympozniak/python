import sys


for i in range(len(sys.path)):
    print(sys.path[i])

a = sys.path[0]
sys.path.remove(sys.path[0])
sys.path.append(a)
print()

for i in range(len(sys.path)):
    print(sys.path[i])
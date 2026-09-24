n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
belt = l + r + d
length = 3*n
t %= length

belt = belt[-t:] + belt[:-t]

l = belt[:n]
r = belt[n:2*n]
b = belt[2*n:]

print(*l)
print(*r)
print(*b)
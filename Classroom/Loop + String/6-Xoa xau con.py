print("Nhap xau s:", end=" ")
s = input()
print("Nhap ky tu c:", end=" ")
c = input()

l = s.find(c)
r = s.rfind(c)
if l != -1 and l != r:
    s = s[:l] + s[r + 1 :]
print(s)

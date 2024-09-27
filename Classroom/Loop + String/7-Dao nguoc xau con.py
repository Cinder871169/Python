print("Nhap xau s:", end=" ")
s = input()
print("Nhap ky tu c:", end=" ")
c = input()

l = s.find(c)
r = s.rfind(c)
if l != -1 and l != r:
    rev = s[l : r + 1][::-1]
s = s[:l] + rev + s[r + 1 :]
print(s)

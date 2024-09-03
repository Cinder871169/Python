h, m, s = map(int, input().split())
goc = (h * 30) + (m * 0.5) + (s * (1 / 120))
print("Angle: ", goc)

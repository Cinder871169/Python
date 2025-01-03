from datetime import datetime

from unicodedata import category


class Genre:
    def __init__(self, id, name):
        self.id = "TL{:03d}".format(id)
        self.name = name


class Movie:
    def __init__(self, id, genre, time, name, eps):
        self.id = "P{:03d}".format(id)
        self.genre = genre
        self.time = datetime.strptime(time, "%d/%m/%Y")
        self.name = name
        self.eps = eps

    def __str__(self):
        return f"{self.id} {self.genre.name} {self.time.strftime('%d/%m/%Y')} {self.name} {self.eps}"


n, m = map(int, input().split())
genres = []
movies = []
for i in range(n):
    genres.append(Genre(i + 1, input()))
for i in range(m):
    x = input()
    for j in genres:
        if x == j.id:
            movies.append(Movie(i + 1, j, input(), input(), int(input())))
movies.sort(key=lambda e: (e.time, e.name, -e.eps))
print(*movies, sep="\n")

# 2 3
# Hai huoc
# Tinh cam
# TL001
# 25/11/2021
# Phim so 1
# 10
# TL001
# 04/12/2021
# Phim so 2
# 15
# TL002
# 25/11/2021
# Phim so 3
# 5

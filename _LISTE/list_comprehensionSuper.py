movies = [
    ("Star Wars", 2000),
    ("Gandhi", 1995),
    ("Casablanca", 1990),
    ("Groundhog Day", 2015),
    ("Gattaca", 2018),
    ("Rear Window", 2000),
    ("To Kill A Mockingbird", 1999),
    ("Good Will Hunting", 2001),
    ("Raiders of the Lost Ark", 2002),
]


before_2000 = [title for (title, year) in movies if year <= 2000]


print(before_2000)
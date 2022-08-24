# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = ", ".join(genres)
        self.rating = 0
        self.num_rate = 0
    
    def __str__(self):
        if self.num_rate != 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres}\n{self.num_rate} ratings, average {(self.rating / self.num_rate):.1f} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {self.genres}\nno ratings"

    def rate(self, rating: int):
        self.rating += rating
        self.num_rate += 1

def minimum_grade(rating: float, series_list: list):
    answ = []
    for series in series_list:
        if series.rating >= rating:
            answ.append(series)
    return answ

def includes_genre(genre: str, series_list: list):
    answ = []
    for series in series_list:
        if genre in series.genres:
            answ.append(series)
    return answ

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)

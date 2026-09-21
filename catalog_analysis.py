import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    avg_score = 0.0
    if not movies:
        return avg_score
    for i in range(len(movies)):
        avg_score += movies[i]["rating"]
    return round(avg_score / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    ages = []
    avg_ages = 0
    if not movies:
        return ages
    for i in range(len(movies)):
        age = current_year - movies[i]["year"]
        ages.append(age)
        avg_ages += age
    return (max(ages), min(ages), math.ceil(avg_ages/len(movies)))

def duration_in_hours(minutes):
    time_hour = minutes // 60
    time_min = minutes % 60
    return f"{time_hour}ч {time_min}м"

def rating_tier(rating):
    masterpiece = "шедевр" if rating >= 9 else None
    if masterpiece:
        return masterpiece
    elif 7 <= rating <= 8.9:
        return "хорошо"
    elif 5 <= rating <= 6.9:
        return "средне"
    else:
        return "слабо"

def decade_label(year):
    match (year):
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(movies, threshold=120):
    result = 0
    for i in range(len(movies)):
        if (movies[i]["duration_min"] > threshold):
            result += 1
    return result

def normalize_title(title):
    words = title.split()
    result = [w[0].upper() + w[1:] for w in words]
    return " ".join(result)

def make_slug(title):
    result = normalize_title(title)
    return result.lower().replace(" ", "-")

def format_report_line(movie):
    norm_title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    sorted_genres = sorted(list(movie["genres"]))
    genres_str = ", ".join(sorted_genres)

    return (
        f'"{norm_title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {genres_str}'
    )

def titles_sorted_by_rating(movies):
    result = []
    sort_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    for i in range(len(sort_movies)):
        result.append(sort_movies[i]["title"])
    return result

def top_n_by_rating(movies, n=3):
    result = []
    sort_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    if n > len(movies):
        return
    for i in range(n):
        title_rating = (sort_movies[i]["title"], sort_movies[i]["rating"])
        result.append(title_rating)
    return result

def count_by_genre(movies):
    genre_cnt = {}
    for m in movies:
        for g in m["genres"]:
            genre_cnt[g] = genre_cnt.get(g, 0) + 1
    return genre_cnt

def actor_filmography(movies):
    actor_films = {}
    for m in movies:
        for a in m["actors"]:
            if a not in actor_films:
                actor_films[a] = []
            actor_films[a].append(m["title"])
    return actor_films

def all_genres(movies):
    set_genres = set()
    for m in movies:
        set_genres = set_genres | m["genres"]
    return  set_genres

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    a_genres = set(movies_a["genres"])
    b_genres = set(movies_b["genres"])
    return a_genres - b_genres

if __name__ == "__main__":
    #Вывод на экран названий всех фильмов, которые не относятся к жанру comedy
    for i in range(len(movies)):
        if "comedy" in movies[i]["genres"]:
            continue
        else:
            print(movies[i]["title"])

    #Вывод на экран первый по порядку в списке фильм с рейтингом выше 9.0 или нет такого
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Найден шедевр: {movies[i]['title']}")
            break
        i += 1
    else:
        print("Шедевров не найдено")

    #Вывод словаря (созданный с помощью генератора) фильмов с рейтингов выше среднего
    avg = average_rating(movies)
    print({m["title"]: m["rating"] for m in movies if m["rating"] > avg})

    # print(count_long_movies(movies))
    # print(normalize_title("silent hours red green blue"))
    # print(make_slug("silent hours red green blue"))
    # print(format_report_line(movies[0]))
    # print(titles_sorted_by_rating(movies))
    # print(top_n_by_rating(movies))
    # print(count_by_genre(movies))
    # print(actor_filmography(movies))
    print(all_genres(movies))
    print(common_actors(movies[0], movies[4]))
    print(genres_only_in_one(movies[0], movies[1]))

if __name__=="__main__":
    no_movies = int(input())
    movies_time = []
    for _ in range(no_movies):
        movies_time.append(list(map(int, input().split())))
    movie_watched = 0
    time_passed = 0
    movies_time.sort(key=lambda x: x[1])
    for start, end in movies_time:
        if start >= time_passed:
            movie_watched += 1
            time_passed = end
    print(movie_watched)
    exit(0)
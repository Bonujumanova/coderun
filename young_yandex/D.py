import sys


def main():
    n, k = map(int, input().split())
    themes = list(map(int, input().split()))

    count_exercises_by_themes: dict[int, int] = {}
    for item in themes:
        count_exercises_by_themes[item] = count_exercises_by_themes.get(item, -1) + 1

    exercises: list = sorted(list(count_exercises_by_themes.keys()))
    # exercises: list[int] = list(set(themes))[:k]


    for exercise, total_exercis_by_one_theme in count_exercises_by_themes.items():
        if len(exercises) != k:
            if total_exercis_by_one_theme > 0:
                exercises.append(exercise)
                count_exercises_by_themes[exercise] -= 1
        print(*exercises[:k])
        break


if __name__ == '__main__':
    main()

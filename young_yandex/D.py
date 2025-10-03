import sys


def main():
    n, k = input().split()
    themes = map(str, input().split())

    count_exercises_by_themes = {}
    for item in themes:
        if item in count_exercises_by_themes:
            count_exercises_by_themes[item] += 1
        else:
            count_exercises_by_themes[item] = 0
    exercises: list = sorted(list(count_exercises_by_themes.keys()))

    for exercise, total_exercis_by_one_theme in count_exercises_by_themes.items():
        if len(exercises) != k:
            if total_exercis_by_one_theme > 0:
                exercises.append(exercise)
                count_exercises_by_themes[exercise] -= 1
        print(' '.join(exercises))
        break


if __name__ == '__main__':
    main()



# exercises = list(set(themes))
# if len(exercises) < k:
#     while len(exercises) != k:
#         for char in
#
#         exercises.append()
#
#


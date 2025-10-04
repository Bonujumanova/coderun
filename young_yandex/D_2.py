def find_k_items(k: int, themes: list[int]) -> str:
    used: set[int] = set()
    result: list[int] = []
    for theme in themes:  # Сначала добавляем все уникальные темы

        if theme not in used:
            result.append(theme)
            used.add(theme)
            if len(result) == k:
                break

    if len(result) < k:  # Если уникальных тем не хватило,
        # добираем остальные задачи
        for theme in themes:

            if len(result) == k:
                break
            if theme in used:
                result.append(theme)

    return " ".join(map(str, result))


def main() -> None:
    _, k = map(int, input().split())
    themes: list[int] = list(map(int, input().split()))

    print(find_k_items(k, themes))


if __name__ == "__main__":
    main()
# Студент: Егорченкова Кристина / Группа:  РПО 11/2

# 1. Стадион: Время О(n) / Память О(1) / худший случай: если элемента нет или он в конце, придется проверить весь список
# 2. Пункт выдачи: Время О(1) / Память О(1)
# 3. Проходная: Время О(n^2) / Память О(1)
# 4. Проходная: Время О(n) / Память О(n) / худший случай: в списке нет дубликатов
# 5. Прайс склада: Время О(n log n) / Память О(n)
# 6. Архив чеков: Время О(log n) / Память О(1)
# 7. Теплица: Время О(n) / Память О(1)
# 8. Курьеры: Время О(n^2) / Память О(1)
# 9. Служба поддержки: Время О(n) / Память О(n)
# 10. Отчет по заказам: Время О(n^2) / Память О(n)
# 11. Упаковка: Время О(log n) / Паять О(1)
# 12. Склад: Время О(n+m) / Память О(n+m)


TIME = {
    "01_find_pass": "O(n)",
    "02_first_and_last": "O(1)",
    "03_has_duplicate_badges": "O(n^2)",
    "04_has_duplicate_badges_fast": "O(n)",
    "05_three_cheapest": "O(n log n)",
    "06_find_receipt": "O(log n)",
    "07_average_and_spikes": "O(n)",
    "08_closest_pair_distance": "O(n^2)",
    "09_word_counts": "O(n)",
    "10_unique_keep_order": "O(n^2)",
    "11_halving_steps": "O(log n)",
    "12_merge_sorted": "O(n + m)",
}

SPACE = {
    "01_find_pass": "O(1)",
    "02_first_and_last": "O(1)",
    "03_has_duplicate_badges": "O(1)",
    "04_has_duplicate_badges_fast": "O(n)",
    "05_three_cheapest": "O(n)",
    "06_find_receipt": "O(1)",
    "07_average_and_spikes": "O(1)",
    "08_closest_pair_distance": "O(1)",
    "09_word_counts": "O(n)",
    "10_unique_keep_order": "O(n)",
    "11_halving_steps": "O(1)",
    "12_merge_sorted": "O(n + m)",
}

WORST_CASE = {
    "01_find_pass": "если элемента нет или он в конце, придется проверить весь список",
    "04_has_duplicate_badges_fast": "в списке нет дубликатов",
}

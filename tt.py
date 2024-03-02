"""
Модуль для расчета минимального количества транспортных платформ для перевозки 
роботов.

Данный модуль содержит функции для определения количества транспортных 
платформ,
необходимых для перевозки роботов с учетом их веса и грузоподъемности платформ.
"""


def min_transport_platforms(weights: list[int], limit: int) -> int:
    """
    Вычисляет минимальное количество транспортных платформ для перевозки
    роботов.

    Аргументы:
        weights: Список весов роботов.
        limit: Грузоподъемность одной платформы.

    Возвращает:
        Минимальное количество платформ, необходимое для перевозки всех 
        роботов.
    """
    weights.sort()
    left: int = 0  # Индекс самого легкого робота
    right: int = len(weights) - 1  # Индекс самого тяжелого робота
    platforms: int = 0  # Количество использованных платформ

    while left <= right:
        # Если легкий и тяжелый роботы помещаются на одну платформу, ставим их
        # вместе
        if left != right and weights[left] + weights[right] <= limit:
            left += 1
        # Перемещаем тяжелого робота на платформу
        right -= 1
        platforms += 1

    return platforms


def main() -> None:
    """
    Основная функция для чтения ввода и вывода результата.
    """
    # Читаем веса роботов из первой строки ввода
    weights: list[int] = list(map(int, input().split()))
    # Читаем грузоподъемность платформы из второй строки ввода
    limit: int = int(input())
    # Вычисляем необходимое количество платформ
    result: int = min_transport_platforms(weights, limit)
    # Выводим результат
    print(result)


if __name__ == '__main__':
    main()

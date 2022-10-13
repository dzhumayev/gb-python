# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек 
# в этой четверти (x и y).

try:
    quarter = int(input("Введите номер четверти: "))

    if quarter >= 1 and quarter <= 4:
        if quarter == 1:
            print("{x ∈ ℝ: x > 0}, {y ∈ ℝ: y > 0}")
        elif quarter == 2:
            print("{x ∈ ℝ: x < 0}, {y ∈ ℝ: y > 0}")
        elif quarter == 3:
            print("{x ∈ ℝ: x < 0}, {y ∈ ℝ: y < 0}")
        else:
            print("{x ∈ ℝ: x > 0}, {y ∈ ℝ: y < 0}")
    else:
        print(f"Четверть с номером {quarter} не существует")
except ValueError:
    print("Введено не числовое значение")
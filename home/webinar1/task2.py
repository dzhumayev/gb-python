# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

print(f"Дано утверждение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            print(f"\nИсходные данные - x = {x}, y = {y}, z = {z}")
            result = not(x or y or z) == (not(x) and not(y) and not(z))
            print(f"Результат утверждение: {'Истина' if result else 'Ложь'}")


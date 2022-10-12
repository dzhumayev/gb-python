inputData = input("Введите день недели: ")
if inputData.isdigit():
    dayNumber = (int)(inputData)
    if dayNumber >= 1 and dayNumber <= 7:
        if dayNumber <= 5:
            print(f"День недели с номером {dayNumber} будний")
        else:
            print(f"День недели с номером {dayNumber} выходной")
    else:
        print(f"День недели с номером {dayNumber} не существует")
else:
    print("Введено не числовое значение")
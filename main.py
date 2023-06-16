from datetime import datetime # імпортуємо бібліотеку

nowTime = datetime.now() # дізнаємось, який зараз час та кладемо це в змінну nowTime

hour = nowTime.hour # дізнаємось котра година
minute = nowTime.minute # дізнаємось котра хвилина
time = input("do you want to know time?")
if time == ("yes"):
    print(f"Поточний час {hour}:{minute}") # виводимо результат
else:
    print("good bye!")

import json
import os
from datetime import datetime

now = datetime.now()

with open("pagges.json", "r") as file:
    a = json.load(file)


def save():
    with open("pagges.json", "w") as file:
        json.dump(a, file, indent=4)


while True:
    os.system("cls" if os.name == "nt" else "clear")
    today_day = now.strftime("%d")
    today_month = now.strftime("%m")
    today_year = now.strftime("%Y")

    if today_day != a["last_day"]:
        a["day"] = 0
        a["last_day"] = today_day
        print("Статистика за день обновлена🔄")

    if today_month != a["last_month"]:
        a["month"] = 0
        a["last_month"] = today_month
        print("Статистика за месяц обновлена🔄")

    if today_year != a["last_year"]:
        a["year"] = 0
        a["last_year"] = today_year
        print("Статистика за год обновлена🔄")

    print("[1] Добавить страницы")
    print("[2] Показать статистику")
    print("[3] Выход")
    choice = input("-> ")
    if choice == "1":
        quantity = int(input("-> "))
        a["day"] += quantity
        a["month"] += quantity
        a["year"] += quantity
    elif choice == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"{a['day']} страниц прочитано за день\n{a['month']} страниц прочитано за месяц\n{a['year']} страниц прочитано за год"
        )
        exit = input("press enter to continue\n")
    elif choice == "3":
        break
    save()

DAY = 2

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

def part1():
    summa = 0
    for game in content:
        game = game.split()
        legal = True
        for i in range(2, len(game), 2):
            print(game[i], game[i+1])
            if int(game[i]) > 14:
                print("bröt")
                legal = False
                break
            if int(game[i]) > 13 and "blue" not in game[i+1]:
                print("bröt")
                legal = False
                break
            if int(game[i]) > 12 and "red" in game[i+1]:
                print("bröt")
                legal = False
                break
        if legal is True:
            summa += int(game[1][:-1])
        print("Sum:",summa)

def part2():
    summa = 0
    for game in content:
        game = game.split()
        min_red = 0
        min_green = 0
        min_blue = 0
        for i in range(2, len(game), 2):
            dices = int(game[i])
            if "red" in game[i+1] and dices > min_red:
                min_red = dices
            elif "green" in game[i+1] and dices > min_green:
                min_green = dices
            elif "blue" in game[i+1] and dices > min_blue:
                min_blue = dices
        power = min_red * min_green * min_blue
        summa += power
        print(summa)

part2()
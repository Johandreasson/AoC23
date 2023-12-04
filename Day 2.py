day = 2

input_path = f"inputs/day{day}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

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
        if int(game[i]) > 13 and game[i+1] is not "blue":
            print("bröt")
            legal = False
            break
        if int(game[i]) > 12 and game[i+1] is "red":
            print("bröt")
            legal = False
            break
    if legal is True:
        summa += int(game[1][:-1])
        print(game[1][:-1])
        print(summa)

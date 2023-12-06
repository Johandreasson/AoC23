DAY = 4

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

extra = [0 for _ in range(len(content))]
i=0
total_points = 0
total_tickets = 0
while i < len(content):
    ticket = content[i]
    total_tickets += 1
    winning_nums = ticket[9:39].split()
    guessed = ticket[41:].split()
    points = 0
    correct_guess = 0
    for guess in guessed:
        if guess in winning_nums:
            correct_guess += 1
            
            extra[i+correct_guess] += 1
            if points == 0:
                points +=1
            else:
                points *= 2
    if extra[i] > 0:
        extra[i] -= 1
    else:
        i+=1
        print(i)
        
    total_points += points
print(total_tickets)
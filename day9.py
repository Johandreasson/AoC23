DAY = 9

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

content = [[int(x) for x in item.split()] for item in content]

summa_fram = 0
summa_bak = 0

def find_zero(data, values):
  if all(x == 0 for x in data):
    return values
  increases = []
  try:
    for i, value in enumerate(data):
      increases.append(data[i+1]-value)
  except IndexError:
    pass
  values.append(increases)
  find_zero(increases, values)
  
def predict(data):
  calc_values = [data]
  find_zero(data, calc_values)
  calc_values.insert
  for i in range(len(calc_values), -1, -1):
    try:
      calc_values[i].insert(0,calc_values[i][0] - calc_values[i+1][0])
      calc_values[i].append(calc_values[i][-1] + calc_values[i+1][-1])
    except IndexError:
      continue
  return (calc_values[0][-1], calc_values[0][0])

print("Predicting...")
for readings in content:
   result = predict(readings)
   summa_fram += result[0]
   summa_bak += result[1]
   
print("Front:", summa_fram)
print("Back:", summa_bak)

#1930851503 för lågt? Men algoritmen stämmer. Nvm, Hittade ett bugg :)
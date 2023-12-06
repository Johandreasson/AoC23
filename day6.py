DAY = 6

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()
    
def day6():
  time = [int(t) for t in content[0].split()[1:]]
  record = [int(r) for r in content[1].split()[1:]]
  winnable = []
  x=1
  for i, race in enumerate(time):
    race_speeds = [t*(race-t) for t in range(1, race+1) if t*(race-t) > record[i]]
    winnable.append(len(race_speeds))
  
  for race in winnable:
    x = x*race
    
  time = 48989083
  record = 390110311121360
  
  race_speed = [t*(time-t) for t in range(1, time+1) if t*(time-t) > record]
  
  print(x)
  print(len(race_speed))

day6()
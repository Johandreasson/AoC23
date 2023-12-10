import math
DAY = 8

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

nodes = {}

for item in content[2:]:
  item = item.replace(",", "").replace("(", "").replace(")", "").split()
  nodes[item[0]] = [item[2], item[3]]

current_pos ={node.split()[0]:0 for node in content[2:] if node[2] == "A"}
print(current_pos)


for position in current_pos.keys():
  initial_pos = position
  steps = 0
  while(position[2] != "Z"):
    for direction in content[0]:
      steps += 1
      if direction == "L":
        """go left"""
        #print(nodes[position][0])
        position = nodes[position][0]
      else:
        """go right"""
        #print(nodes[position][1])
        position = nodes[position][1]
      if position[2] == "Z":
        print(initial_pos, "=", steps)
        current_pos[initial_pos] = steps
        break      
print(current_pos)

steps = [x for x in current_pos.values()]
print(math.lcm(steps[0], steps[1], steps[2], steps[3], steps[4], steps[5]))
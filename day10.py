DAY = 10

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has."""

#Allowed
rules = {
  "N":((0, -1), ("S", "|", "F", "7")),
  "E": ((1, 0), ["S", "-", "J", "7"]),
  "S":((0, 1), ["S", "|", "J", "L"]),
  "W": ((-1, 0), ["S", "-", "L", "F"]),
}

def allowed_tile(tile, test_next):
  pass

def find_path(tile, path=[]):
  path.append(tile)
  line, item = tile
  loop = False
  while loop is False:
    print(path, "\n")
    for direction in rules.keys():
      offset_x, offset_y = rules[direction][0]
      next_tile = content[line+offset_y][item+offset_x]
      if next_tile in rules[direction][1]:
        if next_tile == tile:
          loop = True
          return path
        next_tile = (line+offset_y, item+offset_x)
        if next_tile not in path:
          path.append(direction)
          path.append(next_tile)
          line, item = next_tile
          break
  
    for i in range(line-1, line+2):
      try:
        for j in range(item-1, item+2):
          print(content[i][j], end="")
      except IndexError:
        continue
      print()

def find_start(data):
  start_tile = "S"
  for i,line in enumerate(data):
    for j,item in enumerate(line):
      if item == start_tile:
        return i, j

if __name__ == "__main__":
  current_tile = find_start(content)
  print(find_path(current_tile))
DAY = 7

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()
    
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
five=[]
four=[]
full_house=[]
three=[]
two_pair=[]
one_pair=[]
high_card=[]
test = {x:0 for x in cards}

category = [
  five,
  four,
  full_house,
  three,
  two_pair,
  one_pair,
  high_card,
]

for hand in content:
  hand = hand.split()
  test_hand = test.copy()
  for item in hand[0]:
    test_hand[item] += 1
  if "J" in hand[0]:
    """Annoying thing to work with Jokers"""
    #Then the amount of J transforms to the most common card
    j = test_hand["J"]
    test_hand["J"] = 0
    max_key = max(test_hand, key=test_hand.get)
    test_hand[max_key] += j
    #Full houses?
    #If two pair, become the highest valued pair
    #if nothing, become the highest value in hand
  
  if 5 in test_hand.values():
    print("Five of a kind!")
    five.append(hand)
    continue
  if 4 in test_hand.values():
    print("Four of a kind!")
    four.append(hand)
    continue
  if 3 in test_hand.values():
    if 2 in test_hand.values():
      print("Full House!")
      full_house.append(hand)
    else:
      print("Three of a kind!")
      three.append(hand)
    continue
  if 2 in test_hand.values():
    pairs = 0
    for item in test_hand.values():
      if item == 2:
        pairs += 1
    if pairs == 2:
      two_pair.append(hand)
    else:
      one_pair.append(hand)
    continue
  high_card.append(hand)

rank = len(content)
for cat in category:
  for i, hand in enumerate(cat):
    hex_convert = ""
    for item in hand[0]:
      hex_convert += hex(cards.index(item))
    hex_convert = [hex(cards.index(x)) for x in hand[0]]
    hand.insert(0,hex_convert)
  sorted_cat = sorted(cat, key=lambda x: (int(x[0][0], 16), int(x[0][1], 16), int(x[0][2], 16), int(x[0][3], 16), int(x[0][4], 16), x[1]))
  for hand in sorted_cat:
    hand.append(rank)
    rank -= 1

total_winning = 0
for cat in category:
  for hand in cat:
      total_winning += int(hand[2]) * hand[3]

print(total_winning)
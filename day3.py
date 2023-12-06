DAY = 3

input_path = f"inputs/day{DAY}.txt"

# Open and read the contents of the file
with open(input_path, "r", encoding="utf-8") as file:
    content = file.read().splitlines()

def check_machine_part(line, item):
    length = 0
    part = ""
    is_machine_part = False
    while(item+length < len(content[line]) and content[line][item+length].isdigit()):
        part += content[line][item+length]
        length += 1
    for i in range(line-1, line+2):
        try:
            for j in range(item-1, item+length+1):
                print(content[i][j], end="")
                if content[i][j] in "@*/+$&%#=!'^-":
                    is_machine_part = True
        except IndexError:
            continue
        print()
    return is_machine_part, length, int(part)

def part1():
    """Find all the numbers that touches a symbol"""
    summa=0
    for i, line in enumerate(content):
        item = 0
        while(item < len(line)):   
            if line[item].isdigit():
                machine_part, length, part = check_machine_part(i, item)
                if machine_part is True:
                    #print("Machine part found:", part)
                    summa+=part
                item += length
            else:
                item += 1
    print(summa)

def check_gear_ratio(line, item):
    products = []
    product = 0
    gear_ratio = 1
    print(content[line-1],"\n", content[line], "\n", content[line+1])    
    for i in range(line-1, line+2):
        
        try:
            #for j in range(item-1, item+2):
            j = item-1
            length = 0
            backtrack = 0
            while(j < item + 2):
                if content[i][j].isdigit():
                    product = ""
                    length = 0
                    backtrack = 0
                    while(j-backtrack-1 >= 0 and content[i][j-backtrack-1].isdigit()):
                        backtrack += 1
                    while(j+length-backtrack < len(content[i]) and content[i][j+length-backtrack].isdigit()):
                        product += content[i][j+length-backtrack]
                        length += 1
                    print("Product:", product)
                    if product != "0" and int(product) not in products:
                        products.append(int(product))
                    j += length-backtrack
                j+=1
        except IndexError:
            continue
    print(products)
    if len(products) >= 2:
        for item in products:
            gear_ratio = gear_ratio * item
        print(gear_ratio)
    return gear_ratio

def part2():
    """Find the asterix's that touches two numbers and multiply them"""
    # 72451209 FÖR LÅGT!
    # 80703681 för högt
    summa=0
    for i, line in enumerate(content):
        item = 0
        while(item < len(line)):
            if line[item] == "*":             
                summa +=check_gear_ratio(i, item)
            item += 1   
    print(summa)
                

if __name__ == "__main__":
    part2()

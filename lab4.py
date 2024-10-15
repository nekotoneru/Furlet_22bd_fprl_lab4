symbol = input("enter a symbol: ")
found = 0

with open("text4.txt", "r") as file:
    lines = file.readlines()

for line_num, line in enumerate(lines, start = 1):
    stripped_line = line.strip()
    if stripped_line.endswith(symbol):
        found = 1
        revline = stripped_line[::-1]
        print("line: ", line_num)
        print(revline)

if found == 0:
    print("there is no lines with that symbol")
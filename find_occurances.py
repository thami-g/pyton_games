def find_all_occurances(string, char):
    count_total = 0
    index = -1
    
    while True:
        index = string.find(char, index +1)
        if index == -1:
            break
        count_total += 1
    return count_total

def find_all_char_occurances():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        # if key already exists it will not be overwritten or set again to 0
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)

char = '1'
string = '11123'
print(find_all_occurances(string, char))
print(find_all_char_occurances())
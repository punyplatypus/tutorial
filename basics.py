import sys
print("test")
max = 0
list = [1, 2, 3, 44, 4, 5, 6, 99, 4, 5, 6]
for number in list:
    if max < number:
        max = number
    print(max)
print(max)

def add_cool_word(sentence):
    cool_word = " cool"
    sentence = sentence + cool_word
    return(sentence)

def main():
    list_args = sys.argv
    res = add_cool_word(list_args[1])
    print(res)

main()
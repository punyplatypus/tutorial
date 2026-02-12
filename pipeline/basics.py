import sys

def test():
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

def read_args():
    list_args = sys.argv
    try:
        input = list_args[1]
    except IndexError:
        print("please use input parameter")
        input = "no cool"
        exit()
    return(input)

def main():
    input = read_args()
    res = add_cool_word(input)
    print(res)

main()
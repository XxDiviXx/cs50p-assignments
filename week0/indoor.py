#program takes in any input and prints out in all lowercase
def main():
    name = input("Enter a word to be lowercased:   ")
    name = lowerc(name)
    print(name)

def lowerc(a):
    return a.lower()

main()

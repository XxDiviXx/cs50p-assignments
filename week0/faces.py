def main():
    a=input("Enter your emoticon ")
    convert(a)

def convert(d):
    d=d.replace(":)","🙂")
    d=d.replace(":(","🙁")
    print(d)

main()

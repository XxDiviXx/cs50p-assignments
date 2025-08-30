def main():
    a=int(input("Enter the mass of an object. "))
    calc(a)

def calc(d):
    c=300000000
    e=d*(c*c)
    print(f"{e:,}")

main()
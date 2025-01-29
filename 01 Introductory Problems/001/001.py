def main(num):
    while num > 1:
        print(num, end=" ")
        if num&1:
            num = num*3+1
        else:
            num = num//2

    print(1)

if __name__=="__main__":
    # read input
    num = int(input())
    main(num)
    exit(0)


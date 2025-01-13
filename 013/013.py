def main(n):
    if n == 1:
        return ['0', '1']
    temp = []
    prev = main(n-1)
    for ch in prev:
        temp.append('0'+ch)
    for ch in prev[::-1]:
        temp.append('1'+ch)
    return temp

if __name__=="__main__":
    n = int(input())
    lst = main(n)
    for str in lst:
        print(''.join(str))
    exit(0)
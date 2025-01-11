if __name__=="__main__":
    n = int(input())
    MOD = 10**9+7
    print((1<<n)%MOD) # bitwise way
    # print((2**n)%MOD) # power way
    exit(0)
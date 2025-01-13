if __name__=="__main__":
    inpt_str = str(input())
    n = len(inpt_str)
    freq = [0]*26
    for ch in inpt_str:
        freq[ord(ch)-ord('A')] += 1
    
    ans_temp = ['']*n
    i = 0
    j = n-1
    odd = -1
    for idx in range(26):
        if freq[idx]:
            if freq[idx]&1:
                if odd != -1:
                    print('NO SOLUTION')
                    exit(0)
                else:
                    odd = idx
            else:
                while freq[idx]:
                    ans_temp[i] = chr(ord('A')+idx)
                    ans_temp[j] = chr(ord('A')+idx)
                    freq[idx] -= 2
                    i += 1
                    j -= 1

    for idx in range(i, j+1):
        ans_temp[idx] = chr(ord('A')+odd)
    
    print(''.join(ans_temp))
    exit(0)


def get_permutation(string):
    if len(string) == 1:
        return string
    ans = set()
    for i in range(len(string)):
        after = get_permutation(string[:i]+string[i+1:])
        for word in after:
            ans.add(string[i]+word)
    return ans
if __name__=="__main__":
    string = str(input())
    string = ''.join(sorted(list(string)))
    all_permutation = get_permutation(string)
    print(len(all_permutation))
    for word in all_permutation:
        print(''.join(word))
    exit(0)
if __name__=="__main__":
    no_of_applicant, no_of_apartment, k = list(map(int, input().split()))
    applicant_size = list(map(int, input().split()))
    apartment_size = list(map(int, input().split()))
    ans = 0
    apartment_size.sort()
    applicant_size.sort()
    applicant = 0
    apartment = 0
    while applicant < no_of_applicant and apartment < no_of_apartment:
        low = applicant_size[applicant] - k
        high = applicant_size[applicant] + k
        if apartment_size[apartment] < low:
            apartment += 1
        elif apartment_size[apartment] > high:
            applicant += 1
        else:
            applicant += 1
            apartment += 1
            ans += 1 
    print(ans)
    exit(0)
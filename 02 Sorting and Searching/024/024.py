if __name__=="__main__":
    no_customers = int(input())
    arrival_time = []
    departure_time = []
    for _ in range(no_customers):
        av_time, dp_time = list(map(int, input().split()))
        arrival_time.append(av_time) 
        departure_time.append(dp_time)
    
    arrival_time.sort()
    departure_time.sort()
    max_customer = 0
    curr_customer = 0
    a_i = 0
    d_i = 0
    while a_i < no_customers and d_i < no_customers:
        if arrival_time[a_i] <= departure_time[d_i]:
            curr_customer += 1
            a_i += 1
        else:
            curr_customer -= 1
            d_i += 1

        max_customer = max(max_customer, curr_customer)
    print(max_customer)
    exit(0)
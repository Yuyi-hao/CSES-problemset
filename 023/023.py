def get_ticket(max_price, tickets, low, high):
    res = -1
    temp = -1
    while low <= high:
        mid = (low+high)//2
        if tickets[mid] < 0:
            temp = max(get_ticket(max_price, tickets, mid+1, high), get_ticket(max_price, tickets, low, mid-1))
            break
        if tickets[mid] <= max_price:
            res = mid
            low = mid+1
        else:
            high = mid-1
    return max(temp, res)



if __name__=="__main__":
    no_ticket, no_customer = list(map(int, input().split()))
    tickets = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    tickets.sort()
    for idx in range(no_customer):
        curr_price = customers[idx]
        ticket = get_ticket(curr_price, tickets, 0, no_ticket-1)
        if ticket != -1:
            print(tickets[ticket])
            tickets[ticket] *= -1
        else:
            print(-1)
    exit(0)
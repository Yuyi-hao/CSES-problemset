
def get_digit(query):
    if query < 10:
        return query
    digit_length = 1 
    while query > 9*(10**(digit_length-1))*digit_length:
        query -= 9*(10**(digit_length-1))*digit_length
        digit_length += 1

    num = (10**(digit_length-1))  +  ((query-1)//digit_length)
    location = (query-1)%digit_length
    return str(num)[location]


if __name__=="__main__":
    queries = int(input())
    for _ in range(queries):
        query = int(input())
        digit = get_digit(query)
        print(digit)
    
    exit(0)
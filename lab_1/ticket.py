def is_lucky(number: int):
    number_copy = number
    last_digits_sum = 0
    first_digits_sum = 0
    for i in range(6):
        if i < 3:
            last_digits_sum += number_copy % 10
        else:
            first_digits_sum += number_copy % 10
            number //= 10
    return last_digits_sum == first_digits_sum


def get_nearest_lucky_ticket(ticket_number: int):
    lower_number = ticket_number
    upper_number = ticket_number
    while True:
        if is_lucky(lower_number):
            return lower_number
        elif is_lucky(upper_number):
            return upper_number
        lower_number -= 1
        upper_number += 1


if __name__ == '__main__':
    print(get_nearest_lucky_ticket(123411))
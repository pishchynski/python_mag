def calculate_gcd(first, second):
    return calculate_gcd(second, first % second) if second > 0 else first

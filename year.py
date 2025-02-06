def get_year_word(n: int):
    m = n % 100
    b = m % 10
    if m >= 10 and m <= 20:
        return "лет"
    else:
        if b == 0 or b >= 5:
            return "лет"
        elif b >= 2 and b <= 4:
            return "года"
        elif b == 1:
            return "год"

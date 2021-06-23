from .constants import NUM_NAME, HUNDRED, ONE_DIGIT, TWO_DIGITS


def format_num(amount: str) -> str:
    try:
        full_amount = f'{float(amount):,.2f}'
    except ValueError:
        raise ValueError("Invalid number format given")
    return full_amount


def tokenize_cents(amount: str) -> dict[str, str]:
    cents = amount.split('.')[1]
    cents_tokens = {'Cents': cents}
    return cents_tokens


def tokenize_integer(amount: str) -> dict[str, str]:
    integer_parts = amount.split('.')[0].split(',')
    num_names = NUM_NAME[:len(integer_parts)]
    num_names.reverse()
    integer_tokens = {}
    for idx, name in enumerate(num_names):
        integer_tokens[name] = integer_parts[idx]
    return integer_tokens


def tokenize(amount: str) -> dict[str, str]:
    full_amount = format_num(amount)
    tokens = tokenize_integer(full_amount) | tokenize_cents(full_amount)
    return tokens


def translate_three_digits(three_digits: str) -> str:
    hundreds_digit = three_digits[0]
    tens_digit = three_digits[1]
    ones_digit = three_digits[2]

    hundreds_word = ONE_DIGIT[int(hundreds_digit)]

    if tens_digit == '0' and ones_digit == '0':
        return f'{hundreds_word} Hundred'
    elif tens_digit == '0' and ones_digit != '0':
        ones_word = translate_one_digit(ones_digit)
        return f'{hundreds_word} Hundred And {ones_word}'
    else:
        tens_and_ones = f'{tens_digit}{ones_digit}'
        tens_and_ones_word = translate_two_digits(tens_and_ones)
        return f'{hundreds_word} Hundred And {tens_and_ones_word}'


def translate_two_digits(two_digits: str) -> str:
    if int(two_digits) in TWO_DIGITS.keys():
        return TWO_DIGITS[int(two_digits)]
    else:
        tens_part = int(f'{two_digits[0]}0')
        ones_part = int(two_digits[1])
        tens_word = TWO_DIGITS[tens_part]
        ones_word = ONE_DIGIT[ones_part]
        return f'{tens_word} {ones_word}'


def translate_one_digit(one_digit: str) -> str:
    return ONE_DIGIT[int(one_digit)]

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


def translate_digits(digits: str) -> str:
    digits = str(int(digits))
    if len(digits) == 3:
        return translate_three_digits(digits)
    elif len(digits) == 2:
        return translate_two_digits(digits)
    elif len(digits) == 1:
        return translate_one_digit(digits)


def translate_full_amount(full_amount: str) -> str:
    tokens = tokenize(full_amount)

    tokens_with_rm_zero = {}
    for key in tokens:
        if int(tokens[key]) != 0:
            tokens_with_rm_zero[key] = tokens[key]

    tokens_words = {}
    for key, value in tokens_with_rm_zero.items():
        tokens_words[key] = translate_digits(tokens_with_rm_zero[key])

    integer_part_words = ""
    cents_part_words = ""

    if len(tokens_words) == 1 and 'Cents' in tokens_words.keys():
        cents_part_words = f'{tokens_words[0]} Cents Only'
        return cents_part_words
    else:
        for key, value in tokens_words.items():
            if key != 'Cents':
                integer_part_words += f'{value} {key} '
            else:
                cents_part_words += f'{value} {key} '

    if len(cents_part_words) == 0:
        full_words = f'{integer_part_words}Only'
    else:
        full_words = f'{integer_part_words}And {cents_part_words}Only'

    return full_words

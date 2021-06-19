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


def tokenize(amount):
    full_amount = format_num(amount)
    tokens = tokenize_integer(full_amount) | tokenize_cents(full_amount)
    return tokens

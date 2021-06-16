from .constants import NUM_NAME, HUNDRED, ONE_DIGIT, TWO_DIGITS

def _rm_leading_items(list_, num):
    removals = [idx for idx in range(0, num)]
    list_ = [val for idx, val in enumerate(list_) if idx not in removals]
    return list_

def _rm_empty_dict_items(dict_):
    new_dict = {}
    for key in dict_:
        if dict_[key] != '':
            new_dict[key] = dict_[key]
    return new_dict

def _rm_leading_zeros(amount):
    try:
        amount = str('{:.2f}'.format(float(amount)))
        return amount
    except ValueError:
        pass

#TODO: Add function to remove leading zeros (completed)
#TODO: Add tests for leading zeros cases
#TODO: Add support for decimals (completed)
#TODO: Add tests for decimal cases

def _tokenize_integer_part(integer):
    tokens = {}
    integer = str(integer).replace(',', '')
    integer = list(integer)
    num_of_num_names = len(integer) // 3 + 1
    leading_separater = len(integer) % 3
    num_names = NUM_NAME[:num_of_num_names]

    if len(integer) <= 3:
        tokens[num_names[0]] = ''.join(integer)
    else:
        tokens[num_names[-1]] = ''.join(integer[:leading_separater])
        integer = _rm_leading_items(integer, leading_separater)

        starting_num_name = 2
        while len(integer) > 0:
            tokens[num_names[-starting_num_name]] = ''.join(integer[:3])
            integer = _rm_leading_items(integer, 3)
            starting_num_name += 1

    integer_tokens = _rm_empty_dict_items(tokens)

    return integer_tokens

def _tokenize_decimal_part(decimal):
    decimal_tokens = {'Decimal': decimal}
    return decimal_tokens

def tokenize_amount(amount):
    amount = _rm_leading_zeros(amount)
    integer_and_decimal = amount.split('.')
    integer = integer_and_decimal[0]
    decimal = integer_and_decimal[1]
    integer_tokens = _tokenize_integer_part(integer)
    decimal_tokens = _tokenize_decimal_part(decimal)
    tokens = integer_tokens | decimal_tokens
    return tokens

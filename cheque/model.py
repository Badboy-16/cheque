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

def tokenize(amount):
    tokens = {}
    amount = str(amount).replace(',', '')
    amount = list(amount)
    num_of_num_names = len(amount) // 3 + 1
    leading_separater = len(amount) % 3
    num_names = NUM_NAME[:num_of_num_names]

    if len(amount) <= 3:
        tokens[num_names[0]] = ''.join(amount)
    else:
        tokens[num_names[-1]] = ''.join(amount[:leading_separater])
        amount = _rm_leading_items(amount, leading_separater)

        starting_num_name = 2
        while len(amount) > 0:
            tokens[num_names[-starting_num_name]] = ''.join(amount[:3])
            amount = _rm_leading_items(amount, 3)
            starting_num_name += 1

    output_tokens = _rm_empty_dict_items(tokens)

    return output_tokens

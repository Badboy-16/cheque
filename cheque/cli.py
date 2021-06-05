import argparse

def create_parser():

    parser = argparse.ArgumentParser(
        prog='cheque',
        description='Convert cheque amounts to words'
    )

    parser.add_argument(
        'amount',
        nargs='*',
        help='amounts to be converted to words'
    )

    parser.add_argument(
        '-C',
        '--all-upper',
        action='store_true',
        help='output words in all uppercase'
    )

    return parser
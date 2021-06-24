import argparse


def create_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser(
        prog='cheque',
        description='Convert cheque amounts to words'
    )

    parser.add_argument(
        'amount',
        action='store',
        help='amounts to be converted to words'
    )

    parser.add_argument(
        '-U',
        '--upper',
        action='store_true',
        help='output words in all uppercase'
    )

    return parser

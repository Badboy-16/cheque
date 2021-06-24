from .cli import create_parser
from .model import translate_full_amount
from .model import print_full_words


def main() -> int:
    exit_code = 0
    parser = create_parser()
    args = parser.parse_args()
    amount_in_words = translate_full_amount(args.amount)
    if args.upper:
        amount_in_words = amount_in_words.upper()
    exit_code = print_full_words(amount_in_words)
    return exit_code


if '__name__' == '__main__':
    exit(main())

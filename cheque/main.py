from .cli import create_parser

def main() -> int:
    exit_code = 0
    parser = create_parser()
    args = parser.parse_args()
    if args.amount:
        #TODO: Enrich function to process input amount
        convert_amount(*args.amount)
        if args.upper:
            #TODO: Enrich function to capitalise all letters
            all_upper()
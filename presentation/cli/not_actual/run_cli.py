from presentation.cli.constants import AtmOperationsEnum
from presentation.cli.not_actual.parser_config import create_parser


def cli_runner():
    atm_parser = create_parser()
    args = atm_parser.parse_args()
    if args.operation == AtmOperationsEnum.EXIT:
        print("EXIT")
    print(args)

if __name__ == "__main__":
    cli_runner()
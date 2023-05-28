from argparse import ArgumentParser, Namespace


def create_parser() -> ArgumentParser:
    """Create argument parser instance for command line interaction with bank ATM."""

    atm_parser = ArgumentParser()
    subparsers = atm_parser.add_subparsers(title="parser for a banking operation",
                                           dest="operation")

    exit_parser = subparsers.add_parser(name="exit",
                                        description="end the interaction")

    deposit_parser = subparsers.add_parser(name="deposit",
                                           description="deposit operation requires '--client' and '--amount' parameters")
    deposit_parser.add_argument("client",
                                help="first and last name of the bank's client")
    deposit_parser.add_argument("amount",
                                help="required amount of money")

    withdraw_parser = subparsers.add_parser(name="withdraw",
                                            description="withdraw operation requires '--client' and '--amount' parameters")
    withdraw_parser.add_argument("client",
                                 help="first and last name of the bank's client")
    withdraw_parser.add_argument("amount",
                                 help="required amount of money")

    bank_statement_parser = subparsers.add_parser(name="show_bank_statement",
                                                  description="show bank statement operation requires '--since' and '--till' date parameters")
    bank_statement_parser.add_argument("--since",
                                       help="start date of the bank statement period")
    bank_statement_parser.add_argument("--till",
                                       help="date of the end of the bank statement period")

    return atm_parser

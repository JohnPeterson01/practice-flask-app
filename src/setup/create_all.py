from argparse import ArgumentParser

from src.setup.operations import create_all, drop_all


# Taken from microcosm_postgres
def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--drop", "-D", action="store_true")
    # Allow services to set custom arguments for `createall`
    arguments, _ = parser.parse_known_args()
    return arguments


def main(app_name, testing):
    args = parse_args()
    if args.drop:
        drop_all(app_name, testing)
    create_all(app_name, testing)

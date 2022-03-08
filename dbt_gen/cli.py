from argparse import ArgumentParser

import dbt_gen.generate_source_yaml
import dbt_gen.generate_base_model
import dbt_gen.generate_dbt


def add_parser(sub_parsers, name, config_func):
    subparser = sub_parsers.add_parser(name)
    config_func(subparser)
    return subparser


def cli():
    parser = ArgumentParser()
    sub_parsers = parser.add_subparsers(help="Action")

    add_parser(sub_parsers, "generate_source", dbt_gen.generate_source_yaml.config_parser)
    add_parser(sub_parsers, "generate_base_model", dbt_gen.generate_base_model.config_parser)
    add_parser(sub_parsers, "generate_dbt", dbt_gen.generate_dbt.config_parser)

    args = parser.parse_args()

    if "func" in args:
        args.func(args)
    else:
        print("Please choose action\n")
        parser.print_help()


def main():
    cli()

import click
import os
import tomllib


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "./sources.toml"), "rb") as file:
    sources = tomllib.load(file)


def common_options(func):
    for option in [
        click.option("-d", "--date", type=str, prompt=True, help="year of publication"),
        click.option(
            "-t", "--title", type=str, prompt=True, default="", help="title of article"
        ),
        click.option(
            "-a",
            "--author",
            type=str,
            nargs=2,
            prompt=True,
            default=["", ""],
            help="author first and last name (use quotes around multi-part names)",
        ),
    ]:
        func = option(func)
    return func


def source_option(func):
    for option in [
        click.option(
            "-s",
            "--source",
            type=click.Choice(sources.keys()),
            default=None,
            help="use one of the pre-configured common sources",
        )
    ]:
        func = option(func)
    return func


def url_option(func):
    for option in [
        click.option(
            "-url",
            type=str,
            prompt=True,
            default="",
            help="url where the source can be found",
        )
    ]:
        func = option(func)
    return func

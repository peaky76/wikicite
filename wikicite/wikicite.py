from datetime import date, datetime
import os
import click
import tomllib
from wikicite.create_citation import create_citation
import wikicite.markdown as md


TODAY = date.today().strftime("%d %B %Y")

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "./sources.toml"), "rb") as file:
    sources = tomllib.load(file)


@click.group()
def cite():
    pass


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


@cite.command()
@common_options
@click.option("-p", "--publisher", type=str, prompt=True, help="publisher")
@click.option("-l", "--location", type=str, prompt=True, help="location of publisher")
@click.option("-isbn", type=str, prompt=True, default="", help="isbn of book")
def book(title, author, publisher, location, date, isbn):
    ref_name = (
        f"{author[1]}{date}"
        if author[1]
        else f"{title[:6].replace(' ','').title()}{date}"
    )

    attributes = {
        "last": author[1],
        "first": author[0],
        "title": title,
        "location": location,
        "publisher": publisher,
        "isbn": isbn,
        "date": date.strip(),
    }

    create_citation(ref_name, "book", attributes)


@cite.command()
@source_option
@common_options
@url_option
def news(source, author, title, date, url):
    source = sources[source] if source else None

    raw_date = datetime.strptime(str(date), "%d%m%Y") or None
    article_date = raw_date.strftime("%e %B %Y") or ""
    ymd_date = raw_date.strftime("%y%m%d") or ""
    ref_name = (
        f"{author[1]}{ymd_date}"
        if author[1]
        else f"{source['abbr']}{ymd_date}"
        if source
        else f"{title[:6].replace(' ','').title()}{ymd_date}"
    )

    attributes = {
        "last": author[1],
        "first": author[0],
        "title": title,
        "work": md.link(source["name"]) if source else "",
        "location": source["location"] if source else "",
        "url": url,
        "date": article_date.strip(),
        "access-date": TODAY,
    }

    create_citation(ref_name, "news", attributes)


@cite.command()
@source_option
@common_options
@url_option
def web(source, author, title, date, url):
    source = sources[source] if source else None

    raw_date = datetime.strptime(str(date), "%d%m%Y") or None
    article_date = raw_date.strftime("%e %B %Y") or ""
    ymd_date = raw_date.strftime("%y%m%d") or ""
    ref_name = (
        f"{author[1]}{ymd_date}"
        if author[1]
        else f"{source['abbr']}{ymd_date}"
        if source
        else f"{title[:6].replace(' ','').title()}{ymd_date}"
    )

    attributes = {
        "last": author[1],
        "first": author[0],
        "title": title,
        "work": md.link(source["name"]) if source else "",
        "location": source["location"] if source else "",
        "url": url,
        "date": article_date.strip(),
        "access-date": TODAY,
    }
    create_citation(ref_name, "web", attributes)

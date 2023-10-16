from datetime import date, datetime
import os
import click
import tomllib
from wikicite.create_citation import create_citation
from wikicite.get_reference_name import get_reference_name
import wikicite.markdown as md
from wikicite.options import common_options, source_option, url_option


TODAY = date.today().strftime("%d %B %Y")

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "./sources.toml"), "rb") as file:
    sources = tomllib.load(file)


@click.group()
def cite():
    pass


@cite.command()
@common_options
@click.option("-p", "--publisher", type=str, prompt=True, help="publisher")
@click.option("-l", "--location", type=str, prompt=True, help="location of publisher")
@click.option("-isbn", type=str, prompt=True, default="", help="isbn of book")
def book(title, author, publisher, location, date, isbn):
    ref_name = get_reference_name(author, date, title)

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
    ref_name, attributes = prep_news_or_web(source, author, title, date, url)
    create_citation(ref_name, "news", attributes)


@cite.command()
@source_option
@common_options
@url_option
def web(source, author, title, date, url):
    ref_name, attributes = prep_news_or_web(source, author, title, date, url)
    create_citation(ref_name, "web", attributes)


def prep_news_or_web(source, author, title, date, url):
    source = sources[source] if source else None
    raw_date = datetime.strptime(str(date), "%d%m%Y") or None
    article_date = raw_date.strftime("%e %B %Y") or ""
    ymd_date = raw_date.strftime("%y%m%d") or ""
    ref_name = get_reference_name(author, ymd_date, title, source)

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

    return ref_name, attributes

from datetime import date, datetime
import os
import click
import tomllib
import wikicite.markdown as md

CITE_TYPES = ("news", "web")
TODAY = date.today().strftime("%d %B %Y")

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "./sources.toml"), "rb") as file:
    sources = tomllib.load(file)


@click.command()
@click.argument("cite_type", type=click.Choice(CITE_TYPES, case_sensitive=False))
@click.option(
    "-s",
    "--source",
    type=click.Choice(sources.keys()),
    default=None,
    help="use one of the pre-configured common sources",
)
@click.option(
    "-a",
    "--author",
    type=str,
    nargs=2,
    prompt=True,
    default=["", ""],
    help="author first and last name (use quotes around multi-part names)",
)
@click.option(
    "-t", "--title", type=str, prompt=True, default="", help="title of article"
)
@click.option("-d", "--date", type=str, prompt=True, help="date of publication")
@click.option(
    "-url", type=str, prompt=True, default="", help="url where the source can be found"
)
def cite(cite_type, source, author, title, date, url):
    source = sources[source] if source else None

    raw_date = datetime.strptime(str(date), "%d%m%Y") or None
    article_date = raw_date.strftime("%e %B %Y") or ""
    ymd_date = raw_date.strftime("%y%m%d") or ""
    ref_name = (
        f"{author[1]}{ymd_date}"
        if author[1]
        else f"{source['abbr']}{ymd_date}"
        if source
        else f"{title[:6]}{ymd_date}"
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
    attributes = {key: val for key, val in attributes.items() if val}

    click.echo(f"<ref name={ref_name}>")
    click.echo(
        md.template(
            " |".join(
                [f"cite {cite_type}"]
                + [f"{key}={val}" for key, val in attributes.items() if val]
            )
        )
    )
    click.echo("</ref>")

import click
import yaml
from datetime import date, datetime
import wikicite.markdown as md

TODAY = date.today().strftime('%d %B %Y')

with open('wikicite/sources.yaml', 'r') as file:
    sources = yaml.safe_load(file)


@click.command()
@click.argument('cite_type', type=click.Choice(sources.keys(), case_sensitive=False))
@click.argument('source_id', type=str)
@click.option('-a', '--author', type=str, nargs=2, prompt=True, default=['', ''], help='author first and last name (use quotes around multi-part names)')
@click.option('-t', '--title', type=str, prompt=True, default='', help='title of article')
@click.option('-d', '--date', type=str, prompt=True, help='date of publication')
@click.option('-url', type=str, prompt=True, default='', help='url where the source can be found')
def cite(cite_type, source_id, author, title, date, url):

    source = sources[cite_type][source_id]

    raw_date = datetime.strptime(str(date), '%d%m%Y') or None
    article_date = raw_date.strftime("%e %B %Y") or ''
    ymd_date = raw_date.strftime('%y%m%d') or ''
    ref_name = f"{author[1]}{ymd_date}" if author[1] else f"{source['abbr']}{ymd_date}"
    
    attributes = {
        'last': author[1],
        'first': author[0],
        'title': title,
        'work': md.link(source['name']),
        'location': source['location'],
        'url': url,
        'date': article_date.strip(),
        'access-date': TODAY,
    }

    click.echo(f"<ref name={ref_name}>")
    click.echo(md.template(' |'.join(
        [f"cite {cite_type}"] +
        [f"{key}={val}" for key, val in attributes.items() if val])
    ))
    click.echo('</ref>')

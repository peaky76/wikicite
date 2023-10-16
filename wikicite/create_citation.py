import click
import wikicite.markdown as md


def create_citation(ref_name, cite_type, attributes):
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

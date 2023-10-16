def get_reference_name(author, date, title, source={}):
    return (
        f"{author[1]}{date}"
        if author[1]
        else f"{source['abbr']}{date}"
        if source.get("abbr")
        else f"{title[:6].replace(' ','').title()}{date}"
    )

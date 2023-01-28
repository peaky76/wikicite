def link(page, alias=None):
    return f"[[{page}|{alias}]]" if alias else f"[[{page}]]"


def template(content):
    return f"{'{{'}{content}{'}}'}"

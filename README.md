# wikicite

<!-- [![CI](https://img.shields.io/github/workflow/status/rgieseke/cite/CI?style=for-the-badge&label=actions&logo=github&logoColor=white)](https://github.com/rgieseke/wikicite/actions) -->

[![PyPI](https://img.shields.io/pypi/v/wikicite.svg?style=for-the-badge)](https://pypi.org/project/wikicite/)

## Installation

```
pip install wikicite
```

## Usage

Command line tool to create ready-to-use Wikipedia citations from a series of inputs.

```
$ wikicite news bbc -t 'An Important Article' -a Fred Bloggs -d 01062020 -url http://www.bbc.co.uk/an-important-article

<ref name=Bloggs200601>
{{cite news |last=Bloggs |first=Fred |title=An Important Article |work=[[BBC]] |url=http://www.bbc.co.uk/an-important-article |date=1 June 2020 |access-date=28 January 2023}}
</ref>
```

Where any options are not specified, the user will be prompted to add them, but all except date are optional.
A note on formatting for certain options:

- Titles `-t` or `--title` should be provided in quotation marks
- Authors `-a` or `--author` should be provided as `<firstname> <lastname>`. Where multi-part names are needed, quotation marks should be used to identify the parts, e.g. `Lynn 'Faulds Wood'` or `'John Paul' Jones`
- Dates `-d` or `--date` should be provided in `ddmmyyyy` format

For a full list of options, see

```
$ cite --help
```

For more details on Wikipedia citations please see [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Citing_sources)

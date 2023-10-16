from click.testing import CliRunner
from wikicite.wikicite import cite, TODAY


def test_basic_full_citation():
    runner = CliRunner()
    result = runner.invoke(
        cite,
        [
            "news",
            "g",
            "-t",
            "An Important Article",
            "-a",
            "Fred",
            "Bloggs",
            "-d",
            "01062020",
            "-url",
            "http://www.theguardian.com/an-important-article",
        ],
    )
    assert result.exit_code == 0
    assert "<ref name=Bloggs200601>" in result.output
    assert (
        f"{'{{'}cite news |last=Bloggs |first=Fred |title=An Important Article |work=[[The Guardian]] |location=London |url=http://www.theguardian.com/an-important-article |date=1 June 2020 |access-date={TODAY}{'}}'}"
        in result.output
    )
    assert "</ref>" in result.output


def runner():
    test_basic_full_citation()
    print("1 test passed successfully")

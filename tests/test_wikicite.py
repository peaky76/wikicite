from click.testing import CliRunner
from wikicite.wikicite import cite, TODAY


def test_wikicite_link():
    runner = CliRunner()
    result = runner.invoke(cite, ["link", "Test"])
    assert result.exit_code == 0
    assert "[[Test]]" in result.output


def test_basic_full_citation():
    runner = CliRunner()
    result = runner.invoke(
        cite,
        [
            "news",
            "-s",
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
    test_wikicite_link()
    print("2 tests passed successfully")

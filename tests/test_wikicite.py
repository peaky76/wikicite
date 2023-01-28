from click.testing import CliRunner
from wikicite.wikicite import cite


def test_basic_full_citation():
    # TODO: Find source of test failure

    runner = CliRunner()
    result = runner.invoke(cite, ['news', 'g', '-t', "An Important Article", '-a', 'Fred', 'Bloggs', '-d', '01062020', '-url' 'http://www.theguardian.com/an-important-article'])
    assert result.exit_code == 0
    assert "<ref name=Bloggs200601>" in result.output
    assert "{{cite news |last=Bloggs |first=Fred |title=An Important Article |work=[[BBC]] |url=http://www.theguardian.com/an-important-article |date=1 June 2020 |access-date=28 January 2023}}" in result.output
    assert "</ref>" in result.output


def runner():
    test_basic_full_citation()
    print('1 test passed successfully')
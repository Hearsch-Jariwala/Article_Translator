from main import get_article_text, get_and_translate
from click.testing import CliRunner


def test_get_article_text():
    article_txt = get_article_text(
        "https://en.wikipedia.org/wiki/Artificial_intelligence"
    )
    assert article_txt.__contains__(
        "as opposed to the natural intelligence displayed by animals "
        "including humans."
    )
    assert len(article_txt) > 25

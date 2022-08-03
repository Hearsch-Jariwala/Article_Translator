import requests
from bs4 import BeautifulSoup
import click
from transformers import pipeline


def translate(article_text):
    article_sentences = article_text.split(".")
    output = ""
    translator = pipeline(model="Helsinki-NLP/opus-mt-en-es")
    for sentence in article_sentences:
        translation = translator(sentence)
        output += list(translation[0].values())[0]
    return output


@click.command()
@click.option(
    "--url",
    type=str,
    default="https://en.wikipedia.org/wiki/Artificial_intelligence",
)
def get_and_translate(url):
    """
    It takes a URL, downloads the article text, and translates it to spanish
    """

    # translate
    article_text = get_article_text(url)
    translation = translate(article_text)
    print("Translation in Spanish: ")
    print(translation)


def get_article_text(article_url):
    # Get article
    page = requests.get(article_url)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract body text
    body_text = soup.find_all("p")
    body_text = [i.text for i in body_text]
    article_text = " ".join(body_text)
    return article_text


if __name__ == "__main__":
    get_and_translate()  # pylint: disable=no-value-for-parameter

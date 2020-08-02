from datetime import datetime
import unittest

from scrapping.spiders.quotes import QuotesSpider

from scrapy.http import Request, TextResponse


def fake_response_from_file(file_name, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file
    @param file_name: The relative filename from the responses directory,
                      but absolute paths are also accepted.
    @param url: The URL of the response.
    returns: A scrapy HTTP response which can be used for unittesting.
    """
    if not url:
        url = 'http://www.example.com'

    with open(file_name, 'r') as fake_responde_html:
        file_content = fake_responde_html.read()

    request = Request(url=url)
    response = TextResponse(
        url=url,
        request=request,
        body=file_content,
        encoding='utf-8'
    )
    return response


class TestParsers(unittest.TestCase):

    def setUp(self):
        self.created_at = datetime.now().isoformat()
        self.expected = {
            'id': 0,
            'bio': 'In 1879, Albert Einstein was born in Ulm, Germany.',
            'birthdate': 'March 14, 1879',
            'name': 'Albert Einstein'
        }

    def test_parse_author(self):
        fake_response = fake_response_from_file('scrapping/tests/resources/albert_einstein.html')
        result = QuotesSpider().parse_author(fake_response)
        self.expected['created_at'] = result['created_at']
        # Test created_at
        self.assertTrue(result['created_at'] > self.created_at)

        # Test other results
        self.assertEqual(self.expected, result)

    def test_parse(self):
        expected = '(<GET http://quotes.toscrape.com/author/Albert-Einstein>, ' \
                   '<GET http://quotes.toscrape.com/author/J-K-Rowling>, ' \
                   '<GET http://quotes.toscrape.com/author/Albert-Einstein>, ' \
                   '<GET http://quotes.toscrape.com/author/Jane-Austen>, ' \
                   '<GET http://quotes.toscrape.com/author/Marilyn-Monroe>, ' \
                   '<GET http://quotes.toscrape.com/author/Albert-Einstein>, ' \
                   '<GET http://quotes.toscrape.com/author/Andre-Gide>, ' \
                   '<GET http://quotes.toscrape.com/author/Thomas-A-Edison>, ' \
                   '<GET http://quotes.toscrape.com/author/Eleanor-Roosevelt>, ' \
                   '<GET http://quotes.toscrape.com/author/Steve-Martin>, ' \
                   '<GET http://quotes.toscrape.com/page/2/>)'
        fake_response = fake_response_from_file('scrapping/tests/resources/quotes.html')
        result = QuotesSpider().parse(fake_response)
        self.assertEqual(expected, str(tuple(result)))


if __name__ == '__main__':
    unittest.main()

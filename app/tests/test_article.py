import unittest
from app.models import Articles

class TestArticle(unittest.TestCase):
    '''
    Test the behavior of the Articles class
    '''
    def setUp(self):
        #will run before every test
        self.new_article=Articles("kenyan gazette","was established in the year  1954","https://newsapi.org/v2/sources","https://newsapi/img.png","18-10-2020")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    '''
    Test our  News if it is initialized correctly
    '''
    def self_init(self):
        self.assertEqual(self.new_article.title,"kenyan gazette")
        self.assertEqual(self.new_article.description,"was established in the year  1954")
        self.assertEqual(self.new_article.url,"https://newsapi.org/v2/sources")
        self.assertEqual(self.new_article.urlToImage,"Kenyatta and some colonial government")
        self.assertEqual(self.new_article.publishedAt,"https://kenya.org.com")

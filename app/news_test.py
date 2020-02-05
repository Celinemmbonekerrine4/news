import unittest
from app.models.news import News

# News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_News = News('abc-news','ABC NEWS','trusted source',' https://abcnews.go.com','general','en','us')

    def test_instance(self):
            self.assertTrue(isinstance(self.new_News,News))

if __name__ == '__main__':
    unittest.main()
    


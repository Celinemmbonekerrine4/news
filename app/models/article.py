class Article:

    all_article = []
def __init__(self,news_id,name,description,url,category,language,country):
    self.news_id = id
    self.name = name
    self.url = url
    self.category = category
    self.language = language
    self.country = country
    

def save_article(self):
        Article.all_article.append(self)


@classmethod
def clear_article(cls):
    Article.all_article.clear()

@classmethod
def get_article(cls,id):

    response = []

    for Article in cls.all_article:

        if Article.news_id == id:
            response.append(Article)

        return response

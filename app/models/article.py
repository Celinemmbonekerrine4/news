class Article:

    all_article = []

    def __init__(self,id,name,description,url,urlToImage,content):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
    
    

# def save_article(self):
#         Article.all_article.append(self)


# @classmethod
# def clear_article(cls):
#     Article.all_article.clear()

# @classmethod
# def get_article(cls,id):

#     response = []

#     for Article in cls.all_article:

#         if Article.news_id == id:
#             response.append(Article)

#         return response

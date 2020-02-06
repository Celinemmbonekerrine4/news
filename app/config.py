class Config:
    NEWS_API_KEY = 'cd2297074fc14b4ca59f3b4f3135f6c2'

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?sortBy=publishedAt&apiKey={}'

    ARTICLE_API_BASE_URL = "https://newsapi.org/v2/everything?sources={}&apiKey={}"


class prodConfig(Config):
    pass



class DevConfig(Config):
    DEBUG = True

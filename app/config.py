class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&from=2020-01-01&sortBy=publishedAt&apiKey=cd2297074fc14b4ca59f3b4f3135f6c2'
class prodConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

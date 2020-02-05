from app import app
from .request import get_news
from flask import render_template, request, redirect, url_for
from .request import get_news, get_news, search_news
from app.models import article
from .forms import articleForm

# Article = Article.article



@app.route('/')
def index():

    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_showing')
    name = 'Home - Welcome To The Informative News Highlight'
    message = 'News article'
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search', news_name=search_news))

    else:

        return render_template('index.html',message=message,title=title, popular=popular_news, upcoming=upcoming_news, now_showing=now_showing_news)


@app.route('/news/<int:id>')
def news(id):
    news = get_news(id)
    name = f'(news.name)'
    # article = article.get_article(news.id)

    return render_template('news.html', name=name, news=news)


@app.route('/search/<news_name>')
def search(news_name):
    news_name_list = news_name.split('')
    news_name_format = + (news_name_list)
    search_news = search_news(news_name_format)
    name = f'search results for {news_name}'
    return render_template('search.html,news = searched_news')


@app.route('/news/article/new/<int:id>', methods=['GET POST'])
def new_article(id):
    form = articleForm()
    news = get_news(id)

    if form.validate_on_submit():
        name = form.name.data
        article = form.article.data
        new_article = article(News.id, name, article)
        new_article.save_article()
        return redirect(url_for('news', id=News.id))

    name = f'{News.name} article'
    return render_template('new_article.html', name=news, article_form=form, news=news)

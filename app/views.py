from flask import render_template
from app import app
from .request import get_news, get_sources


@app.route('/sources')
def sources():
	'''
	View Function that returns the source page and its data
	'''
	# Getting sources according to category
	news_sources = get_sources('sources')

	title = 'Home - Find the latest news highlights'

	return render_template('sources.html', title=title, sources = news_sources)


@app.route('/')
def index():
	'''
	View Function that returns the source page and its data
	'''

	news = get_news()
	'''
	View root page function that returns the index page and its data
	'''
	return render_template('index.html', articles = news)    



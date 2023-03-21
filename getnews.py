from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='API_KEY')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Silicon Valley Bank',
                                          sources='wall-street-journal,new-york-times',
                                          category='business',
                                          language='en',
                                          country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='Sillicon Valley Bank',
                                      sources='wall-street-journal,new-york-times',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2023-02-20',
                                      to='2023-3-10',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()

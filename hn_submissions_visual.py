from operator import itemgetter

import requests

from plotly.graph_objs import bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    # Ensure there is a descendants key
    if 'descendants' not in response_dict:
        response_dict['descendants'] = 0
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                            reverse=True)

news_links, comments, news_titles = [], [], []
for submission_dict in submission_dicts:
    news_title = submission_dict['title']
    short_title = news_title[:20]
    news_url = submission_dict['hn_link']
    news_link = f"<a href='{news_url}'>{short_title}</a>"
    news_links.append(news_link)

    comments.append(submission_dict['comments'])

    news_titles.append(news_title)

# Make vizualization
data = [{
    'type': 'bar',
    'x': news_links,
    'y': comments,
    'hovertext': news_titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]


my_layout = {
    'title': 'Most-Commented Hacker News articles',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hk_news.html')
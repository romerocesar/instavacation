import random
import string

import hug
from hug.middleware import CORSMiddleware
import pandas as pd

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.get('/vacation', api=api)
def vacation():
    posts = get_posts("username")
    results = compute_results(posts)
    return results


def get_posts(username):
    ans = []
    for i in range(100):
        post = generate_random_post()
        ans.append(post)
    return ans


def generate_random_post():
    post = {}
    post['location'] = random.choice(['los angeles', 'toronto',
                                      'seattle', 'san juan islands',
                                      'dubai', 'honolulu'])
    post['likes'] = random.randint(1, 1000)
    post['username'] = random.sample(string.ascii_lowercase, 5)
    return post


def compute_results(posts):
    df = pd.DataFrame(posts)
    grouped = df.groupby('location')['likes'].sum()
    return grouped.to_dict()

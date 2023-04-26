import random
import string

import hug
import pandas as pd


@hug.get()
def vacation_spot():
    posts = get_posts("username")
    results = compute_results(posts)
    response = hug.Response("blah")
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    response.set_header('Access-Control-Allow-Headers', 'Content-Type')
    print("test123")
    return response


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

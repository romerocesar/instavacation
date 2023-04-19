import random

import hug


@hug.get()
def vacation_spot():
    posts = get_posts()
    ans = compute_results(posts)
    results = {
            'toronto': 20,
            'seattle': 30,
            'san juan islands': 40,
            'honolulu': 50,
            'dubai':60
    }
    return results


def get_posts(username):
    ans = []
    for i in range(100):
        post = generate_random_post()
        ans.append(post)
    return ans

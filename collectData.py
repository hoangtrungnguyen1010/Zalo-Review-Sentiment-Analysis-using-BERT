from google_play_scraper import app

import pandas as pd

import numpy as np

from google_play_scraper import Sort, reviews_all

applist = ['com.zing.zalo']


us_reviews = reviews_all(
    applist[0],
    sleep_milliseconds=0, # defaults to 0
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

df = pd.DataFrame(np.array(us_reviews),columns=['review'])
df = df.join(pd.DataFrame(df.pop('review').tolist()))
df.to_csv("Dataset/dataset.csv", index=True)

# for i in range(1, len(applist)):
#     us_reviews = reviews_all(
#     applist[i],
#     sleep_milliseconds=0, # defaults to 0
#     sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
#     )

#     df = pd.DataFrame(np.array(us_reviews),columns=['review'])
#     df = df.join(pd.DataFrame(df.pop('review').tolist()))
#     df.to_csv("Dataset/dataset.csv", mode = 'a', index=False, header = False)

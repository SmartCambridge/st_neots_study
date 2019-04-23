#!/usr/bin/env python

import pandas as pd

import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt

plots = [
    {'year': 2019,
     'zone': 'a428_east'
     },
    {'year': 2019,
     'zone': 'a428_west'
     },
    {'year': 2019,
     'zone': 'a1m_north'
     },
    {'year': 2019,
     'zone': 'a1m_south'
     },
]

fig, axies = plt.subplots(nrows=4, ncols=1, figsize=(7.0, 10.0))
fig.subplots_adjust(hspace=0.4, wspace=0.4)
# fig.tight_layout()

for ctr, plot in enumerate(plots):

    df = pd.read_csv('transits-{}-{}.csv'.format(plot['zone'], plot['year']), delimiter=',')
    df['Date'] = pd.to_datetime(df['Date'])
    df.index = df['Date']
    del df['Date']

    df.boxplot(
        by=df.index.dayofyear,
        column=['Duration'],
        grid=False,
        whis='range',
        ax=axies[ctr])

fig.suptitle('Transit times')

plt.savefig('day_of_year')

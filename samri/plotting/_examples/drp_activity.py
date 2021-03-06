#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import samri.plotting.maps as maps
from behaviopy.plotting import qualitative_times
from os import path

data_dir = path.join(path.dirname(path.realpath(__file__)),"../../../example_data/ioanas2018")
data_path = path.join(data_dir,'DSURQEc_drp.csv')
df = pd.read_csv(data_path)

df = df.rename(columns={'t':'Mean t-Statistic'})

# definitions for the axes
left, width = 0.06, 0.9
bottom, height = 0.06, 0.9

session_coordinates = [left, bottom, width, height]
roi_coordinates = [left+0.02, bottom+0.7, 0.3, 0.2]

fig = plt.figure(1)

ax1 = plt.axes(session_coordinates)
qualitative_times(df,
        ax=ax1,
        x='Session',
        y='Mean t-Statistic',
        condition='treatment',
        unit='subject',
        ci=90,
        palette=["#56B4E9", "#E69F00"],
        order=['nave','acute','chronic (2w)','chronic (4w)','post'],
        bp_style=False,
        renames={
                'Session':{
                        'ofM':'nave',
                        'ofMaF':'acute',
                        'ofMcF1':'chronic (2w)',
                        'ofMcF2':'chronic (4w)',
                        'ofMpF':'post',
                        },
                },
        )

ax2 = plt.axes(roi_coordinates)
maps.atlas_label("~/ni_data/templates/roi/DSURQEc_drp.nii.gz",
        scale=0.3,
        color="#E69F00",
        ax=ax2,
        annotate=False,
        alpha=0.8,
        )

save_as(drp_activity.py)

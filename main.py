import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("out.csv", index_col="date")

df.fillna(0.0, inplace=True)

bcr.bar_chart_race(

    df=df.loc[:, :],

    filename="Azab.mp4",

    n_bars=10,

    fig_kwargs=
        {
            'figsize': (30, 20),
            #'figsize': (20, 11),
            'dpi': 60,
            'facecolor': '#F8FAFF'
        },
    fixed_max=True,
    steps_per_period=30,
    period_length=400,

     colors=['#001219','#005f73','#0a9396','#94d2bd','#e9d8a6','#ee9b00','#ca6702','#bb3e03','#ae2012','#9b2226'],

    title={
            'label': 'covid19 confirmed (global)',
            'size': 28,
            'color': '#000000',
            'weight': 'bold',
            'pad': 12
        },
    period_label={
            'x': .95,
            'y': .15,
            'ha': 'right',
            'va': 'center',
            'size': 28,
            'weight':'bold',
        },
    # style the bar label text
    bar_label_font={'size': 18, 'weight': 'bold',},

    # style the labels in x and y axis
    tick_label_font={'size': 18, 'weight': 'bold',},

    bar_kwargs={'alpha': .99, 'lw': 0},

    period_template='{x:.0f}',

    bar_size=.4,

    filter_column_colors = True,

)
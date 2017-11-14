import pandas as pd
import numpy as np
import plotly as py


def format_string(sal):
    sal = sal.replace("$", "")
    sal = (sal.split(","))
    sal = "".join(sal)
    return sal

py.offline.init_notebook_mode()

# Reading "Regions" and "Starting Median Salary" in CSV file
# ?? : Why do we need to use usecols and names ??
df = pd.read_csv("salaries-by-region.csv", names=["Region", "Starting Median Salary"], usecols=[1, 2],
                 thousands=',')

# Get data frames for different regions
cali_df = df[df["Region"] == "California"]
west_df = df[df["Region"] == "Western"]
midwest_df = df[df["Region"] == "Midwestern"]
south_df = df[df["Region"] == "Southern"]
north_df = df[df["Region"] == "Northeastern"]

cali_sal = cali_df["Starting Median Salary"].tolist()
west_sal = west_df["Starting Median Salary"].tolist()
midwest_sal = midwest_df["Starting Median Salary"].tolist()
south_sal = south_df["Starting Median Salary"].tolist()
north_sal = north_df["Starting Median Salary"].tolist()

i = 0
for i in range(0, len(cali_sal), 1):
    cali_sal[i] = format_string(cali_sal[i])

for i in range(0, len(west_sal), 1):
    west_sal[i] = format_string(west_sal[i])

for i in range(0, len(midwest_sal), 1):
    midwest_sal[i] = format_string(midwest_sal[i])

for i in range(0, len(south_sal), 1):
    south_sal[i] = format_string(south_sal[i])

for i in range(0, len(north_sal), 1):
    north_sal[i] = format_string(north_sal[i])

cali_sal = np.asfarray(cali_sal, float)
west_sal = np.asfarray(west_sal, float)
midwest_sal = np.asfarray(midwest_sal, float)
south_sal = np.asfarray(south_sal, float)
north_sal = np.asfarray(north_sal, float)

cali_avg_sal = np.mean(cali_sal)
west_avg_sal = np.mean(west_sal)
midwest_avg_sal = np.mean(midwest_sal)
south_avg_sal = np.mean(south_sal)
north_avg_sal = np.mean(north_sal)

'''
print cali_sal, cali_avg_sal
print
print west_sal, west_avg_sal
print
print midwest_sal, midwest_avg_sal
print
print south_sal, south_avg_sal
print
print north_sal, north_avg_sal
'''

locations = ['California', 'Midwestern', 'Western', 'Southern', 'Northeastern']
costs = [cali_avg_sal, midwest_avg_sal, west_avg_sal, south_avg_sal, north_avg_sal]

data = [dict(
        type='choropleth',
        locations=locations,
        z=costs,
        locationmode='USA-states',
        text=df['text'],
        marker=dict(
            line=dict(
                color='rgb(255,255,255)',
                width=2
            )),
        colorbar=dict(
            title="Millions USD")
        )]

layout = dict(
        title='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
        geo=dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'),
        )

fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename='d3-cloropleth-map')

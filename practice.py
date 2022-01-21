import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import plotly as py
import plotly

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv' # Read in your data
df_sample = pd.read_csv(url,sep=",")
States = ["North Carolina"]
df_sample_r = df_sample[df_sample['state'].isin(States)] # Read in state names
values = df_sample_r["cases"]# Read in the values contained within your file
fips = df_sample_r["fips"] # Read in FIPS Codes

colorscale = ["#171c42","#223f78","#1267b2","#4590c4","#8cb5c9","#b6bed5","#dab2be",
              "#d79d8b","#c46852","#a63329","#701b20","#3c0911"] # Create a colorscale

# For colorscale help: https://react-colorscales.getforge.io/

endpts = list(np.linspace(-75, 75, len(colorscale) - 1)) # Identify a suitable range for your data

fig = ff.create_choropleth(
    fips=fips, values=values, colorscale=colorscale, show_state_data=True,
    scope=States, # Define your scope
    binning_endpoints=endpts, # If your values is a list of numbers, you can bin your values into half-open intervals
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    legend_title='# of cases', title='Number of Covid19 cases per county in North Carolina'
)
py.show()

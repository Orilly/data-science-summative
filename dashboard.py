from shiny import App, ui, render # import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import seaborn as sns
import os

## load, collate and clean data

files = os.listdir("data/")
merged = None
for filename in files:
    _df = pd.read_csv("data/"+filename)
    if merged is None:
        merged = _df
    else:
        merged = pd.merge(merged, _df, on=["Country", "Year", "Code", "ContinentCode"], how="outer")

rename_dict = {"Happiness Index 0 (unhappy) - 10 (happy)": "happiness",
               "Gross Domestic Product billions of U.S. dollars": "GDP",
                "GDP per capita current U.S. dollars": "GDP_per_capita",
                "GDP per capita Purchasing Power Parity": "GDPPPP",
                "Human Development Index (0 - 1)": "HDI",
                "Percent urban population": "Percent_urban_population",
                "Value added in the services sector as percent of GDP": "Services_value_added_GDP"}

df = merged[(merged["Year"] >= 2015) & (merged["Year"] <= 2024)]
df = df.rename(rename_dict, axis=1)
econ_indicators = ["GDP", "GDPPPP", "GDP_per_capita", "Percent_urban_population", "Services_value_added_GDP", "HDI"]
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

## set up shiny app GUI

gui = ui.page_sidebar(
    ui.sidebar(ui.h4("Variables"),
               ui.input_select("indicator", "Economic indicator", choices=econ_indicators, selected="HDI"),
               ui.input_select("year", "Year", choices=years, selected=2018)),

    ui.card(ui.h4("Graph"),
            ui.output_plot("plot_data"),
            style="margin:8px; padding:10px;"),

    ui.card(ui.h4("Descriptive and inferential statistics"),
            ui.output_text("R2"),
            ui.output_text("pvalue"),
            style="margin:8px; padding:10px;"),   

    title="Economic indicators predicting happiness (linear regression)"
)

## set up shiny app server

def server(input, output, session):
    @output
    @render.text
    def R2():
        data = df[df["Year"] == int(input.year())]
        model = smf.ols(f'happiness ~ {input.indicator()}', data=data).fit()
        return f"R-squared: {model.rsquared.round(3)}"

    @output
    @render.text
    def pvalue():
        data = df[df["Year"] == int(input.year())]
        model = smf.ols(f'happiness ~ {input.indicator()}', data=data).fit()
        return f"P-value: {model.pvalues[input.indicator()].round(4)}"

    @output
    @render.plot
    def plot_data():
        data = df[df["Year"] == int(input.year())]
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.regplot(x=input.indicator(), y="happiness", data=data)
        return fig

## run app

app = App(gui, server)
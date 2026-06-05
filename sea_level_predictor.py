import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Ler os dados
    df = pd.read_csv("epa-sea-level.csv")

    # Criar gráfico de dispersão
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Primeira linha de regressão (todos os dados)
    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_extended = np.arange(
        df["Year"].min(),
        2051
    )

    ax.plot(
        years_extended,
        result.intercept +
        result.slope * years_extended,
        "r",
        label="Fit: 1880-2050"
    )

    # Segunda linha de regressão (2000 em diante)
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = np.arange(
        2000,
        2051
    )

    ax.plot(
        years_recent,
        result_recent.intercept +
        result_recent.slope * years_recent,
        "g",
        label="Fit: 2000-2050"
    )

    # Títulos e rótulos
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    ax.legend()

    # Salvar figura
    fig.savefig("sea_level_plot.png")

    return fig
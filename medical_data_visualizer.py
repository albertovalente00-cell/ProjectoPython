import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importar dados
df = pd.read_csv("medical_examination.csv")

# Adicionar coluna overweight
df["overweight"] = (
    df["weight"] / ((df["height"] / 100) ** 2) > 25
).astype(int)

# Normalizar colesterol e glicose
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


def draw_cat_plot():
    # Criar DataFrame para gráfico categórico
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight",
        ],
    )

    # Agrupar e contar
    df_cat = (
        df_cat.groupby(
            ["cardio", "variable", "value"]
        )
        .size()
        .reset_index(name="total")
    )

    # Criar gráfico
    g = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    )

    fig = g.fig

    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # Limpar dados
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (
            df["height"]
            >= df["height"].quantile(0.025)
        )
        & (
            df["height"]
            <= df["height"].quantile(0.975)
        )
        & (
            df["weight"]
            >= df["weight"].quantile(0.025)
        )
        & (
            df["weight"]
            <= df["weight"].quantile(0.975)
        )
    ]

    # Correlação
    corr = df_heat.corr()

    # Máscara
    mask = np.triu(
        np.ones_like(corr, dtype=bool)
    )

    # Figura
    fig, ax = plt.subplots(
        figsize=(12, 10)
    )

    # Heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    fig.savefig("heatmap.png")
    return fig
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar dados
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    index_col="date",
    parse_dates=True
)

# Limpar dados (remover 2,5% superiores e inferiores)
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Criar cópia dos dados
    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(
        df_line.index,
        df_line["value"],
        color="red"
    )

    ax.set_title(
        "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Criar cópia
    df_bar = df.copy()

    # Adicionar ano e mês
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    # Ordem correta dos meses
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    df_bar["month"] = pd.Categorical(
        df_bar["month"],
        categories=months,
        ordered=True
    )

    # Média por ano e mês
    df_bar = (
        df_bar.groupby(["year", "month"])["value"]
        .mean()
        .unstack()
    )

    fig = df_bar.plot(
        kind="bar",
        figsize=(12, 8)
    ).figure

    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")

    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Preparar dados
    df_box = df.copy()
    df_box.reset_index(inplace=True)

    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month

    # Ordenar meses
    df_box = df_box.sort_values("month_num")

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(20, 8)
    )

    # Box plot por ano
    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title(
        "Year-wise Box Plot (Trend)"
    )
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Box plot por mês
    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        order=[
            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug",
            "Sep", "Oct", "Nov", "Dec"
        ],
        ax=axes[1]
    )

    axes[1].set_title(
        "Month-wise Box Plot (Seasonality)"
    )
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
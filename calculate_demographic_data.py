import pandas as pd
import os


def calculate_demographic_data(print_data=True):

    # Caminho do arquivo CSV
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "adult.data.csv")

    # Nomes das colunas do dataset
    columns = [
        'age', 'workclass', 'fnlwgt', 'education',
        'education-num', 'marital-status', 'occupation',
        'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss',
        'hours-per-week', 'native-country', 'salary'
    ]

    # Ler o arquivo
    df = pd.read_csv(
        csv_file,
        names=columns,
        skipinitialspace=True
    )

    # Quantidade de pessoas por raça
    race_count = df['race'].value_counts()

    # Idade média dos homens
    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(),
        1
    )

    # Percentagem com Bacharelado
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100,
        1
    )

    # Educação avançada
    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    # Percentagem com educação avançada e salário >50K
    higher_education_rich = round(
        (
            df[higher_education]['salary'] == '>50K'
        ).mean() * 100,
        1
    )

    # Percentagem sem educação avançada e salário >50K
    lower_education_rich = round(
        (
            df[~higher_education]['salary'] == '>50K'
        ).mean() * 100,
        1
    )

    # Mínimo de horas trabalhadas
    min_work_hours = df['hours-per-week'].min()

    # Pessoas que trabalham o mínimo
    min_workers = df[
        df['hours-per-week'] == min_work_hours
    ]

    # Percentagem que ganha >50K
    rich_percentage = round(
        (
            min_workers['salary'] == '>50K'
        ).mean() * 100,
        1
    )

    # País com maior percentagem de >50K
    country_percentages = (
        df[df['salary'] == '>50K']['native-country']
        .value_counts()
        / df['native-country'].value_counts()
        * 100
    )

    highest_earning_country = country_percentages.idxmax()

    highest_earning_country_percentage = round(
        country_percentages.max(),
        1
    )

    # Ocupação mais popular na Índia
    top_IN_occupation = (
        df[
            (df['native-country'] == 'India')
            & (df['salary'] == '>50K')
        ]['occupation']
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print(
            "Percentage with Bachelors degrees:",
            percentage_bachelors
        )
        print(
            "Higher education rich:",
            higher_education_rich
        )
        print(
            "Lower education rich:",
            lower_education_rich
        )
        print(
            "Min work hours:",
            min_work_hours
        )
        print(
            "Rich percentage:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )
        print(
            "Top occupations in India:",
            top_IN_occupation
        )

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__ == "__main__":
    calculate_demographic_data()
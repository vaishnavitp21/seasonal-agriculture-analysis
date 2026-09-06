from scipy import stats


def seasonal_profit_kruskal_test(df):
    groups = [
        group["Profit_per_Hectare_INR"].values
        for _, group in df.groupby("Season")
    ]

    statistic, p_value = stats.kruskal(*groups)

    return statistic, p_value
def pairwise_season_tests(df):
    seasons = sorted(df["Season"].unique())

    results = []

    for i in range(len(seasons)):
        for j in range(i + 1, len(seasons)):

            season_a = seasons[i]
            season_b = seasons[j]

            values_a = df.loc[
                df["Season"] == season_a,
                "Profit_per_Hectare_INR"
            ]

            values_b = df.loc[
                df["Season"] == season_b,
                "Profit_per_Hectare_INR"
            ]

            statistic, p_value = stats.mannwhitneyu(
                values_a,
                values_b,
                alternative="two-sided"
            )

            results.append({
                "Season A": season_a,
                "Season B": season_b,
                "U Statistic": statistic,
                "p-value": p_value,
                "Significant_at_5pct": p_value < 0.05
            })

    return results


def spearman_correlations(df, columns):
    """
    Calculate Spearman correlation matrix.
    """

    return df[columns].corr(method="spearman")
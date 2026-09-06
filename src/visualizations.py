import matplotlib.pyplot as plt
import seaborn as sns
def seasonal_profit_plot(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x="Season",
        y="Profit_per_Hectare_INR",
        estimator="mean",
        errorbar=None)
    plt.axhline(
        y=0,
        linestyle="--",
        linewidth=1)
    plt.title(
        "Average Profit per Hectare Across Seasons"
    )
    plt.xlabel("Season")
    plt.ylabel("Profit per Hectare (INR)")
    plt.tight_layout()
    plt.show()
def seasonal_water_efficiency_plot(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x="Season",
        y="Water_Efficiency_t_per_1000m3",
        estimator="mean",
        errorbar=None
    )
    plt.title(
        "Average Water Efficiency Across Seasons"
    )
    plt.xlabel("Season")
    plt.ylabel("Water Efficiency")
    plt.tight_layout()
    plt.show()


def crop_profit_plot(crop_summary):
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=crop_summary.reset_index(),
        x="Crop",
        y="Average_Profit_per_Hectare_INR"
    )
    plt.axhline(
        y=0,
        linestyle="--",
        linewidth=1
    )
    plt.xticks(rotation=45)
    plt.title(
        "Average Profit per Hectare by Crop"
    )
    plt.xlabel("Crop")
    plt.ylabel("Profit per Hectare (INR)")
    plt.tight_layout()
    plt.show()


def crop_season_heatmap(crop_season_data):
    """
    Plot crop-season profitability heatmap.
    """

    plt.figure(figsize=(10, 6))

    sns.heatmap(
        crop_season_data,
        annot=True,
        fmt=".0f",
        center=0
    )

    plt.title(
        "Average Profit per Hectare by Crop and Season"
    )
    plt.xlabel("Season")
    plt.ylabel("Crop")

    plt.tight_layout()
    plt.show()


def correlation_heatmap(correlation_matrix):
    """
    Plot correlation matrix.
    """

    plt.figure(figsize=(14, 11))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        fmt=".2f",
        center=0
    )

    plt.title("Spearman Correlation Matrix")

    plt.tight_layout()
    plt.show()
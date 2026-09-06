import pandas as pd


def seasonal_summary(df):
    """
    Calculate agricultural performance metrics by season.
    """

    return df.groupby("Season").agg(
        Number_of_Farms=("Farm_ID", "count"),
        Average_Yield_Tonnes_Ha=(
            "Yield_Tonnes_Ha",
            "mean"
        ),
        Average_Profit_INR=(
            "Profit_INR",
            "mean"
        ),
        Average_Profit_per_Hectare_INR=(
            "Profit_per_Hectare_INR",
            "mean"
        ),
        Average_Water_Used_m3=(
            "Water_Used_m3",
            "mean"
        ),
        Average_Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        ),
        Average_Disease_Risk_pct=(
            "Disease_Pest_Risk_pct",
            "mean"
        )
    ).round(2)


def crop_summary(df):
    """
    Calculate crop-wise agricultural performance.
    """

    return df.groupby("Crop").agg(
        Number_of_Farms=("Farm_ID", "count"),
        Average_Yield_Tonnes_Ha=(
            "Yield_Tonnes_Ha",
            "mean"
        ),
        Average_Profit_per_Hectare_INR=(
            "Profit_per_Hectare_INR",
            "mean"
        ),
        Average_Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        ),
        Average_Disease_Risk_pct=(
            "Disease_Pest_Risk_pct",
            "mean"
        )
    ).sort_values(
        "Average_Profit_per_Hectare_INR",
        ascending=False
    ).round(2)


def irrigation_summary(df):
    """
    Calculate performance by irrigation method.
    """

    return df.groupby("Irrigation_Method").agg(
        Number_of_Farms=("Farm_ID", "count"),
        Average_Yield_Tonnes_Ha=(
            "Yield_Tonnes_Ha",
            "mean"
        ),
        Average_Profit_per_Hectare_INR=(
            "Profit_per_Hectare_INR",
            "mean"
        ),
        Average_Water_Used_m3=(
            "Water_Used_m3",
            "mean"
        ),
        Average_Water_Efficiency=(
            "Water_Efficiency_t_per_1000m3",
            "mean"
        )
    ).sort_values(
        "Average_Profit_per_Hectare_INR",
        ascending=False
    ).round(2)


def crop_season_profit(df):
    """
    Calculate average profit per hectare for
    each crop-season combination.
    """

    return df.pivot_table(
        values="Profit_per_Hectare_INR",
        index="Crop",
        columns="Season",
        aggfunc="mean"
    )


def economic_comparison(df):
    """
    Compare revenue, cost and profit across seasons.
    """

    return df.groupby("Season").agg(
        Average_Revenue=(
            "Revenue_INR",
            "mean"
        ),
        Average_Total_Cost=(
            "Total_Cost_INR",
            "mean"
        ),
        Average_Profit=(
            "Profit_INR",
            "mean"
        ),
        Average_Revenue_per_Hectare=(
            "Revenue_per_Hectare_INR",
            "mean"
        ),
        Average_Cost_per_Hectare=(
            "Cost_per_Hectare_INR",
            "mean"
        ),
        Average_Profit_per_Hectare=(
            "Profit_per_Hectare_INR",
            "mean"
        )
    ).round(2)
import pandas as pd
import numpy as np
def check_missing_values(df):
    missing = df.isnull().sum()

    summary = pd.DataFrame({
        "Missing Values": missing,
        "Percentage": (missing / len(df)) * 100
    })

    return summary[summary["Missing Values"] > 0].sort_values(
        "Missing Values",
        ascending=False
    )
def check_duplicates(df):
    return df.duplicated().sum()
def validate_numeric_values(df):
    checks = {
        "Negative farm area": (df["Farm_Area_Hectares"] <= 0).sum(),
        "Negative rainfall": (df["Rainfall_mm"] < 0).sum(),
        "Negative yield": (df["Yield_Tonnes_Ha"] < 0).sum(),
        "Negative production": (df["Production_Tonnes"] < 0).sum(),
        "Negative water usage": (df["Water_Used_m3"] < 0).sum(),
        "Invalid soil pH": (
            (df["Soil_pH"] < 0) |
            (df["Soil_pH"] > 14)
        ).sum()
    }
    return pd.DataFrame(
        checks.items(),
        columns=["Validation Check", "Count"]
    )


def fill_missing_values(df, columns):
    """
    Fill missing numerical values using the median.
    """

    df = df.copy()

    for column in columns:
        df[column] = df[column].fillna(
            df[column].median()
        )

    return df


def create_performance_metrics(df):
    """
    Create normalized economic performance metrics.
    """

    df = df.copy()

    df["Profit_per_Hectare_INR"] = (
        df["Profit_INR"] /
        df["Farm_Area_Hectares"]
    )

    df["Revenue_per_Hectare_INR"] = (
        df["Revenue_INR"] /
        df["Farm_Area_Hectares"]
    )

    df["Cost_per_Hectare_INR"] = (
        df["Total_Cost_INR"] /
        df["Farm_Area_Hectares"]
    )

    df["Profit_Margin_pct"] = (
        df["Profit_INR"] /
        df["Revenue_INR"]
    ) * 100

    return df
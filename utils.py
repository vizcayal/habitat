import pandas as pd
import numpy as np

def adf_test(timeseries, series_name=""):
    from statsmodels.tsa.stattools import adfuller
    """
    Performs the Augmented Dickey-Fuller test for stationarity.

    Null Hypothesis (H0): The time series has a unit root (it is non-stationary).
    Alternative Hypothesis (H1): The time series does not have a unit root (it is stationary).

    Args:
        timeseries (pd.Series): The time series data to test.
        series_name (str): Optional name of the series for printing.
    """
    print(f"\nResults of Dickey-Fuller Test for {series_name if series_name else 'the series'}:")
    # The adfuller function returns:
    # adf_statistic, p_value, num_lags_used, num_observations, critical_values, icbest
    dftest = adfuller(timeseries.dropna(), autolag='AIC') # dropna() to handle NaNs from differencing
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput[f'Critical Value ({key})'] = value

    print(dfoutput)

    if dftest[1] <= 0.05: # if p-value <= 0.05
        print("Conclusion: Reject the null hypothesis (H0). Data is likely stationary.")
        return True
    else:
        print("Conclusion: Fail to reject the null hypothesis (H0). Data is likely non-stationary.")
        return False
# Space-Weather-Timeseries-Forecasting-using-OLS-GBRT-and-LSTM
# Installation
Install the packages from `requirements.txt` file using `pip`. 
```
pip install -r requirements.txt
```
# Data
This folder contains the time series data file that was used in this project and it is named data.csv. This data contains the recorded space weather dataset that was recorded for one year. 
There are multiple columns in the data.csv file. 

The target column in this project was the data in the foF2o and in the foF2m columns which represent the observed and the modeled plasma density in the weather respectively.  

Multivariate analysis: The target and all other covariates including SSN, Kp, Dst, and TEC are used for forecasting. 

 

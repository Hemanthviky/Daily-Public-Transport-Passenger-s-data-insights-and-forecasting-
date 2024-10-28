# Passenger Journey Forecasting

## Overview
This project analyzes daily public transport passenger journeys by service type, focusing on understanding patterns and trends over time. The analysis is based on a dataset containing passenger counts categorized by service types, such as Local Route, Light Rail, Peak Service, Rapid Route, and School.

## Data Preparation
- The dataset was loaded, and the 'Date' column was converted to datetime format, enabling time series analysis.
- Missing values in the 'Other' service type were filled with the median value.
- Data was aggregated daily to handle duplicate dates.

## Insights Gained
1. **Overall Passenger Distribution**
   - The total number of passengers for each service type was visualized. The Rapid Route service had the highest passenger count, indicating it is the most popular service type. This insight can help allocate resources more effectively.

2. **Descriptive Statistics**
   - Key statistics (mean, minimum, maximum) were provided for each service type, revealing usage patterns and variability in daily passenger counts.

3. **Trend Analysis**
   - Passenger trends over time for each service type were analyzed. Visualizations showed distinct trends, helping to understand seasonal patterns or changes in ridership.

4. **Correlation Between Service Types**
   - A correlation matrix illustrated relationships between different service types. High correlations suggest that certain services may serve overlapping commuter needs.

5. **Outlier Detection**
   - Outliers were identified based on passenger counts exceeding three standard deviations from the mean. These outliers may indicate unusual events affecting service usage.

## Forecasting Model
To predict future passenger journeys, a SARIMA (Seasonal Autoregressive Integrated Moving Average) model was employed.

### Model Explanation
- SARIMA is a popular time series forecasting method that accounts for seasonality and trends in the data. It combines autoregressive and moving average components with differencing to achieve stationarity in the time series.

### Model Parameters
- **Order (p, d, q):**
  - `p`: The number of lag observations (autoregressive part).
  - `d`: The number of times that the raw observations are differenced (to make the series stationary).
  - `q`: The size of the moving average window (moving average part).
  
- **Seasonal Order (P, D, Q, s):**
  - `P`: The number of seasonal autoregressive terms.
  - `D`: The number of seasonal differences.
  - `Q`: The number of seasonal moving average terms.
  - `s`: The length of the seasonal cycle (in this case, 7 days for weekly seasonality).

## Forecasting Process
1. The dataset was split into training (all but the last 7 days) and testing (the last 7 days) sets.
2. The SARIMA model was fitted on the training data.
3. A forecast was generated for the next 7 days.
4. The performance of the model was evaluated using Root Mean Square Error (RMSE), providing insight into the accuracy of the forecast.

## Conclusion
This project successfully analyzed daily public transport passenger journeys, uncovering valuable insights and forecasting future trends using the SARIMA model. The findings can help in resource allocation, understanding passenger behavior, and improving service efficiency.

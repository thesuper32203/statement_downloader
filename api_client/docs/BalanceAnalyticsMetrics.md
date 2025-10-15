# BalanceAnalyticsMetrics

Balance analytics metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_balance** | **float** | Available Balance | [optional] 
**available_balance_date** | **str** | Available Balance date | [optional] 
**average_daily_balance_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average daily ending balance each month over the report time period | [optional] 
**average_daily_balance_for_the_report_time_period** | **float** | Average Daily Balance | [optional] 
**average_weekday_balance_for_the_report_time_period** | **float** | Average Weekday Balance | [optional] 
**count_daily_negative_balances_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndCount]**](ObbDateRangeAndCount.md) | Number of negative daily ending balances each month over the report time period | [optional] 
**current_running_balance** | **float** | Current Running Balance Date | [optional] 
**current_running_balance_date** | **str** | Current Running Balance date | [optional] 
**daily_balances_by_weekday_for_the_report_time_period** | [**List[ObbDailyBalance]**](ObbDailyBalance.md) | Daily balance of the account during weekdays over the length of the report | [optional] [default to []]
**daily_balances_for_the_report_time_period** | [**List[ObbDailyBalance]**](ObbDailyBalance.md) | Daily balance of the account over the length of the report | [optional] [default to []]
**historic_number_of_weeks_average_balance_increasing** | [**ObbNumWeeksAverageBalanceIncreasing**](ObbNumWeeksAverageBalanceIncreasing.md) |  | [optional] 
**maximum_daily_balance_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Maximum daily ending balance each month over the report time period | [optional] 
**maximum_running_balance_for_the_report_time_period** | **float** | Maximum Running Balance | [optional] 
**minimum_daily_balance_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Minimum daily ending balance each month over the report time period | [optional] 
**minimum_running_balance_for_the_report_time_period** | **float** | Minimum Running Balance | [optional] 

## Example

```python
from openapi_client.models.balance_analytics_metrics import BalanceAnalyticsMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAnalyticsMetrics from a JSON string
balance_analytics_metrics_instance = BalanceAnalyticsMetrics.from_json(json)
# print the JSON string representation of the object
print(BalanceAnalyticsMetrics.to_json())

# convert the object into a dict
balance_analytics_metrics_dict = balance_analytics_metrics_instance.to_dict()
# create an instance of BalanceAnalyticsMetrics from a dict
balance_analytics_metrics_from_dict = BalanceAnalyticsMetrics.from_dict(balance_analytics_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



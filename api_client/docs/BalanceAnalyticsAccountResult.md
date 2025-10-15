# BalanceAnalyticsAccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_details** | [**ObbAccountDetails**](ObbAccountDetails.md) |  | 
**account_id** | **int** | An account ID represented as a number | 
**balance_analytics_metrics** | [**BalanceAnalyticsMetrics**](BalanceAnalyticsMetrics.md) |  | [optional] 
**current_report_request** | [**ObbCurrentReportRequestDetails**](ObbCurrentReportRequestDetails.md) |  | 
**historic_data_availability** | [**ObbDataAvailability**](ObbDataAvailability.md) |  | 

## Example

```python
from openapi_client.models.balance_analytics_account_result import BalanceAnalyticsAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAnalyticsAccountResult from a JSON string
balance_analytics_account_result_instance = BalanceAnalyticsAccountResult.from_json(json)
# print the JSON string representation of the object
print(BalanceAnalyticsAccountResult.to_json())

# convert the object into a dict
balance_analytics_account_result_dict = balance_analytics_account_result_instance.to_dict()
# create an instance of BalanceAnalyticsAccountResult from a dict
balance_analytics_account_result_from_dict = BalanceAnalyticsAccountResult.from_dict(balance_analytics_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



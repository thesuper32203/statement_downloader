# CashFlowAnalyticsAccountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_details** | [**ObbAccountDetails**](ObbAccountDetails.md) |  | 
**account_id** | **int** | An account ID represented as a number | 
**cashflow_analytics_metrics** | [**CashFlowAnalyticsMetrics**](CashFlowAnalyticsMetrics.md) |  | [optional] 
**current_report_request** | [**ObbCurrentReportRequestDetails**](ObbCurrentReportRequestDetails.md) |  | 
**historic_data_availability** | [**ObbDataAvailability**](ObbDataAvailability.md) |  | 

## Example

```python
from openapi_client.models.cash_flow_analytics_account_result import CashFlowAnalyticsAccountResult

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowAnalyticsAccountResult from a JSON string
cash_flow_analytics_account_result_instance = CashFlowAnalyticsAccountResult.from_json(json)
# print the JSON string representation of the object
print(CashFlowAnalyticsAccountResult.to_json())

# convert the object into a dict
cash_flow_analytics_account_result_dict = cash_flow_analytics_account_result_instance.to_dict()
# create an instance of CashFlowAnalyticsAccountResult from a dict
cash_flow_analytics_account_result_from_dict = CashFlowAnalyticsAccountResult.from_dict(cash_flow_analytics_account_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BalanceAnalyticsBusinessSummary

Balance analytics summarized across all accounts in the report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_analytics_metrics** | [**BalanceAnalyticsMetrics**](BalanceAnalyticsMetrics.md) |  | [optional] 
**current_report_request** | [**ObbCurrentReportRequestDetails**](ObbCurrentReportRequestDetails.md) |  | [optional] 
**historic_data_availability** | [**ObbDataAvailability**](ObbDataAvailability.md) |  | [optional] 

## Example

```python
from openapi_client.models.balance_analytics_business_summary import BalanceAnalyticsBusinessSummary

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAnalyticsBusinessSummary from a JSON string
balance_analytics_business_summary_instance = BalanceAnalyticsBusinessSummary.from_json(json)
# print the JSON string representation of the object
print(BalanceAnalyticsBusinessSummary.to_json())

# convert the object into a dict
balance_analytics_business_summary_dict = balance_analytics_business_summary_instance.to_dict()
# create an instance of BalanceAnalyticsBusinessSummary from a dict
balance_analytics_business_summary_from_dict = BalanceAnalyticsBusinessSummary.from_dict(balance_analytics_business_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



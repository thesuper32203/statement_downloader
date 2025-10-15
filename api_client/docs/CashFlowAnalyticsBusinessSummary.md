# CashFlowAnalyticsBusinessSummary

Cash flow analytics summarized across all accounts in the report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cashflow_analytics_metrics** | [**CashFlowAnalyticsMetrics**](CashFlowAnalyticsMetrics.md) |  | [optional] 
**current_report_request** | [**ObbCurrentReportRequestDetails**](ObbCurrentReportRequestDetails.md) |  | 
**historic_data_availability** | [**ObbDataAvailability**](ObbDataAvailability.md) |  | 

## Example

```python
from openapi_client.models.cash_flow_analytics_business_summary import CashFlowAnalyticsBusinessSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowAnalyticsBusinessSummary from a JSON string
cash_flow_analytics_business_summary_instance = CashFlowAnalyticsBusinessSummary.from_json(json)
# print the JSON string representation of the object
print(CashFlowAnalyticsBusinessSummary.to_json())

# convert the object into a dict
cash_flow_analytics_business_summary_dict = cash_flow_analytics_business_summary_instance.to_dict()
# create an instance of CashFlowAnalyticsBusinessSummary from a dict
cash_flow_analytics_business_summary_from_dict = CashFlowAnalyticsBusinessSummary.from_dict(cash_flow_analytics_business_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



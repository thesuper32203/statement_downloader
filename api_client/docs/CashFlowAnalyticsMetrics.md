# CashFlowAnalyticsMetrics

Cash flow analytics metrics and calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflow** | [**CashFlowInflowAttributes**](CashFlowInflowAttributes.md) |  | [optional] 
**negative_triggers** | [**CashFlowNegativeTriggers**](CashFlowNegativeTriggers.md) |  | [optional] 
**outflow** | [**CashFlowOutflowAttributes**](CashFlowOutflowAttributes.md) |  | [optional] 
**revenue_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Sum of all transactions categorized as revenue, split by months | [optional] 
**revenue_for_the_report_time_period** | **float** | Sum of all transactions categorized as revenue | [optional] 
**transaction_analytics** | [**CashFlowTransactionAnalyticsAttributes**](CashFlowTransactionAnalyticsAttributes.md) |  | [optional] 

## Example

```python
from openapi_client.models.cash_flow_analytics_metrics import CashFlowAnalyticsMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowAnalyticsMetrics from a JSON string
cash_flow_analytics_metrics_instance = CashFlowAnalyticsMetrics.from_json(json)
# print the JSON string representation of the object
print(CashFlowAnalyticsMetrics.to_json())

# convert the object into a dict
cash_flow_analytics_metrics_dict = cash_flow_analytics_metrics_instance.to_dict()
# create an instance of CashFlowAnalyticsMetrics from a dict
cash_flow_analytics_metrics_from_dict = CashFlowAnalyticsMetrics.from_dict(cash_flow_analytics_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



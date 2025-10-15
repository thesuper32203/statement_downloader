# BalanceAndCashFlowAnalyticsReportConstraints

Request parameters from the partner to control the customer accounts included in the report, and the length of time to report on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **List[int]** | The list of account IDs to include in the report. If omitted, all accounts on record for the customer will be used. | [optional] 
**length_of_report** | **int** | Number of days to search for transactions. Must be one of 30, 90, 180, 270, 365, or 730. If omitted, defaults to 2 years from current time at which the request was received (730 days). | [optional] 

## Example

```python
from openapi_client.models.balance_and_cash_flow_analytics_report_constraints import BalanceAndCashFlowAnalyticsReportConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAndCashFlowAnalyticsReportConstraints from a JSON string
balance_and_cash_flow_analytics_report_constraints_instance = BalanceAndCashFlowAnalyticsReportConstraints.from_json(json)
# print the JSON string representation of the object
print(BalanceAndCashFlowAnalyticsReportConstraints.to_json())

# convert the object into a dict
balance_and_cash_flow_analytics_report_constraints_dict = balance_and_cash_flow_analytics_report_constraints_instance.to_dict()
# create an instance of BalanceAndCashFlowAnalyticsReportConstraints from a dict
balance_and_cash_flow_analytics_report_constraints_from_dict = BalanceAndCashFlowAnalyticsReportConstraints.from_dict(balance_and_cash_flow_analytics_report_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



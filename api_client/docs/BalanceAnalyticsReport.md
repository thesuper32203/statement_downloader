# BalanceAnalyticsReport

Balance analytics report data as JSON

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_results** | [**List[BalanceAnalyticsAccountResult]**](BalanceAnalyticsAccountResult.md) | Balance results per account | [optional] 
**business_id** | **int** | Business ID | [optional] 
**business_summary** | [**BalanceAnalyticsBusinessSummary**](BalanceAnalyticsBusinessSummary.md) |  | [optional] 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**report_header** | [**ObbReportHeader**](ObbReportHeader.md) |  | 
**requester_name** | **str** | Name of requester | [optional] 
**title** | **str** | Title of the report | 

## Example

```python
from openapi_client.models.balance_analytics_report import BalanceAnalyticsReport

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceAnalyticsReport from a JSON string
balance_analytics_report_instance = BalanceAnalyticsReport.from_json(json)
# print the JSON string representation of the object
print(BalanceAnalyticsReport.to_json())

# convert the object into a dict
balance_analytics_report_dict = balance_analytics_report_instance.to_dict()
# create an instance of BalanceAnalyticsReport from a dict
balance_analytics_report_from_dict = BalanceAnalyticsReport.from_dict(balance_analytics_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



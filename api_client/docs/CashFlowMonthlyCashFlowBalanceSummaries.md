# CashFlowMonthlyCashFlowBalanceSummaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**min_daily_balance** | **float** | Min Daily Balance for each month for all accounts | 
**max_daily_balance** | **float** | Max Daily Balance for each month for all accounts | 
**average_daily_balance** | **float** | Average Daily Balance for each month for all accounts | 
**standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance for each month for all accounts | [optional] 
**number_of_days_negative_balance** | **str** | Number of Days Negative Balance for each month for all accounts | 
**number_of_days_positive_balance** | **str** | Number of Days Positive Balance for each month for all accounts | 

## Example

```python
from openapi_client.models.cash_flow_monthly_cash_flow_balance_summaries import CashFlowMonthlyCashFlowBalanceSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlyCashFlowBalanceSummaries from a JSON string
cash_flow_monthly_cash_flow_balance_summaries_instance = CashFlowMonthlyCashFlowBalanceSummaries.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlyCashFlowBalanceSummaries.to_json())

# convert the object into a dict
cash_flow_monthly_cash_flow_balance_summaries_dict = cash_flow_monthly_cash_flow_balance_summaries_instance.to_dict()
# create an instance of CashFlowMonthlyCashFlowBalanceSummaries from a dict
cash_flow_monthly_cash_flow_balance_summaries_from_dict = CashFlowMonthlyCashFlowBalanceSummaries.from_dict(cash_flow_monthly_cash_flow_balance_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



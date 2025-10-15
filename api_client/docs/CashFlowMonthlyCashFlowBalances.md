# CashFlowMonthlyCashFlowBalances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**min_daily_balance** | **float** | Min Daily Balance for each month | 
**max_daily_balance** | **float** | Max Daily Balance for each month | 
**average_daily_balance** | **float** | Average Daily Balance for each month | 
**standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance for each month | [optional] 
**number_of_days_negative_balance** | **str** | Number of Days Negative Balance for each month | 
**number_of_days_positive_balance** | **str** | Number of Days positive balance for each month | 

## Example

```python
from openapi_client.models.cash_flow_monthly_cash_flow_balances import CashFlowMonthlyCashFlowBalances

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlyCashFlowBalances from a JSON string
cash_flow_monthly_cash_flow_balances_instance = CashFlowMonthlyCashFlowBalances.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlyCashFlowBalances.to_json())

# convert the object into a dict
cash_flow_monthly_cash_flow_balances_dict = cash_flow_monthly_cash_flow_balances_instance.to_dict()
# create an instance of CashFlowMonthlyCashFlowBalances from a dict
cash_flow_monthly_cash_flow_balances_from_dict = CashFlowMonthlyCashFlowBalances.from_dict(cash_flow_monthly_cash_flow_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



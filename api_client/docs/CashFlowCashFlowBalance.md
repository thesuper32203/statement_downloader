# CashFlowCashFlowBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_balances** | [**List[CashFlowMonthlyCashFlowBalances]**](CashFlowMonthlyCashFlowBalances.md) | List of attributes for each month | 
**min_daily_balance** | **float** | Min daily balance across entire transaction history | 
**max_daily_balance** | **float** | Max Daily Balance across entire transaction history | 
**twelve_month_average_daily_balance** | **float** | Average Daily Balance across twelve months for the account | 
**six_month_average_daily_balance** | **float** | Average Daily Balance across six months for the account | 
**two_month_average_daily_balance** | **float** | Average Daily Balance across two months for the account | 
**twelve_month_standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance across twelve months for the account | 
**six_month_standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance across six months for the account | [optional] 
**two_month_standard_deviation_of_daily_balance** | **str** | Standard Deviation of Daily Balance across two months for the account | 
**number_days_negative_balance** | **str** | Number of Days Negative Balance over entire transaction history | [optional] 
**number_of_days_positive_balance** | **str** | Number of Days positive balance over entire transaction history | 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_balance import CashFlowCashFlowBalance

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowBalance from a JSON string
cash_flow_cash_flow_balance_instance = CashFlowCashFlowBalance.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowBalance.to_json())

# convert the object into a dict
cash_flow_cash_flow_balance_dict = cash_flow_cash_flow_balance_instance.to_dict()
# create an instance of CashFlowCashFlowBalance from a dict
cash_flow_cash_flow_balance_from_dict = CashFlowCashFlowBalance.from_dict(cash_flow_cash_flow_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



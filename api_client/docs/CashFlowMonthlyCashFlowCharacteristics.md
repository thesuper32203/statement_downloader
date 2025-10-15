# CashFlowMonthlyCashFlowCharacteristics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**total_credits_less_total_debits** | **float** | Total Credits - Total Debits by month | 
**total_credits_less_total_debits_less_transfers** | **float** | Total Credits - Total Debits by month (Without Transfers) | 
**average_transaction_amount** | **float** | Average transaction amount by month | 

## Example

```python
from openapi_client.models.cash_flow_monthly_cash_flow_characteristics import CashFlowMonthlyCashFlowCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlyCashFlowCharacteristics from a JSON string
cash_flow_monthly_cash_flow_characteristics_instance = CashFlowMonthlyCashFlowCharacteristics.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlyCashFlowCharacteristics.to_json())

# convert the object into a dict
cash_flow_monthly_cash_flow_characteristics_dict = cash_flow_monthly_cash_flow_characteristics_instance.to_dict()
# create an instance of CashFlowMonthlyCashFlowCharacteristics from a dict
cash_flow_monthly_cash_flow_characteristics_from_dict = CashFlowMonthlyCashFlowCharacteristics.from_dict(cash_flow_monthly_cash_flow_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CashFlowMonthlycashflowDebits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**number_of_debits** | **str** | Number of Debits by month | 
**total_debits_amount** | **float** | Total Amount of Debits by month | 
**largest_debit** | **float** | Largest Debit by month | 
**number_of_debits_less_transfers** | **str** | Number of Debits by month (less transfers) | 
**total_debits_amount_less_transfers** | **float** | Total amount of debits by month (less transfers) | 
**average_debit_amount** | **float** | The average debit amount | 

## Example

```python
from openapi_client.models.cash_flow_monthlycashflow_debits import CashFlowMonthlycashflowDebits

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlycashflowDebits from a JSON string
cash_flow_monthlycashflow_debits_instance = CashFlowMonthlycashflowDebits.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlycashflowDebits.to_json())

# convert the object into a dict
cash_flow_monthlycashflow_debits_dict = cash_flow_monthlycashflow_debits_instance.to_dict()
# create an instance of CashFlowMonthlycashflowDebits from a dict
cash_flow_monthlycashflow_debits_from_dict = CashFlowMonthlycashflowDebits.from_dict(cash_flow_monthlycashflow_debits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



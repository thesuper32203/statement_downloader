# CashFlowCashFlowDebit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_debits** | [**List[CashFlowMonthlycashflowDebits]**](CashFlowMonthlycashflowDebits.md) | List of attributes for each month | 
**twelve_month_debit_total** | **float** | Sum of all monthly debit transactions for each month by account | [optional] 
**twelve_month_debit_total_less_transfers** | **float** | Sum of all monthly debit transactions without transfers for the account | [optional] 
**six_month_debit_total** | **float** | Six month sum of all debit transactions | [optional] 
**six_month_debit_total_less_transfers** | **float** | Six month sum of all debit transactions without transfers for the account | [optional] 
**two_month_debit_total** | **float** | Two month sum of all debit transactions | [optional] 
**two_month_debit_total_less_transfers** | **float** | Two month sum of all debit transactions without transfers for the account | [optional] 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_debit import CashFlowCashFlowDebit

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowDebit from a JSON string
cash_flow_cash_flow_debit_instance = CashFlowCashFlowDebit.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowDebit.to_json())

# convert the object into a dict
cash_flow_cash_flow_debit_dict = cash_flow_cash_flow_debit_instance.to_dict()
# create an instance of CashFlowCashFlowDebit from a dict
cash_flow_cash_flow_debit_from_dict = CashFlowCashFlowDebit.from_dict(cash_flow_cash_flow_debit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



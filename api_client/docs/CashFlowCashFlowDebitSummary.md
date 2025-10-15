# CashFlowCashFlowDebitSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_debit_summaries** | [**List[CashFlowMonthlyCashFlowDebitSummaries]**](CashFlowMonthlyCashFlowDebitSummaries.md) | List of attributes for each month | 
**twelve_month_debit_total** | **float** | Sum of all monthly debit transactions for each month by account | 
**twelve_month_debit_total_less_transfers** | **float** | Sum of all monthly debit transactions without transfers for the account | 
**six_month_debit_total** | **float** | Six month sum of all debit transactions by account | 
**six_month_debit_total_less_transfers** | **float** | Six month sum of all debit transactions without transfers for the account | 
**two_month_debit_total** | **float** | Two month sum of all debit transactions by account | 
**two_month_debit_total_less_transfers** | **float** | Two month sum of all debit transactions without transfers for the account | 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_debit_summary import CashFlowCashFlowDebitSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowDebitSummary from a JSON string
cash_flow_cash_flow_debit_summary_instance = CashFlowCashFlowDebitSummary.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowDebitSummary.to_json())

# convert the object into a dict
cash_flow_cash_flow_debit_summary_dict = cash_flow_cash_flow_debit_summary_instance.to_dict()
# create an instance of CashFlowCashFlowDebitSummary from a dict
cash_flow_cash_flow_debit_summary_from_dict = CashFlowCashFlowDebitSummary.from_dict(cash_flow_cash_flow_debit_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



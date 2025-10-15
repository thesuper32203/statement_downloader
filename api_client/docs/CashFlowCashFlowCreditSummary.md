# CashFlowCashFlowCreditSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_credit_summaries** | [**List[CashFlowMonthlyCashFlowCreditSummaries]**](CashFlowMonthlyCashFlowCreditSummaries.md) | List of attributes for each month | 
**twelve_month_credit_total** | **float** | Sum of all credit transactions for each month for all accounts | 
**twelve_month_credit_total_less_transfers** | **float** | Sum of all monthly credit transactions without transfers for all accounts | 
**six_month_credit_total** | **float** | Six month sum of all credit transactions | 
**six_month_credit_total_less_transfers** | **float** | Six month sum of all monthly credit transactions without transfers for all accounts | 
**two_month_credit_total** | **float** | Two month sum of all credit transactions | 
**two_month_credit_total_less_transfers** | **float** | Two month sum of all monthly credit transactions without transfers for all accounts | 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_credit_summary import CashFlowCashFlowCreditSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowCreditSummary from a JSON string
cash_flow_cash_flow_credit_summary_instance = CashFlowCashFlowCreditSummary.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowCreditSummary.to_json())

# convert the object into a dict
cash_flow_cash_flow_credit_summary_dict = cash_flow_cash_flow_credit_summary_instance.to_dict()
# create an instance of CashFlowCashFlowCreditSummary from a dict
cash_flow_cash_flow_credit_summary_from_dict = CashFlowCashFlowCreditSummary.from_dict(cash_flow_cash_flow_credit_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



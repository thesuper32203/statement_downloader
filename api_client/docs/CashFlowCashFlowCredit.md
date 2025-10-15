# CashFlowCashFlowCredit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_credits** | [**List[CashFlowMonthlyCashFlowCredits]**](CashFlowMonthlyCashFlowCredits.md) | List of attributes for each month | 
**twelve_month_credit_total** | **float** | Sum of all credit transactions for each month by account | [optional] 
**twelve_month_credit_total_less_transfers** | **float** | Sum of all monthly credit transactions without transfers for the account | [optional] 
**six_month_credit_total** | **float** | Sum of six month credit transactions | [optional] 
**six_month_credit_total_less_transfers** | **float** | Sum of six month credit transactions without transfers | [optional] 
**two_month_credit_total** | **float** | Sum of two month credit transactions | [optional] 
**two_month_credit_total_less_transfers** | **float** | Sum of two month credit transactions without transfers | [optional] 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_credit import CashFlowCashFlowCredit

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowCredit from a JSON string
cash_flow_cash_flow_credit_instance = CashFlowCashFlowCredit.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowCredit.to_json())

# convert the object into a dict
cash_flow_cash_flow_credit_dict = cash_flow_cash_flow_credit_instance.to_dict()
# create an instance of CashFlowCashFlowCredit from a dict
cash_flow_cash_flow_credit_from_dict = CashFlowCashFlowCredit.from_dict(cash_flow_cash_flow_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



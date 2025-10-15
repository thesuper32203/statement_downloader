# CashFlowCashFlowCharacteristicsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_characteristics_summaries** | [**List[CashFlowMonthlyCashFlowCharacteristicsSummaries]**](CashFlowMonthlyCashFlowCharacteristicsSummaries.md) | List of attributes for each month | [optional] 
**average_monthly_net** | **float** | Average monthly net amount | 
**average_monthly_net_less_transfers** | **float** | Average monthly net less transfers | 
**twelve_month_total_net** | **float** | Sum of all monthly (Total Credits - Total Debits) each month by the account | 
**twelve_month_total_net_less_transfers** | **float** | Sum of all monthly (Total Credits - Total Debits) without transfers by the account | 
**six_month_average_total_credits_less_total_debits** | **float** | 6 Month Average (Total Credits - Total Debits) across all accounts | 
**six_month_average_total_credits_less_total_debits_less_transfers** | **float** | 6 Month Average (Total Credits - Total Debits) - (Without Transfers) across all accounts | 
**two_month_average_total_credits_less_total_debits** | **float** | 2 Month Average (Total Credits - Total Debits) across all accounts | 
**two_month_average_total_credits_less_total_debits_less_transfers** | **float** | 2 Month Average (Total Credits - Total Debits) - (Without Transfers) across all accounts | [optional] 

## Example

```python
from openapi_client.models.cash_flow_cash_flow_characteristics_summary import CashFlowCashFlowCharacteristicsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowCashFlowCharacteristicsSummary from a JSON string
cash_flow_cash_flow_characteristics_summary_instance = CashFlowCashFlowCharacteristicsSummary.from_json(json)
# print the JSON string representation of the object
print(CashFlowCashFlowCharacteristicsSummary.to_json())

# convert the object into a dict
cash_flow_cash_flow_characteristics_summary_dict = cash_flow_cash_flow_characteristics_summary_instance.to_dict()
# create an instance of CashFlowCashFlowCharacteristicsSummary from a dict
cash_flow_cash_flow_characteristics_summary_from_dict = CashFlowCashFlowCharacteristicsSummary.from_dict(cash_flow_cash_flow_characteristics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



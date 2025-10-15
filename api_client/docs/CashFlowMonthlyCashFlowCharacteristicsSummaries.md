# CashFlowMonthlyCashFlowCharacteristicsSummaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | One instance for each complete calendar month in the report | 
**total_credits_less_total_debits** | **float** | Total Credits - Total Debits by month across all accounts | 
**total_credits_less_total_debits_less_transfers** | **float** | Total Credits - Total Debits by month (Without Transfers) across all accounts | 
**average_transaction_amount** | **float** | Average transaction amount across all accounts | 

## Example

```python
from openapi_client.models.cash_flow_monthly_cash_flow_characteristics_summaries import CashFlowMonthlyCashFlowCharacteristicsSummaries

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowMonthlyCashFlowCharacteristicsSummaries from a JSON string
cash_flow_monthly_cash_flow_characteristics_summaries_instance = CashFlowMonthlyCashFlowCharacteristicsSummaries.from_json(json)
# print the JSON string representation of the object
print(CashFlowMonthlyCashFlowCharacteristicsSummaries.to_json())

# convert the object into a dict
cash_flow_monthly_cash_flow_characteristics_summaries_dict = cash_flow_monthly_cash_flow_characteristics_summaries_instance.to_dict()
# create an instance of CashFlowMonthlyCashFlowCharacteristicsSummaries from a dict
cash_flow_monthly_cash_flow_characteristics_summaries_from_dict = CashFlowMonthlyCashFlowCharacteristicsSummaries.from_dict(cash_flow_monthly_cash_flow_characteristics_summaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



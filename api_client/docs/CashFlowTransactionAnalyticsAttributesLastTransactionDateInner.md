# CashFlowTransactionAnalyticsAttributesLastTransactionDateInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date the deposit transaction was posted | 
**deposits_credits** | **float** | Amount of transaction if deposit, otherwise null | [optional] 
**withdrawals_debits** | **float** | Amount of transaction if withdrawal, otherwise null | [optional] 
**zero_amount_transaction** | **float** | Amount of transaction if zero, otherwise null | [optional] 
**transaction_description** | **str** | Description of transaction | [optional] 

## Example

```python
from openapi_client.models.cash_flow_transaction_analytics_attributes_last_transaction_date_inner import CashFlowTransactionAnalyticsAttributesLastTransactionDateInner

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowTransactionAnalyticsAttributesLastTransactionDateInner from a JSON string
cash_flow_transaction_analytics_attributes_last_transaction_date_inner_instance = CashFlowTransactionAnalyticsAttributesLastTransactionDateInner.from_json(json)
# print the JSON string representation of the object
print(CashFlowTransactionAnalyticsAttributesLastTransactionDateInner.to_json())

# convert the object into a dict
cash_flow_transaction_analytics_attributes_last_transaction_date_inner_dict = cash_flow_transaction_analytics_attributes_last_transaction_date_inner_instance.to_dict()
# create an instance of CashFlowTransactionAnalyticsAttributesLastTransactionDateInner from a dict
cash_flow_transaction_analytics_attributes_last_transaction_date_inner_from_dict = CashFlowTransactionAnalyticsAttributesLastTransactionDateInner.from_dict(cash_flow_transaction_analytics_attributes_last_transaction_date_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



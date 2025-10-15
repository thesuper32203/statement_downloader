# CashFlowTransactionAnalyticsAttributes

Transaction Analytics Attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_deposits_credits_for_the_report_time_period** | [**List[CashFlowActivityDepositsCredits]**](CashFlowActivityDepositsCredits.md) | List of all deposit transactions posted to the account during the report period | 
**activity_withdrawals_debits_for_the_report_time_period** | [**List[CashFlowActivityWithdrawalsDebits]**](CashFlowActivityWithdrawalsDebits.md) | List of all withdrawal transactions posted to the account during the report period | 
**average_transaction_value_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Average value of transactions during periods in the report. Values may be positive or negative | 
**historic_weeks_with_zero_transactions** | [**CashFlowNumWeeksZeros**](CashFlowNumWeeksZeros.md) |  | [optional] 
**last_transaction_date** | [**List[CashFlowTransactionAnalyticsAttributesLastTransactionDateInner]**](CashFlowTransactionAnalyticsAttributesLastTransactionDateInner.md) | Latest posted transaction(s) to the account. May be more than one if they share the same timestamp | [optional] 
**net_cash_flow_by_month_for_the_report_time_period** | [**List[ObbDateRangeAndAmount]**](ObbDateRangeAndAmount.md) | Net cash flow for each month during the report period | [optional] 
**net_cash_flow_for_the_report_time_period** | **float** | Net cash flow during the report period (may be positive or negative) | [optional] 

## Example

```python
from openapi_client.models.cash_flow_transaction_analytics_attributes import CashFlowTransactionAnalyticsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowTransactionAnalyticsAttributes from a JSON string
cash_flow_transaction_analytics_attributes_instance = CashFlowTransactionAnalyticsAttributes.from_json(json)
# print the JSON string representation of the object
print(CashFlowTransactionAnalyticsAttributes.to_json())

# convert the object into a dict
cash_flow_transaction_analytics_attributes_dict = cash_flow_transaction_analytics_attributes_instance.to_dict()
# create an instance of CashFlowTransactionAnalyticsAttributes from a dict
cash_flow_transaction_analytics_attributes_from_dict = CashFlowTransactionAnalyticsAttributes.from_dict(cash_flow_transaction_analytics_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



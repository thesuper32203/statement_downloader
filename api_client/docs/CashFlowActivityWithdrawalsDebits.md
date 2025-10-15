# CashFlowActivityWithdrawalsDebits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date the withdrawal transaction was posted | 
**transaction_description** | **str** | Description of transaction | [optional] 
**withdrawals_debits** | **float** | Amount of the withdrawal | 

## Example

```python
from openapi_client.models.cash_flow_activity_withdrawals_debits import CashFlowActivityWithdrawalsDebits

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowActivityWithdrawalsDebits from a JSON string
cash_flow_activity_withdrawals_debits_instance = CashFlowActivityWithdrawalsDebits.from_json(json)
# print the JSON string representation of the object
print(CashFlowActivityWithdrawalsDebits.to_json())

# convert the object into a dict
cash_flow_activity_withdrawals_debits_dict = cash_flow_activity_withdrawals_debits_instance.to_dict()
# create an instance of CashFlowActivityWithdrawalsDebits from a dict
cash_flow_activity_withdrawals_debits_from_dict = CashFlowActivityWithdrawalsDebits.from_dict(cash_flow_activity_withdrawals_debits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



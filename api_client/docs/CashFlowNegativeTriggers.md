# CashFlowNegativeTriggers

Transactions that may be warning signs of bad creditworthiness

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insufficient_fund_fees** | [**CashFlowInsufficientFundsFees**](CashFlowInsufficientFundsFees.md) |  | [optional] 

## Example

```python
from openapi_client.models.cash_flow_negative_triggers import CashFlowNegativeTriggers

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowNegativeTriggers from a JSON string
cash_flow_negative_triggers_instance = CashFlowNegativeTriggers.from_json(json)
# print the JSON string representation of the object
print(CashFlowNegativeTriggers.to_json())

# convert the object into a dict
cash_flow_negative_triggers_dict = cash_flow_negative_triggers_instance.to_dict()
# create an instance of CashFlowNegativeTriggers from a dict
cash_flow_negative_triggers_from_dict = CashFlowNegativeTriggers.from_dict(cash_flow_negative_triggers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



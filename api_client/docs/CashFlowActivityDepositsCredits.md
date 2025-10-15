# CashFlowActivityDepositsCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date the deposit transaction was posted | 
**deposits_credits** | **float** | Amount of the deposit | 
**transaction_description** | **str** | Description of transaction | [optional] 

## Example

```python
from openapi_client.models.cash_flow_activity_deposits_credits import CashFlowActivityDepositsCredits

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowActivityDepositsCredits from a JSON string
cash_flow_activity_deposits_credits_instance = CashFlowActivityDepositsCredits.from_json(json)
# print the JSON string representation of the object
print(CashFlowActivityDepositsCredits.to_json())

# convert the object into a dict
cash_flow_activity_deposits_credits_dict = cash_flow_activity_deposits_credits_instance.to_dict()
# create an instance of CashFlowActivityDepositsCredits from a dict
cash_flow_activity_deposits_credits_from_dict = CashFlowActivityDepositsCredits.from_dict(cash_flow_activity_deposits_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



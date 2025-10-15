# DepositSwitchAccount

Deposit Switch account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | The user&#39;s bank account number | 
**bank_identifier** | **str** | Code used to identify the financial institution also known as the bank routing number | 
**title** | **str** | The title of the account | [optional] 
**type** | **str** | Financial institution account type. Options &#x60;checking&#x60; or &#x60;savings&#x60; | 

## Example

```python
from openapi_client.models.deposit_switch_account import DepositSwitchAccount

# TODO update the JSON string below
json = "{}"
# create an instance of DepositSwitchAccount from a JSON string
deposit_switch_account_instance = DepositSwitchAccount.from_json(json)
# print the JSON string representation of the object
print(DepositSwitchAccount.to_json())

# convert the object into a dict
deposit_switch_account_dict = deposit_switch_account_instance.to_dict()
# create an instance of DepositSwitchAccount from a dict
deposit_switch_account_from_dict = DepositSwitchAccount.from_dict(deposit_switch_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BillPaySwitchIdentity

Identity information for the user. Mandatory when use case is BPS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | User first name | 
**last_name** | **str** | User last name | 
**zip_code** | **str** | Postal / zip code of the user | 
**address** | **str** | First line of user address | 
**address2** | **str** | Second line of user address | [optional] 
**city** | **str** | City in which user is located | 
**state** | **str** | State in which user is located | 
**phone** | **str** | User phone number | 
**email** | **str** | User email address | [optional] 

## Example

```python
from openapi_client.models.bill_pay_switch_identity import BillPaySwitchIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaySwitchIdentity from a JSON string
bill_pay_switch_identity_instance = BillPaySwitchIdentity.from_json(json)
# print the JSON string representation of the object
print(BillPaySwitchIdentity.to_json())

# convert the object into a dict
bill_pay_switch_identity_dict = bill_pay_switch_identity_instance.to_dict()
# create an instance of BillPaySwitchIdentity from a dict
bill_pay_switch_identity_from_dict = BillPaySwitchIdentity.from_dict(bill_pay_switch_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MicroDepositInitiation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_login_id** | **str** | An institution login ID (from the account record) | [optional] 
**receiver** | [**Receiver**](Receiver.md) |  | 
**callback_url** | **str** | A callback URL where to receive micro deposit notifications | [optional] 

## Example

```python
from openapi_client.models.micro_deposit_initiation import MicroDepositInitiation

# TODO update the JSON string below
json = "{}"
# create an instance of MicroDepositInitiation from a JSON string
micro_deposit_initiation_instance = MicroDepositInitiation.from_json(json)
# print the JSON string representation of the object
print(MicroDepositInitiation.to_json())

# convert the object into a dict
micro_deposit_initiation_dict = micro_deposit_initiation_instance.to_dict()
# create an instance of MicroDepositInitiation from a dict
micro_deposit_initiation_from_dict = MicroDepositInitiation.from_dict(micro_deposit_initiation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



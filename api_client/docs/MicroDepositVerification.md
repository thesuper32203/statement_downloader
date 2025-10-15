# MicroDepositVerification

A list of amounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amounts** | **List[float]** | The list of amounts to be verified | 

## Example

```python
from openapi_client.models.micro_deposit_verification import MicroDepositVerification

# TODO update the JSON string below
json = "{}"
# create an instance of MicroDepositVerification from a JSON string
micro_deposit_verification_instance = MicroDepositVerification.from_json(json)
# print the JSON string representation of the object
print(MicroDepositVerification.to_json())

# convert the object into a dict
micro_deposit_verification_dict = micro_deposit_verification_instance.to_dict()
# create an instance of MicroDepositVerification from a dict
micro_deposit_verification_from_dict = MicroDepositVerification.from_dict(micro_deposit_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VerifiedMicroDeposit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Micro entries successful verification status | [optional] 
**status_description** | **str** | Micro entries successful verification description | [optional] 

## Example

```python
from openapi_client.models.verified_micro_deposit import VerifiedMicroDeposit

# TODO update the JSON string below
json = "{}"
# create an instance of VerifiedMicroDeposit from a JSON string
verified_micro_deposit_instance = VerifiedMicroDeposit.from_json(json)
# print the JSON string representation of the object
print(VerifiedMicroDeposit.to_json())

# convert the object into a dict
verified_micro_deposit_dict = verified_micro_deposit_instance.to_dict()
# create an instance of VerifiedMicroDeposit from a dict
verified_micro_deposit_from_dict = VerifiedMicroDeposit.from_dict(verified_micro_deposit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



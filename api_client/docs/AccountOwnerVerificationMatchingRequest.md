# AccountOwnerVerificationMatchingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**AccountOwnerVerificationMatchingRequestName**](AccountOwnerVerificationMatchingRequestName.md) |  | 
**address** | [**AccountOwnerVerificationMatchingRequestAddress**](AccountOwnerVerificationMatchingRequestAddress.md) |  | [optional] 
**phone** | **str** | A valid phone number. It may only include digits. | [optional] 
**email** | **str** | An email address | [optional] 

## Example

```python
from openapi_client.models.account_owner_verification_matching_request import AccountOwnerVerificationMatchingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerVerificationMatchingRequest from a JSON string
account_owner_verification_matching_request_instance = AccountOwnerVerificationMatchingRequest.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerVerificationMatchingRequest.to_json())

# convert the object into a dict
account_owner_verification_matching_request_dict = account_owner_verification_matching_request_instance.to_dict()
# create an instance of AccountOwnerVerificationMatchingRequest from a dict
account_owner_verification_matching_request_from_dict = AccountOwnerVerificationMatchingRequest.from_dict(account_owner_verification_matching_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



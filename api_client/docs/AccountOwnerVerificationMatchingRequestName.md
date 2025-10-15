# AccountOwnerVerificationMatchingRequestName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the account holder | 
**middle_name** | **str** | The middle name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | 
**suffix** | **str** | A generational or academic suffix | [optional] 

## Example

```python
from openapi_client.models.account_owner_verification_matching_request_name import AccountOwnerVerificationMatchingRequestName

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerVerificationMatchingRequestName from a JSON string
account_owner_verification_matching_request_name_instance = AccountOwnerVerificationMatchingRequestName.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerVerificationMatchingRequestName.to_json())

# convert the object into a dict
account_owner_verification_matching_request_name_dict = account_owner_verification_matching_request_name_instance.to_dict()
# create an instance of AccountOwnerVerificationMatchingRequestName from a dict
account_owner_verification_matching_request_name_from_dict = AccountOwnerVerificationMatchingRequestName.from_dict(account_owner_verification_matching_request_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



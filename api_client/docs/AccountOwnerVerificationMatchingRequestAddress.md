# AccountOwnerVerificationMatchingRequestAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line1** | **str** | Address line 1 | [optional] 
**line2** | **str** | Address line 2 | [optional] 
**line3** | **str** | Address line 3 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**country** | **str** | Two-letter ISO 3166-1 alpha-2 country code | [optional] 
**postal_code** | **str** | A ZIP code | [optional] 
**type** | **str** | The type of address (e.g. Home or Business). | [optional] 

## Example

```python
from openapi_client.models.account_owner_verification_matching_request_address import AccountOwnerVerificationMatchingRequestAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerVerificationMatchingRequestAddress from a JSON string
account_owner_verification_matching_request_address_instance = AccountOwnerVerificationMatchingRequestAddress.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerVerificationMatchingRequestAddress.to_json())

# convert the object into a dict
account_owner_verification_matching_request_address_dict = account_owner_verification_matching_request_address_instance.to_dict()
# create an instance of AccountOwnerVerificationMatchingRequestAddress from a dict
account_owner_verification_matching_request_address_from_dict = AccountOwnerVerificationMatchingRequestAddress.from_dict(account_owner_verification_matching_request_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



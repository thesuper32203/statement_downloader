# AccountOwnerVerificationAddress

Account owner address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_address** | **str** | A street address | [optional] 
**type** | **str** | The type of address location: * \&quot;Business\&quot; * \&quot;Home\&quot; * \&quot;Mailing\&quot; | [optional] 
**line1** | **str** | Address line 1 | [optional] 
**line2** | **str** | Address line 2 | [optional] 
**line3** | **str** | Address line 3 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | A ZIP code | [optional] 
**country** | **str** | Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3). | [optional] 
**address_scores** | [**AddressScore**](AddressScore.md) |  | [optional] 

## Example

```python
from openapi_client.models.account_owner_verification_address import AccountOwnerVerificationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerVerificationAddress from a JSON string
account_owner_verification_address_instance = AccountOwnerVerificationAddress.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerVerificationAddress.to_json())

# convert the object into a dict
account_owner_verification_address_dict = account_owner_verification_address_instance.to_dict()
# create an instance of AccountOwnerVerificationAddress from a dict
account_owner_verification_address_from_dict = AccountOwnerVerificationAddress.from_dict(account_owner_verification_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



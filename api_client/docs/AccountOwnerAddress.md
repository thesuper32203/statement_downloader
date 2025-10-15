# AccountOwnerAddress

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

## Example

```python
from openapi_client.models.account_owner_address import AccountOwnerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerAddress from a JSON string
account_owner_address_instance = AccountOwnerAddress.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerAddress.to_json())

# convert the object into a dict
account_owner_address_dict = account_owner_address_instance.to_dict()
# create an instance of AccountOwnerAddress from a dict
account_owner_address_from_dict = AccountOwnerAddress.from_dict(account_owner_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



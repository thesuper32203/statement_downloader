# ObbAccountOwner

Who is on record as the owner of the account. May be the business name, the business owner name, or otherwise.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of the owner on record for the account | 
**name** | **str** | Name of the owner on record for the account | 

## Example

```python
from openapi_client.models.obb_account_owner import ObbAccountOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ObbAccountOwner from a JSON string
obb_account_owner_instance = ObbAccountOwner.from_json(json)
# print the JSON string representation of the object
print(ObbAccountOwner.to_json())

# convert the object into a dict
obb_account_owner_dict = obb_account_owner_instance.to_dict()
# create an instance of ObbAccountOwner from a dict
obb_account_owner_from_dict = ObbAccountOwner.from_dict(obb_account_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccountOwnerHolders


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holders** | [**List[AccountOwnerDetails]**](AccountOwnerDetails.md) | List of account owners | 

## Example

```python
from openapi_client.models.account_owner_holders import AccountOwnerHolders

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerHolders from a JSON string
account_owner_holders_instance = AccountOwnerHolders.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerHolders.to_json())

# convert the object into a dict
account_owner_holders_dict = account_owner_holders_instance.to_dict()
# create an instance of AccountOwnerHolders from a dict
account_owner_holders_from_dict = AccountOwnerHolders.from_dict(account_owner_holders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



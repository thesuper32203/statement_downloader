# AccountOwner

Owner of a customer account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_name** | **str** | The name of the account owner. Can be multiple account owners in one string. This is how the source data is returned from the institution. | 
**owner_address** | **str** | A street address | 
**as_of_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 

## Example

```python
from openapi_client.models.account_owner import AccountOwner

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwner from a JSON string
account_owner_instance = AccountOwner.from_json(json)
# print the JSON string representation of the object
print(AccountOwner.to_json())

# convert the object into a dict
account_owner_dict = account_owner_instance.to_dict()
# create an instance of AccountOwner from a dict
account_owner_from_dict = AccountOwner.from_dict(account_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



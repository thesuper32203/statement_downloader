# CustomerAccounts

A list of customer accounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[CustomerAccount]**](CustomerAccount.md) | List of customer accounts | 

## Example

```python
from openapi_client.models.customer_accounts import CustomerAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAccounts from a JSON string
customer_accounts_instance = CustomerAccounts.from_json(json)
# print the JSON string representation of the object
print(CustomerAccounts.to_json())

# convert the object into a dict
customer_accounts_dict = customer_accounts_instance.to_dict()
# create an instance of CustomerAccounts from a dict
customer_accounts_from_dict = CustomerAccounts.from_dict(customer_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



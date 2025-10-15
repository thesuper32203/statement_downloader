# CustomerAccountsSimple

A list of accounts with basic information of a customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[CustomerAccountSimple]**](CustomerAccountSimple.md) | A list of accounts with basic information of a customer | 

## Example

```python
from openapi_client.models.customer_accounts_simple import CustomerAccountsSimple

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAccountsSimple from a JSON string
customer_accounts_simple_instance = CustomerAccountsSimple.from_json(json)
# print the JSON string representation of the object
print(CustomerAccountsSimple.to_json())

# convert the object into a dict
customer_accounts_simple_dict = customer_accounts_simple_instance.to_dict()
# create an instance of CustomerAccountsSimple from a dict
customer_accounts_simple_from_dict = CustomerAccountsSimple.from_dict(customer_accounts_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



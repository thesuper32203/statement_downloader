# CustomerAccountMultipleStatements

A list of customer account statements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statements** | [**List[CustomerAccountMultipleStatement]**](CustomerAccountMultipleStatement.md) | List of customer account statements | 

## Example

```python
from openapi_client.models.customer_account_multiple_statements import CustomerAccountMultipleStatements

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAccountMultipleStatements from a JSON string
customer_account_multiple_statements_instance = CustomerAccountMultipleStatements.from_json(json)
# print the JSON string representation of the object
print(CustomerAccountMultipleStatements.to_json())

# convert the object into a dict
customer_account_multiple_statements_dict = customer_account_multiple_statements_instance.to_dict()
# create an instance of CustomerAccountMultipleStatements from a dict
customer_account_multiple_statements_from_dict = CustomerAccountMultipleStatements.from_dict(customer_account_multiple_statements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



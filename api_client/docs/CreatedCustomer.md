# CreatedCustomer

A new customer that was just enrolled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**username** | **str** | The customer&#39;s username, assigned by the partner (a unique identifier), following these rules: minimum 6 characters maximum 255 characters any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % &amp; * _ - + the use of email in this field is discouraged it is recommended to use a unique non-email identifier. Use of special characters may result in an error (e.g. í, ü, etc.). Usernames are unique. A username used in Test Drive can&#39;t be reused in other plans. | 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 

## Example

```python
from openapi_client.models.created_customer import CreatedCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedCustomer from a JSON string
created_customer_instance = CreatedCustomer.from_json(json)
# print the JSON string representation of the object
print(CreatedCustomer.to_json())

# convert the object into a dict
created_customer_dict = created_customer_instance.to_dict()
# create an instance of CreatedCustomer from a dict
created_customer_from_dict = CreatedCustomer.from_dict(created_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



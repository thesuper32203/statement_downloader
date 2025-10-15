# NewCustomer

A new customer to be enrolled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The customer&#39;s username, assigned by the partner (a unique identifier), following these rules: minimum 6 characters maximum 255 characters any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % &amp; * _ - + the use of email in this field is discouraged it is recommended to use a unique non-email identifier. Use of special characters may result in an error (e.g. í, ü, etc.). Usernames are unique. A username used in Test Drive can&#39;t be reused in other plans. | 
**first_name** | **str** | The first name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | [optional] 
**application_id** | **str** | &#x60;applicationId&#x60; value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved. | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**email** | **str** | An email address | [optional] 

## Example

```python
from openapi_client.models.new_customer import NewCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of NewCustomer from a JSON string
new_customer_instance = NewCustomer.from_json(json)
# print the JSON string representation of the object
print(NewCustomer.to_json())

# convert the object into a dict
new_customer_dict = new_customer_instance.to_dict()
# create an instance of NewCustomer from a dict
new_customer_from_dict = NewCustomer.from_dict(new_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



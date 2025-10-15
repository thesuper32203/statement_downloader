# GetCustomer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**username** | **str** | The customer&#39;s username, assigned by the partner (a unique identifier), following these rules: minimum 6 characters maximum 255 characters any mix of uppercase, lowercase, numeric, and non-alphabet special characters ! @ . # $ % &amp; * _ - + the use of email in this field is discouraged it is recommended to use a unique non-email identifier. Use of special characters may result in an error (e.g. í, ü, etc.). Usernames are unique. A username used in Test Drive can&#39;t be reused in other plans. | 
**first_name** | **str** | The first name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**email** | **str** | An email address | [optional] 
**type** | **str** | The type of customer (\&quot;active\&quot; or \&quot;testing\&quot; or \&quot;\&quot; for all types) | 
**created_date** | **str** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**last_modified_date** | **str** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**application_id** | **str** | &#x60;applicationId&#x60; value returned from the Get App Registration Status API and the partner assign the customers to. This cannot be changed once set. Only applicable in cases of partners with multiple registered applications. If the partner only has one app, this can usually be omitted. This field is populated after the app is in a status approved. | [optional] 

## Example

```python
from openapi_client.models.get_customer200_response import GetCustomer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomer200Response from a JSON string
get_customer200_response_instance = GetCustomer200Response.from_json(json)
# print the JSON string representation of the object
print(GetCustomer200Response.to_json())

# convert the object into a dict
get_customer200_response_dict = get_customer200_response_instance.to_dict()
# create an instance of GetCustomer200Response from a dict
get_customer200_response_from_dict = GetCustomer200Response.from_dict(get_customer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



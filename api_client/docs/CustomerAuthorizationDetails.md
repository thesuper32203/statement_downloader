# CustomerAuthorizationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution_login_id** | **int** | Institution login id of the customer. | 
**authorization_start_date** | **str** | Authorization start date and time in ISO 8601 format. | 
**authorization_end_date** | **str** | Authorization end date and time in ISO 8601 format. | 

## Example

```python
from openapi_client.models.customer_authorization_details import CustomerAuthorizationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAuthorizationDetails from a JSON string
customer_authorization_details_instance = CustomerAuthorizationDetails.from_json(json)
# print the JSON string representation of the object
print(CustomerAuthorizationDetails.to_json())

# convert the object into a dict
customer_authorization_details_dict = customer_authorization_details_instance.to_dict()
# create an instance of CustomerAuthorizationDetails from a dict
customer_authorization_details_from_dict = CustomerAuthorizationDetails.from_dict(customer_authorization_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



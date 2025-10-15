# Customers

A list of customers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**found** | **int** | The total number of results matching search criteria | [optional] 
**displaying** | **int** | The number of results returned | 
**more_available** | **bool** | If the value of &#x60;moreAvailable&#x60; is \&quot;true\&quot;, you can retrieve the next page of results by increasing the value of the start parameter in your next request:\&quot;...&amp;start&#x3D;6&amp;limit&#x3D;5\&quot; | 
**customers** | [**List[Customer]**](Customer.md) | A list of customer records | 

## Example

```python
from openapi_client.models.customers import Customers

# TODO update the JSON string below
json = "{}"
# create an instance of Customers from a JSON string
customers_instance = Customers.from_json(json)
# print the JSON string representation of the object
print(Customers.to_json())

# convert the object into a dict
customers_dict = customers_instance.to_dict()
# create an instance of Customers from a dict
customers_from_dict = Customers.from_dict(customers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ConsumerUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | [optional] 
**address** | **str** | A street address | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**zip** | **str** | A ZIP code | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**ssn** | **str** | A full SSN with or without hyphens | [optional] 
**birthday** | [**Birthday**](Birthday.md) |  | [optional] 
**email** | **str** | An email address | [optional] 
**suffix** | **str** | A generational or academic suffix | [optional] 
**end_user** | [**ConsumerEndUser**](ConsumerEndUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.consumer_update import ConsumerUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerUpdate from a JSON string
consumer_update_instance = ConsumerUpdate.from_json(json)
# print the JSON string representation of the object
print(ConsumerUpdate.to_json())

# convert the object into a dict
consumer_update_dict = consumer_update_instance.to_dict()
# create an instance of ConsumerUpdate from a dict
consumer_update_from_dict = ConsumerUpdate.from_dict(consumer_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



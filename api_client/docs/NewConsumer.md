# NewConsumer

A new consumer to be created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the account holder | 
**last_name** | **str** | The last name of the account holder | 
**address** | **str** | A street address | 
**city** | **str** | City | 
**state** | **str** | State | 
**zip** | **str** | A ZIP code | 
**phone** | **str** | A phone number (max length 15). | 
**ssn** | **str** | A full SSN with or without hyphens | 
**birthday** | [**Birthday**](Birthday.md) |  | 
**email** | **str** | An email address | [optional] 
**suffix** | **str** | A generational or academic suffix | [optional] 
**end_user** | [**ConsumerEndUser**](ConsumerEndUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.new_consumer import NewConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of NewConsumer from a JSON string
new_consumer_instance = NewConsumer.from_json(json)
# print the JSON string representation of the object
print(NewConsumer.to_json())

# convert the object into a dict
new_consumer_dict = new_consumer_instance.to_dict()
# create an instance of NewConsumer from a dict
new_consumer_from_dict = NewConsumer.from_dict(new_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



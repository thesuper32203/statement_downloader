# ConsumerDetails

A Consumer Details for Re-Issue CRA Report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | [optional] 
**first_name** | **str** | The first name of the account holder | [optional] 
**middle_name** | **str** | The middle name of the account holder | [optional] 
**last_name** | **str** | The last name of the account holder | [optional] 
**address** | **str** | Address line 1 | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State | [optional] 
**zip** | **str** | A ZIP code | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**ssn** | **str** | Last 4 digits of a SSN | [optional] 
**email** | **str** | An email address | [optional] 

## Example

```python
from openapi_client.models.consumer_details import ConsumerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerDetails from a JSON string
consumer_details_instance = ConsumerDetails.from_json(json)
# print the JSON string representation of the object
print(ConsumerDetails.to_json())

# convert the object into a dict
consumer_details_dict = consumer_details_instance.to_dict()
# create an instance of ConsumerDetails from a dict
consumer_details_from_dict = ConsumerDetails.from_dict(consumer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



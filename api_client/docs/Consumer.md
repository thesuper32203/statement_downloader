# Consumer

A Mastercard Open Finance consumer record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | 
**first_name** | **str** | The first name of the account holder | 
**last_name** | **str** | The last name of the account holder | 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | 
**address** | **str** | A street address | 
**city** | **str** | City | 
**state** | **str** | State | 
**zip** | **str** | A ZIP code | 
**phone** | **str** | A phone number (max length 15). | 
**ssn** | **str** | Last 4 digits of a SSN | 
**birthday** | [**Birthday**](Birthday.md) |  | 
**email** | **str** | An email address | 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**suffix** | **str** | A generational or academic suffix | [optional] 
**end_user** | [**ConsumerEndUser**](ConsumerEndUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.consumer import Consumer

# TODO update the JSON string below
json = "{}"
# create an instance of Consumer from a JSON string
consumer_instance = Consumer.from_json(json)
# print the JSON string representation of the object
print(Consumer.to_json())

# convert the object into a dict
consumer_dict = consumer_instance.to_dict()
# create an instance of Consumer from a dict
consumer_from_dict = Consumer.from_dict(consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



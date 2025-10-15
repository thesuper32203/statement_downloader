# CreatedConsumer

A consumer that was just created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A consumer ID. See Create Consumer API for how to create a consumer ID. | [optional] 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | [optional] 
**customer_id** | **int** | A customer ID represented as a number. See Add Customer API for how to create a customer ID. | [optional] 

## Example

```python
from openapi_client.models.created_consumer import CreatedConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedConsumer from a JSON string
created_consumer_instance = CreatedConsumer.from_json(json)
# print the JSON string representation of the object
print(CreatedConsumer.to_json())

# convert the object into a dict
created_consumer_dict = created_consumer_instance.to_dict()
# create an instance of CreatedConsumer from a dict
created_consumer_from_dict = CreatedConsumer.from_dict(created_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



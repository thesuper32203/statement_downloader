# ConsumerInfo

The SSN and date of birth of a consumer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssn** | **str** | The consumer&#39;s full SSN without hyphens | 
**dob** | **int** | The consumer&#39;s date of birth in Unix epoch time (in seconds). See: Handling Epoch Dates and Times. The timestamp should be set at the start of day of birth. | [optional] 

## Example

```python
from openapi_client.models.consumer_info import ConsumerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerInfo from a JSON string
consumer_info_instance = ConsumerInfo.from_json(json)
# print the JSON string representation of the object
print(ConsumerInfo.to_json())

# convert the object into a dict
consumer_info_dict = consumer_info_instance.to_dict()
# create an instance of ConsumerInfo from a dict
consumer_info_from_dict = ConsumerInfo.from_dict(consumer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



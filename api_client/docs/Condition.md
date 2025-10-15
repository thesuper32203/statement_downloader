# Condition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribe_for** | **str** | The field or entity that the event is subscribed for, such as an institution or account ID. | 
**includes** | **List[str]** | A list of specific IDs or values to include in the subscription condition. | [optional] 
**excludes** | **List[str]** | A list of specific IDs or values to exclude from the subscription condition. | [optional] 

## Example

```python
from openapi_client.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print(Condition.to_json())

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_from_dict = Condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



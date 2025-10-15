# StateAttribute

An attribute which represents some state over time, such as a balance or a calculation, including derivatives, ratios, or projections. Reports the state over the requested time interval(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Name of Attribute as mentioned in Data Dictionary | 
**reported_by_time_periods** | [**List[StateTimeInterval]**](StateTimeInterval.md) | List of state values grouped by specified Time Interval | 

## Example

```python
from openapi_client.models.state_attribute import StateAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of StateAttribute from a JSON string
state_attribute_instance = StateAttribute.from_json(json)
# print the JSON string representation of the object
print(StateAttribute.to_json())

# convert the object into a dict
state_attribute_dict = state_attribute_instance.to_dict()
# create an instance of StateAttribute from a dict
state_attribute_from_dict = StateAttribute.from_dict(state_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StateTimeInterval

For a StateAttribute, describes a time interval type being reported and a list of periods generated according to that type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[StatePeriod]**](StatePeriod.md) | Periods of the specified time interval type, describing the attribute calculations | 
**time_interval_type** | **str** | Possible values for strategies in which attributes may be aggregated and reported across varying time intervals. Allowed Values - MONTHLY_CALENDAR - MONTHLY_ROLLING_30 | [default to 'MONTHLY_CALENDAR']

## Example

```python
from openapi_client.models.state_time_interval import StateTimeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of StateTimeInterval from a JSON string
state_time_interval_instance = StateTimeInterval.from_json(json)
# print the JSON string representation of the object
print(StateTimeInterval.to_json())

# convert the object into a dict
state_time_interval_dict = state_time_interval_instance.to_dict()
# create an instance of StateTimeInterval from a dict
state_time_interval_from_dict = StateTimeInterval.from_dict(state_time_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



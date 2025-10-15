# TransactionalTimeInterval

For a TransactionalAttribute, describes a time interval type being reported and a list of periods generated according to that type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periods** | [**List[TransactionalPeriod]**](TransactionalPeriod.md) | Periods of the specified time interval type, describing the attribute calculations | 
**time_interval_type** | **str** | Possible values for strategies in which attributes may be aggregated and reported across varying time intervals. Allowed Values - MONTHLY_CALENDAR - MONTHLY_ROLLING_30 | [default to 'MONTHLY_CALENDAR']

## Example

```python
from openapi_client.models.transactional_time_interval import TransactionalTimeInterval

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalTimeInterval from a JSON string
transactional_time_interval_instance = TransactionalTimeInterval.from_json(json)
# print the JSON string representation of the object
print(TransactionalTimeInterval.to_json())

# convert the object into a dict
transactional_time_interval_dict = transactional_time_interval_instance.to_dict()
# create an instance of TransactionalTimeInterval from a dict
transactional_time_interval_from_dict = TransactionalTimeInterval.from_dict(transactional_time_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



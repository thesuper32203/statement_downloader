# TransactionalAttribute

An attribute which represents some categorization/classification of transactions. Enumerates those identified transactions and reports aggregations of them over the requested time interval(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_by_time_periods** | [**List[TransactionalTimeInterval]**](TransactionalTimeInterval.md) | List of aggregations by specified Time Interval | 
**attribute_name** | **str** | Name of Attribute as mentioned in Data Dictionary | 
**stream_ids** | **List[str]** | List of stream IDs categorized as belonging to this attribute | 
**transaction_ids** | **List[str]** | List of transaction IDs categorized as belonging to this attribute | 

## Example

```python
from openapi_client.models.transactional_attribute import TransactionalAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalAttribute from a JSON string
transactional_attribute_instance = TransactionalAttribute.from_json(json)
# print the JSON string representation of the object
print(TransactionalAttribute.to_json())

# convert the object into a dict
transactional_attribute_dict = transactional_attribute_instance.to_dict()
# create an instance of TransactionalAttribute from a dict
transactional_attribute_from_dict = TransactionalAttribute.from_dict(transactional_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ThirdPartyAccessPeriod

Object which describes access validity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Multiple types will be supported. Presently below types are supported. * \&quot;timeframe\&quot;: Specifies a timeframe bounded by a startTime and endTime.   The startTime is the time at which the access was granted and the access key generated,   and the endTime is the time at which the access was revoked. Times are represented in ISO 8601 format(\&quot;2022-03-10T06:06:20Z\&quot;) | 
**start_time** | **datetime** | A date-time with time zone | 
**end_time** | **datetime** | A date-time with time zone | 

## Example

```python
from openapi_client.models.third_party_access_period import ThirdPartyAccessPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyAccessPeriod from a JSON string
third_party_access_period_instance = ThirdPartyAccessPeriod.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyAccessPeriod.to_json())

# convert the object into a dict
third_party_access_period_dict = third_party_access_period_instance.to_dict()
# create an instance of ThirdPartyAccessPeriod from a dict
third_party_access_period_from_dict = ThirdPartyAccessPeriod.from_dict(third_party_access_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



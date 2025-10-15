# ForesightAnalyticsReportDataSegments

Requested segments for attribute values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geolocation** | [**List[GeoLocationItems]**](GeoLocationItems.md) | Geolocation array of objects; | [optional] 

## Example

```python
from openapi_client.models.foresight_analytics_report_data_segments import ForesightAnalyticsReportDataSegments

# TODO update the JSON string below
json = "{}"
# create an instance of ForesightAnalyticsReportDataSegments from a JSON string
foresight_analytics_report_data_segments_instance = ForesightAnalyticsReportDataSegments.from_json(json)
# print the JSON string representation of the object
print(ForesightAnalyticsReportDataSegments.to_json())

# convert the object into a dict
foresight_analytics_report_data_segments_dict = foresight_analytics_report_data_segments_instance.to_dict()
# create an instance of ForesightAnalyticsReportDataSegments from a dict
foresight_analytics_report_data_segments_from_dict = ForesightAnalyticsReportDataSegments.from_dict(foresight_analytics_report_data_segments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



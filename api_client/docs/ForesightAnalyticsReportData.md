# ForesightAnalyticsReportData

Parameters supplied by the client requesting the analytics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_cra_purpose** | **bool** | Field to indicate if the requested report is for CRA or NONCRA. For small business lending or other similar business use cases, pass the value as “true” for purposes of this field. | 
**segments** | [**ForesightAnalyticsReportDataSegments**](ForesightAnalyticsReportDataSegments.md) |  | [optional] 
**analytics** | **List[str]** | Analytics information for the requested report. The allowed values are benchmarking &amp; forecasting. If it is null, default to benchmarking and forecasting | [optional] 
**time_interval_types** | **List[str]** | Requested time interval for attribute values. | [optional] 

## Example

```python
from openapi_client.models.foresight_analytics_report_data import ForesightAnalyticsReportData

# TODO update the JSON string below
json = "{}"
# create an instance of ForesightAnalyticsReportData from a JSON string
foresight_analytics_report_data_instance = ForesightAnalyticsReportData.from_json(json)
# print the JSON string representation of the object
print(ForesightAnalyticsReportData.to_json())

# convert the object into a dict
foresight_analytics_report_data_dict = foresight_analytics_report_data_instance.to_dict()
# create an instance of ForesightAnalyticsReportData from a dict
foresight_analytics_report_data_from_dict = ForesightAnalyticsReportData.from_dict(foresight_analytics_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AnalyticsReportData

Parameters supplied by the client requesting the analytics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_cra_purpose** | **bool** | Field to indicate if the requested report is for CRA or NONCRA. For small business lending or other similar business use cases, pass the value as “true” for purposes of this field. | 
**applicant_is_personal_guarantor** | **bool** | Field to indicate if the business owner will personally guarantee the loan. If true, a consumer record will be required. | [optional] 
**time_interval_types** | **List[str]** | Requested time interval for attribute values. | [optional] 

## Example

```python
from openapi_client.models.analytics_report_data import AnalyticsReportData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsReportData from a JSON string
analytics_report_data_instance = AnalyticsReportData.from_json(json)
# print the JSON string representation of the object
print(AnalyticsReportData.to_json())

# convert the object into a dict
analytics_report_data_dict = analytics_report_data_instance.to_dict()
# create an instance of AnalyticsReportData from a dict
analytics_report_data_from_dict = AnalyticsReportData.from_dict(analytics_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



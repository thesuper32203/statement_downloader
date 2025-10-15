# ObbCurrentReportRequestDetails

Requested attributes of the report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_begin_date** | **str** | Date from when the requested data is available | [optional] 
**report_end_date** | **str** | Date to which the requested data is available | [optional] 
**report_request_date** | **str** | The date and time the report was requested | 
**requested_days_for_report** | **int** | Number of days requested for the report | 
**requested_report_begin_date** | **str** | Date the report would have begun on if enough data was available for which the partner requested | 

## Example

```python
from openapi_client.models.obb_current_report_request_details import ObbCurrentReportRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ObbCurrentReportRequestDetails from a JSON string
obb_current_report_request_details_instance = ObbCurrentReportRequestDetails.from_json(json)
# print the JSON string representation of the object
print(ObbCurrentReportRequestDetails.to_json())

# convert the object into a dict
obb_current_report_request_details_dict = obb_current_report_request_details_instance.to_dict()
# create an instance of ObbCurrentReportRequestDetails from a dict
obb_current_report_request_details_from_dict = ObbCurrentReportRequestDetails.from_dict(obb_current_report_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



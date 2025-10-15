# ObbReportHeader

Details about the business the report is generated for and metadata about the report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_address** | **str** | Business address line 1 | [optional] 
**business_city** | **str** | Business address city | [optional] 
**business_name** | **str** | Name of the business | [optional] 
**business_state** | **str** | Business address state | [optional] 
**business_zip** | **str** | Business address zip | [optional] 
**reference_number** | **str** | Partner-provided reference number | [optional] 
**report_date** | **str** | Date the report was requested | 
**report_id** | **str** | Generated unique report ID | 

## Example

```python
from openapi_client.models.obb_report_header import ObbReportHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ObbReportHeader from a JSON string
obb_report_header_instance = ObbReportHeader.from_json(json)
# print the JSON string representation of the object
print(ObbReportHeader.to_json())

# convert the object into a dict
obb_report_header_dict = obb_report_header_instance.to_dict()
# create an instance of ObbReportHeader from a dict
obb_report_header_from_dict = ObbReportHeader.from_dict(obb_report_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



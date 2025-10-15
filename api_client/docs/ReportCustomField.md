# ReportCustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The name of the custom field | [optional] 
**value** | **str** | The value of the custom field | [optional] 
**shown** | **bool** | If the custom field will show on the PDF or not | [optional] 

## Example

```python
from openapi_client.models.report_custom_field import ReportCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCustomField from a JSON string
report_custom_field_instance = ReportCustomField.from_json(json)
# print the JSON string representation of the object
print(ReportCustomField.to_json())

# convert the object into a dict
report_custom_field_dict = report_custom_field_instance.to_dict()
# create an instance of ReportCustomField from a dict
report_custom_field_from_dict = ReportCustomField.from_dict(report_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



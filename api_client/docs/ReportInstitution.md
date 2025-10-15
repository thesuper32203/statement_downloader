# ReportInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of a financial institution, represented as a number | 
**name** | **str** | Finicity institution name | 
**url_home_app** | **str** | The URL of the Financial Institution | 
**accounts** | [**List[ReportInstitutionAccount]**](ReportInstitutionAccount.md) | A list of account records | [optional] 

## Example

```python
from openapi_client.models.report_institution import ReportInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of ReportInstitution from a JSON string
report_institution_instance = ReportInstitution.from_json(json)
# print the JSON string representation of the object
print(ReportInstitution.to_json())

# convert the object into a dict
report_institution_dict = report_institution_instance.to_dict()
# create an instance of ReportInstitution from a dict
report_institution_from_dict = ReportInstitution.from_dict(report_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



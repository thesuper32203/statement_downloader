# PayrollEmploymentHistoryVOIE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_date** | **int** | The last time the payroll data was updated in the payroll provider&#39;s system | 
**employment_id** | **str** | This is a Mastercard assigned ID to the employment record. It remains consistent for that employment record, even if the report is refreshed. It can be used to limit the employment records that are returned in the report. | [optional] 
**employer_name** | **str** | Name of the employer as stated by the employer in the payroll system | 
**payroll_source** | **str** | The name of the payroll source where the data was retrieved | 
**payroll_provider** | **str** | The name of the provider who provides payroll data to payroll source | [optional] 
**employee** | [**PayrollEmployeeRecord**](PayrollEmployeeRecord.md) |  | 
**employment** | [**PayrollEmploymentRecord**](PayrollEmploymentRecord.md) |  | 
**income** | [**PayrollVOIEIncomeRecord**](PayrollVOIEIncomeRecord.md) |  | 

## Example

```python
from openapi_client.models.payroll_employment_history_voie import PayrollEmploymentHistoryVOIE

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollEmploymentHistoryVOIE from a JSON string
payroll_employment_history_voie_instance = PayrollEmploymentHistoryVOIE.from_json(json)
# print the JSON string representation of the object
print(PayrollEmploymentHistoryVOIE.to_json())

# convert the object into a dict
payroll_employment_history_voie_dict = payroll_employment_history_voie_instance.to_dict()
# create an instance of PayrollEmploymentHistoryVOIE from a dict
payroll_employment_history_voie_from_dict = PayrollEmploymentHistoryVOIE.from_dict(payroll_employment_history_voie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



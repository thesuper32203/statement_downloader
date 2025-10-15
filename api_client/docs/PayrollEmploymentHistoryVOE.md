# PayrollEmploymentHistoryVOE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_date** | **int** | The last time the payroll data was updated in the payroll provider&#39;s system | 
**employer_name** | **str** | Name of the employer as stated by the employer in the payroll system | 
**payroll_source** | **str** | The name of the payroll source where the data was retrieved | 
**payroll_provider** | **str** | The name of the provider who provides payroll data to payroll source | [optional] 
**employee** | [**PayrollEmployeeRecord**](PayrollEmployeeRecord.md) |  | 
**employment** | [**PayrollEmploymentRecord**](PayrollEmploymentRecord.md) |  | 
**income** | [**PayrollVOEIncomeRecord**](PayrollVOEIncomeRecord.md) |  | 

## Example

```python
from openapi_client.models.payroll_employment_history_voe import PayrollEmploymentHistoryVOE

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollEmploymentHistoryVOE from a JSON string
payroll_employment_history_voe_instance = PayrollEmploymentHistoryVOE.from_json(json)
# print the JSON string representation of the object
print(PayrollEmploymentHistoryVOE.to_json())

# convert the object into a dict
payroll_employment_history_voe_dict = payroll_employment_history_voe_instance.to_dict()
# create an instance of PayrollEmploymentHistoryVOE from a dict
payroll_employment_history_voe_from_dict = PayrollEmploymentHistoryVOE.from_dict(payroll_employment_history_voe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



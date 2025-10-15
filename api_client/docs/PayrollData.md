# PayrollData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssn** | **str** | The consumer&#39;s full SSN without hyphens. Only required for the Direct API Payroll solution, not required for the Credentialed Payroll solution. | [optional] 
**dob** | **int** | The consumer&#39;s date of birth in Unix epoch time (in seconds). See: Handling Epoch Dates and Times. The timestamp should be set at the start of day of birth. | [optional] 
**report_id** | **str** | The report ID of the original payroll report for refresh use cases. If used, only the employment records from the original report will be included in the refreshed report response. | [optional] 
**payroll_account_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.payroll_data import PayrollData

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollData from a JSON string
payroll_data_instance = PayrollData.from_json(json)
# print the JSON string representation of the object
print(PayrollData.to_json())

# convert the object into a dict
payroll_data_dict = payroll_data_instance.to_dict()
# create an instance of PayrollData from a dict
payroll_data_from_dict = PayrollData.from_dict(payroll_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



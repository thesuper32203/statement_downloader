# PayrollEmployeeRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of the employee: first, middle (if stated), and last name | 
**given_name** | **str** | First name of employee | [optional] 
**middle_name** | **str** | Middle name of employee, if stated | [optional] 
**family_name** | **str** | Last name of employee | [optional] 
**address** | [**List[PayrollEmployeeAddress]**](PayrollEmployeeAddress.md) | Array of addresses | [optional] 

## Example

```python
from openapi_client.models.payroll_employee_record import PayrollEmployeeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollEmployeeRecord from a JSON string
payroll_employee_record_instance = PayrollEmployeeRecord.from_json(json)
# print the JSON string representation of the object
print(PayrollEmployeeRecord.to_json())

# convert the object into a dict
payroll_employee_record_dict = payroll_employee_record_instance.to_dict()
# create an instance of PayrollEmployeeRecord from a dict
payroll_employee_record_from_dict = PayrollEmployeeRecord.from_dict(payroll_employee_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



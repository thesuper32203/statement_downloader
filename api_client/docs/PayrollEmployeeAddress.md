# PayrollEmployeeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Employee address as stated by the employer in the payroll system | [optional] 
**city** | **str** | Employee city as stated by the employer in the payroll system | [optional] 
**state** | **str** | Employee state as stated by the employer in the payroll system | [optional] 
**zip** | **str** | Employee zip code as stated by the employer in the payroll system | [optional] 

## Example

```python
from openapi_client.models.payroll_employee_address import PayrollEmployeeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollEmployeeAddress from a JSON string
payroll_employee_address_instance = PayrollEmployeeAddress.from_json(json)
# print the JSON string representation of the object
print(PayrollEmployeeAddress.to_json())

# convert the object into a dict
payroll_employee_address_dict = payroll_employee_address_instance.to_dict()
# create an instance of PayrollEmployeeAddress from a dict
payroll_employee_address_from_dict = PayrollEmployeeAddress.from_dict(payroll_employee_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



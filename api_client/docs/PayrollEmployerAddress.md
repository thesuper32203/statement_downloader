# PayrollEmployerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Employer address as stated by the employer in the payroll system | [optional] 
**city** | **str** | Employer city as stated by the employer in the payroll system | [optional] 
**state** | **str** | Employer state as stated by the employer in the payroll system | [optional] 
**zip** | **str** | Employer zip code as stated by the employer in the payroll system | [optional] 

## Example

```python
from openapi_client.models.payroll_employer_address import PayrollEmployerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollEmployerAddress from a JSON string
payroll_employer_address_instance = PayrollEmployerAddress.from_json(json)
# print the JSON string representation of the object
print(PayrollEmployerAddress.to_json())

# convert the object into a dict
payroll_employer_address_dict = payroll_employer_address_instance.to_dict()
# create an instance of PayrollEmployerAddress from a dict
payroll_employer_address_from_dict = PayrollEmployerAddress.from_dict(payroll_employer_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



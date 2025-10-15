# Employee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the employee | [optional] 
**address1** | **str** | Employee address as stated by the employer in the payroll system | [optional] 
**address2** | **str** | Employee address as stated by the employer in the payroll system | [optional] 
**city** | **str** | Employee city as stated by the employer in the payroll system | [optional] 
**state** | **str** | Employee state as stated by the employer in the payroll system | [optional] 
**zip** | **str** | Employee zip code as stated by the employer in the payroll system | [optional] 

## Example

```python
from openapi_client.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print(Employee.to_json())

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_from_dict = Employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MonthlyIncome

Current estimated monthly pay for the employment.  This is a mandatory field only for VOIE-payroll report type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_monthly_base_pay** | **float** | Mastercard Open Finance estimated monthly base pay amount for the employment | [optional] 
**estimated_monthly_overtime_pay** | **float** | Mastercard Open Finance estimated monthly overtime pay amount for the employment | [optional] 
**estimated_monthly_bonus_pay** | **float** | Mastercard Open Finance estimated monthly bonus pay amount for the employment | [optional] 
**estimated_monthly_other_pay** | **float** | Mastercard Open Finance estimated monthly other pay amount for the employment | [optional] 
**estimated_monthly_total_pay** | **float** | Sum of all Mastercard Open Finance estimated monthly pay amounts | 
**estimated_monthly_commission_pay** | **float** | Mastercard Open Finance estimated monthly commission pay amount for the employment | [optional] 

## Example

```python
from openapi_client.models.monthly_income import MonthlyIncome

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyIncome from a JSON string
monthly_income_instance = MonthlyIncome.from_json(json)
# print the JSON string representation of the object
print(MonthlyIncome.to_json())

# convert the object into a dict
monthly_income_dict = monthly_income_instance.to_dict()
# create an instance of MonthlyIncome from a dict
monthly_income_from_dict = MonthlyIncome.from_dict(monthly_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



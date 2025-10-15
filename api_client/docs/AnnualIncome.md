# AnnualIncome


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **str** | The year for the amounts given in YTD totals for an employer | 
**gross_pay_amount_ytd** | **float** | Year to date (YTD) gross pay amount for the indicated year | 
**net_pay_amount_ytd** | **float** | Year to date (YTD) net pay amount for the indicated year | [optional] 
**base_pay_amount_ytd** | **float** | Year to date (YTD) base pay amount for the year indicated | [optional] 
**overtime_pay_amount_ytd** | **float** | Year to date (YTD) overtime pay amount for the year indicated | [optional] 
**other_pay_amount_ytd** | **float** | Year to date (YTD) other pay amount for the indicated year. Other pay is pay that is not categorized into one of the other categories. | [optional] 
**commission_pay_amount_ytd** | **float** | Year to date (YTD) commission pay amount for the indicated year | [optional] 

## Example

```python
from openapi_client.models.annual_income import AnnualIncome

# TODO update the JSON string below
json = "{}"
# create an instance of AnnualIncome from a JSON string
annual_income_instance = AnnualIncome.from_json(json)
# print the JSON string representation of the object
print(AnnualIncome.to_json())

# convert the object into a dict
annual_income_dict = annual_income_instance.to_dict()
# create an instance of AnnualIncome from a dict
annual_income_from_dict = AnnualIncome.from_dict(annual_income_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



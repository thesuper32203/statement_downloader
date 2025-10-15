# PaystubMonthlyIncomeRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_monthly_base_pay** | **float** | The estimated monthly base pay amount for the employment from the paystub, calculated by Finicity | [optional] 
**estimated_monthly_overtime_pay** | **float** | The estimated monthly overtime pay amount for the employment from the paystub, calculated by Finicity | [optional] 
**estimated_monthly_bonus_pay** | **float** | The estimated monthly bonus pay amount for the employment from the paystub, calculated by Finicity | [optional] 
**estimated_monthly_commission_pay** | **float** | The estimated commission bonus pay amount for the employment from the paystub, calculated by Finicity | [optional] 

## Example

```python
from openapi_client.models.paystub_monthly_income_record import PaystubMonthlyIncomeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PaystubMonthlyIncomeRecord from a JSON string
paystub_monthly_income_record_instance = PaystubMonthlyIncomeRecord.from_json(json)
# print the JSON string representation of the object
print(PaystubMonthlyIncomeRecord.to_json())

# convert the object into a dict
paystub_monthly_income_record_dict = paystub_monthly_income_record_instance.to_dict()
# create an instance of PaystubMonthlyIncomeRecord from a dict
paystub_monthly_income_record_from_dict = PaystubMonthlyIncomeRecord.from_dict(paystub_monthly_income_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



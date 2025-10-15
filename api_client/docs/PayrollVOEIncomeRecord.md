# PayrollVOEIncomeRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_frequency** | **str** | The current pay frequency or how often a regular pay check is:  * &#x60;Daily&#x60;  * &#x60;Weekly&#x60;  * &#x60;Bi-Weekly&#x60;  * &#x60;Semi-Monthly&#x60;  * &#x60;Monthly&#x60;  * &#x60;Quarterly&#x60;  * &#x60;Semi-Annual&#x60;  * &#x60;Annual&#x60;  * &#x60;Every 2.6 wks&#x60;  * &#x60;Every 4 wks&#x60;  * &#x60;Every 5.2 wks&#x60;  * &#x60;Other&#x60;  * &#x60;Unknown&#x60;  | [optional] 

## Example

```python
from openapi_client.models.payroll_voe_income_record import PayrollVOEIncomeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollVOEIncomeRecord from a JSON string
payroll_voe_income_record_instance = PayrollVOEIncomeRecord.from_json(json)
# print the JSON string representation of the object
print(PayrollVOEIncomeRecord.to_json())

# convert the object into a dict
payroll_voe_income_record_dict = payroll_voe_income_record_instance.to_dict()
# create an instance of PayrollVOEIncomeRecord from a dict
payroll_voe_income_record_from_dict = PayrollVOEIncomeRecord.from_dict(payroll_voe_income_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PayrollVOIEIncomeRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_frequency** | **str** | The current pay frequency or how often a regular pay check is:  * &#x60;Daily&#x60;  * &#x60;Weekly&#x60;  * &#x60;Bi-Weekly&#x60;  * &#x60;Semi-Monthly&#x60;  * &#x60;Monthly&#x60;  * &#x60;Quarterly&#x60;  * &#x60;Semi-Annual&#x60;  * &#x60;Annual&#x60;  * &#x60;Every 2.6 wks&#x60;  * &#x60;Every 4 wks&#x60;  * &#x60;Every 5.2 wks&#x60;  * &#x60;Other&#x60;  * &#x60;Unknown&#x60;  | [optional] 
**pay_type** | **str** | The current pay type:  * &#x60;Salary&#x60;  * &#x60;Hourly&#x60;  * &#x60;Daily&#x60;  | [optional] 
**base_pay_rate** | **float** | The current base or regular pay rate. Please use in conjunction with the &#x60;basePayRateUnit&#x60; field. | [optional] 
**base_pay_rate_unit** | **str** | Unit for the base pay rate:  * &#x60;Hourly&#x60;  * &#x60;Daily&#x60;  * &#x60;Weekly&#x60;  * &#x60;Bi-Weekly&#x60;  * &#x60;Semi-Monthly&#x60;  * &#x60;Monthly&#x60;  * &#x60;Quarterly&#x60;  * &#x60;Semi-Annual&#x60;  * &#x60;Annual&#x60;  * &#x60;Every 2.6 wks&#x60;  * &#x60;Every 5.2 wks&#x60;  * &#x60;Other&#x60;  | [optional] 
**oldest_pay_statement_available** | **str** | The date of the oldest direct pay statement available from the payroll source, as measured by the oldest &#x60;payDate&#x60; from all the pay statements delivered. | [optional] 
**annual_income** | [**List[AnnualIncome]**](AnnualIncome.md) | The annual pay for the current year, through prior year 2 (as available)  This is a mandatory field only for VOIE-payroll report type. | [optional] 
**monthly_income** | [**MonthlyIncome**](MonthlyIncome.md) |  | [optional] 
**direct_pay_statements** | [**List[DirectPayStatements]**](DirectPayStatements.md) | An array of payment histories for each available paycheck | [optional] 

## Example

```python
from openapi_client.models.payroll_voie_income_record import PayrollVOIEIncomeRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PayrollVOIEIncomeRecord from a JSON string
payroll_voie_income_record_instance = PayrollVOIEIncomeRecord.from_json(json)
# print the JSON string representation of the object
print(PayrollVOIEIncomeRecord.to_json())

# convert the object into a dict
payroll_voie_income_record_dict = payroll_voie_income_record_instance.to_dict()
# create an instance of PayrollVOIEIncomeRecord from a dict
payroll_voie_income_record_from_dict = PayrollVOIEIncomeRecord.from_dict(payroll_voie_income_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VOIEPaystubWithStatementPayStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_period** | **str** | The pay period of the pay statement | [optional] 
**billable** | **bool** | This will display true if the pay statement is billable. If a pay statement has been digitized previously, this will display as false as it will not be billable. | 
**asset_id** | **str** | The asset ID of the stored pay statement | 
**pay_date** | **int** | The listed pay date for the pay statement | [optional] 
**start_date** | **int** | The beginning of the pay period | [optional] 
**end_date** | **int** | The end of the pay period | [optional] 
**net_pay_current** | **float** | The total pay after deductions for the employee for the current pay period | [optional] 
**net_pay_ytd** | **float** | The total accumulation of pay after deductions for the employee for the current pay year | [optional] 
**gross_pay_current** | **float** | The total pay before deductions for the employee for the current pay period | [optional] 
**gross_pay_ytd** | **float** | The total accumulation of pay before deductions for the employee for the current pay year | [optional] 
**payroll_provider** | **str** | The payroll provider extracted from the pay statement | [optional] 
**employer** | [**Employer**](Employer.md) |  | 
**employee** | [**Employee**](Employee.md) |  | 
**pay_stat** | [**List[PayStat]**](PayStat.md) | Information pertaining to the earnings on the pay statement | 
**direct_deposits** | [**List[DirectDeposit]**](DirectDeposit.md) | Information pertaining to the direct deposits on the pay statement | [optional] 
**institutions** | **List[str]** | Not populated for the voieWithStatement style of paystub report. For the VOIE - Paystub (with TXVerify) reports this would include details of the financial institution accounts and income streams with matching transactions to the pay statement. | 
**error_code** | **int** | Error code for the asset | [optional] 
**error_message** | **str** | Error message for the asset | [optional] 
**monthly_income** | [**PaystubTxVerifyMonthlyIncomeRecord**](PaystubTxVerifyMonthlyIncomeRecord.md) |  | 

## Example

```python
from openapi_client.models.voie_paystub_with_statement_pay_statement import VOIEPaystubWithStatementPayStatement

# TODO update the JSON string below
json = "{}"
# create an instance of VOIEPaystubWithStatementPayStatement from a JSON string
voie_paystub_with_statement_pay_statement_instance = VOIEPaystubWithStatementPayStatement.from_json(json)
# print the JSON string representation of the object
print(VOIEPaystubWithStatementPayStatement.to_json())

# convert the object into a dict
voie_paystub_with_statement_pay_statement_dict = voie_paystub_with_statement_pay_statement_instance.to_dict()
# create an instance of VOIEPaystubWithStatementPayStatement from a dict
voie_paystub_with_statement_pay_statement_from_dict = VOIEPaystubWithStatementPayStatement.from_dict(voie_paystub_with_statement_pay_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



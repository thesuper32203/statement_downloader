# VOIEPayStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_period** | **str** | The pay period of the pay statement | [optional] 
**billable** | **bool** | Designates whether the pay statement is billable | [optional] 
**asset_id** | **str** | The asset ID of the stored pay statement | [optional] 
**pay_date** | **int** | The listed pay date for the pay statement | [optional] 
**start_date** | **int** | The beginning of the pay period | [optional] 
**end_date** | **int** | The end of the pay period | [optional] 
**net_pay_current** | **float** | The total pay after deductions for the employee for the current pay period | [optional] 
**net_pay_ytd** | **float** | The total accumulation of pay after deductions for the employee for the current pay year | [optional] 
**gross_pay_current** | **float** | The total pay before deductions for the employee for the current pay period | [optional] 
**gross_pay_ytd** | **float** | The total accumulation of pay before deductions for the employee for the current pay year | [optional] 
**payroll_provider** | **str** | The company that provides the pay stub. | [optional] 
**match_type** | **str** | The statement match category. Possible values:    * \&quot;NET_PAY_MATCH\&quot;     * \&quot;SPLIT_INTERVIEW_AMOUNT_SUM_TO_NET_PAY_MATCH\&quot;     * \&quot;SPLIT_DIRECT_DEPOSIT_SUM_TO_NET_PAY_MATCH\&quot;     * \&quot;SPLIT_LESS_THAN_NET_PAY_SUM_TO_NET_PAY_MATCH\&quot;     * \&quot;PARTIAL\&quot;     * \&quot;TRANSACTION_DATE_RANGE_INVALID\&quot;     * \&quot;NO_MATCH\&quot; | [optional] 
**employer** | [**Employer**](Employer.md) |  | [optional] 
**employee** | [**Employee**](Employee.md) |  | [optional] 
**pay_stat** | [**List[PayStat]**](PayStat.md) | Information pertaining to the earnings on the pay statement | [optional] 
**deductions** | [**List[Deduction]**](Deduction.md) | Information pertaining to deductions on the pay statement | [optional] 
**direct_deposits** | [**List[DirectDeposit]**](DirectDeposit.md) | Information pertaining to direct deposits on the pay statement | [optional] 

## Example

```python
from openapi_client.models.voie_pay_statement import VOIEPayStatement

# TODO update the JSON string below
json = "{}"
# create an instance of VOIEPayStatement from a JSON string
voie_pay_statement_instance = VOIEPayStatement.from_json(json)
# print the JSON string representation of the object
print(VOIEPayStatement.to_json())

# convert the object into a dict
voie_pay_statement_dict = voie_pay_statement_instance.to_dict()
# create an instance of VOIEPayStatement from a dict
voie_pay_statement_from_dict = VOIEPayStatement.from_dict(voie_pay_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DirectPayStatements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_pay_history_id** | **str** | An ID for the income and employment details for the given pay period | 
**last_pay_period_indicator** | **bool** | Most recent available pay check | 
**main_pay_statement_fields** | [**MainPayStatementFields**](MainPayStatementFields.md) |  | 
**earnings** | [**List[Earnings]**](Earnings.md) | Categorization of pay, for the pay period | 
**deductions** | [**List[Deductions]**](Deductions.md) | Deductions from the pay check | [optional] 

## Example

```python
from openapi_client.models.direct_pay_statements import DirectPayStatements

# TODO update the JSON string below
json = "{}"
# create an instance of DirectPayStatements from a JSON string
direct_pay_statements_instance = DirectPayStatements.from_json(json)
# print the JSON string representation of the object
print(DirectPayStatements.to_json())

# convert the object into a dict
direct_pay_statements_dict = direct_pay_statements_instance.to_dict()
# create an instance of DirectPayStatements from a dict
direct_pay_statements_from_dict = DirectPayStatements.from_dict(direct_pay_statements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



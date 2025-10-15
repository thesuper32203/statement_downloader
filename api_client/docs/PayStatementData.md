# PayStatementData

Data to be included within the pay statement report

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_ids** | **List[str]** | A list of pay statement asset IDs | 
**extract_earnings** | **bool** | Field to indicate whether to extract the earnings on all pay statements | [optional] [default to True]
**extract_deductions** | **bool** | Field to indicate whether to extract the deductions on all pay statements | [optional] [default to False]
**extract_direct_deposit** | **bool** | Field to indicate whether to extract the direct deposits on all pay statements | [optional] [default to True]

## Example

```python
from openapi_client.models.pay_statement_data import PayStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of PayStatementData from a JSON string
pay_statement_data_instance = PayStatementData.from_json(json)
# print the JSON string representation of the object
print(PayStatementData.to_json())

# convert the object into a dict
pay_statement_data_dict = pay_statement_data_instance.to_dict()
# create an instance of PayStatementData from a dict
pay_statement_data_from_dict = PayStatementData.from_dict(pay_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



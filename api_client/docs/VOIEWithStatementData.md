# VOIEWithStatementData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_ids** | **List[str]** | A list of pay statement asset IDs | 
**extract_earnings** | **bool** | Field to indicate whether to extract the earnings on all pay statements | [optional] [default to True]
**extract_deductions** | **bool** | Field to indicate whether to extract the deductions on all pay statements | [optional] [default to False]
**extract_direct_deposit** | **bool** | Field to indicate whether to extract the direct deposits on all pay statements | [optional] [default to True]

## Example

```python
from openapi_client.models.voie_with_statement_data import VOIEWithStatementData

# TODO update the JSON string below
json = "{}"
# create an instance of VOIEWithStatementData from a JSON string
voie_with_statement_data_instance = VOIEWithStatementData.from_json(json)
# print the JSON string representation of the object
print(VOIEWithStatementData.to_json())

# convert the object into a dict
voie_with_statement_data_dict = voie_with_statement_data_instance.to_dict()
# create an instance of VOIEWithStatementData from a dict
voie_with_statement_data_from_dict = VOIEWithStatementData.from_dict(voie_with_statement_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# VOIEWithInterviewData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_verify_interview** | [**List[TxVerifyInterview]**](TxVerifyInterview.md) | An array of &#x60;TxVerifyInterview&#x60; objects | 
**extract_earnings** | **bool** | Field to indicate whether to extract the earnings on all pay statements | [optional] [default to True]
**extract_deductions** | **bool** | Field to indicate whether to extract the deductions on all pay statements | [optional] [default to False]
**extract_direct_deposit** | **bool** | Field to indicate whether to extract the direct deposits on all pay statements | [optional] [default to True]

## Example

```python
from openapi_client.models.voie_with_interview_data import VOIEWithInterviewData

# TODO update the JSON string below
json = "{}"
# create an instance of VOIEWithInterviewData from a JSON string
voie_with_interview_data_instance = VOIEWithInterviewData.from_json(json)
# print the JSON string representation of the object
print(VOIEWithInterviewData.to_json())

# convert the object into a dict
voie_with_interview_data_dict = voie_with_interview_data_instance.to_dict()
# create an instance of VOIEWithInterviewData from a dict
voie_with_interview_data_from_dict = VOIEWithInterviewData.from_dict(voie_with_interview_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



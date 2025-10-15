# NsfIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**potential_settlement_date** | **date** | The date for a potential settlement date | 
**score** | **int** | A risk score from 0-100 that indicates the likelihood of a nsf return risk, where a higher score indicates a higher likelihood of settlement or lower likelihood of return. | 
**indicator** | **str** | &#x60;indicator&#x60; conveys the &#x60;score&#x60;, projecting 3 possible values: \&quot;Low Risk\&quot;, \&quot;Medium Risk\&quot;, or \&quot;High Risk\&quot; | 
**reasons** | [**NsfReasonItem**](NsfReasonItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.nsf_indicator import NsfIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of NsfIndicator from a JSON string
nsf_indicator_instance = NsfIndicator.from_json(json)
# print the JSON string representation of the object
print(NsfIndicator.to_json())

# convert the object into a dict
nsf_indicator_dict = nsf_indicator_instance.to_dict()
# create an instance of NsfIndicator from a dict
nsf_indicator_from_dict = NsfIndicator.from_dict(nsf_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



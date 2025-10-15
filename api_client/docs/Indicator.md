# Indicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**potential_settlement_date** | **date** | The date for all days included in the response. | 
**composite_score** | **int** | A risk score from 0-100 that indicates the likelihood of return risk, where a higher score indicates a higher likelihood of settlement or lower likelihood of return. | 
**score_indicator** | **str** | &#x60;scoreIndicator&#x60; conveys the &#x60;compositeScore&#x60;, projecting 3 possible values: \&quot;Highly Likely to Settle\&quot;, \&quot;Likely to Settle\&quot;, and \&quot;Less Likely to Settle\&quot; | 
**reasons** | [**ReasonItem**](ReasonItem.md) |  | 

## Example

```python
from openapi_client.models.indicator import Indicator

# TODO update the JSON string below
json = "{}"
# create an instance of Indicator from a JSON string
indicator_instance = Indicator.from_json(json)
# print the JSON string representation of the object
print(Indicator.to_json())

# convert the object into a dict
indicator_dict = indicator_instance.to_dict()
# create an instance of Indicator from a dict
indicator_from_dict = Indicator.from_dict(indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



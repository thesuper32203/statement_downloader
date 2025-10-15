# Earnings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Where available, the employer description of earnings on the paycheck | [optional] 
**type** | **str** | Categorization of the earnings:  * &#x60;base&#x60;  * &#x60;bonus&#x60;  * &#x60;overtime&#x60;  * &#x60;commission&#x60;  * &#x60;tips&#x60;  * &#x60;other&#x60;  | 
**rate** | **float** | Rate of pay | [optional] 
**amount** | **float** | Earnings amount for each earning type | 
**amount_ytd** | **float** | Earnings YTD amount if available | [optional] 

## Example

```python
from openapi_client.models.earnings import Earnings

# TODO update the JSON string below
json = "{}"
# create an instance of Earnings from a JSON string
earnings_instance = Earnings.from_json(json)
# print the JSON string representation of the object
print(Earnings.to_json())

# convert the object into a dict
earnings_dict = earnings_instance.to_dict()
# create an instance of Earnings from a dict
earnings_from_dict = Earnings.from_dict(earnings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



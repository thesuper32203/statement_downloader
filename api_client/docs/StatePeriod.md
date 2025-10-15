# StatePeriod

Statistics for one period in the report of a StateAttribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beginning_value** | **float** | Value on the first date in the period | 
**count** | **int** | Count of data points during the period | 
**end_date** | **date** | End date for the period being reported | 
**ending_value** | **float** | Value on the last date in the period | 
**max** | **float** | Maximum amount during the period | [optional] 
**mean** | **float** | Mean of amounts during the period | [optional] 
**median** | **float** | Median of amounts during the period | [optional] 
**min** | **float** | Minimum amount during the period | [optional] 
**standard_deviation** | **float** | Standard deviation of amounts during the period | [optional] 
**start_date** | **date** | Start date for the period being reported | 
**sum** | **float** | Sum of amounts during the period | [optional] 

## Example

```python
from openapi_client.models.state_period import StatePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of StatePeriod from a JSON string
state_period_instance = StatePeriod.from_json(json)
# print the JSON string representation of the object
print(StatePeriod.to_json())

# convert the object into a dict
state_period_dict = state_period_instance.to_dict()
# create an instance of StatePeriod from a dict
state_period_from_dict = StatePeriod.from_dict(state_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



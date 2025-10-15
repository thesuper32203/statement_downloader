# TransactionalPeriod

Statistics for one period in the report of a TransactionalAttribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of data points during the period | 
**end_date** | **date** | End date for the period being reported | 
**max** | **float** | Maximum amount during the period | [optional] 
**mean** | **float** | Mean of amounts during the period | [optional] 
**median** | **float** | Median of amounts during the period | [optional] 
**min** | **float** | Minimum amount during the period | [optional] 
**standard_deviation** | **float** | Standard deviation of amounts during the period | [optional] 
**start_date** | **date** | Start date for the period being reported | 
**sum** | **float** | Sum of amounts during the period | [optional] 

## Example

```python
from openapi_client.models.transactional_period import TransactionalPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionalPeriod from a JSON string
transactional_period_instance = TransactionalPeriod.from_json(json)
# print the JSON string representation of the object
print(TransactionalPeriod.to_json())

# convert the object into a dict
transactional_period_dict = transactional_period_instance.to_dict()
# create an instance of TransactionalPeriod from a dict
transactional_period_from_dict = TransactionalPeriod.from_dict(transactional_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



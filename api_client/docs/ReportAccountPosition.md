# ReportAccountPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The id of the investment position | [optional] 
**currency** | **str** | What currency the account operates in | [optional] 
**symbol** | **str** | The investment position’s market ticker symbol | [optional] 
**security_name** | **str** | The security name for the investment holding | [optional] 
**units** | **float** | The number of units of the holding | [optional] 
**market_value** | **float** | Market value of an investment position at the time of retrieval | [optional] 
**current_price** | **float** | The current price of the investment holding | [optional] 
**security_type** | **float** | Type of security of the investment position | [optional] 

## Example

```python
from openapi_client.models.report_account_position import ReportAccountPosition

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAccountPosition from a JSON string
report_account_position_instance = ReportAccountPosition.from_json(json)
# print the JSON string representation of the object
print(ReportAccountPosition.to_json())

# convert the object into a dict
report_account_position_dict = report_account_position_instance.to_dict()
# create an instance of ReportAccountPosition from a dict
report_account_position_from_dict = ReportAccountPosition.from_dict(report_account_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



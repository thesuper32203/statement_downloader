# NetMonthly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**month** | **int** | Timestamp for the first day of this month | 
**net** | **float** | Total income during the given month, across all income streams | 

## Example

```python
from openapi_client.models.net_monthly import NetMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of NetMonthly from a JSON string
net_monthly_instance = NetMonthly.from_json(json)
# print the JSON string representation of the object
print(NetMonthly.to_json())

# convert the object into a dict
net_monthly_dict = net_monthly_instance.to_dict()
# create an instance of NetMonthly from a dict
net_monthly_from_dict = NetMonthly.from_dict(net_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



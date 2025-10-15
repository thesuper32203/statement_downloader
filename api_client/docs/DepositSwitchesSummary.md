# DepositSwitchesSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID | 
**customer_type** | **str** | The type of Mastercard Open Finance customer (&#x60;active&#x60; or &#x60;testing&#x60;) | 
**switches** | [**List[DepositSwitchesSummarySwitchesInner]**](DepositSwitchesSummarySwitchesInner.md) | Deposit switches summary | [optional] 

## Example

```python
from openapi_client.models.deposit_switches_summary import DepositSwitchesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DepositSwitchesSummary from a JSON string
deposit_switches_summary_instance = DepositSwitchesSummary.from_json(json)
# print the JSON string representation of the object
print(DepositSwitchesSummary.to_json())

# convert the object into a dict
deposit_switches_summary_dict = deposit_switches_summary_instance.to_dict()
# create an instance of DepositSwitchesSummary from a dict
deposit_switches_summary_from_dict = DepositSwitchesSummary.from_dict(deposit_switches_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



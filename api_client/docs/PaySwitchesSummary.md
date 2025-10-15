# PaySwitchesSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID | 
**customer_type** | **str** | The type of Mastercard Open Finance customer (&#x60;active&#x60; or &#x60;testing&#x60;) | 
**switches** | [**List[PaySwitchesSummarySwitchesInner]**](PaySwitchesSummarySwitchesInner.md) | Pay switches summary | [optional] 

## Example

```python
from openapi_client.models.pay_switches_summary import PaySwitchesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PaySwitchesSummary from a JSON string
pay_switches_summary_instance = PaySwitchesSummary.from_json(json)
# print the JSON string representation of the object
print(PaySwitchesSummary.to_json())

# convert the object into a dict
pay_switches_summary_dict = pay_switches_summary_instance.to_dict()
# create an instance of PaySwitchesSummary from a dict
pay_switches_summary_from_dict = PaySwitchesSummary.from_dict(pay_switches_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



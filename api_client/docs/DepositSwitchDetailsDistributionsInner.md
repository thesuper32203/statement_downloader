# DepositSwitchDetailsDistributionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of distribution for the account.  Possible values include &#x60;total&#x60;, &#x60;percent&#x60;, or &#x60;fixed&#x60;. | 
**allocated_value** | **float** | The amount being distributed to the account. When distribution type is &#x60;percent&#x60;, this number represents a percentage of the total pay. When distribution type is &#x60;fixed&#x60;, this number represents a fixed dollar amount. This value is not set when distribution type is &#x60;total&#x60;. | [optional] 
**bank_identifier** | **str** | The bank routing number | 
**account_number_ends_with** | **str** | The trailing portion of customer&#39;s bank account number | 

## Example

```python
from openapi_client.models.deposit_switch_details_distributions_inner import DepositSwitchDetailsDistributionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DepositSwitchDetailsDistributionsInner from a JSON string
deposit_switch_details_distributions_inner_instance = DepositSwitchDetailsDistributionsInner.from_json(json)
# print the JSON string representation of the object
print(DepositSwitchDetailsDistributionsInner.to_json())

# convert the object into a dict
deposit_switch_details_distributions_inner_dict = deposit_switch_details_distributions_inner_instance.to_dict()
# create an instance of DepositSwitchDetailsDistributionsInner from a dict
deposit_switch_details_distributions_inner_from_dict = DepositSwitchDetailsDistributionsInner.from_dict(deposit_switch_details_distributions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



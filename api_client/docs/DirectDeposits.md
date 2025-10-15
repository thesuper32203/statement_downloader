# DirectDeposits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type_code** | **str** | Bank account type:  * &#x60;Checking&#x60;  * &#x60;Savings&#x60;  * &#x60;Loan&#x60;: Loan account employee choose to direct a portion of their net pay to help pay off a loan  | [optional] 
**amount** | **float** | Direct deposit amount | [optional] 
**account_last_four** | **str** | Last four digits of the deposit account number | [optional] 
**routing_number** | **str** | Routing number for the deposit account | [optional] 

## Example

```python
from openapi_client.models.direct_deposits import DirectDeposits

# TODO update the JSON string below
json = "{}"
# create an instance of DirectDeposits from a JSON string
direct_deposits_instance = DirectDeposits.from_json(json)
# print the JSON string representation of the object
print(DirectDeposits.to_json())

# convert the object into a dict
direct_deposits_dict = direct_deposits_instance.to_dict()
# create an instance of DirectDeposits from a dict
direct_deposits_from_dict = DirectDeposits.from_dict(direct_deposits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



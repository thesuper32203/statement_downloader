# Receiver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_number** | **str** | Routing number of receiving bank | 
**account_number** | **str** | Micro entries receiving account number of bank | 
**account_type** | **str** | The list of supported account types. * \&quot;personalChecking\&quot;: Personal Checking * \&quot;businessChecking\&quot;: Business Checking * \&quot;personalSavings\&quot;: Personal Savings * \&quot;businessSavings\&quot;: Business Savings * \&quot;checking\&quot;: Standard checking, will be deprecated * \&quot;savings\&quot;: Standard savings, will be deprecated | 
**name** | **str** | Name of the customer | 
**memo** | **str** | Transaction memo to be displayed for transactions | [optional] 

## Example

```python
from openapi_client.models.receiver import Receiver

# TODO update the JSON string below
json = "{}"
# create an instance of Receiver from a JSON string
receiver_instance = Receiver.from_json(json)
# print the JSON string representation of the object
print(Receiver.to_json())

# convert the object into a dict
receiver_dict = receiver_instance.to_dict()
# create an instance of Receiver from a dict
receiver_from_dict = Receiver.from_dict(receiver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



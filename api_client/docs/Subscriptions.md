# Subscriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of subscriptions currently displayed in the response. | 
**offset** | **int** | The number of items you asked the start of the list to be offset. | 
**limit** | **int** | The number of items you asked the list to be limited. | 
**total** | **int** | The total number of items in the collection. | 
**subscriptions** | [**List[SubscriptionDetail]**](SubscriptionDetail.md) | List of subscription objects returned by the API. | 

## Example

```python
from openapi_client.models.subscriptions import Subscriptions

# TODO update the JSON string below
json = "{}"
# create an instance of Subscriptions from a JSON string
subscriptions_instance = Subscriptions.from_json(json)
# print the JSON string representation of the object
print(Subscriptions.to_json())

# convert the object into a dict
subscriptions_dict = subscriptions_instance.to_dict()
# create an instance of Subscriptions from a dict
subscriptions_from_dict = Subscriptions.from_dict(subscriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



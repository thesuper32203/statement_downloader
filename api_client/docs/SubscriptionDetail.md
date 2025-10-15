# SubscriptionDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | A unique UUID identifier for the subscription. | 
**url** | **str** | The webhook Url where the event notifications will be sent. The URL must be aligned with RFC 2396. | [optional] 
**events** | [**List[Event]**](Event.md) | List of events for the subscription. | 
**status** | **str** | The status of the event (e.g. active, inactive, pending, removed). | 
**created_date** | **datetime** | Subcription creation date. | 
**last_updated_date** | **datetime** | Subcription last updated date. | 

## Example

```python
from openapi_client.models.subscription_detail import SubscriptionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetail from a JSON string
subscription_detail_instance = SubscriptionDetail.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetail.to_json())

# convert the object into a dict
subscription_detail_dict = subscription_detail_instance.to_dict()
# create an instance of SubscriptionDetail from a dict
subscription_detail_from_dict = SubscriptionDetail.from_dict(subscription_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



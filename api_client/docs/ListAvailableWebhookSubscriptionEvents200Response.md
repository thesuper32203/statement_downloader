# ListAvailableWebhookSubscriptionEvents200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AvailableEvent]**](AvailableEvent.md) | List of available events. | 

## Example

```python
from openapi_client.models.list_available_webhook_subscription_events200_response import ListAvailableWebhookSubscriptionEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAvailableWebhookSubscriptionEvents200Response from a JSON string
list_available_webhook_subscription_events200_response_instance = ListAvailableWebhookSubscriptionEvents200Response.from_json(json)
# print the JSON string representation of the object
print(ListAvailableWebhookSubscriptionEvents200Response.to_json())

# convert the object into a dict
list_available_webhook_subscription_events200_response_dict = list_available_webhook_subscription_events200_response_instance.to_dict()
# create an instance of ListAvailableWebhookSubscriptionEvents200Response from a dict
list_available_webhook_subscription_events200_response_from_dict = ListAvailableWebhookSubscriptionEvents200Response.from_dict(list_available_webhook_subscription_events200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



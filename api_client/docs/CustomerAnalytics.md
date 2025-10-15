# CustomerAnalytics

Analytics and attributes generated at a customer level

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactional_attributes** | [**List[TransactionalAttribute]**](TransactionalAttribute.md) | List of calculated transactional attributes | 
**state_attributes** | [**List[StateAttribute]**](StateAttribute.md) | List of calculated state attributes | 
**streams** | [**List[StreamModel]**](StreamModel.md) | List of generated streams | 

## Example

```python
from openapi_client.models.customer_analytics import CustomerAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAnalytics from a JSON string
customer_analytics_instance = CustomerAnalytics.from_json(json)
# print the JSON string representation of the object
print(CustomerAnalytics.to_json())

# convert the object into a dict
customer_analytics_dict = customer_analytics_instance.to_dict()
# create an instance of CustomerAnalytics from a dict
customer_analytics_from_dict = CustomerAnalytics.from_dict(customer_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AccountAnalytics

Analytics calculated for one account in the report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactional_attributes** | [**List[TransactionalAttribute]**](TransactionalAttribute.md) | List of calculated transactional attributes | 
**state_attributes** | [**List[StateAttribute]**](StateAttribute.md) | List of calculated state attributes | 
**streams** | [**List[StreamModel]**](StreamModel.md) | List of generated streams | 

## Example

```python
from openapi_client.models.account_analytics import AccountAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAnalytics from a JSON string
account_analytics_instance = AccountAnalytics.from_json(json)
# print the JSON string representation of the object
print(AccountAnalytics.to_json())

# convert the object into a dict
account_analytics_dict = account_analytics_instance.to_dict()
# create an instance of AccountAnalytics from a dict
account_analytics_from_dict = AccountAnalytics.from_dict(account_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



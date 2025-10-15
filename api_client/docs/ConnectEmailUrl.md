# ConnectEmailUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | A generated Data Connect URL | 
**email_config** | [**EmailOptions**](EmailOptions.md) |  | 

## Example

```python
from openapi_client.models.connect_email_url import ConnectEmailUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectEmailUrl from a JSON string
connect_email_url_instance = ConnectEmailUrl.from_json(json)
# print the JSON string representation of the object
print(ConnectEmailUrl.to_json())

# convert the object into a dict
connect_email_url_dict = connect_email_url_instance.to_dict()
# create an instance of ConnectEmailUrl from a dict
connect_email_url_from_dict = ConnectEmailUrl.from_dict(connect_email_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



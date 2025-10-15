# ConnectUrl

A Data Connect URL object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | **str** | A generated Data Connect URL | 

## Example

```python
from openapi_client.models.connect_url import ConnectUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectUrl from a JSON string
connect_url_instance = ConnectUrl.from_json(json)
# print the JSON string representation of the object
print(ConnectUrl.to_json())

# convert the object into a dict
connect_url_dict = connect_url_instance.to_dict()
# create an instance of ConnectUrl from a dict
connect_url_from_dict = ConnectUrl.from_dict(connect_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



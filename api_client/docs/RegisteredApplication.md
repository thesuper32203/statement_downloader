# RegisteredApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_app_id** | **int** | Identifier to track the application registration from the App Registration and Get App Registration Status APIs, represented as a number | 
**status** | **str** | The status of an app registration request. \&quot;A\&quot; means approved. \&quot;P\&quot; means pending which is the status when initially submitted or when the app is modified and awaiting approval. \&quot;R\&quot; means rejected. If it is rejected there will be a note with the rejected reason. \&quot;S\&quot; stands for \&quot;Skipped\&quot; and indicates that app registration with the data provider will not be required. | 

## Example

```python
from openapi_client.models.registered_application import RegisteredApplication

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredApplication from a JSON string
registered_application_instance = RegisteredApplication.from_json(json)
# print the JSON string representation of the object
print(RegisteredApplication.to_json())

# convert the object into a dict
registered_application_dict = registered_application_instance.to_dict()
# create an instance of RegisteredApplication from a dict
registered_application_from_dict = RegisteredApplication.from_dict(registered_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



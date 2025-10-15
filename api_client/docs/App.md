# App

List of applications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pre_app_id** | **int** | The Pre-app Id is generated after the partner submits the request to create an application using the /aggregation/v1/partners/applications API. | [optional] 
**application_id** | **str** | The Application Id is assigned to the pre-app after the pre-app approval. | [optional] 
**status** | **str** | The application registration status with Mastercard (&#39;A&#39;&#x3D;Approved, &#39;P&#39;&#x3D;Pending, &#39;D&#39;&#x3D;Deleted, &#39;R&#39;&#x3D;Rejected, &#39;S&#39;&#x3D;Skipped) | [optional] 
**name** | **str** | The name of the application submitted by the partner. | [optional] 
**scopes** | **str** | The scope of the application for the partner. | [optional] 
**note** | **str** | The note for the pre-application status. | [optional] 
**created_date** | **str** | The application creation date and time in ISO 8601 format. | [optional] 
**modified_date** | **str** | The application modification date and time are in ISO 8601 format. | [optional] 
**submitted_date** | **str** | The application submitted date and time in ISO 8601 format. | [optional] 

## Example

```python
from openapi_client.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



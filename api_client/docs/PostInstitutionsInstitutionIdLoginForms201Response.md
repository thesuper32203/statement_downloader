# PostInstitutionsInstitutionIdLoginForms201Response

The data used by the calling application to render a login form

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier associated with this session&#39;ed form | 
**event_stream_id** | **str** | Unique reference to the event stream used to send events to the SDK | 
**elements** | [**List[PostInstitutionsInstitutionIdLoginForms201ResponseElementsInner]**](PostInstitutionsInstitutionIdLoginForms201ResponseElementsInner.md) | An array of elements that is to be rendered | 

## Example

```python
from openapi_client.models.post_institutions_institution_id_login_forms201_response import PostInstitutionsInstitutionIdLoginForms201Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostInstitutionsInstitutionIdLoginForms201Response from a JSON string
post_institutions_institution_id_login_forms201_response_instance = PostInstitutionsInstitutionIdLoginForms201Response.from_json(json)
# print the JSON string representation of the object
print(PostInstitutionsInstitutionIdLoginForms201Response.to_json())

# convert the object into a dict
post_institutions_institution_id_login_forms201_response_dict = post_institutions_institution_id_login_forms201_response_instance.to_dict()
# create an instance of PostInstitutionsInstitutionIdLoginForms201Response from a dict
post_institutions_institution_id_login_forms201_response_from_dict = PostInstitutionsInstitutionIdLoginForms201Response.from_dict(post_institutions_institution_id_login_forms201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



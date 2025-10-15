# PostInstitutionsInstitutionIdLoginFormsRequest

Object used to generate a new session'ed login form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The preferred language translation of the requested login form. Supported languages are English:&#39;en&#39;, English-United States:&#39;en-us&#39;, Spanish:&#39;es&#39;, Spanish-United States:&#39;es-us&#39;, French:&#39;fr&#39;, French-Canada:&#39;fr-ca&#39; | 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**configuration_id** | **str** | Unique identifier of the configuration object | [optional] 
**service_agreement** | [**ServiceAgreement**](ServiceAgreement.md) |  | 

## Example

```python
from openapi_client.models.post_institutions_institution_id_login_forms_request import PostInstitutionsInstitutionIdLoginFormsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostInstitutionsInstitutionIdLoginFormsRequest from a JSON string
post_institutions_institution_id_login_forms_request_instance = PostInstitutionsInstitutionIdLoginFormsRequest.from_json(json)
# print the JSON string representation of the object
print(PostInstitutionsInstitutionIdLoginFormsRequest.to_json())

# convert the object into a dict
post_institutions_institution_id_login_forms_request_dict = post_institutions_institution_id_login_forms_request_instance.to_dict()
# create an instance of PostInstitutionsInstitutionIdLoginFormsRequest from a dict
post_institutions_institution_id_login_forms_request_from_dict = PostInstitutionsInstitutionIdLoginFormsRequest.from_dict(post_institutions_institution_id_login_forms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



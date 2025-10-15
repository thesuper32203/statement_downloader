# EmailOptions

Configuration for the Data Connect email's sent to customers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | The email address for the customer receiving the Data Connect email | 
**var_from** | **str** | The name of a person or business sending the Data Connect email | [optional] 
**support_phone** | **str** | The support phone number listed in the email | [optional] 
**subject** | **str** | The subject line of the email. The default is \&quot;Verify your Financial Information\&quot;. | [optional] 
**first_name** | **str** | The first name of the customer or both names of the customers for joint borrowers. Example: \&quot;Marvin and Jenny\&quot;. | [optional] 
**institution_name** | **str** | The name of your company | [optional] 
**institution_address** | **str** | The institution address to appear in the footer of the email | [optional] 
**signature** | **List[str]** | A signature for the email | [optional] 

## Example

```python
from openapi_client.models.email_options import EmailOptions

# TODO update the JSON string below
json = "{}"
# create an instance of EmailOptions from a JSON string
email_options_instance = EmailOptions.from_json(json)
# print the JSON string representation of the object
print(EmailOptions.to_json())

# convert the object into a dict
email_options_dict = email_options_instance.to_dict()
# create an instance of EmailOptions from a dict
email_options_from_dict = EmailOptions.from_dict(email_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



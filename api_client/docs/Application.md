# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_description** | **str** | A short description of the app. This will be visible to end users in the FI interface. | 
**app_name** | **str** | The name of the application assigned to the customer | 
**app_url** | **str** | An URL for the app. This will be visible to end users in the FI interface. | 
**owner_address_line1** | **str** | Address line 1 | 
**owner_address_line2** | **str** | Address line 2 | 
**owner_city** | **str** | City for the business entity that owns the app. Information for registration purposes only and not given to the end user. | 
**owner_country** | **str** | Country for the  business entity that owns the app. Information for registration purposes only and not given to the end user. | 
**owner_name** | **str** | Business name for the business entity that owns the app. Information for registration purposes only and not given to the end user. | 
**owner_postal_code** | **str** | Zip code for the business entity that owns the app. Information for registration purposes only and not given to the end user. | 
**owner_state** | **str** | State for the business entity that owns the app. Information for registration purposes only and not given to the end user. | 
**image** | **str** | An app logo passed as a Base64 encoded image (1:1 SVG file, must be less than 50KB) | 

## Example

```python
from openapi_client.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



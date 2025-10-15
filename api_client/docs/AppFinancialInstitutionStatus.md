# AppFinancialInstitutionStatus

The registration status fields for each specific OAuth financial institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of a financial institution, represented as a number | 
**abbrv_name** | **str** | The application&#39;s abbreviated name | [optional] 
**logo_url** | **str** | An URL to a logo file | [optional] 
**decryption_key_activated** | **bool** | Status of decryption keys for financial institution app registration | 
**created_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**last_modified_date** | **int** | A date in Unix epoch time (in seconds). See: [Handling Epoch Dates and Times](https://developer.mastercard.com/open-banking-us/documentation/codes-and-formats/). | 
**status** | **bool** | \&quot;false\&quot; indicates registration is still pending | 

## Example

```python
from openapi_client.models.app_financial_institution_status import AppFinancialInstitutionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AppFinancialInstitutionStatus from a JSON string
app_financial_institution_status_instance = AppFinancialInstitutionStatus.from_json(json)
# print the JSON string representation of the object
print(AppFinancialInstitutionStatus.to_json())

# convert the object into a dict
app_financial_institution_status_dict = app_financial_institution_status_instance.to_dict()
# create an instance of AppFinancialInstitutionStatus from a dict
app_financial_institution_status_from_dict = AppFinancialInstitutionStatus.from_dict(app_financial_institution_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



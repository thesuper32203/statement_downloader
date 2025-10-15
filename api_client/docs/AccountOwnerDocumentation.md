# AccountOwnerDocumentation

Account owner documentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Country specific tax ID associated with the customer. * **United States**: Social Security number (SSN) or Taxpayer         Identification Number (TIN)    * Format: 123-45-7890  * **Canada**: Social Insurance Number (SIM) or Numero d&#39;assurance sociale (NAS)    * Format: 123-456-789 | [optional] 
**tax_id_country** | **str** | Country code is Iso3166-1 Alpha-2 code and Alpha 3 standard (max length 3). | [optional] 
**government_id** | **str** | A federal or state issued identification number in alphanumeric characters. * **United States**:    * Passport: 6-9 digits.    * US Visa: 8 digits.    * Driver&#39;s license: 1-19 digits * **Canada**:    * Passport: 8 digits    * Driver: 6-9 digits | [optional] 

## Example

```python
from openapi_client.models.account_owner_documentation import AccountOwnerDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerDocumentation from a JSON string
account_owner_documentation_instance = AccountOwnerDocumentation.from_json(json)
# print the JSON string representation of the object
print(AccountOwnerDocumentation.to_json())

# convert the object into a dict
account_owner_documentation_dict = account_owner_documentation_instance.to_dict()
# create an instance of AccountOwnerDocumentation from a dict
account_owner_documentation_from_dict = AccountOwnerDocumentation.from_dict(account_owner_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



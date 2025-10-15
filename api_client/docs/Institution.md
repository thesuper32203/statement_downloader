# Institution

A financial institution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of a financial institution, represented as a number | 
**name** | **str** | The name of the institution | [optional] 
**trans_agg** | **bool** | \&quot;true\&quot;: The institution is certified for the Transaction Aggregation product \&quot;false\&quot;: The institution is decertified for the Transaction Aggregation product | 
**ach** | **bool** | \&quot;true\&quot;: The institution is certified for the ACH product \&quot;false\&quot;: The institution is decertified for the ACH product | 
**state_agg** | **bool** | \&quot;true\&quot;: The institution is certified for the Statement Aggregation product \&quot;false\&quot;: The institution is decertified for the Statement Aggregation product | 
**voi** | **bool** | \&quot;true\&quot;: The institution is certified for the VOI product \&quot;false\&quot;: The institution is decertified for the VOI product | 
**voa** | **bool** | \&quot;true\&quot;: The institution is certified for the VOA product \&quot;false\&quot;: The institution is decertified for the VOA product | 
**aha** | **bool** | \&quot;true\&quot;: The institution is certified for the Account History Aggregation product \&quot;false\&quot;: The institution is decertified for the Account History Aggregation product | 
**avail_balance** | **bool** | \&quot;true\&quot;: The institution is certified for the Account Balance Check (ABC) product \&quot;false\&quot;: The institution is decertified for the Account Balance Check (ABC) product | 
**account_owner** | **bool** | \&quot;true\&quot;: The institution is certified for the Account Owner product \&quot;false\&quot;: The institution is decertified for the Account Owner product | 
**student_loan_data** | **bool** | \&quot;true\&quot;: The institution is certified for the Student Loan Data product  \&quot;false\&quot;: The institution is decertified for the Student Loan Data product | [optional] 
**loan_payment_details** | **bool** | \&quot;true\&quot;: The institution is certified for the Loan Payment Detail product  \&quot;false\&quot;: The institution is decertified for the Loan Payment Detail product | [optional] 
**account_type_description** | **str** | Values: Banking, Investments, Credit Cards/Accounts, Workplace Retirement, Mortgages and Loans, Insurance | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**url_home_app** | **str** | The URL of the institution&#39;s primary home page | [optional] 
**url_logon_app** | **str** | The URL of the institution&#39;s login page | [optional] 
**oauth_enabled** | **bool** | \&quot;true\&quot;: The institution is an OAuth connection  \&quot;false\&quot;: The institution isn&#39;t an OAuth connection | 
**url_forgot_password** | **str** | Institution&#39;s forgot password page | [optional] 
**url_online_registration** | **str** | Institution&#39;s signup page | [optional] 
**var_class** | **str** | Institution&#39;s class | [optional] 
**special_text** | **str** | Special instructions given to customers for login | [optional] 
**time_zone** | **str** | The time zone of the institution. | [optional] 
**special_instructions** | **List[str]** | Instructions given to the customer before they are sent to the institution website to login for OAuth institutions.  Note: this helps the customer to provide the proper permission for data needed for the application. | [optional] 
**special_instutions_title** | **str** | The title of the special instructions, if one exists or is required. | [optional] 
**address** | [**InstitutionAddress**](InstitutionAddress.md) |  | [optional] 
**currency** | **str** | A currency code | 
**email** | **str** | An email address | [optional] 
**status** | **str** | Status for the institution: \&quot;online\&quot;, \&quot;offline\&quot;, \&quot;maintenance\&quot;, \&quot;testing\&quot;, \&quot;beta\&quot;, \&quot;validated\&quot;, \&quot;migrating\&quot; | 
**new_institution_id** | **int** | The ID of a financial institution, represented as a number | [optional] 
**branding** | [**Branding**](Branding.md) |  | [optional] 
**oauth_institution_id** | **int** | The ID of a financial institution, represented as a number | [optional] 

## Example

```python
from openapi_client.models.institution import Institution

# TODO update the JSON string below
json = "{}"
# create an instance of Institution from a JSON string
institution_instance = Institution.from_json(json)
# print the JSON string representation of the object
print(Institution.to_json())

# convert the object into a dict
institution_dict = institution_instance.to_dict()
# create an instance of Institution from a dict
institution_from_dict = Institution.from_dict(institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



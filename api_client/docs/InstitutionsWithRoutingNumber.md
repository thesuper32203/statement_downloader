# InstitutionsWithRoutingNumber

List of institutions with matching routing numbers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of a financial institution, represented as a number | [optional] 
**name** | **str** | The name of the institution | [optional] 
**trans_agg** | **bool** | \&quot;true\&quot;: The institution is certified for the Transaction Aggregation product \&quot;false\&quot;: The institution is decertified for the Transaction Aggregation product | [optional] 
**ach** | **bool** | \&quot;true\&quot;: The institution is certified for the ACH product \&quot;false\&quot;: The institution is decertified for the ACH product | [optional] 
**state_agg** | **bool** | \&quot;true\&quot;: The institution is certified for the Statement Aggregation product \&quot;false\&quot;: The institution is decertified for the Statement Aggregation product | [optional] 
**voi** | **bool** | \&quot;true\&quot;: The institution is certified for the VOI product \&quot;false\&quot;: The institution is decertified for the VOI product | [optional] 
**voa** | **bool** | \&quot;true\&quot;: The institution is certified for the VOA product \&quot;false\&quot;: The institution is decertified for the VOA product | [optional] 
**aha** | **bool** | \&quot;true\&quot;: The institution is certified for the Account History Aggregation product \&quot;false\&quot;: The institution is decertified for the Account History Aggregation product | [optional] 
**avail_balance** | **bool** | \&quot;true\&quot;: The institution is certified for the Account Balance Check (ABC) product \&quot;false\&quot;: The institution is decertified for the Account Balance Check (ABC) product | [optional] 
**account_owner** | **bool** | \&quot;true\&quot;: The institution is certified for the Account Owner product \&quot;false\&quot;: The institution is decertified for the Account Owner product | [optional] 
**student_loan_data** | **bool** | \&quot;true\&quot;: The institution is certified for the Student Loan Data product  \&quot;false\&quot;: The institution is decertified for the Student Loan Data product | [optional] 
**loan_payment_details** | **bool** | \&quot;true\&quot;: The institution is certified for the Loan Payment Detail product  \&quot;false\&quot;: The institution is decertified for the Loan Payment Detail product | [optional] 
**payment_initiation** | **bool** | Institution connection is certified for paymentInitiation | [optional] [default to False]
**bill_pay_data** | **bool** | billPayData is certified | [optional] [default to False]
**liability_data** | **bool** | liabilityData is certified | [optional] [default to False]
**account_type_description** | **str** | Values: Banking, Investments, Credit Cards/Accounts, Workplace Retirement, Mortgages and Loans, Insurance | [optional] 
**phone** | **str** | A phone number (max length 15). | [optional] 
**url_home_app** | **str** | The URL of the institution&#39;s primary home page | [optional] 
**url_logon_app** | **str** | The URL of the institution&#39;s login page | [optional] 
**oauth_enabled** | **bool** | \&quot;true\&quot;: The institution is an OAuth connection  \&quot;false\&quot;: The institution isn&#39;t an OAuth connection | [optional] 
**url_forgot_password** | **str** | Institution&#39;s forgot password page | [optional] 
**url_online_registration** | **str** | Institution&#39;s signup page | [optional] 
**var_class** | **str** | Institution&#39;s class | [optional] 
**special_text** | **str** | Special instructions given to customers for login | [optional] 
**time_zone** | **str** | The time zone of the institution. | [optional] 
**special_instructions** | **List[str]** | Instructions given to the customer before they are sent to the institution website to login for OAuth institutions.  Note: this helps the customer to provide the proper permission for data needed for the application. | [optional] 
**special_instutions_title** | **str** | The title of the special instructions, if one exists or is required. | [optional] 
**address** | [**InstitutionAddress**](InstitutionAddress.md) |  | [optional] 
**currency** | **str** | A currency code | [optional] 
**email** | **str** | An email address | [optional] 
**status** | **str** | Status for the institution: \&quot;online\&quot;, \&quot;offline\&quot;, \&quot;maintenance\&quot;, \&quot;testing\&quot;, \&quot;beta\&quot;, \&quot;validated\&quot;, \&quot;migrating\&quot; | [optional] 
**new_institution_id** | **int** | The ID of a financial institution, represented as a number | [optional] 
**branding** | [**Branding**](Branding.md) |  | [optional] 
**display_name** | **str** | A version of the institution connection name that is more user friendly | [optional] 
**oauth_institution_id** | **int** | The ID of a financial institution, represented as a number | [optional] 
**country_codes** | [**List[InstitutionsWithRoutingNumberCountryCodesInner]**](InstitutionsWithRoutingNumberCountryCodesInner.md) |  | [optional] 
**overall_status_temp** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The overall status for the institution:   - online - Connection is active, financial institution is available and functioning   - offline - Connection is inactive due to an issue. Financial institution is not available in Data Connect search   - maintenance - Financial institution is undergoing planned maintenance and is not available at this time   - testing (Limited Availability)  - A new connection with the financial institution is still undergoing development and is only available to some select partners   - investigating - Connection is new and/or under monitoring due to instability | [optional] 
**trans_agg_status** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The production status for the Transaction Aggregation product for the institution.   - online - product is functioning correctly for the institution   - investigating - product is degraded for the institution and is being investigated   - offline - product is offline for the institution | [optional] 
**voa_status** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The production status for the VOA  product for the institution.   - online - product is functioning correctly for the institution   - investigating - product is degraded for the institution and is being investigated   - offline - product is offline for the institution | [optional] 
**voi_status** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The production status for the VOI product for the institution.   - online - product is functioning correctly for the institution   - investigating - product is degraded for the institution and is being investigated   - offline - product is offline for the institution | [optional] 
**state_agg_status** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The production status for the Statement Aggregation product for the institution.   - online - product is functioning correctly for the institution   - investigating - product is degraded for the institution and is being investigated   - offline - product is offline for the institution | [optional] 
**ach_status** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The production status for the ACH product for the institution.   - online - product is functioning correctly for the institution   - investigating - product is degraded for the institution and is being investigated   - offline - product is offline for the institution | [optional] 
**aha_status** | **str** | Beta Data - Can be ignored. Should use &#x60;status&#x60; field instead. The production status for the Account History Aggregation product for the institution.   - online - product is functioning correctly for the institution   - investigating - product is degraded for the institution and is being investigated   - offline - product is offline for the institution | [optional] 

## Example

```python
from openapi_client.models.institutions_with_routing_number import InstitutionsWithRoutingNumber

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionsWithRoutingNumber from a JSON string
institutions_with_routing_number_instance = InstitutionsWithRoutingNumber.from_json(json)
# print the JSON string representation of the object
print(InstitutionsWithRoutingNumber.to_json())

# convert the object into a dict
institutions_with_routing_number_dict = institutions_with_routing_number_instance.to_dict()
# create an instance of InstitutionsWithRoutingNumber from a dict
institutions_with_routing_number_from_dict = InstitutionsWithRoutingNumber.from_dict(institutions_with_routing_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



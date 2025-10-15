# ConnectJointBorrowerEmailParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | By default, the Data Connect application is in English. You don&#39;t need to pass this parameter unless you want to translate Data Connect into one of our supported languages.  * Spanish (United States): &#x60;es&#x60; * French (Canada): &#x60;fr&#x60;  | [optional] 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**borrowers** | [**List[Borrower]**](Borrower.md) | (MVS) Array of borrowers to pass the primary and joint borrower&#39;s customer and consumer IDs | 
**redirect_uri** | **str** | The URL that customers will be redirected to after completing Mastercard Data Connect.  Required unless Data Connect is embedded inside our application (iframe). Required for NON SDK integrations, should be iOS universal link OR Android app link when Data Connect is hosted in a web view / secure container of the partner mobile app. | [optional] 
**webhook** | **str** | The publicly available URL you want to be notified with events as the user progresses through the application. See [Data Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details. | [optional] 
**webhook_content_type** | **str** | The content type the webhook events will be sent in. Supported types: \&quot;application/json\&quot; and \&quot;application/xml\&quot;. | [optional] [default to 'application/json']
**webhook_data** | **object** | Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**webhook_headers** | **object** | Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**institution_settings** | **object** | Advanced options for configuration of which institutions to display in. See [Institution Settings](https://developer.mastercard.com/open-banking-us/documentation/connect/connect-institutions-settings/). | [optional] 
**email** | [**EmailOptions**](EmailOptions.md) |  | 
**experience** | **str** | The &#x60;experience&#x60; field allows you to customize: * Brand: color and logo * Icon: displayed on the \&quot;Share your data\&quot; page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Data Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company. For each additional experience you create thereafter, they&#39;ll give you a unique ID. See [Configure the Data Connect Experience](https://developer.mastercard.com/open-banking-us/documentation/connect/configure-connect-experience/).  Experience values options: * \&quot;default\&quot;: your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don&#39;t pass the experience parameter, then Data Connect&#39;s out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run. | 
**from_date** | **int** | The &#x60;fromDate&#x60; parameter is used when experiences are associated with a credit decisioning report and any other reports with transaction data. The value is in epoch time and must be 10 digits. Example: 1494449017. If it&#39;s greater than 10 digits, then the &#x60;fromDate&#x60; is set to the credit decisioning report&#39;s default &#x60;fromDate&#x60;.  For an experience that generates multiple reports, the &#x60;fromDate&#x60; gets passed to the reports that support it.  However, Data Connect doesn&#39;t pass this parameter to the following reports: * Pay Statement Extraction Report * VOIE - Paystub (with TXVerify) Report * Statement Report * Verification of Income Report * VOIE - Payroll Report  Note: this field isn&#39;t used if you&#39;re only collecting transaction data without a report. | [optional] 
**report_custom_fields** | [**List[ReportCustomField]**](ReportCustomField.md) | The &#x60;reportCustomFields&#x60; parameter is used when experiences are associated with a credit decisioning report.  Designate up to 5 custom fields that you&#39;d like associated with the report when it&#39;s generated. Every custom field consists of three variables: &#x60;label&#x60;, &#x60;value&#x60;, and &#x60;shown&#x60;. The &#x60;shown&#x60; variable is \&quot;true\&quot; or \&quot;false\&quot;. * \&quot;true\&quot;: (default) display the custom field in the PDF report * \&quot;false\&quot;: don&#39;t display the custom field in the PDF report  For an experience that generates multiple reports, the &#x60;reportCustomFields&#x60; parameter gets passed to all reports.  All custom fields display in the Reseller Billing API. | [optional] 
**single_use_url** | **bool** | \&quot;true\&quot;: The URL link expires after a Data Connect session successfully completes.  Note: when the &#x60;singleUseUrl&#x60; and the &#x60;experience&#x60; parameters are passed in the same call, the &#x60;singleUseUrl&#x60; value overrides the &#x60;singleUseUrl&#x60; value configured in the &#x60;experience&#x60; parameter. | [optional] 

## Example

```python
from openapi_client.models.connect_joint_borrower_email_parameters import ConnectJointBorrowerEmailParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectJointBorrowerEmailParameters from a JSON string
connect_joint_borrower_email_parameters_instance = ConnectJointBorrowerEmailParameters.from_json(json)
# print the JSON string representation of the object
print(ConnectJointBorrowerEmailParameters.to_json())

# convert the object into a dict
connect_joint_borrower_email_parameters_dict = connect_joint_borrower_email_parameters_instance.to_dict()
# create an instance of ConnectJointBorrowerEmailParameters from a dict
connect_joint_borrower_email_parameters_from_dict = ConnectJointBorrowerEmailParameters.from_dict(connect_joint_borrower_email_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



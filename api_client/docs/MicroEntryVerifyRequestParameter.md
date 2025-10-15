# MicroEntryVerifyRequestParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | [optional] 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | [optional] 
**redirect_uri** | **str** | The URL that customers will be redirected to after completing Mastercard Data Connect.  Required unless Data Connect is embedded inside our application (iframe). Required for NON SDK integrations, should be iOS universal link OR Android app link when Data Connect is hosted in a web view / secure container of the partner mobile app. | [optional] 
**webhook** | **str** | The publicly available URL you want to be notified with events as the user progresses through the application. See [Data Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details. | [optional] 
**webhook_content_type** | **str** | The content type the webhook events will be sent in. Supported types: \&quot;application/json\&quot; and \&quot;application/xml\&quot;. | [optional] [default to 'application/json']
**webhook_data** | **object** | Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**webhook_headers** | **object** | Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**experience** | **str** | The &#x60;experience&#x60; field allows you to customize: * Brand: color and logo * Icon: displayed on the \&quot;Share your data\&quot; page * Popular institutions: displayed on the Bank Search page * Report: the credit decisioning report to send when Data Connect completes. * MVS modules: financial, payroll, paystub  Note: the Finicity sales engineers (SE) help you set up a default experience for your company. For each additional experience you create thereafter, they&#39;ll give you a unique ID. See [Configure the Data Connect Experience](https://developer.mastercard.com/open-banking-us/documentation/connect/configure-connect-experience/).  Experience values options: * \&quot;default\&quot;: your default experience (must be defined) * GUID: the code for a different experience * Not defined: If you don&#39;t pass the experience parameter, then Data Connect&#39;s out of the box default experience (add accounts but no branding) is used, and the MVS modules will not run. | [optional] 
**account_id** | **str** | An account ID | [optional] 

## Example

```python
from openapi_client.models.micro_entry_verify_request_parameter import MicroEntryVerifyRequestParameter

# TODO update the JSON string below
json = "{}"
# create an instance of MicroEntryVerifyRequestParameter from a JSON string
micro_entry_verify_request_parameter_instance = MicroEntryVerifyRequestParameter.from_json(json)
# print the JSON string representation of the object
print(MicroEntryVerifyRequestParameter.to_json())

# convert the object into a dict
micro_entry_verify_request_parameter_dict = micro_entry_verify_request_parameter_instance.to_dict()
# create an instance of MicroEntryVerifyRequestParameter from a dict
micro_entry_verify_request_parameter_from_dict = MicroEntryVerifyRequestParameter.from_dict(micro_entry_verify_request_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



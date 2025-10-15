# TransferDepositSwitchParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_agreement** | [**ServiceAgreement**](ServiceAgreement.md) |  | [optional] 
**accounts** | [**List[DepositSwitchAccount]**](DepositSwitchAccount.md) | List of customer accounts (one or more) for Deposit Switch. | 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**language** | **str** | By default, the Data Connect application is in English. You don&#39;t need to pass this parameter unless you want to translate Data Connect into one of our supported languages.  * Spanish (United States): &#x60;es&#x60;  | [optional] 
**webhook** | **str** | The publicly available URL you want to be notified with events as the user progresses through the application. See [Data Connect Webhook Event](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-connect/) for event details. | [optional] 
**webhook_content_type** | **str** | The content type the webhook events will be sent in. Supported types: \&quot;application/json\&quot; and \&quot;application/xml\&quot;. | [optional] [default to 'application/json']
**webhook_data** | **object** | Allows additional identifiable information to be inserted into the payload of connect webhook events. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**webhook_headers** | **object** | Allows additional identifiable information to be included as headers of connect webhook event. See: [Custom Webhooks](https://developer.mastercard.com/open-banking-us/documentation/webhooks/webhooks-custom/). | [optional] 
**redirect_uri** | **str** | The URL that customers will be redirected to after completing Mastercard Data Connect.  Required unless Data Connect is embedded inside our application (iframe). Required for NON SDK integrations, should be iOS universal link OR Android app link when Data Connect is hosted in a web view / secure container of the partner mobile app. | [optional] 
**experience** | **str** | The &#x60;experience&#x60; field allows you to customize:    * To toggle landing screen visibility    Note: the Finicity sales engineers (SE) help you set up a default   experience for your company. For each additional experience you create   thereafter, they&#39;ll give you a unique ID. See [Configure the Data Connect   Experience](https://developer.mastercard.com/open-banking-us/documentation/connect/configure-connect-experience/).     Experience values options:    * \&quot;default\&quot;: your default experience (must be defined)   * GUID: the code for a different experience | [optional] 

## Example

```python
from openapi_client.models.transfer_deposit_switch_parameters import TransferDepositSwitchParameters

# TODO update the JSON string below
json = "{}"
# create an instance of TransferDepositSwitchParameters from a JSON string
transfer_deposit_switch_parameters_instance = TransferDepositSwitchParameters.from_json(json)
# print the JSON string representation of the object
print(TransferDepositSwitchParameters.to_json())

# convert the object into a dict
transfer_deposit_switch_parameters_dict = transfer_deposit_switch_parameters_instance.to_dict()
# create an instance of TransferDepositSwitchParameters from a dict
transfer_deposit_switch_parameters_from_dict = TransferDepositSwitchParameters.from_dict(transfer_deposit_switch_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



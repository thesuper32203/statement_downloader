# ConnectGenerateTransferBillPaySwitchParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_agreement** | [**ServiceAgreement**](ServiceAgreement.md) |  | [optional] 
**accounts** | [**List[DepositSwitchAccount]**](DepositSwitchAccount.md) | List of customer accounts (one or more) for Deposit Switch. | [optional] 
**partner_id** | **str** | Your Partner ID displayed in the [Developer Dashboard](https://developer.mastercard.com/account/log-in) | 
**customer_id** | **str** | A customer ID. See Add Customer API for how to create a customer ID. | 
**experience** | **str** | The &#x60;experience&#x60; field allows you to customize:    * To toggle landing screen visibility    Note: the Finicity sales engineers (SE) help you set up a default   experience for your company. For each additional experience you create   thereafter, they&#39;ll give you a unique ID. See [Configure the Data Connect   Experience](https://developer.mastercard.com/open-banking-us/documentation/connect/configure-connect-experience/).     Experience values options:    * \&quot;default\&quot;: your default experience (must be defined)   * GUID: the code for a different experience | [optional] 
**language** | **str** | By default, the Data Connect application is in English. You don&#39;t need to pass this parameter unless you want to translate Data Connect into one of our supported languages.  * Spanish (United States): &#x60;es&#x60;  | [optional] 
**single_use_url** | **bool** | \&quot;true\&quot;: The URL link expires after a Data Connect session successfully completes.  Note: when the &#x60;singleUseUrl&#x60; and the &#x60;experience&#x60; parameters are passed in the same call, the &#x60;singleUseUrl&#x60; value overrides the &#x60;singleUseUrl&#x60; value configured in the &#x60;experience&#x60; parameter. | 
**redirect_uri** | **str** | The URL that customers will be redirected to after completing Mastercard Data Connect.  Required unless Data Connect is embedded inside our application (iframe). Required for NON SDK integrations, should be iOS universal link OR Android app link when Data Connect is hosted in a web view / secure container of the partner mobile app. | [optional] 
**cards** | [**List[Card]**](Card.md) | List of the user cards. Mandatory when use case is BPS. | 
**identity** | [**BillPaySwitchIdentity**](BillPaySwitchIdentity.md) |  | 

## Example

```python
from openapi_client.models.connect_generate_transfer_bill_pay_switch_parameters import ConnectGenerateTransferBillPaySwitchParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectGenerateTransferBillPaySwitchParameters from a JSON string
connect_generate_transfer_bill_pay_switch_parameters_instance = ConnectGenerateTransferBillPaySwitchParameters.from_json(json)
# print the JSON string representation of the object
print(ConnectGenerateTransferBillPaySwitchParameters.to_json())

# convert the object into a dict
connect_generate_transfer_bill_pay_switch_parameters_dict = connect_generate_transfer_bill_pay_switch_parameters_instance.to_dict()
# create an instance of ConnectGenerateTransferBillPaySwitchParameters from a dict
connect_generate_transfer_bill_pay_switch_parameters_from_dict = ConnectGenerateTransferBillPaySwitchParameters.from_dict(connect_generate_transfer_bill_pay_switch_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



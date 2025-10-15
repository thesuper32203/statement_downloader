# PaySwitchDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | A customer ID | 
**customer_type** | **str** | The type of Mastercard Open Finance customer (&#x60;active&#x60; or &#x60;testing&#x60;) | 
**switch_id** | **str** | Pay switch ID | 
**switch_status** | **str** | Pay switch status. Possible values include &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;failed&#x60;.  * processing - The pay switch is currently being processed. * completed - The pay switch has been completed successfully. * failed - The pay switch has failed. Refer to failureReason for more details.  | 
**failure_reason** | **str** | Pay switch failure reason. Possible values include - * account-lockout - The account is locked out, most likely the end user has had too many failed attempts. * account-unusable - The user&#39;s bank account is unusable for the selected product or use case. * bad-credentials - Either the username or password was incorrect. This is our most common fail reason. * connection-error - A network error occurred which caused the connection between our system and the bank/payroll system to be lost. * device-disconnected - The device used to start the task is no longer connected. * expired - The user&#39;s password has expired and they must create a new one. * no-data-found - No verify data was found for the user. * routing-number-not-supported - The account did not support the routing number entered. * session-timeout - The user&#39;s session timed out. * system-unavailable - The system was unavailable. For example, the site is undergoing maintenance or it is outside the window of scheduled availability for the site. * transaction-pending - There is an allocation already in progress and additional updates cannot be made at this time. * unknown-failure - We encountered an unexpected error. * user-abandon - The user was asked an MFA question, but did not answer the question.  | [optional] 
**created_date** | **str** | Date and time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ) when deposit switch was performed | 
**updated_date** | **str** | Date and time in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ) when deposit switch status was updated | 
**authenticated** | **bool** | Indicates whether or not the pay switch task has successfully authenticated against the payroll system | [optional] 
**provider** | [**PaySwitchDetailsProvider**](PaySwitchDetailsProvider.md) |  | 
**payment_methods** | [**List[PaySwitchDetailsPaymentMethodsInner]**](PaySwitchDetailsPaymentMethodsInner.md) | Pay switch payment details | 

## Example

```python
from openapi_client.models.pay_switch_details import PaySwitchDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaySwitchDetails from a JSON string
pay_switch_details_instance = PaySwitchDetails.from_json(json)
# print the JSON string representation of the object
print(PaySwitchDetails.to_json())

# convert the object into a dict
pay_switch_details_dict = pay_switch_details_instance.to_dict()
# create an instance of PaySwitchDetails from a dict
pay_switch_details_from_dict = PaySwitchDetails.from_dict(pay_switch_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



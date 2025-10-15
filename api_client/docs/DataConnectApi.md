# openapi_client.DataConnectApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_connect_url**](DataConnectApi.md#generate_connect_url) | **POST** /connect/v2/generate | Generate Data Connect URL
[**generate_fix_connect_url**](DataConnectApi.md#generate_fix_connect_url) | **POST** /connect/v2/generate/fix | Generate Fix Data Connect URL
[**generate_joint_borrower_connect_url**](DataConnectApi.md#generate_joint_borrower_connect_url) | **POST** /connect/v2/generate/jointBorrower | Generate Data Connect URL - Joint Borrower
[**generate_lite_connect_url**](DataConnectApi.md#generate_lite_connect_url) | **POST** /connect/v2/generate/lite | Generate Lite Data Connect URL
[**generate_transfer_bill_pay_switch_url**](DataConnectApi.md#generate_transfer_bill_pay_switch_url) | **POST** /connect/generate/transfer/bill-pay-switch | Data Connect Transfer URL for Bill Pay Switch
[**generate_transfer_deposit_switch_url**](DataConnectApi.md#generate_transfer_deposit_switch_url) | **POST** /connect/generate/transfer/deposit-switch | Data Connect Transfer URL for Deposit Switch
[**get_all_experience**](DataConnectApi.md#get_all_experience) | **GET** /connect/experiences | Get Experience IDs
[**send_connect_email**](DataConnectApi.md#send_connect_email) | **POST** /connect/v2/send/email | Send Data Connect Email
[**send_joint_borrower_connect_email**](DataConnectApi.md#send_joint_borrower_connect_email) | **POST** /connect/v2/send/email/jointBorrower | Send Data Connect Email - Joint Borrower
[**verify_micro_entry_microdeposit**](DataConnectApi.md#verify_micro_entry_microdeposit) | **POST** /connect/v2/generate/microentry/verify | Account Validation Assistant User verification of microdeposits


# **generate_connect_url**
> ConnectUrl generate_connect_url(connect_parameters)

Generate Data Connect URL

Generate a Data Connect URL link to add within your own applications.

Optional Parameters:
* `experience`: Configure different customer experiences per Data Connect session by changing the brand, color, logo, icon, the type of credit decisioning report to generate after the session ends, and more.
* `language`: By default, the Data Connect application is in English. You don't need to pass  this parameter unless you want to translate Data Connect into one of our supported languages.

  * Spanish (United States)
  * French (Canada)


MVS Developers: You can pre-populate the consumer's SSN on the Find employment records page at the beginning of the MVS payroll app. Pass the SSN value for the consumer in the body of the request call.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_parameters import ConnectParameters
from openapi_client.models.connect_url import ConnectUrl
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    connect_parameters = openapi_client.ConnectParameters() # ConnectParameters | 

    try:
        # Generate Data Connect URL
        api_response = api_instance.generate_connect_url(connect_parameters)
        print("The response of DataConnectApi->generate_connect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->generate_connect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_parameters** | [**ConnectParameters**](ConnectParameters.md)|  | 

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_fix_connect_url**
> ConnectUrl generate_fix_connect_url(fix_connect_parameters)

Generate Fix Data Connect URL

Use the Data Connect Fix API when the following conditions occur:
* The connection to the user's financial institution is lost
* The user's credentials were updated (for any number of reasons)
* The user's MFA challenge has expired

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_url import ConnectUrl
from openapi_client.models.fix_connect_parameters import FixConnectParameters
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    fix_connect_parameters = openapi_client.FixConnectParameters() # FixConnectParameters | 

    try:
        # Generate Fix Data Connect URL
        api_response = api_instance.generate_fix_connect_url(fix_connect_parameters)
        print("The response of DataConnectApi->generate_fix_connect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->generate_fix_connect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fix_connect_parameters** | [**FixConnectParameters**](FixConnectParameters.md)|  | 

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_joint_borrower_connect_url**
> ConnectUrl generate_joint_borrower_connect_url(connect_joint_borrower_parameters)

Generate Data Connect URL - Joint Borrower

Same as Data Connect Full (`POST /connect/v2/generate`) but for joint borrowers.

MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Data Connect session.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_joint_borrower_parameters import ConnectJointBorrowerParameters
from openapi_client.models.connect_url import ConnectUrl
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    connect_joint_borrower_parameters = openapi_client.ConnectJointBorrowerParameters() # ConnectJointBorrowerParameters | 

    try:
        # Generate Data Connect URL - Joint Borrower
        api_response = api_instance.generate_joint_borrower_connect_url(connect_joint_borrower_parameters)
        print("The response of DataConnectApi->generate_joint_borrower_connect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->generate_joint_borrower_connect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_joint_borrower_parameters** | [**ConnectJointBorrowerParameters**](ConnectJointBorrowerParameters.md)|  | 

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_lite_connect_url**
> ConnectUrl generate_lite_connect_url(lite_connect_parameters)

Generate Lite Data Connect URL

Data Connect Lite is a variation of Data Connect Full (`POST /connect/v2/generate`), which has a limited set of features.
* Sign in, user's credentials, and Multi-Factor Authentication (MFA)
* No user account management

The Data Connect Web SDK isn't a requirement when using Data Connect lite. However, if you want to use the SDK events, routes, and user events, then you must integrate with the Data Connect Web SDK.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_url import ConnectUrl
from openapi_client.models.lite_connect_parameters import LiteConnectParameters
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    lite_connect_parameters = openapi_client.LiteConnectParameters() # LiteConnectParameters | 

    try:
        # Generate Lite Data Connect URL
        api_response = api_instance.generate_lite_connect_url(lite_connect_parameters)
        print("The response of DataConnectApi->generate_lite_connect_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->generate_lite_connect_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lite_connect_parameters** | [**LiteConnectParameters**](LiteConnectParameters.md)|  | 

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_transfer_bill_pay_switch_url**
> ConnectTransferBillPaySwitchLink generate_transfer_bill_pay_switch_url(connect_generate_transfer_bill_pay_switch_parameters)

Data Connect Transfer URL for Bill Pay Switch

Generate a Data Connect Transfer URL which you can use in your application to allow end users to set up a bill pay switch.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_generate_transfer_bill_pay_switch_parameters import ConnectGenerateTransferBillPaySwitchParameters
from openapi_client.models.connect_transfer_bill_pay_switch_link import ConnectTransferBillPaySwitchLink
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    connect_generate_transfer_bill_pay_switch_parameters = openapi_client.ConnectGenerateTransferBillPaySwitchParameters() # ConnectGenerateTransferBillPaySwitchParameters | 

    try:
        # Data Connect Transfer URL for Bill Pay Switch
        api_response = api_instance.generate_transfer_bill_pay_switch_url(connect_generate_transfer_bill_pay_switch_parameters)
        print("The response of DataConnectApi->generate_transfer_bill_pay_switch_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->generate_transfer_bill_pay_switch_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_generate_transfer_bill_pay_switch_parameters** | [**ConnectGenerateTransferBillPaySwitchParameters**](ConnectGenerateTransferBillPaySwitchParameters.md)|  | 

### Return type

[**ConnectTransferBillPaySwitchLink**](ConnectTransferBillPaySwitchLink.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. Returns Data Connect URL. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_transfer_deposit_switch_url**
> ConnectTransferDepositSwitchLink generate_transfer_deposit_switch_url(transfer_deposit_switch_parameters)

Data Connect Transfer URL for Deposit Switch

Generate a Data Connect Transfer URL which you can use in your application to allow end users to set up a deposit switch.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_transfer_deposit_switch_link import ConnectTransferDepositSwitchLink
from openapi_client.models.transfer_deposit_switch_parameters import TransferDepositSwitchParameters
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    transfer_deposit_switch_parameters = openapi_client.TransferDepositSwitchParameters() # TransferDepositSwitchParameters | 

    try:
        # Data Connect Transfer URL for Deposit Switch
        api_response = api_instance.generate_transfer_deposit_switch_url(transfer_deposit_switch_parameters)
        print("The response of DataConnectApi->generate_transfer_deposit_switch_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->generate_transfer_deposit_switch_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_deposit_switch_parameters** | [**TransferDepositSwitchParameters**](TransferDepositSwitchParameters.md)|  | 

### Return type

[**ConnectTransferDepositSwitchLink**](ConnectTransferDepositSwitchLink.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. Returns Data Connect URL. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_experience**
> List[Experiences] get_all_experience(app_name, product_code=product_code)

Get Experience IDs

Retrieve Data Connect experiences by application name. Optionally, filter the experiences by product codes.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.experiences import Experiences
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    app_name = 'test app' # str | Unique name of the application provided to Mastercard during app registration.
    product_code = ['[\"ABC\"]'] # List[str] | Filter the results by product code (a unique billing code assigned to each Open Finance product used). Specify either one single product or multiple products separated by commas. (optional)

    try:
        # Get Experience IDs
        api_response = api_instance.get_all_experience(app_name, product_code=product_code)
        print("The response of DataConnectApi->get_all_experience:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->get_all_experience: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **str**| Unique name of the application provided to Mastercard during app registration. | 
 **product_code** | [**List[str]**](str.md)| Filter the results by product code (a unique billing code assigned to each Open Finance product used). Specify either one single product or multiple products separated by commas. | [optional] 

### Return type

[**List[Experiences]**](Experiences.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response. Returns all retrieved Experience. |  -  |
**400** | The request was rejected. |  -  |
**404** | The requested entity was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_connect_email**
> ConnectEmailUrl send_connect_email(connect_email_parameters)

Send Data Connect Email

Same as Data Connect Full (`POST /connect/v2/generate`) but send a Data Connect email to a consumer.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_email_parameters import ConnectEmailParameters
from openapi_client.models.connect_email_url import ConnectEmailUrl
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    connect_email_parameters = openapi_client.ConnectEmailParameters() # ConnectEmailParameters | 

    try:
        # Send Data Connect Email
        api_response = api_instance.send_connect_email(connect_email_parameters)
        print("The response of DataConnectApi->send_connect_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->send_connect_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_email_parameters** | [**ConnectEmailParameters**](ConnectEmailParameters.md)|  | 

### Return type

[**ConnectEmailUrl**](ConnectEmailUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated and the email sent |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_joint_borrower_connect_email**
> ConnectEmailUrl send_joint_borrower_connect_email(connect_joint_borrower_email_parameters)

Send Data Connect Email - Joint Borrower

Same as Data Connect Joint Borrower (`POST /connect/v2/generate/jointBorrower`) but send a Data Connect email  to at least one of the joint borrower's email addresses.

When the consumer opens the email, MVS prompts both the primary and joint borrower to enter each of their financial, payroll, and paystub information in the same Data Connect session.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_email_url import ConnectEmailUrl
from openapi_client.models.connect_joint_borrower_email_parameters import ConnectJointBorrowerEmailParameters
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    connect_joint_borrower_email_parameters = openapi_client.ConnectJointBorrowerEmailParameters() # ConnectJointBorrowerEmailParameters | 

    try:
        # Send Data Connect Email - Joint Borrower
        api_response = api_instance.send_joint_borrower_connect_email(connect_joint_borrower_email_parameters)
        print("The response of DataConnectApi->send_joint_borrower_connect_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->send_joint_borrower_connect_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_joint_borrower_email_parameters** | [**ConnectJointBorrowerEmailParameters**](ConnectJointBorrowerEmailParameters.md)|  | 

### Return type

[**ConnectEmailUrl**](ConnectEmailUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated and the email sent |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_micro_entry_microdeposit**
> ConnectUrl verify_micro_entry_microdeposit(micro_entry_verify_request_parameter)

Account Validation Assistant User verification of microdeposits

The UI re-engages the consumer to enter two microdeposit amounts found in their account and validates them.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.connect_url import ConnectUrl
from openapi_client.models.micro_entry_verify_request_parameter import MicroEntryVerifyRequestParameter
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finicity.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.finicity.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: FinicityAppToken
configuration.api_key['FinicityAppToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppToken'] = 'Bearer'

# Configure API key authorization: FinicityAppKey
configuration.api_key['FinicityAppKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['FinicityAppKey'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataConnectApi(api_client)
    micro_entry_verify_request_parameter = openapi_client.MicroEntryVerifyRequestParameter() # MicroEntryVerifyRequestParameter | 

    try:
        # Account Validation Assistant User verification of microdeposits
        api_response = api_instance.verify_micro_entry_microdeposit(micro_entry_verify_request_parameter)
        print("The response of DataConnectApi->verify_micro_entry_microdeposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataConnectApi->verify_micro_entry_microdeposit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **micro_entry_verify_request_parameter** | [**MicroEntryVerifyRequestParameter**](MicroEntryVerifyRequestParameter.md)|  | 

### Return type

[**ConnectUrl**](ConnectUrl.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The URL link was successfully generated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


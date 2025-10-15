# openapi_client.AccountValidationAssistanceApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_micro_deposits_details**](AccountValidationAssistanceApi.md#get_micro_deposits_details) | **GET** /microentry/v1/customers/{customerId}/accounts/{accountId} | Get Micro Entries Details
[**initiate_micro_amount_deposits**](AccountValidationAssistanceApi.md#initiate_micro_amount_deposits) | **POST** /microentry/v1/customers/{customerId} | Initiate Micro Entries
[**verify_micro_amount_deposits**](AccountValidationAssistanceApi.md#verify_micro_amount_deposits) | **POST** /microentry/v1/customers/{customerId}/accounts/{accountId}/amounts | Verify Micro Entries


# **get_micro_deposits_details**
> MicroDepositDetails get_micro_deposits_details(customer_id, account_id)

Get Micro Entries Details

Fetch the micro entries details.
`customerId` and `accountId` are the identifiers of the customer and account receiving the micro entries.

  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.micro_deposit_details import MicroDepositDetails
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
    api_instance = openapi_client.AccountValidationAssistanceApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID

    try:
        # Get Micro Entries Details
        api_response = api_instance.get_micro_deposits_details(customer_id, account_id)
        print("The response of AccountValidationAssistanceApi->get_micro_deposits_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountValidationAssistanceApi->get_micro_deposits_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 

### Return type

[**MicroDepositDetails**](MicroDepositDetails.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Micro entries were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_micro_amount_deposits**
> InitiatedMicroDeposit initiate_micro_amount_deposits(customer_id, micro_deposit_initiation)

Initiate Micro Entries

Initiate the micro entries to customer's account.

Two random micro amounts less than a dollar each will be deposited to provided customer's account.

  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.initiated_micro_deposit import InitiatedMicroDeposit
from openapi_client.models.micro_deposit_initiation import MicroDepositInitiation
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
    api_instance = openapi_client.AccountValidationAssistanceApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    micro_deposit_initiation = openapi_client.MicroDepositInitiation() # MicroDepositInitiation | 

    try:
        # Initiate Micro Entries
        api_response = api_instance.initiate_micro_amount_deposits(customer_id, micro_deposit_initiation)
        print("The response of AccountValidationAssistanceApi->initiate_micro_amount_deposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountValidationAssistanceApi->initiate_micro_amount_deposits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **micro_deposit_initiation** | [**MicroDepositInitiation**](MicroDepositInitiation.md)|  | 

### Return type

[**InitiatedMicroDeposit**](InitiatedMicroDeposit.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Micro entries were successfully initiated |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |
**409** | The resource already exists |  -  |
**429** | The service can&#39;t accept more requests or is not available from the Test Drive. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_micro_amount_deposits**
> VerifiedMicroDeposit verify_micro_amount_deposits(customer_id, account_id, micro_deposit_verification)

Verify Micro Entries

Verify the micro entries as received by customer in customer's account.
Customer needs to verify the micro amounts received in customer's account. `customerId` and `accountId` are the identifiers of the customer and account  receiving the micro entries.

  _Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.micro_deposit_verification import MicroDepositVerification
from openapi_client.models.verified_micro_deposit import VerifiedMicroDeposit
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
    api_instance = openapi_client.AccountValidationAssistanceApi(api_client)
    customer_id = '1005061234' # str | A customer ID
    account_id = '5011648377' # str | The account ID
    micro_deposit_verification = openapi_client.MicroDepositVerification() # MicroDepositVerification | 

    try:
        # Verify Micro Entries
        api_response = api_instance.verify_micro_amount_deposits(customer_id, account_id, micro_deposit_verification)
        print("The response of AccountValidationAssistanceApi->verify_micro_amount_deposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountValidationAssistanceApi->verify_micro_amount_deposits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A customer ID | 
 **account_id** | **str**| The account ID | 
 **micro_deposit_verification** | [**MicroDepositVerification**](MicroDepositVerification.md)|  | 

### Return type

[**VerifiedMicroDeposit**](VerifiedMicroDeposit.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Micro entries were successfully verified |  -  |
**400** | Micro entries verification failed. status field could be any except \&quot;Verified\&quot; and \&quot;Completed\&quot;. |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


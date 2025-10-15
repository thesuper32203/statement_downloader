# openapi_client.TransferApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_deposit_switches**](TransferApi.md#get_all_deposit_switches) | **GET** /transfer/customers/{customer_id}/deposit-switches | Get Deposit Switches by Customer ID
[**get_all_pay_switches**](TransferApi.md#get_all_pay_switches) | **GET** /transfer/customers/{customer_id}/bill-pay-switches | Get Pay Switches by Customer ID
[**get_bill_pay_switch_details**](TransferApi.md#get_bill_pay_switch_details) | **GET** /transfer/customers/{customer_id}/bill-pay-switches/{switch_id} | Get Pay Switch by ID
[**get_deposit_switch_details**](TransferApi.md#get_deposit_switch_details) | **GET** /transfer/customers/{customer_id}/deposit-switches/{switch_id} | Get Deposit Switch by ID


# **get_all_deposit_switches**
> DepositSwitchesSummary get_all_deposit_switches(customer_id)

Get Deposit Switches by Customer ID

Retrieve summary of deposit switches performed by given customer ID.
_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.deposit_switches_summary import DepositSwitchesSummary
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
    api_instance = openapi_client.TransferApi(api_client)
    customer_id = '1005061234' # str | Unique identifier of the customer

    try:
        # Get Deposit Switches by Customer ID
        api_response = api_instance.get_all_deposit_switches(customer_id)
        print("The response of TransferApi->get_all_deposit_switches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->get_all_deposit_switches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer | 

### Return type

[**DepositSwitchesSummary**](DepositSwitchesSummary.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deposit switches performed by the customer |  -  |
**400** | The request was rejected. |  -  |
**404** | The requested entity was not found |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pay_switches**
> PaySwitchesSummary get_all_pay_switches(customer_id)

Get Pay Switches by Customer ID

Retrieve summary of bill pay switches performed by given customer ID.
_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.pay_switches_summary import PaySwitchesSummary
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
    api_instance = openapi_client.TransferApi(api_client)
    customer_id = '1005061234' # str | Unique identifier of the customer

    try:
        # Get Pay Switches by Customer ID
        api_response = api_instance.get_all_pay_switches(customer_id)
        print("The response of TransferApi->get_all_pay_switches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->get_all_pay_switches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer | 

### Return type

[**PaySwitchesSummary**](PaySwitchesSummary.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pay switches performed by the customer |  -  |
**400** | The request was rejected. |  -  |
**404** | The requested entity was not found |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_pay_switch_details**
> PaySwitchDetails get_bill_pay_switch_details(customer_id, switch_id)

Get Pay Switch by ID

Retrieve bill pay switch details by switch ID.
_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.pay_switch_details import PaySwitchDetails
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
    api_instance = openapi_client.TransferApi(api_client)
    customer_id = '1005061234' # str | Unique identifier of the customer
    switch_id = '65cb40beec86d3bd0e8664cc' # str | Deposit Switch ID

    try:
        # Get Pay Switch by ID
        api_response = api_instance.get_bill_pay_switch_details(customer_id, switch_id)
        print("The response of TransferApi->get_bill_pay_switch_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->get_bill_pay_switch_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer | 
 **switch_id** | **str**| Deposit Switch ID | 

### Return type

[**PaySwitchDetails**](PaySwitchDetails.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pay switch details |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deposit_switch_details**
> DepositSwitchDetails get_deposit_switch_details(customer_id, switch_id)

Get Deposit Switch by ID

Retrieve deposit switch details by switch ID.
_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.deposit_switch_details import DepositSwitchDetails
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
    api_instance = openapi_client.TransferApi(api_client)
    customer_id = '1005061234' # str | Unique identifier of the customer
    switch_id = '65cb40beec86d3bd0e8664cc' # str | Deposit Switch ID

    try:
        # Get Deposit Switch by ID
        api_response = api_instance.get_deposit_switch_details(customer_id, switch_id)
        print("The response of TransferApi->get_deposit_switch_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransferApi->get_deposit_switch_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of the customer | 
 **switch_id** | **str**| Deposit Switch ID | 

### Return type

[**DepositSwitchDetails**](DepositSwitchDetails.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deposit switch details |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


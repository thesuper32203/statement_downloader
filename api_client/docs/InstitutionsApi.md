# openapi_client.InstitutionsApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certified_institutions**](InstitutionsApi.md#get_certified_institutions) | **GET** /institution/v2/certifiedInstitutions | Get Certified Institutions
[**get_certified_institutions_with_rssd**](InstitutionsApi.md#get_certified_institutions_with_rssd) | **GET** /institution/v2/certifiedInstitutions/rssd | Get Certified Institutions With RSSD
[**get_institution**](InstitutionsApi.md#get_institution) | **GET** /institution/v2/institutions/{institutionId} | Get Institution by ID
[**get_institution_branding**](InstitutionsApi.md#get_institution_branding) | **GET** /institution/v2/institutions/{institutionId}/branding | Get Institution Branding by ID
[**get_institutions**](InstitutionsApi.md#get_institutions) | **GET** /institution/v2/institutions | Get Institutions
[**get_institutions_by_routing_number**](InstitutionsApi.md#get_institutions_by_routing_number) | **GET** /institution/v1/institutions/routingNumber/{routing_number} | Get Institutions by Routing Number


# **get_certified_institutions**
> CertifiedInstitutions get_certified_institutions(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)

Get Certified Institutions

Search for financial institutions by certified product.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.certified_institutions import CertifiedInstitutions
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
    api_instance = openapi_client.InstitutionsApi(api_client)
    search = 'finbank' # str | Search term (financial institution `name` field). Leave empty for all FIs. (optional)
    start = 1 # int | Index of the page of results to return (optional) (default to 1)
    limit = 25 # int | Maximum number of results per page (optional) (default to 25)
    type = 'voa' # str | A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\" (optional)
    supported_countries = ['us'] # List[str] | A list of country codes, '*' for all countries. (optional)

    try:
        # Get Certified Institutions
        api_response = api_instance.get_certified_institutions(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)
        print("The response of InstitutionsApi->get_certified_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_certified_institutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term (financial institution &#x60;name&#x60; field). Leave empty for all FIs. | [optional] 
 **start** | **int**| Index of the page of results to return | [optional] [default to 1]
 **limit** | **int**| Maximum number of results per page | [optional] [default to 25]
 **type** | **str**| A product type: \&quot;transAgg\&quot;, \&quot;ach\&quot;, \&quot;stateAgg\&quot;, \&quot;voi\&quot;, \&quot;voa\&quot;, \&quot;aha\&quot;, \&quot;availBalance\&quot;, \&quot;accountOwner\&quot; | [optional] 
 **supported_countries** | [**List[str]**](str.md)| A list of country codes, &#39;*&#39; for all countries. | [optional] 

### Return type

[**CertifiedInstitutions**](CertifiedInstitutions.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institutions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certified_institutions_with_rssd**
> CertifiedInstitutions get_certified_institutions_with_rssd(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)

Get Certified Institutions With RSSD

Search for certified financial institutions w/RSSD.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.certified_institutions import CertifiedInstitutions
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
    api_instance = openapi_client.InstitutionsApi(api_client)
    search = 'finbank' # str | Search term (financial institution `name` field). Leave empty for all FIs. (optional)
    start = 1 # int | Index of the page of results to return (optional) (default to 1)
    limit = 25 # int | Maximum number of results per page (optional) (default to 25)
    type = 'voa' # str | A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\" (optional)
    supported_countries = ['us'] # List[str] | A list of country codes, '*' for all countries. (optional)

    try:
        # Get Certified Institutions With RSSD
        api_response = api_instance.get_certified_institutions_with_rssd(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)
        print("The response of InstitutionsApi->get_certified_institutions_with_rssd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_certified_institutions_with_rssd: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term (financial institution &#x60;name&#x60; field). Leave empty for all FIs. | [optional] 
 **start** | **int**| Index of the page of results to return | [optional] [default to 1]
 **limit** | **int**| Maximum number of results per page | [optional] [default to 25]
 **type** | **str**| A product type: \&quot;transAgg\&quot;, \&quot;ach\&quot;, \&quot;stateAgg\&quot;, \&quot;voi\&quot;, \&quot;voa\&quot;, \&quot;aha\&quot;, \&quot;availBalance\&quot;, \&quot;accountOwner\&quot; | [optional] 
 **supported_countries** | [**List[str]**](str.md)| A list of country codes, &#39;*&#39; for all countries. | [optional] 

### Return type

[**CertifiedInstitutions**](CertifiedInstitutions.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institutions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institution**
> InstitutionWrapper get_institution(institution_id)

Get Institution by ID

Get financial institution details by ID.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.institution_wrapper import InstitutionWrapper
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
    api_instance = openapi_client.InstitutionsApi(api_client)
    institution_id = 4222 # int | The institution ID

    try:
        # Get Institution by ID
        api_response = api_instance.get_institution(institution_id)
        print("The response of InstitutionsApi->get_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **int**| The institution ID | 

### Return type

[**InstitutionWrapper**](InstitutionWrapper.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institution was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institution_branding**
> BrandingWrapper get_institution_branding(institution_id)

Get Institution Branding by ID

Return the branding information for a financial institution.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.branding_wrapper import BrandingWrapper
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
    api_instance = openapi_client.InstitutionsApi(api_client)
    institution_id = 4222 # int | The institution ID

    try:
        # Get Institution Branding by ID
        api_response = api_instance.get_institution_branding(institution_id)
        print("The response of InstitutionsApi->get_institution_branding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institution_branding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_id** | **int**| The institution ID | 

### Return type

[**BrandingWrapper**](BrandingWrapper.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institution branding was successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | The resource doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institutions**
> Institutions get_institutions(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)

Get Institutions

Search for financial institutions.

_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.institutions import Institutions
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
    api_instance = openapi_client.InstitutionsApi(api_client)
    search = 'finbank' # str | Search term (financial institution `name` field). Leave empty for all FIs. (optional)
    start = 1 # int | Index of the page of results to return (optional) (default to 1)
    limit = 25 # int | Maximum number of results per page (optional) (default to 25)
    type = 'voa' # str | A product type: \"transAgg\", \"ach\", \"stateAgg\", \"voi\", \"voa\", \"aha\", \"availBalance\", \"accountOwner\" (optional)
    supported_countries = ['us'] # List[str] | A list of country codes, '*' for all countries. (optional)

    try:
        # Get Institutions
        api_response = api_instance.get_institutions(search=search, start=start, limit=limit, type=type, supported_countries=supported_countries)
        print("The response of InstitutionsApi->get_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institutions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term (financial institution &#x60;name&#x60; field). Leave empty for all FIs. | [optional] 
 **start** | **int**| Index of the page of results to return | [optional] [default to 1]
 **limit** | **int**| Maximum number of results per page | [optional] [default to 25]
 **type** | **str**| A product type: \&quot;transAgg\&quot;, \&quot;ach\&quot;, \&quot;stateAgg\&quot;, \&quot;voi\&quot;, \&quot;voa\&quot;, \&quot;aha\&quot;, \&quot;availBalance\&quot;, \&quot;accountOwner\&quot; | [optional] 
 **supported_countries** | [**List[str]**](str.md)| A list of country codes, &#39;*&#39; for all countries. | [optional] 

### Return type

[**Institutions**](Institutions.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Institutions were successfully retrieved |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_institutions_by_routing_number**
> GetInstitutionsByRoutingNumber200Response get_institutions_by_routing_number(routing_number)

Get Institutions by Routing Number

Get institution details for a given routing number. The endpoint will return an error if it is unable to find a match for the routing number or if the routing number provided is not the correct length.  <br><br> Please note, this endpoint only returns FIs that are mapped to Mastercard financial institutions.  Not every institution can be mapped as not every institution type has a routing number.


_Supported regions_: ![🇺🇸](https://flagcdn.com/20x15/us.png)

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.get_institutions_by_routing_number200_response import GetInstitutionsByRoutingNumber200Response
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
    api_instance = openapi_client.InstitutionsApi(api_client)
    routing_number = 847392234 # int | Institution routing number

    try:
        # Get Institutions by Routing Number
        api_response = api_instance.get_institutions_by_routing_number(routing_number)
        print("The response of InstitutionsApi->get_institutions_by_routing_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->get_institutions_by_routing_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_number** | **int**| Institution routing number | 

### Return type

[**GetInstitutionsByRoutingNumber200Response**](GetInstitutionsByRoutingNumber200Response.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response will contain institution connections that were associated with the provided routing number. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


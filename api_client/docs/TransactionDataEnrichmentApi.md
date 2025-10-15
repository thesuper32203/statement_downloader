# openapi_client.TransactionDataEnrichmentApi

All URIs are relative to *https://api.finicity.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrich_transactions**](TransactionDataEnrichmentApi.md#enrich_transactions) | **POST** /data-enrichment/transactions | Performs enrichment of the provided transactions


# **enrich_transactions**
> EnrichedTransactions enrich_transactions(enrich_transactions_payload)

Performs enrichment of the provided transactions

The operation processes the enclosed transactions for enrichment with categorization and entity recognition. Accepts a batch of 1000 transactions.

### Example

* Api Key Authentication (FinicityAppToken):
* Api Key Authentication (FinicityAppKey):

```python
import openapi_client
from openapi_client.models.enrich_transactions_payload import EnrichTransactionsPayload
from openapi_client.models.enriched_transactions import EnrichedTransactions
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
    api_instance = openapi_client.TransactionDataEnrichmentApi(api_client)
    enrich_transactions_payload = openapi_client.EnrichTransactionsPayload() # EnrichTransactionsPayload | A list of maximum of 1000 transactions to submit for transaction enrichment

    try:
        # Performs enrichment of the provided transactions
        api_response = api_instance.enrich_transactions(enrich_transactions_payload)
        print("The response of TransactionDataEnrichmentApi->enrich_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionDataEnrichmentApi->enrich_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrich_transactions_payload** | [**EnrichTransactionsPayload**](EnrichTransactionsPayload.md)| A list of maximum of 1000 transactions to submit for transaction enrichment | 

### Return type

[**EnrichedTransactions**](EnrichedTransactions.md)

### Authorization

[FinicityAppToken](../README.md#FinicityAppToken), [FinicityAppKey](../README.md#FinicityAppKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Enriched Transactions Response. |  -  |
**400** | The request was rejected |  -  |
**401** | The request lacks valid authentication credentials. Check \&quot;Finicity-App-Key\&quot; or \&quot;Finicity-App-Token\&quot;. |  -  |
**404** | Resource not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


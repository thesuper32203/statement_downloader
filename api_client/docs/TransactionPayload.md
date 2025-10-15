# TransactionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_customer_id** | **str** | A unique identifier assigned to the customer for a particular institution. __Note:__ The externalCustomerId and externalAccountId fields are to allow you to map the transactions back to your data. __Do not send Mastercard plaintext representations of customer or account IDs.__ The representative IDs must be obfuscated through cryptographically strong hashing (we recommend using SHA-2 or SHA-3 methods). | 
**external_account_id** | **str** | A unique identifier assigned to the accounts for a particular institution. __Note:__ The externalCustomerId and externalAccountId fields are to allow you to map the transactions back to your data. __Do not send Mastercard plaintext representations of customer or account IDs.__ The representative IDs must be obfuscated through cryptographically strong hashing (we recommend using SHA-2 or SHA-3 methods). | 
**account_type** | **str** | Indicates the type of account associated with the transaction. Listed below are the current account types supported:  \&quot;checking\&quot;, \&quot;savings\&quot;, \&quot;creditCard\&quot;, \&quot;brokerageAccount\&quot;, \&quot;investment\&quot;, \&quot;healthSavingsAccount\&quot;, \&quot;unknown\&quot;  NOTE : If \&quot;unknown\&quot; is provided, the enrichment service will assume it is a \&quot;checking\&quot; account. An incorrect assumption could impact the results from the enrichment service.  | 
**external_transaction_id** | **str** | A unique identifier for the transaction that assists in linking data back to your systems. | 
**posted_timestamp** | **str** | The date and time when the transaction was officially recorded in the account.  Supported formats are yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;, yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;, yyyy-MM-dd HH:mm:ss.0, yyyy-MM-dd.  | [optional] 
**transaction_timestamp** | **str** | The exact date and time when the transaction was initiated or occurred.  Supported formats are yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;, yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;, yyyy-MM-dd HH:mm:ss.0, yyyy-MM-dd.  | 
**description** | **str** | Description of the transaction. | 
**memo** | **str** | Memo of the transaction. | [optional] 
**amount** | **float** | Value amount for transaction. | 
**transaction_fee** | **float** | A charge applied to the transaction. | [optional] 
**type** | **str** | Type of the transaction. | [optional] 
**direction_indicator** | **str** | - The directionIndicator should be from the perspective of the account holder. - If you always send us positive amount values, you MUST send us corresponding directionIndicator values to ensure the categorization logic works as intended. - If you have internal logic to provide the amount field as either positive or negative, do not send us data in the directionIndicator.  - Listed below are the current directionIndicator types supported:   - \&quot;Debit\&quot;   - \&quot;Credit\&quot;  | [optional] 
**additional_details** | **Dict[str, str]** | A dictionary containing additional details of the transaction being returned in the enrichment response. - This object should not contain any PII. - The max number of allowed keys are 30. - The key max length should be 100. - The value max length should be 255.  | [optional] 
**card_acceptor_id** | **str** | Also known as CAID, Merchant ID, or DE42, cardAcceptorId is an alphanumeric string assigned by the acquiring bank (Acquirer) to a merchant or merchant location. It serves as a unique identifier for the point of transaction origin, such as a physical store, payment terminal, or online checkout page. | [optional] 
**input_is_recurring_transaction** | **bool** | A flag indicating whether the transaction is recurring or not. | [optional] 
**input_merchant_information** | [**InputMerchantInformation**](InputMerchantInformation.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_payload import TransactionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPayload from a JSON string
transaction_payload_instance = TransactionPayload.from_json(json)
# print the JSON string representation of the object
print(TransactionPayload.to_json())

# convert the object into a dict
transaction_payload_dict = transaction_payload_instance.to_dict()
# create an instance of TransactionPayload from a dict
transaction_payload_from_dict = TransactionPayload.from_dict(transaction_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



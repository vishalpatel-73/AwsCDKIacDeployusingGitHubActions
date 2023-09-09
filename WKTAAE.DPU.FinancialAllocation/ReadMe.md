# Space to Utils Project

## Statement JSON Contracts Excercise

- Generate JSON output from GetStatement API's response. 

### Sample C# Request to call GetStatement API:

```
using System;
using System.Net.Http.Headers;
using System.Text;
using System.Net.Http;
using System.Web;
using System.IO;

namespace CSHttpClientSample
{
    static class Program
    {
        static void Main()
        {
            MakeRequest();
            Console.WriteLine("Hit ENTER to exit...");
            Console.ReadLine();
        }

        static async void MakeRequest()
        {
            var client = new HttpClient();


            // Request headers

    client.DefaultRequestHeaders.Add("x-aaaorganizationalunitid", "2018ca86-b631-4a61-b350-ae3e00788a00");
    
    client.DefaultRequestHeaders.Add("x-masteradministrationid", "ca071f4b-a77d-495d-a57e-0d3081203265");
    
            client.DefaultRequestHeaders.CacheControl = CacheControlHeaderValue.Parse("no-cache");

    client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", "dbae0f24842245069b0e17be5cc931fb");
    var uri = "https://znlwe-d002-b198-apim-d1-fis1.azure-api.net/pub/statements/01H7D2K7N46NHE21FYXNK91R6S";

var response = await client.GetAsync(uri);

        }
    }
}

```

### Response:
```
{
    "id": "01H7D2K7N46NHE21FYXNK91R6S",
    "additionalData": {
        "codaReferenceData": {
            "fileReference": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
            "paperStatementNumber": 100,
            "relatedReference": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "transactionReference": "ABCDEF"
        },
        "creditCardAccount": null,
        "creditCardBankInformation": null
    },
    "bank": {
        "bankIdentificationNumber": 0,
        "BIC": "NAP",
        "name": "Not A Bank"
    },
    "bankAccount": {
        "accountNumber": "BE68539007547034",
        "currencyCode": "EUR",
        "customerParty": {
            "address": ["Lodorp 76"],
            "city": "Malderen",
            "countryCode": "BE",
            "name": "Anoeshka Pepers",
            "zip": "1840 "
        },
        "description": "Alladins Lamp"
    },
    "communication": "Dit is een test file",
    "initialBalance": {
        "balanceDate": "2023-07-01T00:00:00",
        "isNegative": true,
        "value": 100.0
    },
    "isDuplicate": false,
    "metadata": {
        "correlationId": "a0b02502-dbd3-42c0-8cd9-63672dba347f",
        "creationDate": "2023-08-09T08:20:00Z",
        "documentAttachments": [{
            "documentId": "e15fdd16-5317-4eb4-b4de-32e0bb576d66",
            "documentType": "Pdf",
            "purpose": "Archive",
            "store": "FIS"
        }],
        "influxType": "DailyFeed",
        "masterAdministrationId": "ca071f4b-a77d-495d-a57e-0d3081203265",
        "organizationId": "2018ca86-b631-4a61-b350-ae3e00788a00",
        "unmappedXmlElements": null
    },
    "movements": [{
        "amount": {
            "currencyCode": "EUR",
            "isNegative": true,
            "value": 1.0,
            "valueType": "NetAmount"
        },
        "counterParty": {
            "accountNumber": null,
            "address": null,
            "bic": "BE16557683824374",
            "identificationCode": null,
            "locality": null,
            "name": "Cyrelle Hillen"
        },
        "customerReference": "ABCDEFGHIJK",
        "date": "2023-07-22T00:00:00",
        "details": null,
        "extensions": {
            "ATMPOSDebit": null,
            "bankCommunication": null,
            "calculationMethod": null,
            "credit": null,
            "creditCardMovementData": null,
            "creditorReference": null,
            "codaTransactionCodes": null,
            "codaPurposeCodes": null,
            "detailAmountInformation": null,
            "europeanDirectDebitSEPA": null,
            "numberOfCreditCard": null,
            "OGM": {
                "isReconstituted": false,
                "value": "335555038793"
            },
            "originalTransactionAmount": null,
            "POSCreditGlobalisation": null,
            "POSCreditIndivualTransaction": null,
            "terminalCashDeposit": null,
            "termInvestment": null,
            "ultimateBeneficiaryOrCreditorIdentification": null,
            "ultimateOrderingCustomerOrDebtorIdentification": null
        },
        "id": "01H5S1QH0GR3DDKNHVMMVZ96TH",
        "message": null,
        "referenceNumber": "ABCDEFGHIJKLMNOPQ",
        "sequenceNumber": 0,
        "type": "BankAccountMovement"
    }],
    "newBalance": {
        "balanceDate": "2023-07-31T00:00:00",
        "isNegative": true,
        "value": 99.0
    },
    "sourceType": "BankStatement",
    "statementNumber": 666,
    "totalCreditAmount": 0.0,
    "totalDebitAmount": 0.0
}
```


## Generate JSON output as:
```
{
	"id": "01H7D2K7N46NHE21FYXNK91R6S",
	"fileType": "BankStatement",
	"statementNumber": 666,
	"paperStatementNumber": 100,
	"bankAccount": {
		"accountNumber": "BE68539007547034",
		"currencyCode": "EUR"
	},
	"initialBalance": {
		"balanceDate": "2023-07-01T00:00:00",
		"isNegative": true,
		"value": 100.0
	},
	"finalBalance": {
		"balanceDate": "2023-07-31T00:00:00",
		"isNegative": true,
		"value": 99.0
	},
	"extensionZone": "",
	"movements": [
		{
			"id": "01H5S1QH0GR3DDKNHVMMVZ96TH",
			"sequenceNumber": 1,
			"date": "2023-07-22T00:00:00",
			"foreignAmount": {
				"currencyCode": "USD",
				"isNegative": true,
				"value": 5.0
			},
			"amount": {
				"currencyCode": "EUR",
				"isNegative": true,
				"value": 10.0
			},
			"bookingTarget": "SuspenseAccount",
			"transactionCodes": "151",
			"details": [
				{
					"id": "01H83NNJN5WAZ3F2JPHZHABERT",
					"detailNr": 1,
					"date": "2023-07-22T00:00:00",
					"amount": {
						"currencyCode": "EUR",
						"isNegative": true,
						"value": 10.0
					},
					"bookingTarget": "SuspenseAccount",
					"transactionCodes": "151"
				}
			],
			"type": "BankAccountMovement"
		},
		{
			"id": "01H83YKGFEMCA3Y9YXGVXM461M",
			"sequenceNumber": 1,
			"date": "2023-07-22T00:00:00",
			"foreignAmount": {
				"currencyCode": "USD",
				"isNegative": true,
				"value": 5.0
			},
			"amount": {
				"currencyCode": "EUR",
				"isNegative": true,
				"value": 10.0
			},
			"bookingTarget": "SuspenseAccount",
			"transactionCodes": "151",
			"details": [
				{
					"id": "01H83NNJN5WAZ3F2JPHZHABERT",
					"detailNr": 1,
					"date": "2023-07-22T00:00:00",
					"amount": {
						"currencyCode": "EUR",
						"isNegative": true,
						"value": 10.0
					},
					"bookingTarget": "SuspenseAccount",
					"transactionCodes": "151"
				}
			],
			"type": "BankAccountMovement"
		}
	]
}
```

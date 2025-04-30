from azure.identity import AzureCliCredential
from azure.mgmt.costmanagement import CostManagementClient
from azure.mgmt.costmanagement.models import QueryDefinition, ReportTimeframeType
from config import AZURE_SUBSCRIPTION_ID

def fetch_cost_data():
    # Use Azure CLI credential (make sure `az login` is done)
    credential = AzureCliCredential()

    if not AZURE_SUBSCRIPTION_ID:
        raise ValueError("AZURE_SUBSCRIPTION_ID environment variable not set.")

    client = CostManagementClient(credential, AZURE_SUBSCRIPTION_ID)

    # Build the query parameters correctly using QueryDefinition
    parameters = QueryDefinition(
        type="Usage",
        timeframe=ReportTimeframeType.MONTH_TO_DATE,
        dataset={
            "granularity": "Daily",
            "aggregation": {
                "totalCost": {
                    "name": "PreTaxCost",
                    "function": "Sum"
                }
            }
        }
    )

    scope = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}"
    result = client.query.usage(scope, parameters)

    return result.as_dict()
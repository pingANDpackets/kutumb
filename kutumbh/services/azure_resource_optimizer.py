from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import os

def find_idle_resources():
    credential = AzureCliCredential()
    subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

    if not subscription_id:
        raise ValueError("AZURE_SUBSCRIPTION_ID environment variable not set.")

    client = ResourceManagementClient(credential, subscription_id)

    idle_resources = []

    for resource in client.resources.list():
        # Dummy logic to flag "idle" resources (customize as needed)
        if "test" in (resource.name or "").lower() or "demo" in (resource.name or "").lower():
            idle_resources.append({
                "id": resource.id,
                "name": resource.name,
                "type": resource.type,
                "location": resource.location
            })

    return idle_resources
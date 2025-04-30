# agents/cost_analyzer_agent.py

import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT

# Initialize Semantic Kernel
kernel = Kernel()

chat_service = AzureChatCompletion(
    deployment_name=AZURE_OPENAI_DEPLOYMENT,
    api_key=AZURE_OPENAI_API_KEY,
    endpoint=AZURE_OPENAI_ENDPOINT
)

kernel.add_service(chat_service)



async def analyze_cost(cost_data):
    """
    Analyzes Azure cost data and generates an optimization report using Azure OpenAI.
    """
    prompt = f"""
You are an Azure cloud cost optimization expert.

Given this Azure subscription cost data:
{cost_data}

Please provide:
- Top cost contributors
- Idle resources
- 3 detailed cost optimization suggestions
- Estimated potential monthly savings
"""
    completion_function = kernel.get_service("azure-openai")
    result = await kernel.run_async(completion_function, input_str=prompt)
    return str(result)
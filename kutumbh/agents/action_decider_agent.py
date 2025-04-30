# agents/action_decider_agent.py

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

async def decide_action(analysis_summary):
    """
    Based on the optimization analysis, suggests whether to apply optimizations automatically or require manual approval.
    """
    prompt = f"""
You are responsible for cloud governance.

Given the following Azure cloud cost analysis:
{analysis_summary}

Decide whether we should:
(A) Automatically apply optimizations
(B) Require manual admin approval
(C) Only log the recommendations

Respond clearly with your choice and a 2-line explanation.
"""
    completion_function = kernel.get_service("azure-openai")
    result = await kernel.run_async(completion_function, input_str=prompt)
    return str(result)
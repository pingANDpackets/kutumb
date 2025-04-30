# main.py

import asyncio
from services.azure_cost_fetcher import fetch_cost_data
from agents.cost_analyzer_agent import analyze_cost
from agents.action_decider_agent import decide_action

async def main():
    print("🚀 Fetching Azure cost data...")
    cost_data = fetch_cost_data()

    print("\n🔍 Analyzing cost data with AI agent...")
    analysis_summary = await analyze_cost(cost_data)
    print("\n--- AI Cost Analysis ---")
    print(analysis_summary)

    print("\n🧠 Deciding next action based on analysis...")
    action_decision = await decide_action(analysis_summary)
    print("\n--- AI Action Decision ---")
    print(action_decision)

    # Instead of real actions, simulate a manual approval step
    print("\n❓ Do you want to simulate applying the optimizations? [Y/N]")
    user_input = input().strip().lower()

    if user_input == "y":
        print("\n✅ Simulation: Actions would be applied now (no real Azure changes).")
    else:
        print("\n❌ Simulation: No changes applied.")

    print("\n🎯 Process completed. Azure environment remains unchanged.")

if __name__ == "__main__":
    asyncio.run(main())
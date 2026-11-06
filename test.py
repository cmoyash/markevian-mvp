from models.buisness_profile import BusinessProfile
from agents.baseagent import BaseAgent
from agents.leadstrategy_agent import LeadStrategyAgent
from knowledge_base.business_data import KnowledgeBase
from services.gemini_services import GeminiService




knowledge = KnowledgeBase(profile=BusinessProfile)
data = knowledge.load_business_config("knowledgebase_data/business_data.json")
profile = BusinessProfile(**data)
gemini = GeminiService()
strategy_agent = LeadStrategyAgent(gemini=gemini , profile=profile)


print("generating strategy....")
strategy = strategy_agent.generate_lead_strategy()

print("\n" + "=" * 60)
print("LEAD STRATEGY")
print("=" * 60)
print(f"Target Industry: {strategy.target_industry}")
print(f"Location: {strategy.location}")
print(f"Signals: {strategy.signals_to_research}")
print(f"Criteria: {strategy.qualification_criteria}")


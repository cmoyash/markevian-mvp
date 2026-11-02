from services.gemini_services import GeminiService
from agents.baseagent import BaseAgent
from prompts.leadstratgy_prompt import LEAD_STRATEGY
from models.buisness_profile import BusinessProfile
from models.lead_starategy import LeadStarategy
from google.genai import types
from typing import Any



class LeadStrategyAgent(BaseAgent):
    def __init__(self, gemini: GeminiService , profile: BusinessProfile):
        super().__init__(gemini)
        self.profile = profile


    def build_prompt(self) -> str:

        business_name = self.profile.business_name
        services = ("\n").join(self.profile.services)
        target_market = self.profile.target_market
        target_industries = ("\n").join(self.profile.target_industries)

        prompt = LEAD_STRATEGY.format(
            business_name = business_name , 
            services = services ,
            target_market = target_market , 
            target_industries = target_industries
        )
        return prompt

    def generate_lead_strategy(self) -> Any:
        prompt = self.build_prompt()

        response = self.gemini.generate_response(
            prompt=prompt ,
            config=types.GenerateContentConfig(
                response_mime_type = "application/json" ,
                response_schema = LeadStarategy
            )
        )
        return response.parsed
    
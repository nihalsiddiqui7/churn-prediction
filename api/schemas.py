from pydantic import BaseModel

class CustomerData(BaseModel):
    support_calls: int
    total_spend: float
    payment_delay: int
    last_interaction: int
    subscription_type: str
    contract_length: str
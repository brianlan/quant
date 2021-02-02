from typing import List, Tuple


from ...struct.base import FundRecord

class EastMoney:
    def __init__(self):
        pass
    
    def get_all_fund_ids(self) -> List[str]:
        pass
    
    def get_history_by_fund_id(self, fund_id: str) -> List[FundRecord]:
        pass

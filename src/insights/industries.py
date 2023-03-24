from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    types_industry = set()
    list_types_industry = []
    for type_industry in data:
        types_industry.add(type_industry["industry"])

        list_types_industry = [
            types for types in types_industry if types != ''
        ]

    return list_types_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_industry = [ind for ind in jobs if ind['industry'] == industry]

    return filter_industry

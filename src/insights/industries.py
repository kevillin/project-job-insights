from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    unique_industry = set()
    for job in read(path):
        if job["industry"] != "":
            print(job)
            unique_industry.add(job["industry"])
    return list(unique_industry)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industry_by_filter = []
    for job in jobs:
        if job["industry"] == industry:
            industry_by_filter.append(job)
    return industry_by_filter


if __name__ == "__main__":
    print(get_unique_industries("data/jobs.csv"))

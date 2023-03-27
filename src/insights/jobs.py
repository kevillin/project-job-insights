from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        readJobs = list(csv.DictReader(file))
        return readJobs


def get_unique_job_types(path: str) -> List[str]:
    unique_type = set()
    for job in read(path):
        unique_type.add(job["job_type"])
    return list(unique_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_type_by_filter = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_type_by_filter.append(job)
    return job_type_by_filter


if __name__ == "__main__":
    print(read("data/jobs.csv"))

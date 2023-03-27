from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    max_salary = 0
    for job in read(path):
        if job["max_salary"].isdigit():
            result = int(job["max_salary"])
            if result > max_salary:
                max_salary = result
    return max_salary


def get_min_salary(path: str) -> int:
    min_salary = 383416
    for job in read(path):
        if job["min_salary"].isdigit():
            result = int(job["min_salary"])
            if result < min_salary:
                min_salary = result
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        max = int(job["max_salary"])
        min = int(job["min_salary"])
        salary = int(salary)
    except Exception:
        raise ValueError("salary must be an integer")

    if min > max:
        raise ValueError("min must be less than max")

    result = min <= salary <= max
    return result


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter.append(job)
        except ValueError:
            continue

    return filter


if __name__ == "__main__":
    print(get_max_salary("data/jobs.csv"))

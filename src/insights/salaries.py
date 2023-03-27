from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    filter_data = [
        types for types in data if types["max_salary"] != ''
        and types["max_salary"] != 'invalid'
    ]

    salary_max = 0
    for values in filter_data:
        if int(values["max_salary"]) > salary_max:
            salary_max = int(values["max_salary"])

    return salary_max


def get_min_salary(path: str) -> int:
    data = read(path)
    filter_data = [
        types for types in data if types["min_salary"] != ''
        and types["min_salary"] != 'invalid'
    ]

    salary_min = 10000000
    for values in filter_data:
        if int(values["min_salary"]) < salary_min:
            salary_min = int(values["min_salary"])

    return salary_min


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    verify = False
    try:
        if int(job['min_salary']) > int(job['max_salary']):
            raise ValueError(
                "minimo salrio precisa ser menor que salrio maximo"
            )

        verify = int(salary) <= int(job['max_salary']) and int(
            salary) >= int(job['min_salary'])

        return verify
    except (ValueError, KeyError, TypeError):
        raise ValueError
    finally:
        return verify


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filter_salary = []
    for job in jobs:
        matches_salary = matches_salary_range(job, salary)
        if matches_salary:
            filter_salary.append(job)

    return filter_salary

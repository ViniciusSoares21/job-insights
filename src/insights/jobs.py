from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        users_reader = csv.DictReader(file)
        users_list_dic = []
        for list_users in users_reader:
            users_list_dic.append(list_users)

        return users_list_dic


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    types_job = set()
    list_types_job = []
    for type_job in data:
        types_job.add(type_job["job_type"])
    for types in types_job:
        list_types_job.append(types)

    return list_types_job


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filter_jobs = [job for job in jobs if job['job_type'] == job_type]

    return filter_jobs

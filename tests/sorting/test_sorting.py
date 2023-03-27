from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs_sort = [
        {"max_salary": 3000, "min_salary": 2200, "date_posted": '2021-05-08'},
        {"max_salary": 800, "min_salary": 550, "date_posted": '2023-05-08'},
        {"max_salary": 10000, "min_salary": 7500, "date_posted": '2020-05-08'},
        {"max_salary": 2000, "min_salary": 1500, "date_posted": '2019-05-08'},
        ]

    """ valida ordenação com max_salary """
    jobs_reuslt_max = [
        {"max_salary": 10000, "min_salary": 7500, "date_posted": '2020-05-08'},
        {"max_salary": 3000, "min_salary": 2200, "date_posted": '2021-05-08'},
        {"max_salary": 2000, "min_salary": 1500, "date_posted": '2019-05-08'},
        {"max_salary": 800, "min_salary": 550, "date_posted": '2023-05-08'},
        ]

    sort_by(jobs_sort, 'max_salary')
    for job_index in range(len(jobs_reuslt_max)):
        assert jobs_sort[job_index] == jobs_reuslt_max[job_index]

    """ valida ordenação com min_salary """
    jobs_reuslt_min = [
        {"max_salary": 800, "min_salary": 550, "date_posted": '2023-05-08'},
        {"max_salary": 2000, "min_salary": 1500, "date_posted": '2019-05-08'},
        {"max_salary": 3000, "min_salary": 2200, "date_posted": '2021-05-08'},
        {"max_salary": 10000, "min_salary": 7500, "date_posted": '2020-05-08'},
        ]

    sort_by(jobs_sort, 'min_salary')
    for job_index in range(len(jobs_reuslt_min)):
        assert jobs_sort[job_index] == jobs_reuslt_min[job_index]

    """ valida ordenação com date_posted """
    jobs_reuslt_date = [
        {"max_salary": 800, "min_salary": 550, "date_posted": '2023-05-08'},
        {"max_salary": 3000, "min_salary": 2200, "date_posted": '2021-05-08'},
        {"max_salary": 10000, "min_salary": 7500, "date_posted": '2020-05-08'},
        {"max_salary": 2000, "min_salary": 1500, "date_posted": '2019-05-08'},
        ]

    sort_by(jobs_sort, 'date_posted')
    for job_index in range(len(jobs_reuslt_date)):
        assert jobs_sort[job_index] == jobs_reuslt_date[job_index]

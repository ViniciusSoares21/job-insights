from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    result_keys = {'salary', 'title', 'type'}
    result_keys_by_func = set()
    for job in jobs:
        keys = job.keys()
        for key in keys:
            result_keys_by_func.add(key)
    assert result_keys_by_func == result_keys

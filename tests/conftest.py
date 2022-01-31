import pytest
from os import path
from python_excersises.ex_2.calculations import main_function


@pytest.fixture(scope="class")
def output_file_path():
    filename = path.join(path.dirname(__file__), "test_data/top_products.csv")
    return filename


@pytest.fixture(scope="class")
def run_script_and_create_output(output_file_path):
    main_function(
        path_to_data=path.join(path.dirname(__file__), "test_data/data.csv"),
        path_to_curr=path.join(path.dirname(__file__), "test_data/currencies.csv"),
        path_to_match=path.join(path.dirname(__file__), "test_data/matchings.csv"),
        path_to_output=path.join(path.dirname(__file__), "test_data/top_products.csv")
    )

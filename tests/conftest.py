import pytest
from os import path


@pytest.fixture(scope="class")
def output_file_path():
    filename = path.join(path.dirname(__file__), "../ex_2/top_products.csv")
    return filename

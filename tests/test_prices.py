import pytest
from os import path

from python_excersises.tests.helpers import get_headers, get_rows


class TestExcerciseTwo:
    def test_check_result_file(self, output_file_path):
        file = path.exists(output_file_path)
        assert file, "Output file does not exist in expected path."

    def test_check_headers_of_result_file(self, output_file_path):
        expected_headers = [
            "matching_id",
            "total_price",
            "avg_price",
            "currency",
            "ignored_products_count",
        ]
        actual_headers = get_headers(output_file_path)
        assert sorted(expected_headers) == sorted(
            actual_headers
        ), "Output file doesn't have needed headers"

    def test_check_entries_amount(self, output_file_path):
        rows_amount = len(get_rows(output_file_path))
        assert rows_amount == 7, "Rows amount is not equal to expected total top_priced_count"

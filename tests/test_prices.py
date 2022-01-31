import pytest
from os.path import exists

from python_excersises.tests.helpers import (
    get_headers,
    get_rows,
    get_rows_with_matching_id_1,
    get_rows_with_matching_id_2,
    get_rows_with_matching_id_3,
)


class TestExcerciseTwo:
    def test_check_result_file(self, output_file_path):
        file = exists(output_file_path)
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
        assert (
            rows_amount == 7
        ), "Rows amount is not equal to expected total top_priced_count"

    def test_check_entries_amount_per_each_matching_id(self, output_file_path):
        assert (
            len(get_rows_with_matching_id_1(output_file_path)) == 2
        ), "Entries with matching_id=1 should be 2"
        assert (
            len(get_rows_with_matching_id_2(output_file_path)) == 2
        ), "Entries with matching_id=2 should be 2"
        assert (
            len(get_rows_with_matching_id_3(output_file_path)) == 3
        ), "Entries with matching_id=3 should be 3"

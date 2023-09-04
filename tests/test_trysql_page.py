import re
import uuid
import allure
from tests.test_base import BaseTest
from pages.TrysqlPage import TrysqlPage


@allure.epic("Tests for TrySQL Page")
class TestTrysql(BaseTest):
    def setup_method(self):
        self.trysqlPage = TrysqlPage(self.driver)
        self.random_string = str(uuid.uuid1())[:8]
        self.test_sql_CustomerName = f"Test Customer{self.random_string}"
        self.test_sql_ContactName = f"Test Contact{self.random_string}"
        self.test_sql_Address = f"Test Address{self.random_string}"
        self.test_sql_City = "Test city"
        self.test_sql_PostalCode = "TST TST"
        self.test_sql_Country = "UK"
        self.expected_row_result_table = [self.test_sql_CustomerName, self.test_sql_ContactName, self.test_sql_Address,
                                          self.test_sql_City, self.test_sql_PostalCode, self.test_sql_Country]

    @allure.description("TASK 1. Retrieve all rows from the Customers table and make sure that the record "
                        "with ContactName equal to 'Giovanni Rovelli' has Address = 'Via Ludovico il Moro 22'")
    def test_customers_contactname_address(self):
        actual_address = self.trysqlPage.get_address_by_contactname_from_table("SELECT * FROM Customers;")

        assert actual_address == self.trysqlPage.EXPECTED_ADDRESS, \
            f"ContactName = {self.trysqlPage.CONTACT_NAME} should have address {self.trysqlPage.EXPECTED_ADDRESS} " \
            f"Got {actual_address}"

    @allure.description("TASK 2. Retrieve only those rows from the Customers table where city='London'. "
                        "Verify that there are exactly 6 records in the table")
    def test_customers_filter_by_city(self):
        actual_num_rows = int(self.trysqlPage.get_number_of_rows_from_table("SELECT * FROM Customers WHERE "
                                                                            "city='London';"))
        actual_num_rows_from_div = int(re.findall("[0-9]+", self.trysqlPage.get_number_of_rows_from_div_element())[0])

        assert actual_num_rows_from_div == self.trysqlPage.EXPECTED_CITY_NUM_RECORDS, \
            f"Number of rows in div element {self.trysqlPage.RESULT_NUM_RECORDS_DIV} " \
            f"should be equal to {self.trysqlPage.EXPECTED_CITY_NUM_RECORDS}. But got {actual_num_rows_from_div}"

        assert actual_num_rows == self.trysqlPage.EXPECTED_CITY_NUM_RECORDS, \
            f"Number of rows in the table {self.trysqlPage.RESULT_SQL_TABLE[1]} " \
            f"should be equal to {self.trysqlPage.EXPECTED_CITY_NUM_RECORDS}. But got {actual_num_rows}"

    @allure.description("TASK 3. Add a new record to the Customers table and confirm that this record has been added.")
    def test_customers_insert_data(self):
        # INSERT test data to table
        self.trysqlPage.run_sql_query(
            f"INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) "
            f"VALUES ('{self.test_sql_CustomerName}', '{self.test_sql_ContactName}', '{self.test_sql_Address}', "
            f"'{self.test_sql_City}', '{self.test_sql_PostalCode}', '{self.test_sql_Country}');"
        )

        # Get inserted test data from table
        actual_row = self.trysqlPage.get_row_from_result_table_as_list(
            f"SELECT CustomerName, ContactName, Address, City, PostalCode, Country FROM Customers "
            f"WHERE CustomerName='{self.test_sql_CustomerName}' AND ContactName='{self.test_sql_ContactName}' AND "
            f"Address='{self.test_sql_Address}' AND City='{self.test_sql_City}' AND "
            f"PostalCode='{self.test_sql_PostalCode}' AND Country='{self.test_sql_Country}';"
        )

        # Compare two lists
        assert actual_row == self.expected_row_result_table, f"Inserted data should be equal to expected data"

    @allure.description("TASK 4. Update all fields (except CustomerID) in any record of the Customers table "
                        "and verify that the changes have been saved to the database.")
    def test_customers_update_data(self):
        # INSERT test data to table
        self.trysqlPage.run_sql_query(
            f"INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) "
            f"VALUES ('{self.test_sql_CustomerName}', '{self.test_sql_ContactName}', '{self.test_sql_Address}', "
            f"'{self.test_sql_City}', '{self.test_sql_PostalCode}', '{self.test_sql_Country}');"
        )

        # UPDATE test data to table
        self.trysqlPage.run_sql_query(
            f"UPDATE Customers SET CustomerName='{self.test_sql_CustomerName}13', "
            f"ContactName='{self.test_sql_ContactName}13', "
            f"Address='{self.test_sql_Address}13', "
            f"City='{self.test_sql_City}13', "
            f"PostalCode='{self.test_sql_PostalCode}13', "
            f"Country='{self.test_sql_Country}13' "
            f"WHERE CustomerName='{self.test_sql_CustomerName}' AND ContactName='{self.test_sql_ContactName}'"
            f"AND Address='{self.test_sql_Address}';"
        )

        # Get updated test data from table
        actual_row = self.trysqlPage.get_row_from_result_table_as_list(
            f"SELECT CustomerName, ContactName, Address, City, PostalCode, Country FROM Customers "
            f"WHERE CustomerName='{self.test_sql_CustomerName}13' AND ContactName='{self.test_sql_ContactName}13' AND "
            f"Address='{self.test_sql_Address}13' AND City='{self.test_sql_City}13' AND "
            f"PostalCode='{self.test_sql_PostalCode}13' AND Country='{self.test_sql_Country}13';"
        )

        expected_row = [self.test_sql_CustomerName + "13",
                        self.test_sql_ContactName + "13",
                        self.test_sql_Address + "13",
                        self.test_sql_City + "13",
                        self.test_sql_PostalCode + "13",
                        self.test_sql_Country + "13"]

        # Compare two lists
        assert actual_row == expected_row, f"Updated data should be equal to expected data"

    @allure.description("TASK 5. Check that 'Get your own SQL server' button is visible on the TrySQL Page and has appropriate text")
    def test_get_your_own_server_button(self):
        text = self.trysqlPage.get_element_text(self.trysqlPage.GET_OWN_SERVER_BUTTON)

        assert text == self.trysqlPage.GET_OWN_SERVER_BUTTON_TEXT, \
            f"Text of 'Get your own SQL server' button " \
            f"should be {self.trysqlPage.GET_OWN_SERVER_BUTTON_TEXT}. But got {text}"

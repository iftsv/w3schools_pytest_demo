from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


class TrysqlPage(BasePage):
    TRYSQL_PAGE_URI = "/sql/trysql.asp?filename=trysql_select_all"
    RUN_SQL_BUTTON = (By.CSS_SELECTOR, "button.ws-btn")
    RESULT_SQL_TABLE = (By.CSS_SELECTOR, "#resultSQL table>tbody")

    CONTACT_NAME = "Giovanni Rovelli"
    EXPECTED_ADDRESS = "Via Ludovico il Moro 22"

    RESULT_NUM_RECORDS_DIV = (By.CSS_SELECTOR, "#resultSQL div>div>div")
    EXPECTED_CITY_NUM_RECORDS = 6

    GET_OWN_SERVER_BUTTON = (By.CSS_SELECTOR, "#getwebsitebtn")
    GET_OWN_SERVER_BUTTON_TEXT = "Get your own SQL server"

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f"{TestData.BASE_URL}{self.TRYSQL_PAGE_URI}")

    """This is use to clear then to enter SQL query and click Run SQL button"""
    def run_sql_query(self, sql_query: str):
        self.driver.execute_script(f"window.editor.setValue(\"{sql_query}\");")
        self.do_click(self.RUN_SQL_BUTTON)

    def get_address_by_contactname_from_table(self, sql_query):
        self.run_sql_query(sql_query)
        table = self.get_sql_result_table(self.RESULT_SQL_TABLE)
        rows = table.find_elements(By.TAG_NAME, "tr")
        address = ""
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            for i in range(len(cols)):
                if i == 2 and cols[i].text == self.CONTACT_NAME:
                    address = cols[3].text
                    break
        return address

    def get_number_of_rows_from_div_element(self):
        div_text = self.get_element_text(self.RESULT_NUM_RECORDS_DIV)
        return div_text

    def get_number_of_rows_from_table(self, sql_query):
        self.run_sql_query(sql_query)
        table = self.get_sql_result_table(self.RESULT_SQL_TABLE)
        rows = table.find_elements(By.TAG_NAME, "tr")
        # ignore header of table
        return len(rows) - 1

    def get_row_from_result_table_as_list(self, sql_query):
        self.run_sql_query(sql_query)
        table = self.get_sql_result_table(self.RESULT_SQL_TABLE)
        try:
            col_list = []
            cols = table.find_elements(By.TAG_NAME, "tr")[1].find_elements(By.TAG_NAME, "td")
            for col in cols:
                col_list.append(col.text)
            return col_list
        except (IndexError, AttributeError):
            raise Exception(f"Expected some data. But no result in table '{self.RESULT_SQL_TABLE[1]}'")


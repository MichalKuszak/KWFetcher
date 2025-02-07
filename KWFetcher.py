from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import uniform
import time

SLEEP_TIME = uniform(2, 6)


class KWFetcher:

    def __init__(self, full_kw_no) -> None:
        self.department_code: str = None
        self.number_KW: str = None
        self.control_number: str = None
        self.format_kw_no(full_kw_no)

    def format_kw_no(self, full_kw_no) -> None:
        """This function formats the KW number given by the user into a list.
        The elements of the list can then be input on the KW website"""
        kw_elements_list: list = full_kw_no.split("/")
        self.department_code: str = kw_elements_list[0]
        self.number_KW: str = kw_elements_list[1]
        self.control_number: str = kw_elements_list[2]


class MainKW(KWFetcher):
    def __init__(self, full_kw_no) -> None:
        super().__init__(full_kw_no)
        self.properties: list = None

        # Initialize the webdriver
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)

        self.load_kw()

    def load_kw(self) -> None:
        """Loads the main screen of the KW"""
        self.driver.get(
            "https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW?komunikaty=true&kontakt=true&okienkoSerwisowe=false")

        # Input the department code
        department_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div[2]/div/form/div[1]/div[2]/div[2]/div[1]/span[1]/input")
            )
        )
        department_input.send_keys(self.department_code)

        # Input the KW number
        number_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div[2]/div/form/div[1]/div[2]/div[2]/div[1]/span[3]/input")
            )
        )
        number_input.send_keys(self.number_KW)

        # Input the control number
        control_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div/div[2]/div/form/div[1]/div[2]/div[2]/div[1]/span[5]/input")
            )
        )
        control_input.send_keys(self.control_number)

        # Submit the data
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.NAME, "wyszukaj")
            )
        )
        submit_button.click()

        # Get through the scope selection screen

        time.sleep(SLEEP_TIME)
        try:
            accept_cookies_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div/div[4]/div/span/span[2]")
                )
            )
            accept_cookies_button.click()
        except:
            pass
        submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.NAME, "przyciskWydrukZwykly")
                )
        )
        submit_button.click()
        time.sleep(SLEEP_TIME)


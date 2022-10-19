from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(45)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def choose_currency(self, currency='USD'):
        currency_element = self.find_element(
            'css selector', 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency = self.find_element(
            'css selector', f'a[data-modal-header-async-url-param*="changed_currency=1&selected_currency={currency}"]')
        selected_currency.click()

    def select_destination(self, destination):
        destination_input = self.find_element(
            'css selector', 'input[name="ss"]')
        destination_input.send_keys(destination)
        first_result = self.find_elements(
            'class name', 'a80e7dc237')[0]
        first_result.click()

    def select_dates(self, checkin, checkout):
        check_in_input = self.find_element(
            'css selector', 'button[data-testid="date-display-field-start"]')
        check_in_input.click()

        check_in_element = self.find_element(
            'css selector', f'span[data-date="{checkin}"]')
        check_in_element.click()
        check_out_element = self.find_element(
            'css selector', f'span[data-date="{checkout}"]')
        check_out_element.click()

    def select_adults(self, adults=1):
        adults_input = self.find_element(
            'css selector', 'button[data-testid="occupancy-config"]')
        adults_input.click()
        # EC.element_attribute_to_include(
        #     ('css selector', 'span[class="e57ffa4eb5"]'), 'Done')
        # adults_value_element = self.find_element('id', 'group_adults')
        # adults_value = adults_value_element.get_attribute('value')

    def search_destination(self):
        searc_btn = self.find_element('css selector', 'button[type="submit"]')

from selenium import webdriver
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
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

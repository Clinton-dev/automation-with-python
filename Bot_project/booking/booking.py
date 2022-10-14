from selenium import webdriver
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self):
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc, traceback):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

import string

from celery import shared_task
from .models import Screenshot
from selenium import webdriver

@shared_task
def take_screenshot(screenshot_pk):
    screenshot = Screenshot.objects.get(pk=screenshot_pk)
    url = screenshot.url
    # call Selenium webdriver

    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    # TODO: generate random file name
    driver.save_screenshot('screenshot_{}.png'.format(screenshot.id))
    driver.quit()


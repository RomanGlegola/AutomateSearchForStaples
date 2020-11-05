from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def run_webdriver():
    """
    this function runs chrome driver
    :return:
    """
    try:
        return webdriver.Chrome(
            "WebDriver/chromedriver.exe")
    except:
        print("You should use ChromeDriver 87.0.4240.22")


def scenario(driver, website='https://www.google.com'):
    """
    this function navigate to website
    :param driver:
    :param website:
    :return:
    """
    try:
        driver.get(website)
    except:
        print(f'Website {website} is unreachable')
        quit_webdriver(driver)


def close_google_poopup(driver):
    """
    this function close's the google poopup that appears after navigate into website.
    For now I managed to work around this google poopup. I tryed to locate element by linktext, partial link text,
    id, xpatch, aria label, class, text, and much more both by webdriver.click() and by javascript.click(). I didn't
    tryed mock mouse jet. Only option that works for me is sending specific key chain into webdriver.
    :param driver:
    :return:
    """
    try:
        ActionChains(driver).send_keys(Keys.TAB, Keys.TAB, Keys.ENTER).perform()
    #     WebDriverWait(driver, 10).until(
    #         ec.presence_of_element_located((By.ID, 'introAgreeButton'))
    #     )
    #     driver.execute_script("arguments[0].click();", driver.find_element_by_id('introAgreeButton'))
    except:
        print("Couldn't find element to close google poopup")
        quit_webdriver(driver)


def search_text_field(driver,
                      text_field_selector=
                      '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input',
                      populate_field='Staples'):
    """
    this function populate the search text field
    :param driver:
    :param text_field_selector:
    :param populate_field:
    :return:
    """
    try:
        if driver.find_element(By.CSS_SELECTOR,
                               text_field_selector):
            driver.find_element(By.CSS_SELECTOR,
                                text_field_selector). \
                send_keys(populate_field)
    except:
        print("Couldn't find element to close populate the text field")
        quit_webdriver(driver)


def press_search_button(driver,
                        search_button_selector='#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b'):
    """
    this function press 'search' button under the search text field.
    At first it click() at non interactable bottom navigation panel on the bottom on the site in order to hide list
    with search result'a. After this webdriver will attempt to click() 'Search' button. If this wont work Webdriver will
    press Enter key.
    :param driver:
    :param search_button_selector:
    :return:
    """
    try:
        if driver.find_element(By.CSS_SELECTOR, '#fbar > div > div.b2hzT > div'):
            driver.find_element(By.CSS_SELECTOR, '#fbar > div > div.b2hzT > div').\
                click()
        if driver.find_element(By.CSS_SELECTOR,
                               search_button_selector):
            driver.find_element(By.CSS_SELECTOR,
                                search_button_selector).click()
        else:
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            print("Couldn't click element because it was obscured")

    except:
        print("Couldn't find element to click 'Search' button")
        quit_webdriver(driver)


def quit_webdriver(driver):
    """
    this function quit's chrome driver
    :param driver:
    :return:
    """
    try:
        driver.close()
    except:
        print("Couldn't close webdriver")


driver = run_webdriver()
scenario(driver)
close_google_poopup(driver)
search_text_field(driver)
press_search_button(driver)

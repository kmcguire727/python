'''
    This code is a modification of Joseph Zahar's work on Medium.
    Original content can be found here: 
    https://medium.com/@JosephZahar/dynamic-web-scraping-monitor-flight-prices-fluctuation-before-paying-for-you-next-trip-6b4cc46aac9d
'''

import pandas as pd
from datetime import date
from selenium import webdriver

def webscrape_airlines():
    # open csv
    webscrapped_flights = pd.read_csv("/home/kpm727/Documents/python/flight_price_tracker_prj/webscrapped_flights.csv")
    today_date = date.today()
    driver = webdriver.Chrome()

    # # navigate to UA website
    # # departure flights
    # for day in range(12, 19):
    #     driver.get(
    #         f"https://www.united.com/en/us/fsr/choose-flights?f=LHR&t=IAD&d=2023-03-{day}&tt=1&sc=7&px=1&taxng=1&newHP=True&clm=7&st=bestmatches&tqp=R"
    #     )

    #     WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located(
    #             (
    #                 By.XPATH,
    #                 '//*[@id="flightResults-content"]/div[3]/div[1]/div/div[2]/div[1]/div[1]/div/button',
    #             )
    #         )
    #     )

    #     price = driver.find_element(
    #         By.CLASS_NAME,
    #         "app-components-Shopping-PriceCard-styles__priceValue--21Ki_",
    #     ).text.strip()[1:]
    #     webscrapped_flights = webscrapped_flights.append(
    #         {
    #             "airline_name": "United Airlines",
    #             "type": "Departure",
    #             "flight_date": f"{day} March",
    #             "timestamp": today_date,
    #             "price": price,
    #         },
    #         ignore_index=True,
    #     )
import os
import csv
import json
import requests
from bs4 import BeautifulSoup

container = []                                                      #container which stores data


def scrape_data(url):
    with open("data/Abilene_TX.csv", "w") as file:                  #create csv file
        writer = csv.writer(file)
        writer.writerow(
            (
                "Name_site",                                        #this is a title,collected data will be recorded under them
                "Link"
            )
        )

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
        "accept": "*/*"

    }
    req = requests.get(url=url, headers=headers)
    if not os.path.exists("data"):                                       #this is os library which create directory "data"
        os.mkdir("data")

    soup = BeautifulSoup(req.text, "lxml")                                  #starting search adn scraping element from website
    all_companies = soup.find_all("li", class_="provider provider-row")
    for item in all_companies:
        name_company = item.find("h3", class_="company_info").text.strip()
        link_company = item.find("a", class_="website-link__item").get("href")
        # print(f"{name_company}: {link_company}")

        container.append({                                                  #this is the container where we put the collected data
            "name company": name_company,
            "link company": link_company
        })

        with open("data/Abilene_TX.csv", "a") as file:                      #save data in csv format
            writer = csv.writer(file)
            writer.writerow(
                (
                    name_company,
                    link_company
                )
            )
    with open("data/Abilene_TX.json", "a") as file:                       #sava data in json format
        json.dump(container, file, indent=4, ensure_ascii=False)


def main():
    scrape_data("https://clutch.co/agencies/abilene")


if __name__ == "__main__":
    main()

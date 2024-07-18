from requests_html import HTMLSession
import json
import csv
import pandas as pd

class Reviews:
    def __init__(self, asin):
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'your_user_agent'}
        # in questo caso, MacBook
        self.url = f'https://www.amazon.co.uk/Apple-MacBook-Chip-13-inch-256GB/product-reviews/{self.asin}/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='

    def pagination(self, num_page):
        r = self.session.get(self.url + str(num_page), headers=self.headers)
        if not r.html.find("div[data-hook=review]"):
            return False
        else:
            return r.html.find("div[data-hook=review]")

    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find("a[data-hook=review-title]", first=True).text
            rating = review.find("i[data-hook=review-star-rating] span", first=True).text
            helpful_element = review.find("span[data-hook=helpful-vote-statement]", first=True)
            body_element = review.find("span[data-hook=review-body] span", first=True)
            location = review.find("span[data-hook=review-date]", first=True).text
            verified_element = review.find("span[data-hook=avp-badge]", first=True)
            if body_element is not None and helpful_element is not None and verified_element is not None:
                body = body_element.text.replace("\n", "").strip()
                helpful = helpful_element.text
                verified = verified_element.text
            else:
                if body_element is None and helpful_element is not None and verified_element is not None:
                    body = ""
                    helpful = helpful_element.text
                    verified = verified_element.text
                elif helpful_element is None and body_element is not None and verified_element is not None:
                    helpful = ""
                    body = body_element.text.replace("\n", "").strip()
                    verified = verified_element.text
                elif verified_element is None and body_element is not None and helpful_element is not None:
                    verified = ""
                    body = body_element.text.replace("\n", "").strip()
                    helpful = helpful_element.text
                elif body_element is None and helpful_element is None and verified_element is not None:
                    body = ""
                    helpful = ""
                    verified = verified_element.text
                elif body_element is None and verified_element is None and helpful_element is not None:
                    body = ""
                    verified = ""
                    helpful = helpful_element.text
                elif verified_element is None and helpful_element is None and body_element is not None:
                    verified = ""
                    helpful = ""
                    body = body_element.text.replace("\n", "").strip()
                else:
                    body = ""
                    helpful = ""
                    verified = ""
            data = {"title_review" : title,
                    "body_review" : body,
                    "rating" : rating,
                    "helpful" : helpful,
                    "location" : location,
                    "verified" : verified
                    }
            total.append(data)
        return total

    def save(self, results):
        with open("review.json", "w") as f:
            json.dump(results, f)

if __name__ == "__main__":
    # recuperiamo tutte le features relative al prodotto di nostro interesse
    # amazon = Reviews("B08N5NHG4H")
    # results = []
    # for x in range(1,100):
    #     reviews = amazon.pagination(x)
    #     if reviews is not False:
    #         results.append(amazon.parse(reviews))
    #     else:
    #         print("no more pages")
    #         break
    # print(results)
    # print(len(results))

    # salviamoli in un file json per comodità di struttura
    # amazon.save(results)

    #### convertiamo il file json in csv
    # apri il file json in lettura
    with open('review.json', 'r') as jsonfile:
        # carica il contenuto del file json in una variabile
        data = json.load(jsonfile)
    # crea una lista unica (appiattisci la lista di liste)
    data = [item for sublist in data for item in sublist]
    # recupera gli headers dalle chiavi del primo dizionario
    headers = data[0].keys()
    # crea un nuovo file csv
    with open('amz_mac_uk.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        # metti l'headers
        writer.writeheader()
        # scrivi ognidizionario come una riga nel file csv
        for row in data:
            writer.writerow(row)

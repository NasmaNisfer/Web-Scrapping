import requests
from bs4 import BeautifulSoup

text = "iphone+14"

def tesla():

        url = "https://www.daraz.lk/catalog/?spm=a2a0e.home.search.1.675a4625s25PEH&q=iphone%2013&_keyori=ss&from=search_history&sugg=iphone%2013_0_1"
        r = requests.get(url)


        soup = BeautifulSoup(r.content,"html.parser")
        data = str(soup).split("Rs")
        c=0
        print(len(data))
        for i in range(1,20):
                st = data[i].split(",")
                c=0
                for q in st:
                        print(c)
                        print(q)
                        c=c+1

                print()
        result = soup.find_all("span",class_="pdp-mod-product-badge-title")

        for phone in result:
                print(phone)
                price1 = phone.find("div",class_="_30jeq3 _1_WHN1")
                price = str(phone.find("div",class_="_30jeq3 _1_WHN1")).split(">")
                name = str(phone.find("div",class_="_4rR01T")).split(">")
                image = str(phone.find("img",class_="_396cs4 _3exPp9")).split(" ")
                if price1 != None:
                    print((name[1]+price[1]).replace("</div",""))
                    print(image[-1].replace("/>",""))



def amazon():

        # Function to extract Product Title
        def get_title(soup):
                
                try:
                        # Outer Tag Object
                        title = soup.find("span", attrs={"id":'productTitle'})

                        # Inner NavigatableString Object
                        title_value = title.string

                        # Title as a string value
                        title_string = title_value.strip()

                        # # Printing types of values for efficient understanding
                        # print(type(title))
                        # print(type(title_value))
                        # print(type(title_string))
                        # print()

                except AttributeError:
                        title_string = ""	

                return title_string

        # Function to extract Product Price
        def get_price(soup):

                try:
                        price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

                except AttributeError:

                        try:
                                # If there is some deal price
                                price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()

                        except:		
                                price = ""	

                return price

        # Function to extract Product Rating
        def get_rating(soup):

                try:
                        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
                        
                except AttributeError:
                        
                        try:
                                rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
                        except:
                                rating = ""	

                return rating

        # Function to extract Number of User Reviews
        def get_review_count(soup):
                try:
                        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
                        
                except AttributeError:
                        review_count = ""	

                return review_count

        # Function to extract Availability Status
        def get_availability(soup):
                try:
                        available = soup.find("div", attrs={'id':'availability'})
                        available = available.find("span").string.strip()

                except AttributeError:
                        available = "Not Available"	

                return available	


        if __name__ == '__main__':

                # Headers for request
                HEADERS = ({'User-Agent':
                            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                            'Accept-Language': 'en-US'})

                # The webpage URL
                URL = "https://www.amazon.com/s?k="+text
                
                # HTTP Request
                webpage = requests.get(URL, headers=HEADERS)

                # Soup Object containing all data
                soup = BeautifulSoup(webpage.content, "lxml")

                # Fetch links as List of Tag Objects
                links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

                # Store the links
                links_list = []

                # Loop for extracting links from Tag Objects
                for link in links:
                        links_list.append(link.get('href'))


                # Loop for extracting product details from each link 
                for link in links_list:

                        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

                        new_soup = BeautifulSoup(new_webpage.content, "lxml")
                        
                        # Function calls to display all necessary product information
                        print("Product Title =", get_title(new_soup))
                        print("Product Price =", get_price(new_soup))
                        print("Product Rating =", get_rating(new_soup))
                        print("Number of Product Reviews =", get_review_count(new_soup))
                        print("Availability =", get_availability(new_soup))
                        print()
                        print()
tesla()

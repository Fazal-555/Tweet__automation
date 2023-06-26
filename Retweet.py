from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.common.by import By
import openai

# Set up Selenium webdriver

service = webdriver.chrome.service.Service("C:\Downloads\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://twitter.com/i/flow/login")

time.sleep(2)


username = driver.find_element(By.TAG_NAME, "input")
username.send_keys("fazal25018301")      #Tweeter Dummy Acc


all_buttons = driver.find_elements(
    By.XPATH, "//div[@role='button']"
)

all_buttons[-2].click()
time.sleep(2)


password = driver.find_element(
    By.XPATH, "//input[@type='password']"
)
password.send_keys("20july2001")    #Tweeter Acc

time.sleep(2)

# press on the login button
all_buttons = driver.find_elements(
    By.XPATH, "//div[@role='button']"
)
all_buttons[-1].click()

time.sleep(2)


keyword = "Bitcoin"
driver.get("https://twitter.com/search?q=" + keyword + "&src=typed_query" + "https://twitter.com/search?q=" + keyword + "&src=typed_query&f=live")

time.sleep(2)
#Manipulated Texts
messages = [
    "Bitcoin: the digital currency paving the way for a decentralized financial revolution.",
    "Unlocking financial freedom with Bitcoin's borderless, censorship-resistant nature.",
    "Bitcoin: a digital store of value challenging traditional financial systems.",
    "In Bitcoin we trust: a decentralized network empowering individuals with control over their finances.",
    "Bitcoin: the future of money is here, and it's digital, transparent, and secure. ",
    "Join the Bitcoin movement and be a part of reshaping the financial landscape.",
    "Bitcoin's limited supply makes it a hedge against inflation and a safeguard for wealth preservation. ",
    "Embrace the financial sovereignty offered by Bitcoin's decentralized architecture.",
    "Bitcoin: challenging the status quo and disrupting traditional financial institutions. ",
    "Bitcoin's blockchain technology ensures transparency, security, and immutability in every transaction. ",
    "Bitcoin: a digital asset that transcends borders, empowering individuals with financial inclusivity.",
    "Bitcoin's decentralized network enables peer-to-peer transactions, removing intermediaries. ",
    "Bitcoin: a decentralized revolution empowering individuals with control over their financial destiny. ",
    "Bitcoin's finite supply adds value, making it a digital gold in the 21st century.",
    "Diversify your portfolio with Bitcoin, the digital asset that has shown resilience and growth.",
    "Bitcoin: the catalyst for a paradigm shift in the way we perceive and utilize money. ",
    "Bitcoin is more than just a currency; it's a movement empowering individuals to take control of their financial destiny. ",
    "Bitcoin's decentralized nature means no central authority can manipulate its value. It's a currency of the people. ",
    "Bitcoin: the democratization of money, removing barriers and empowering individuals globally. ",
    "The power of Bitcoin lies in its ability to offer financial sovereignty and protect against economic uncertainty.",
    "Bitcoin: the disruptive force challenging the traditional banking system and offering a new era of financial freedom. "
]


n_scrolls = 7

for scroll in range(n_scrolls):
    # click retweet
    retweet = driver.find_elements(
        By.XPATH, "//div[@data-testid='retweet']"
    )
    driver.execute_script("arguments[0].click();", retweet[-1])

    time.sleep(7)

    # select the "quote tweet" option
    quote_tweet = driver.find_element(
        By.XPATH, "//a[@role='menuitem']"
    )
    quote_tweet.click()

    time.sleep(2)


    quote = driver.find_element(By.XPATH, "//div[contains(@class, 'public-DraftStyleDefault-block')]")
    quote.send_keys(random.choice(messages))

    time.sleep(2)


    tweet = driver.find_element(
        By.XPATH, "//div[@data-testid='tweetButton']"
    )
    tweet.click()

    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
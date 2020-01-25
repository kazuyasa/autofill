from selenium import webdriver
from time import sleep
# import chromedriver_binary

def get_word():
    pass

def get_txt(path):
    # Insert UserInfo From TextFile to List
    userinfo_list=[]
    with open(path) as f:
        text=f.read()
        userinfo_list=text.split("\n")
    # Format list 
    return list(map(lambda info: info.split(":")[1], userinfo_list))



def auto_fill_rakuten(email, password):
    # Open WebForm(Rakuten)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)  
    driver.get('https://grp01.id.rakuten.co.jp/rms/nid/registfwd?service_id=top')
    print(driver.title)

    # Input mail
    driver.find_element_by_name("email").send_keys(email)
    sleep(1)
    driver.find_element_by_name("email2").send_keys(email)
    sleep(1)
    
    # Input Pass
    driver.find_element_by_name("p").send_keys(password)
    sleep(1)


if __name__ == "__main__":
    # Get Info From TextFile
    userinfo_list=get_txt("sample.txt")
    print(userinfo_list)
    # Autofill RegistrationForm
    auto_fill_rakuten(userinfo_list[0], userinfo_list[1])
    # auto_fill_rakuten("sample@gmail.com","pass##12OLK")
import time
import urllist
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


bitwardenId = ""
bitwardenPw = ""

githubId = ""
githubPw = ""


def bitwardeninvite(inviteemail):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    driver.get(urllist.bitwarden)
    driver.find_element(By.NAME, "Email").send_keys(bitwardenId)
    driver.find_element("name", "MasterPassword").send_keys(bitwardenPw + Keys.RETURN)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, f"//a[@href='{urllist.bitwardenOrg}']").click()
    driver.find_element(By.XPATH, f"//a[@href='{urllist.bitwardenOrg}/manage']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-sm btn-outline-primary ml-3']").click()
    driver.find_element("name", "Emails").send_keys(inviteemail)
    driver.find_element(By.XPATH, f"//td[contains(text(),'{urllist.coll1}')]").click()
    driver.find_element(By.XPATH, f"//td[contains(text(),'{urllist.coll2}')]").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-submit']").submit()
    driver.implicitly_wait(5)
    print('Bitwarden 초대')
    driver.close()
    driver.quit()


def githubinvite(inviteemail):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    driver.get("https://github.com/login")
    driver.find_element(By.NAME, "login").send_keys(githubId)
    driver.find_element(By.NAME, "password").send_keys(githubPw + Keys.RETURN)
    driver.implicitly_wait(10)
    driver.get("https://github.com/marketit")
    driver.find_element(By.XPATH, "//summary[@data-hashchange-activated='invite-member']").click()
    driver.find_element(By.NAME, "identifier").send_keys(inviteemail)
    driver.find_element(By.NAME, "identifier").click()
    driver.find_element(By.XPATH, f"//span[contains(text(), 'invite to {urllist.org}')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(), 'Invite')]").click()
    driver.implicitly_wait(3)
    print('Github 초대')
    driver.close()
    driver.quit()


def vpninvite(vpnUsername, vpnUserpw):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    driver.get(urllist.vpn)
    driver.find_element(By.NAME, "admin_username").send_keys("")
    driver.find_element(By.NAME, "admin_pass").send_keys("" + Keys.RETURN)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "//button[@data-target='#modal-user-add']").click()
    driver.find_element(By.NAME, "username").send_keys(vpnUsername)
    driver.find_element(By.NAME, "password").send_keys(vpnUserpw)
    driver.find_element(By.XPATH, "//button[@id='modal-user-add-save']").click()
    driver.implicitly_wait(3)
    print('vpn 생성 완료')
    driver.close()
    driver.quit()

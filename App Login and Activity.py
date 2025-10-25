import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
value1 = "sisinc.com.sis.login.LoginActivity"
value2 = "sisinc.com.sis.NewNavMainActivity.NewNavMainActivity"
usernames = ['darklord128761','cr7Goat007316','deathslayer35112']
desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "android",
    "appPackage": "sisinc.com.sis",
    "appWaitActivity": value1,
    "app": "C:\\Users\\mjcx\\Downloads\\memechat-memes-keyboard-trends-news_5.04.apk",
    "appWaitDuration": 100000,
    "noReset": True,
}
u =0
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
for q in range(0,2):
    u = q
    cat = str(u)
    emails ='jayanthreins+tqw'+cat+'@gmail.com'
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/btn_signup').click()
    time.sleep(2)
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/edit_text_email').click()
    email = driver.find_element_by_id('sisinc.com.sis:id/edit_text_email')
    email.send_keys(emails)
    time.sleep(1)
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/edit_text_username').click()
    usrname = driver.find_element_by_id('sisinc.com.sis:id/edit_text_username')
    usrname.send_keys(usernames[q])
    time.sleep(1)
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/edit_text_password').click()
    password = driver.find_element_by_id('sisinc.com.sis:id/edit_text_password')
    password.send_keys("Am1zomem_123",)
    time.sleep(1)
    driver.back()
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/checkbox_terms_conditions').click()
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/btn_register').click()
    time.sleep(5)
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/ld_btn_yes').click()
    time.sleep(10)
    imga = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(imga).click()
    imga1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(imga1).click()
    imga2  = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(imga2).click()
    imga3  = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(imga3).click()
    imga4  = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(imga4).click()
    imga5  = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[6]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(imga5).click()
    save = 'sisinc.com.sis:id/save_cats'
    driver.implicitly_wait(30)
    driver.find_element_by_id(save).click()

    time.sleep(3)
    search_img = 'sisinc.com.sis:id/img_search'
    driver.implicitly_wait(30)
    driver.find_element_by_id(search_img).click()
    search_img1 = 'sisinc.com.sis:id/editText3'
    driver.implicitly_wait(30)
    search_img2 = driver.find_element_by_id(search_img1)
    search_img2.send_keys('NikhillxD')
    driver.back()
    search_im3 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView'
    driver.implicitly_wait(30)
    driver.find_element_by_xpath(search_im3).click()
    time.sleep(5)
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/follow').click()
    time.sleep(1)
    TouchAction(driver).press(x=1028, y=1493).wait(1000).move_to(x=1033, y=470).release().perform()
    a = 0
    for y in range(1,9):
        a = y
        b = str(a)
        search_im4 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['+b+']/android.widget.ImageView'
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(search_im4).click()
        time.sleep(5)
        driver.find_element_by_id('sisinc.com.sis:id/button1').click()
        driver.back()

    time.sleep(5)
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/action_item5').click()
    driver.implicitly_wait(30)
    driver.find_element_by_id('sisinc.com.sis:id/appsetting').click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[11]/android.widget.ImageView').click()
    time.sleep(10)
for x in range(1,10):
    value = driver.orientation
    time.sleep(50)
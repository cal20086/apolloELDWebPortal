#               Apollo Web Portal - Home Page
import time


def homePage (driver, driver_Name, driver_Version):



    from  selenium.webdriver import ActionChains
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    import tc_reports


#       Fields Address

    title_HomePageAdr = '//a[contains(@href,"<a href="#ctl00_SiteMapPath1_SkipLink")]'
    title_HomePageAdr = "/html/body/form/div[3]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/div/table/tbody/tr/td[1]/span"
    mouseHover_eDashAdr_MainPageAdr = "/html/body/form/div[3]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[13]/table/tbody/tr/td/a"
    hoverChildMenuText_ManagePageAdr = "HOS + DVIR"
#       Variables
    w = WebDriverWait(driver,30)


#   Main

    current_url_page = driver.current_url
    if "ome.aspx" in current_url_page:
        title_HomePage = w.until(EC.presence_of_element_located((By.ID, "ctl00_SiteMapPath1"))).text

        print(title_HomePage)

# **************** Test and report results at TCReport  ******************************************************************************************************************
#       Assert Test and print if assert is fail
        test_Name = "Home page open"
        condition1 = "Home"
        condition2 = title_HomePage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    #       Print Assert OK
        print_Information_Fix = "Home page - Home page open:"
        print_Information_Var = title_HomePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

        #       Mouse Hover
        action = ActionChains(driver)
        hoverMenu = driver.find_element_by_xpath(mouseHover_eDashAdr_MainPageAdr)
        action.move_to_element(hoverMenu).perform()
        hoverChildmenu = driver.find_element_by_link_text(hoverChildMenuText_ManagePageAdr)
        action.move_to_element(hoverChildmenu).click().perform()

    else:
        print("Skiped Home page")

    return ()
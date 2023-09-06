#               Apollo Web Portal - Login



def login_apolloWebPortal (contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, siteAddressVar, test_Case_Type):

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    import tc_reports



#               *************************************************** Element page address ************************************************


#       Carrier details Page Address & Variables
#       Fields Address

    text_UserNameVar = "/html/body/form/div[3]/div/div/table/tbody/tr/td/input[1]"
    text_PasswordVar = "/html/body/form/div[3]/div/div/table/tbody/tr/td/input[2]"
    button_LogInVar = "/html/body/form/div[3]/div/div/table/tbody/tr/td/input[3]"
    mouseHover_eDashVar = "/html/body/form/div[3]/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[13]/table/tbody/tr/td/a"

#       Variables
    control_Reportfile = 0
    print_Information_Fix = ""
    print_Information_Var = ""

    #               Main:

    print("Login page")
    driver.get(siteAddressVar)
    driver.maximize_window()
    w = WebDriverWait(driver,10)

      #       Login
    text_UserName = driver.find_element_by_xpath(text_UserNameVar)
    text_UserName.send_keys(user_ApolloWebPortalVar)
    text_Password = driver.find_element_by_xpath(text_PasswordVar)
    text_Password.send_keys(password_ApolloWebPortalVar)
    button_LogIn = driver.find_element_by_xpath(button_LogInVar)
    button_LogIn.click()

    tc_reports.write_reportfile(control_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)




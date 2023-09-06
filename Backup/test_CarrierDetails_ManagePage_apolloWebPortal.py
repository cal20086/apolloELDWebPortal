#               Apollo Web Portal - Carrier - Details

def carrierDetail_ChildMenu_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    from  selenium.webdriver import ActionChains



#       Carrier details Page Address & Variables
#       Fields Address

    button_Carrier_Actions_Details_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[1]"
    title_Carrier_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[1]/h4"
    input_DOT_Number_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[1]/input"
    input_CarrierName_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[2]/input"
    input_CarrierAddress_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[3]/input"
    dropDown_CarrierCountry_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[4]/select"
    dropDown_TimeZone_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[5]/select"
    dropDrown_Units_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[6]/select"
    input_SupportUsername_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[7]/input"
    input_SupportPassword_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[8]/input"
    input_ConfirmPassword_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[9]/input"
    input_APIKKeyDisplay_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[11]/div/div[1]/input"
    button_APIKey_Generate_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[11]/div/div[2]/button"
    checkBox_EngineDiagnostic_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[12]/div/input"
    checkBox_AllowActivateDrivers_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[13]/div/input"
    checkBox_AutomaticDriving_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[15]/div/input"
    checkBox_ForceECMConnection_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[15]/div/input"
    checkBox_DriverAssetList_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[15]/div/input"
    checkBox_EnableCanadianComplience_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[1]/div[17]/div/input"
    button_SAVE_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[2]/button[1]"
    button_CLOSE_CarrierChildPageAdr = "/html/body/ngb-modal-window/div/div/carrier-modal-form/div[2]/form/div[2]/button[2]"


#       Variables:
    var_DOT_Number_CarrierChildPage = "111111111"
    date = datetime.now()
#   var_CarrierName_CarrierChildPage = "Carrier Teste " + date.strftime("%b %d %Y - %H:%M:%S.%f")
    var_CarrierName_CarrierChildPage = client_Name_Var
    var_CarrierAddress_CarrierChildPage = client_Adress_Var
    var_SupportUsername_CarrierChildPage = "QA" + date.strftime("%f")
    var_SupportPassword_CarrierChildPage = "QAuser"
    w = WebDriverWait(driver, 30)

    #       #######################################     Carriers Main functions    ####################################################
    #   ###############################################################################################################################

    #   Page Title on TCReport
    function_Name = "Carriers Details Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    button_Carrier_Actions_Details_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Actions_Details_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Actions_Details_ManagePage.click()

    #   Carrier Page test:
    title_Carrier_CarrierChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Carrier_CarrierChildPageAdr))))
    print(title_Carrier_CarrierChildPage.text)
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Child Page Open"
    condition1 = "Carrier"
    condition2 = title_Carrier_CarrierChildPage.text
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Carrier Child Page Open"
    print_Information_Var = title_Carrier_CarrierChildPage.text
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Carrier Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)


#   Carrier DOT field test:
    input_DOT_Number_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DOT_Number_CarrierChildPageAdr)))
    input_DOT_Number_CarrierChildPage.clear()
    input_DOT_Number_CarrierChildPage.send_keys(var_DOT_Number_CarrierChildPage)
    read_DOT_Number_CarrierChildPage = input_DOT_Number_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "DOT Number - Carrier Child Page Open"
    condition1 = var_DOT_Number_CarrierChildPage
    condition2 = read_DOT_Number_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DOT Number - Carrier Child Page input type information OK!"
    print_Information_Var = read_DOT_Number_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Carrier Name field test:
    input_CarrierName_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_CarrierName_CarrierChildPageAdr)))
    input_CarrierName_CarrierChildPage.clear()
    input_CarrierName_CarrierChildPage.send_keys(var_CarrierName_CarrierChildPage)
    read_CarrierName_CarrierChildPage = input_CarrierName_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Name - Carrier Child Page Open"
    condition1 = var_CarrierName_CarrierChildPage
    condition2 = read_CarrierName_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Carrier Name - Carrier Child Page input type information OK!"
    print_Information_Var = read_CarrierName_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Carrier Address field test:
    input_CarrierAddress_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_CarrierAddress_CarrierChildPageAdr)))
    input_CarrierAddress_CarrierChildPage.clear()
    input_CarrierAddress_CarrierChildPage.send_keys( var_CarrierAddress_CarrierChildPage)
    read_CarrierAddress_CarrierChildPage = input_CarrierAddress_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Address - Carrier Child Page Open"
    condition1 = var_CarrierAddress_CarrierChildPage
    condition2 = read_CarrierAddress_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Carrier Address - Carrier Child Page input type information OK!"
    print_Information_Var = read_CarrierAddress_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    #       Carrier Country field test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_CarrierCountry_CarrierChildPageAdr))))
#   Read the drop down list and save o the dropDown_ImportOption_CarrierCountry_CarrierChildPage_List list
    dropDown_ImportOption_CarrierCountry_CarrierChildPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropDown_ImportOption_CarrierCountry_CarrierChildPage_List):
        dropDown_CarrierCountry_CarrierChildPage = dropDown.select_by_visible_text(dropDown_ImportOption_CarrierCountry_CarrierChildPage_List[n])
        #read the selected option on the dropdown
        dropDown_CarrierCountry_CarrierChildRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Carrier Country element - Carrier Child Page Open select information OK!"
        lastOptionsDropDown_CarrierCountry_CarrierChildPageVar = dropDown_ImportOption_CarrierCountry_CarrierChildPage_List[n]
        condition1 = lastOptionsDropDown_CarrierCountry_CarrierChildPageVar
        condition2 = dropDown_CarrierCountry_CarrierChildRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Carrier Country element - Carrier Child Page select information OK!"
        print_Information_Var = dropDown_CarrierCountry_CarrierChildRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)


    #       Time Zone field test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_TimeZone_CarrierChildPageAdr))))
    dropDown_ImportOption_TimeZone_CarrierChildPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropDown_ImportOption_TimeZone_CarrierChildPage_List):
        dropDown_TimeZone_CarrierChildPage = dropDown.select_by_visible_text(dropDown_ImportOption_TimeZone_CarrierChildPage_List[n])
        # read the selected option on the dropdown
        dropDown_TimeZone_CarrierChildRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Time Zone element - Carrier Child Page Open select information OK!"
        lastOptionsDropDown_TimeZone_CarrierChildPageVar = dropDown_ImportOption_TimeZone_CarrierChildPage_List[n]
        condition1 = lastOptionsDropDown_TimeZone_CarrierChildPageVar
        condition2 = dropDown_TimeZone_CarrierChildRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Time Zone element - Carrier Child Page information OK!"
        print_Information_Var = dropDown_TimeZone_CarrierChildRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)


    #       Units field test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDrown_Units_CarrierChildPageAdr))))
    dropDown_ImportOption_Units_CarrierChildPage_List = [x.text for x in dropDown.options]

    n = 0
    while n < len(dropDown_ImportOption_Units_CarrierChildPage_List):
        dropDown_Units_CarrierChildPage = dropDown.select_by_visible_text(dropDown_ImportOption_Units_CarrierChildPage_List[n])
        # read the selected option on the dropdown
        dropDown_Units_CarrierChildRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Units element - Carrier Child Page Open select information OK!"
        lastOptionsDropDown_Units_CarrierChildPageVar = dropDown_ImportOption_Units_CarrierChildPage_List[n]
        condition1 = lastOptionsDropDown_Units_CarrierChildPageVar
        condition2 = dropDown_Units_CarrierChildRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Units element - Carrier Child Page information OK!"
        print_Information_Var = dropDown_Units_CarrierChildRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)


    #   Support Username field test:
    input_SupportUsername_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_SupportUsername_CarrierChildPageAdr)))
    input_SupportUsername_CarrierChildPage.clear()
    input_SupportUsername_CarrierChildPage.send_keys(var_SupportUsername_CarrierChildPage)
    read_SupportUsername_CarrierChildPage = input_SupportUsername_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Support Username - Carrier Child Page Open"
    condition1 = var_SupportUsername_CarrierChildPage
    condition2 = read_SupportUsername_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Support Username - Carrier Child Page Open type information OK!"
    print_Information_Var = read_SupportUsername_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


    #    Support Password test:
    input_SupportPassword_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_SupportPassword_CarrierChildPageAdr)))
    input_SupportPassword_CarrierChildPage.clear()
    input_SupportPassword_CarrierChildPage.send_keys(var_SupportPassword_CarrierChildPage)
    read_SupportPassword_CarrierChildPage = input_SupportPassword_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Support Password - Carrier Child Page Open"
    condition1 = var_SupportPassword_CarrierChildPage
    condition2 = read_SupportPassword_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Support Password - Carrier Child Page Open type information OK!"
    print_Information_Var = read_SupportPassword_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    #    Confirm Password test:
    input_ConfirmPassword_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmPassword_CarrierChildPageAdr)))
    input_ConfirmPassword_CarrierChildPage.clear()
    input_ConfirmPassword_CarrierChildPage.send_keys(var_SupportPassword_CarrierChildPage)
    read_ConfirmPassword_CarrierChildPage = input_ConfirmPassword_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Confirm Password - Carrier Child Page Open"
    condition1 = var_SupportPassword_CarrierChildPage
    condition2 = read_ConfirmPassword_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Confirm Password - Carrier Child Page Open type information OK!"
    print_Information_Var = read_ConfirmPassword_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


    #   API Key field test:

    input_APIKKeyDisplay_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_APIKKeyDisplay_CarrierChildPageAdr)))
    w.until(EC.element_to_be_clickable((By.XPATH, button_APIKey_Generate_CarrierChildPageAdr))).click()
    input_APIKKeyDisplay_CarrierChildPage_1 = input_APIKKeyDisplay_CarrierChildPage.get_property('value')
    w.until(EC.element_to_be_clickable((By.XPATH, button_APIKey_Generate_CarrierChildPageAdr))).click()
    input_APIKKeyDisplay_CarrierChildPage_2 = input_APIKKeyDisplay_CarrierChildPage.get_property('value')
    try:
        assert input_APIKKeyDisplay_CarrierChildPage_1 != input_APIKKeyDisplay_CarrierChildPage_2
        print_Information_Fix = "API Key GENERATE works - Carrier Child Page API information OK!"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
        print("except")
        test_Name = "API Generator - Carrier Child Page"
        condition1 = input_APIKKeyDisplay_CarrierChildPage_1
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)


#   Demo CheckBox

    # ########################### SAVE button:

    w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_CarrierChildPageAdr))).click()
    button_Carrier_Actions_Details_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Actions_Details_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Actions_Details_ManagePage.click()

#   Verify the Storage Information on the Carrier Child Page

    #   Carrier DOT field test:
    input_DOT_Number_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DOT_Number_CarrierChildPageAdr)))
    read_DOT_Number_CarrierChildPage = input_DOT_Number_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "DOT Number check saved information - Carrier Child Page"
    condition1 = var_DOT_Number_CarrierChildPage
    condition2 = read_DOT_Number_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DOT Number check saved information - Carrier Child Page input type information OK!"
    print_Information_Var = read_DOT_Number_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #   Carrier Name ReTest field test:
    input_CarrierName_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_CarrierName_CarrierChildPageAdr)))
    read_CarrierName_CarrierChildPage = input_CarrierName_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Name check saved information - Carrier Child Page"
    condition1 = var_CarrierName_CarrierChildPage
    condition2 = read_CarrierName_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Carrier Name check saved information - The information were saved correctly!"
    print_Information_Var = read_CarrierName_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Carrier Address field ReTest:
    input_CarrierAddress_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_CarrierAddress_CarrierChildPageAdr)))
    read_CarrierAddress_CarrierChildPage = input_CarrierAddress_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Address check saved information - Carrier Child Page"
    condition1 = var_CarrierAddress_CarrierChildPage
    condition2 = read_CarrierAddress_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Carrier Address check saved information - Carrier Child Page input type information OK!"
    print_Information_Var = read_CarrierAddress_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #       Carrier Country field test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_CarrierCountry_CarrierChildPageAdr))))
    dropDown_CarrierCountry_CarrierChildRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Country check saved information - Carrier Child Page Open select information OK!"
    condition1 = lastOptionsDropDown_CarrierCountry_CarrierChildPageVar
    condition2 = dropDown_CarrierCountry_CarrierChildRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Carrier Country check saved information - Carrier Child Page select information OK!"
    print_Information_Var = dropDown_CarrierCountry_CarrierChildRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Time Zone field test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_TimeZone_CarrierChildPageAdr))))
    dropDown_TimeZone_CarrierChildRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Time Zone check saved information - Carrier Child Page information OK!"
    condition1 = lastOptionsDropDown_TimeZone_CarrierChildPageVar
    condition2 = dropDown_TimeZone_CarrierChildRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Time Zone check saved information - Carrier Child Page information OK!"
    print_Information_Var = dropDown_TimeZone_CarrierChildRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Units field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDrown_Units_CarrierChildPageAdr))))
    dropDown_Units_CarrierChildRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Child Page Elements Check SAVED Information - 1"
    condition1 = lastOptionsDropDown_Units_CarrierChildPageVar
    condition2 = dropDown_Units_CarrierChildRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Units  check saved information - Carrier Child Page information OK!"
    print_Information_Var = dropDown_Units_CarrierChildRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Support Username field verify:
    input_SupportUsername_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_SupportUsername_CarrierChildPageAdr)))
    read_SupportUsername_CarrierChildPage = input_SupportUsername_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Support Username check saved information - Carrier Child Page"
    condition1 = var_SupportUsername_CarrierChildPage
    condition2 = read_SupportUsername_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Support Username check saved information - Carrier Child Page information OK!"
    print_Information_Var = read_SupportUsername_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #    Support Password test:
    input_SupportPassword_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_SupportPassword_CarrierChildPageAdr)))
    read_SupportPassword_CarrierChildPage = input_SupportPassword_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Support Password  check saved information - Carrier Child Page"
    condition1 = var_SupportPassword_CarrierChildPage
    condition2 = read_SupportPassword_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Support Password check saved information - Carrier Child Page information OK!"
    print_Information_Var = read_SupportPassword_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #    Confirm Password test:
    input_ConfirmPassword_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_ConfirmPassword_CarrierChildPageAdr)))
    read_ConfirmPassword_CarrierChildPage = input_ConfirmPassword_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Confirm Password check saved information - Carrier Child Page"
    condition1 = var_SupportPassword_CarrierChildPage
    condition2 = read_ConfirmPassword_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Confirm Password check saved information - Carrier Child Page information OK!"
    print_Information_Var = read_ConfirmPassword_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #   API Key field test:

    input_APIKKeyDisplay_CarrierChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_APIKKeyDisplay_CarrierChildPageAdr)))
    read_APIKKeyDisplay_CarrierChildPage = input_APIKKeyDisplay_CarrierChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "API Key check saved information - Carrier Child Page"
    condition1 = input_APIKKeyDisplay_CarrierChildPage_2
    condition2 = read_APIKKeyDisplay_CarrierChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "API Key check saved information - Carrier Child Page information OK!"
    print_Information_Var = read_APIKKeyDisplay_CarrierChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)


    #   Demo CheckBox

    #CLOSE button:
    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_CarrierChildPageAdr))).click()

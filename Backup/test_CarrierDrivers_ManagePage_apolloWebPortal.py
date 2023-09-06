#               Apollo Web Portal - Drivers - Details


def carrierDrivers_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import re
    import test_Main_QATest1
    from selenium.webdriver import ActionChains

#       Carrier details Page Address & Variables
#       Fields Address
    button_Carrier_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[2]"
    title_Drivers_DriversChildPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[1]/h3"
    button_DriversDetails_DriversChildPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[5]/div/button"
    title_Driver_DriverChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[1]/h4"
    input_DriverName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[1]/input"
    input_DriverLastName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[2]/input"
    input_DriverUserName_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[3]/input"
    input_DriverPassword_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[4]/input"
    input_DriverConfirmation_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[5]/input"
    dropdown_Ruleset_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[6]/select"
    dropdown_24PeriodeStartingTime_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[7]/select"
    dropdown_Units_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[12]/select"
    dropdown_LicenseState_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[13]/select"
    input_LicenseNumber_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[14]/input"
    button_Driver_SAVE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]/button[1]"
    button_Driver_CLOSE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]/button[3]"
    driverName_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[1]/div"
    userNameName_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]"
    licenseNumber_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[3]"

    #       Variables:
    date = datetime.now()
#   Global variables
    input_DriverName_DriversChildPageVar = test_Main_QATest1.input_DriverName_DriversChildPage_Global
    input_DriverLastName_DriversChildPageVar = test_Main_QATest1.input_DriverLastName_DriversChildPage_Global
    input_DriverUserName_DriversChildPageVar = test_Main_QATest1.input_DriverUserName_DriversChildPage_Global
    input_DriverPassword_DriversChildPageVar = test_Main_QATest1.input_DriverPassword_DriversChildPage_Global
#   Local variables
    input_LicenseNumberFull_DriversChildPageVar = "Lic" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    input_LicenseNumber_DriversChildPageVar = re.sub('\W+','', input_LicenseNumberFull_DriversChildPageVar)
    w = WebDriverWait(driver, 30)

    #       #######################################     Carriers Main functions    ##########################################
    #   #####################################################################################################################

    #   Page Title on TCReport
    function_Name = "Carriers Drivers Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    button_Carrier_Drivers_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Drivers_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Drivers_ManagePage.click()

    #   Drivers Page test:
    title_Drivers_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Drivers_DriversChildPageAdr)))).text
    print(title_Drivers_DriversChildPage)
    #       Assert Test and print if assert is fail
    test_Name = "Drivers Child Page Open"
    condition1 = "Drivers"
    condition2 = title_Drivers_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Drivers Page Open"
    print_Information_Var = title_Drivers_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Drivers Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

#   Read 1st Driver informations
    input_driverName_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, driverName_Drivers_ManagePageAdr))).text
    input_userNameName_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, userNameName_Drivers_ManagePageAdr))).text
    input_licenseNumber_Drivers_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, licenseNumber_Drivers_ManagePageAdr))).text

    # Drivers details page
    button_DriversDetails_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, button_DriversDetails_DriversChildPageAdr)))
    time.sleep(0.5)
    button_DriversDetails_DriversChildPage.click()

    #   Driver Child Page test:
    title_Driver_DriverChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Driver_DriverChildPageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Driver Child Page Open"
    condition1 = "Driver"
    condition2 = title_Driver_DriverChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Child Page Open"
    print_Information_Var = title_Driver_DriverChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Driver Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

#   Compare Driver/Manage Page information with Driver/Child Page
    input_DriverName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr))).text
    print(input_DriverName_DriversChildPage)
    input_DriverLastName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr))).text
    input_DriverUserName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverUserName_DriversChildPageAdr))).text
    input_LicenseNumber_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr))).text
    input_DriverNameLAstName_DriversChildPage = input_DriverName_DriversChildPage + input_DriverLastName_DriversChildPage

    print(input_DriverNameLAstName_DriversChildPage)




    #       Assert Test and print if assert is fail
    test_Name = "Driver Name - Driver Manage page x Driver Child Page"
    condition1 = input_driverName_Drivers_ManagePage
    condition2 = input_DriverNameLAstName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    test_Name = "Driver User Name - Driver Manage page x Driver Child Page"
    condition1 = input_userNameName_Drivers_ManagePage
    condition2 = input_DriverUserName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    test_Name = "Driver License Number - Driver Manage page x Driver Child Page"
    condition1 = input_licenseNumber_Drivers_ManagePage
    condition2 = input_LicenseNumber_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)


    #       Print Assert OK
    print_Information_Fix = "Driver Child Page Open"
    print_Information_Var = title_Driver_DriverChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Driver Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)


   #   Driver Name field test:
    input_DriverName_DriversChildPage.clear()
    input_DriverName_DriversChildPage.send_keys(input_DriverName_DriversChildPageVar)
    read_DriverName_DriversChildPage = input_DriverName_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Name - Password Child Page Open"
    condition1 = input_DriverName_DriversChildPageVar
    condition2 = read_DriverName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Name - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

   #   Driver Last Name field test:
    input_DriverLastName_DriversChildPage.clear()
    input_DriverLastName_DriversChildPage.send_keys(input_DriverLastName_DriversChildPageVar)
    read_DriverLastName_DriversChildPage = input_DriverLastName_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Last Name - Password Child Page Open"
    condition1 = input_DriverLastName_DriversChildPageVar
    condition2 = read_DriverLastName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Last Name - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverLastName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Driver User Name field test:
    input_DriverUserName_DriversChildPage.send_keys(input_DriverUserName_DriversChildPageVar)
    read_DriverUserName_DriversChildPage = input_DriverUserName_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier User Name - Password Child Page Open"
    condition1 = input_DriverUserName_DriversChildPageVar
    condition2 = read_DriverUserName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver User Name - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverUserName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Driver Password field test:
    input_DriverPassword_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverPassword_DriversChildPageAdr)))
    input_DriverPassword_DriversChildPage.clear()
    input_DriverPassword_DriversChildPage.send_keys(input_DriverPassword_DriversChildPageVar)
    read_DriverPassword_DriversChildPage = input_DriverPassword_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Password - Driver Child Page Open"
    condition1 = input_DriverPassword_DriversChildPageVar
    condition2 = read_DriverPassword_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Password - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverPassword_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Driver Confirmation field test:
    input_DriverConfirmation_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverConfirmation_DriversChildPageAdr)))
    input_DriverConfirmation_DriversChildPage.clear()
    input_DriverConfirmation_DriversChildPage.send_keys(input_DriverPassword_DriversChildPageVar)
    read_DriverConfirmation_DriversChildPage = input_DriverConfirmation_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Driver Confirmation - Driver Child Page Open"
    condition1 = input_DriverPassword_DriversChildPageVar
    condition2 = read_DriverConfirmation_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Confirmation - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverConfirmation_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #       Ruleset field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_Ruleset_DriversChilPageAdr))))
    dropdown_Import_Option_Ruleset_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Option_Ruleset_DriversChilPage_List):
        dropdown_Ruleset_DriversChilPage = dropDown.select_by_visible_text(dropdown_Import_Option_Ruleset_DriversChilPage_List[n])
        # read the selected option on the dropdown
        dropdown_Ruleset_DriversChilPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ****************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Driver Ruleset element - Driver Child Page Open select information OK!"
        lastOptionsDropDown_Ruleset_DriversChildPageVar = dropdown_Import_Option_Ruleset_DriversChilPage_List[n]
        condition1 = lastOptionsDropDown_Ruleset_DriversChildPageVar
        condition2 = dropdown_Ruleset_DriversChilPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Driver Ruleset element - Driver Child Page information OK!"
        print_Information_Var = dropdown_Ruleset_DriversChilPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #       24-Periode Starting Time field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_24PeriodeStartingTime_DriversChilPageAdr))))
    dropdown_Import_Option_24PeriodeStartingTime_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Option_24PeriodeStartingTime_DriversChilPage_List):
        dropdown_Ruleset_DriversChilPage = dropDown.select_by_visible_text(dropdown_Import_Option_24PeriodeStartingTime_DriversChilPage_List[n])
        # read the selected option on the dropdown
        dropdown_24PeriodeStartingTime_DriversChilPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Driver 24PeriodeStartingTime element - Driver Child Page Open select information OK!"
        lastOptionsDropDown_24PeriodeStartingTime_DriversChildPageVar = dropdown_Import_Option_24PeriodeStartingTime_DriversChilPage_List[n]
        condition1 = lastOptionsDropDown_24PeriodeStartingTime_DriversChildPageVar
        condition2 = dropdown_24PeriodeStartingTime_DriversChilPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Driver 24PeriodeStartingTime element - Driver Child Page information OK!"
        print_Information_Var = dropdown_24PeriodeStartingTime_DriversChilPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    test_Name = "Driver ChilPage - 1"
    tc_reports.screenshot(driver, driver_Name, test_Name)


    #       Units field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_Units_DriversChilPageAdr))))
    dropdown_Import_Option_Units_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Option_Units_DriversChilPage_List):
        dropdown_Units_DriversChilPage = dropDown.select_by_visible_text(dropdown_Import_Option_Units_DriversChilPage_List[n])
        # read the selected option on the dropdown
        dropdown_Units_DriversChilPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Driver Units element - Driver Child Page Open select information OK!"
        lastOptionsDropDown_Units_DriversChildPageVar = dropdown_Import_Option_Units_DriversChilPage_List[n]
        condition1 = lastOptionsDropDown_Units_DriversChildPageVar
        condition2 = dropdown_Units_DriversChilPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Driver Units element - Driver Child Page information OK!"
        print_Information_Var = dropdown_Units_DriversChilPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)


    #       LicenseState field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_LicenseState_DriversChilPageAdr))))
    dropdown_Import_Option_LicenseState_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Option_LicenseState_DriversChilPage_List):
        dropdown_Units_DriversChilPage = dropDown.select_by_visible_text(dropdown_Import_Option_LicenseState_DriversChilPage_List[n])
        # read the selected option on the dropdown
        dropdown_LicenseState_DriversChilPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Driver LicenseState element - Driver Child Page Open select information OK!"
        lastOptionsDropDown_LicenseState_DriversChildPageVar = dropdown_Import_Option_LicenseState_DriversChilPage_List[n]
        condition1 = lastOptionsDropDown_LicenseState_DriversChildPageVar
        condition2 = dropdown_LicenseState_DriversChilPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Driver LicenseState element - Driver Child Page information OK!"
        print_Information_Var = dropdown_LicenseState_DriversChilPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)


    #   License Number field test:
    input_LicenseNumber_DriversChildPage.clear()
    input_LicenseNumber_DriversChildPage.send_keys(input_LicenseNumber_DriversChildPageVar)
    read_LicenseNumber_DriversChildPage = input_LicenseNumber_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Driver LicenseNumber - Driver Child Page Open"
    condition1 = input_LicenseNumber_DriversChildPageVar
    condition2 = read_LicenseNumber_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver LicenseNumber - Driver Child Page input type information OK!"
    print_Information_Var = read_LicenseNumber_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Driver ChilPage - 2"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    ############################################################################################################################
    #                                                SAVED Info Test                                                           #
    ############################################################################################################################

    w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_SAVE_DriversChildPageAdr))).click()
    time.sleep(0.5)
    # Verify the saved information and SAVE button #####################################################################
    # Drivers details page
    button_DriversDetails_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, button_DriversDetails_DriversChildPageAdr)))
    time.sleep(0.5)
    button_DriversDetails_DriversChildPage.click()


    #   Driver Name field test:
    input_DriverName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr)))
    read_DriverName_DriversChildPage = input_DriverName_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Name SAVED - Password Child Page Open"
    condition1 = input_DriverName_DriversChildPageVar
    condition2 = read_DriverName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Name SAVED - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)

    #   Driver Last Name field test:
    input_DriverLastName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr)))
    read_DriverLastName_DriversChildPage = input_DriverLastName_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Carrier Last Name SAVED - Password Child Page Open"
    condition1 = input_DriverLastName_DriversChildPageVar
    condition2 = read_DriverLastName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Last Name SAVED - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverLastName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)

    #   Driver User Name field test:
    input_DriverUserName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverUserName_DriversChildPageAdr)))
    read_DriverUserName_DriversChildPage = input_DriverUserName_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Driver User Name SAVED - Password Child Page Open"
    condition1 = input_DriverUserName_DriversChildPageVar
    condition2 = read_DriverUserName_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver User Name SAVED - Driver Child Page input type information OK!"
    print_Information_Var = read_DriverUserName_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)

       #       Ruleset field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_Ruleset_DriversChilPageAdr))))
    # read the selected option on the dropdown
    dropdown_Ruleset_DriversChilPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  **************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Driver Ruleset element - Driver Child Page Open select information OK!"
    condition1 = lastOptionsDropDown_Ruleset_DriversChildPageVar
    condition2 = dropdown_Ruleset_DriversChilPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Ruleset element SAVED - Driver Child Page information OK!"
    print_Information_Var = dropdown_Ruleset_DriversChilPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       24-Periode Starting Time field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_24PeriodeStartingTime_DriversChilPageAdr))))

    # read the selected option on the dropdown
    dropdown_24PeriodeStartingTime_DriversChilPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ***************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Driver 24PeriodeStartingTime element SAVED - Driver Child Page Open select information OK!"

    condition1 = lastOptionsDropDown_24PeriodeStartingTime_DriversChildPageVar
    condition2 = dropdown_24PeriodeStartingTime_DriversChilPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver 24PeriodeStartingTime element SAVED - Driver Child Page information OK!"
    print_Information_Var = dropdown_24PeriodeStartingTime_DriversChilPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Driver Driver ChilPage SAVED - 1"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #       Units field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_Units_DriversChilPageAdr))))
    # read the selected option on the dropdown
    dropdown_Units_DriversChilPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Driver Units element SAVED - Driver Child Page Open select information OK!"

    condition1 = lastOptionsDropDown_Units_DriversChildPageVar
    condition2 = dropdown_Units_DriversChilPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Units element SAVED - Driver Child Page information OK!"
    print_Information_Var = dropdown_Units_DriversChilPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)

    #       LicenseState field Check:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropdown_LicenseState_DriversChilPageAdr))))
    # read the selected option on the dropdown
    dropdown_LicenseState_DriversChilPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Driver LicenseState element SAVED - Driver Child Page Open select information OK!"

    condition1 = lastOptionsDropDown_LicenseState_DriversChildPageVar
    condition2 = dropdown_LicenseState_DriversChilPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver LicenseState element SAVED - Driver Child Page information OK!"
    print_Information_Var = dropdown_LicenseState_DriversChilPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   License Number field test:
    input_LicenseNumber_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr)))
    read_LicenseNumber_DriversChildPage = input_LicenseNumber_DriversChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Driver LicenseNumber SAVED - Driver Child Page Open"
    condition1 = input_LicenseNumber_DriversChildPageVar
    condition2 = read_LicenseNumber_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver LicenseNumber SAVED - Driver Child Page input type information OK!"
    print_Information_Var = read_LicenseNumber_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Driver ChilPage SAVED - 2"
    tc_reports.screenshot(driver, driver_Name, test_Name)


    # CLOSE button
    w.until(EC.element_to_be_clickable((By.XPATH, button_Driver_CLOSE_DriversChildPageAdr))).click()

    #   Drivers Page test:
    title_Drivers_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_Drivers_DriversChildPageAdr)))).text
    print(title_Drivers_DriversChildPage)
    #       Assert Test and print if assert is fail
    test_Name = "Drivers Child Page Open"
    condition1 = "Drivers"
    condition2 = title_Drivers_DriversChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver CLOSE button OK "
    print_Information_Var = title_Drivers_DriversChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Drivers Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)
#               Apollo Web Portal - Manage - Home Bases


def carrierHomeBases_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import test_Global_Variables_apolloWebPortal
    import re
    from selenium.webdriver import ActionChains
    import test_Global_Variables_apolloWebPortal


#       Carrier details Page Address & Variables
#       Fields Address
    button_Carrier_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[3]"
    title_HomeBases_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[1]/h3"
    button_PlussNew_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[1]/div/button"
    title_HomeBases_HomeBases_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[1]/h3"
    title_HomeBase_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[1]/h4"
    input_LocationName_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[1]/input"
    input_Address_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[2]/input"
    input_Latitude_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[3]/input"
    input_Longitude_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[4]/input"
    dropDown_TimeZone_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[5]/select"
    checkBox_SetMainOffice_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[1]/div[6]/div/input"
    button_SAVE_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[2]/button[1]"
    button_CLOSE_HomeBase_ChildPageAdr = "/html/body/ngb-modal-window/div/div/homebase-modal-form/div[2]/form/div[2]/button[2]"
    indicator_Sort_Name_HomeBasesPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[5]/div[1]/table/tbody/tr/td[1]"

    text_FirstName_HomeBasesPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[1]"
    button_Details_Action_HomeBasePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/button[1]"
    button_Delete_Action_HomeBasePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/button[2]"
    button_DriverAssignment_Action_HomeBasePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-homebase-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[4]/div/button[3]"

    checkBox_Assignment_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[1]/div[2]/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[3]/div/dx-check-box/div/span"
    button_SAVE_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[2]/button[1]"
    button_CLOSE_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[2]/button[2]"
    button_PageNumber_DriverAssignmentChild_HomeBasesPageAdr = "/html/body/ngb-modal-window/div/div/app-drivers-assigned/div[2]/form/div[1]/div[2]/dx-data-grid/div/div[10]/div/div[1]"

    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)
    """
    input_LocationName_HomeBase_ChildPageVar = "AAA Miami Dolphins Stadium"
    input_Address_HomeBase_ChildPageVar = "347 Don Shula Dr, Miami Gardens, FL 33056"
    input_Latitude_HomeBase_ChildPageVar = "25.95856"
    input_Longitude_HomeBase_ChildPageVar = "-80.23965"
    """

    input_LocationName_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_LocationName_HomeBase_ChildPage_Global
    input_Address_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_Address_HomeBase_ChildPage_Global
    input_Latitude_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_Latitude_HomeBase_ChildPage_Global
    input_Longitude_HomeBase_ChildPageVar = test_Global_Variables_apolloWebPortal.input_Longitude_HomeBase_ChildPage_Global
    input_LocationName_HomeBase_ChildPageVar = input_LocationName_HomeBase_ChildPageVar + str(date)

    #####################################################################################################################################
    #                                                   Home Bases Main functions                                                       #
    #####################################################################################################################################

    #####################################################################################################################################
    #                                                   Home Bases ACTIONS DETAILS Main functions                                       #
    #####################################################################################################################################

    #   Page Title on TCReport
    function_Name = "Carriers Home Bases Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # Home Page button
    button_Carrier_HomeBases_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_HomeBases_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_HomeBases_ManagePage.click()

    #   Home Bases Page Open test:
    title_HomeBases_HomeBases_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_HomeBases_HomeBases_ManagePageAdr)))).text
    print(title_HomeBases_HomeBases_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Home Bases Page Open"
    condition1 = "Home Bases"
    condition2 = title_HomeBases_HomeBases_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Home Bases Page Open"
    print_Information_Var = title_HomeBases_HomeBases_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Bases Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_HomeBases_ManagePageAdr))).click()

    #   Home Bases ChildPage Open test:
    title_HomeBase_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_HomeBase_HomeBase_ChildPageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Home Bases Child Page Open"
    condition1 = "Home Base"
    condition2 = title_HomeBase_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Home Base Child Page Open"
    print_Information_Var = title_HomeBase_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Base New Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Location Name Home Base Child Page test:
    input_LocationName_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_LocationName_HomeBase_ChildPageAdr))))
    input_LocationName_HomeBase_ChildPage.send_keys(input_LocationName_HomeBase_ChildPageVar)
    read_LocationName_HomeBase_ChildPage = input_LocationName_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Location Name Home Base Child Page Open"
    condition1 = input_LocationName_HomeBase_ChildPageVar
    condition2 = read_LocationName_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Location Name Home Base Child Page"
    print_Information_Var = read_LocationName_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #   Address Home Base Child Page test:
    input_Address_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Address_HomeBase_ChildPageAdr))))
    input_Address_HomeBase_ChildPage.send_keys(input_Address_HomeBase_ChildPageVar)
    read_Address_HomeBase_ChildPage = input_Address_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Address Home Base Child Page Open"
    condition1 = input_Address_HomeBase_ChildPageVar
    condition2 = read_Address_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Address Home Base Child Page"
    print_Information_Var = read_Address_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    #   Latitude Home Base Child Page test:
    input_Latitude_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Latitude_HomeBase_ChildPageAdr))))
    input_Latitude_HomeBase_ChildPage.send_keys(input_Latitude_HomeBase_ChildPageVar)
    read_Latitude_HomeBase_ChildPage = input_Latitude_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Latitude Home Base Child Page Open"
    condition1 = input_Latitude_HomeBase_ChildPageVar
    condition2 = read_Latitude_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Latitude Home Base Child Page"
    print_Information_Var = read_Latitude_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Longitude Home Base Child Page test:
    input_Longitude_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Longitude_HomeBase_ChildPageAdr))))
    input_Longitude_HomeBase_ChildPage.send_keys(input_Longitude_HomeBase_ChildPageVar)
    read_Longitude_HomeBase_ChildPage = input_Longitude_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Longitude Home Base Child Page Open"
    condition1 = input_Longitude_HomeBase_ChildPageVar
    condition2 = read_Longitude_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Longitude"
    print_Information_Var = read_Longitude_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Time Zone Home Base Child Page test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_TimeZone_HomeBase_ChildPageAdr))))
    dropDown_Import_TimeZone_HomeBase_ChildPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropDown_Import_TimeZone_HomeBase_ChildPage_List):
        dropDown_TimeZone_HomeBase_ChildPage = dropDown.select_by_visible_text(dropDown_Import_TimeZone_HomeBase_ChildPage_List[n])
        # read the selected option on the dropdown
        dropDown_TimeZone_HomeBase_ChildPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ****************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Time Zone Home Base Child Page Open"
        last_Options_dropDown_TimeZone_HomeBase_ChildPageVar = dropDown_Import_TimeZone_HomeBase_ChildPage_List[n]
        condition1 = last_Options_dropDown_TimeZone_HomeBase_ChildPageVar
        condition2 = dropDown_TimeZone_HomeBase_ChildPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Time Zone Home Base Child Page"
        print_Information_Var = dropDown_TimeZone_HomeBase_ChildPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1

#   Select a random time zone for each test
    n = date.strftime("%S")
    n = int(n[1])
    if n > 7:
        n = n - 3
    dropDown_Random_TimeZone_HomeBase_ChildPage = dropDown.select_by_visible_text(dropDown_Import_TimeZone_HomeBase_ChildPage_List[n])

    #    Set as Main Office Home Base Child Page test:
    read_checkBox_SetMainOffice_HomeBase_ChildPage = w.until(EC.presence_of_element_located((By.XPATH, checkBox_SetMainOffice_HomeBase_ChildPageAdr)))
    if read_checkBox_SetMainOffice_HomeBase_ChildPage.is_selected():
            #       ERROR Assert Test and print if assert is fail
        test_Name = "Set as Main Office CheckBox would be UNCHECKED, but is CHECKED !!!!!!!!!!"
        condition1 = ""
        condition2 = "1"
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    else:
        w.until(EC.presence_of_element_located((By.XPATH, checkBox_SetMainOffice_HomeBase_ChildPageAdr))).click()
        read_checkBox_SetMainOffice_HomeBase_ChildPage = w.until(EC.presence_of_element_located((By.XPATH, checkBox_SetMainOffice_HomeBase_ChildPageAdr)))
        if read_checkBox_SetMainOffice_HomeBase_ChildPage.is_selected():
            #       Print Assert OK
            print_Information_Fix = "Set as Main Office CheckBox IS CHECKED, ok!!!!!!!!!!"
            print_Information_Var = "Checked"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       ERROR Assert Test and print if assert is fail
            test_Name = "Set as Main Office CheckBox would be CHECKED, but is UNCHECKED !!!!!!!!!!"
            condition1 = ""
            condition2 = "1"
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Screenshot
    test_Name = "Home Base Filled up Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)
#   Unselect Main Ofice
    w.until(EC.presence_of_element_located((By.XPATH, checkBox_SetMainOffice_HomeBase_ChildPageAdr))).click()

#   SAVE Button Home Base Child Page test:
    w.until((EC.element_to_be_clickable((By.XPATH, button_SAVE_HomeBase_ChildPageAdr)))).click()

# ************************************************************************************************************************************
#*                                                  Verify SAVED Information                                                         *
# ************************************************************************************************************************************

    #   Home Bases Page Open after SAVE test:
    title_HomeBases_HomeBases_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_HomeBases_HomeBases_ManagePageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Home Bases Page Open after SAVE"
    condition1 = "Home Bases"
    condition2 = title_HomeBases_HomeBases_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Home Bases Page Open after SAVE"
    print_Information_Var = title_HomeBases_HomeBases_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Bases Page after SAVE"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Sort Home Bases Name in alphabetic order
    w.until(EC.presence_of_element_located((By.XPATH, indicator_Sort_Name_HomeBasesPageAdr))).click()
    w.until(EC.presence_of_element_located((By.XPATH, indicator_Sort_Name_HomeBasesPageAdr))).click()
    time.sleep(0.5)

    # Check New Home bases saved
    read_Text_Name_HomeBasesPage = w.until(EC.presence_of_element_located((By.XPATH, text_FirstName_HomeBasesPageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "New Home Bases SAVED"
    condition1 = input_LocationName_HomeBase_ChildPageVar
    condition2 = read_Text_Name_HomeBasesPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Home Bases SAVED"
    print_Information_Var = read_Text_Name_HomeBasesPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "New Home Bases SAVED"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Check Details - All Home base information filled in

    w.until(EC.element_to_be_clickable((By.XPATH, button_Details_Action_HomeBasePageAdr))).click()

    #   Details - Home Bases ChildPage Open test:
    title_HomeBase_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, title_HomeBase_HomeBase_ChildPageAdr)))).text
    #       Assert Test and print if assert is fail
    test_Name = "Details - Home Bases Child Page Open"
    condition1 = "Home Base"
    condition2 = title_HomeBase_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Details - Home Base Child Page Open"
    print_Information_Var = title_HomeBase_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Details - Home Base New Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)


    #   Location Name Home Base Child Page test:
    input_LocationName_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_LocationName_HomeBase_ChildPageAdr))))
    read_LocationName_HomeBase_ChildPage = input_LocationName_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Details Location Name Home Base Child Page"
    condition1 = input_LocationName_HomeBase_ChildPageVar
    condition2 = read_LocationName_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Details - Location Name Home Base Child Page"
    print_Information_Var = read_LocationName_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Address Home Base Child Page test:
    input_Address_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Address_HomeBase_ChildPageAdr))))
    read_Address_HomeBase_ChildPage = input_Address_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Details - Address Home Base Child Page Open"
    condition1 = input_Address_HomeBase_ChildPageVar
    condition2 = read_Address_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Details - Address Home Base Child Page"
    print_Information_Var = read_Address_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Latitude Home Base Child Page test:
    input_Latitude_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Latitude_HomeBase_ChildPageAdr))))
    read_Latitude_HomeBase_ChildPage = input_Latitude_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Details - Latitude Home Base Child Page Open"
    condition1 = input_Latitude_HomeBase_ChildPageVar
    condition2 = read_Latitude_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Details - Latitude Home Base Child Page"
    print_Information_Var = read_Latitude_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Longitude Home Base Child Page test:
    input_Longitude_HomeBase_ChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_Longitude_HomeBase_ChildPageAdr))))
    read_Longitude_HomeBase_ChildPage = input_Longitude_HomeBase_ChildPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Details - Longitude Home Base Child Page Open"
    condition1 = input_Longitude_HomeBase_ChildPageVar
    condition2 = read_Longitude_HomeBase_ChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Details - Longitude"
    print_Information_Var = read_Longitude_HomeBase_ChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Time Zone Home Base Child Page test:
    dropDown = Select(w.until(EC.presence_of_element_located((By.XPATH, dropDown_TimeZone_HomeBase_ChildPageAdr))))
    # read the selected option on the dropdown
    dropDown_TimeZone_HomeBase_ChildPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ****************************************************************************
    #       Assert Test and print if assert is fail
    test_Name = "Details - Time Zone Home Base Child Page Open"

    condition1 = dropDown_Random_TimeZone_HomeBase_ChildPage
    condition2 = dropDown_TimeZone_HomeBase_ChildPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Details - Time Zone Home Base Child Page"
    print_Information_Var = dropDown_TimeZone_HomeBase_ChildPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #    Set as Main Office Home Base Child Page test:
    read_checkBox_SetMainOffice_HomeBase_ChildPage = w.until(EC.presence_of_element_located((By.XPATH, checkBox_SetMainOffice_HomeBase_ChildPageAdr)))
    if read_checkBox_SetMainOffice_HomeBase_ChildPage.is_selected():
        #       ERROR Assert Test and print if assert is fail
        test_Name = "Set as Main Office CheckBox SAVED would be UNCHECKED, but is CHECKED !!!!!!!!!!"
        condition1 = ""
        condition2 = "1"
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    else:
        #       Print Assert OK
        print_Information_Fix = "Set as Main Office CheckBox SAVED IS UNCHECKED, ok!!!!!!!!!!"
        print_Information_Var = "UnChecked"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Home Base Filled up SAVED Child Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)
    w.until(EC.presence_of_element_located((By.XPATH, checkBox_SetMainOffice_HomeBase_ChildPageAdr))).click()


    #   CLOSE Button Home Base Child Page test:
    w.until((EC.element_to_be_clickable((By.XPATH, button_CLOSE_HomeBase_ChildPageAdr)))).click()

    #####################################################################################################################################
    #                                        Home Bases ACTIONS DRIVER ASSIGNMENT Main functions                                        #
    #####################################################################################################################################



    # Drivers Assigment test

    w.until(EC.element_to_be_clickable((By.XPATH, button_DriverAssignment_Action_HomeBasePageAdr))).click()
    read_checkBox_Assignment_DriverAssignmentChild_HomeBasesPage = w.until(EC.presence_of_element_located((By.XPATH, checkBox_Assignment_DriverAssignmentChild_HomeBasesPageAdr)))
    if read_checkBox_Assignment_DriverAssignmentChild_HomeBasesPage.is_selected():
            #       ERROR Assert Test and print if assert is fail
        test_Name = "Driver Assignment CheckBox would be UNCHECKED, but is CHECKED !!!!!!!!!!"
        condition1 = ""
        condition2 = "1"
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    else:
        w.until(EC.presence_of_element_located((By.XPATH, checkBox_Assignment_DriverAssignmentChild_HomeBasesPageAdr))).click()
        time.sleep(0.5)
        read_checkBox_Assignment_DriverAssignmentChild_HomeBasesPage = w.until(EC.presence_of_element_located((By.XPATH,checkBox_Assignment_DriverAssignmentChild_HomeBasesPageAdr)))
        if read_checkBox_Assignment_DriverAssignmentChild_HomeBasesPage.is_selected():
            #       Print Assert OK
            print_Information_Fix = "Driver Assignment CheckBox IS CHECKED, ok!!!!!!!!!!"
            print_Information_Var = "Checked"
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        else:
            #       ERROR Assert Test and print if assert is fail
            test_Name = "Driver Assignment CheckBox would be CHECKED, but is UNCHECKED !!!!!!!!!!"
            condition1 = ""
            condition2 = "1"
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Screenshot
    test_Name = "Driver Assignment CheckBox"
    tc_reports.screenshot(driver, driver_Name, test_Name)
    w.until(EC.presence_of_element_located((By.XPATH, checkBox_Assignment_DriverAssignmentChild_HomeBasesPageAdr))).click()


    # CLOSE Button
    w.until(EC.element_to_be_clickable((By.XPATH, button_CLOSE_DriverAssignmentChild_HomeBasesPageAdr))).click()



    #####################################################################################################################################
    #                                                   Home Bases ACTIONS DELETE Main functions                                        #
    #####################################################################################################################################


    # Check New Home bases saved
    read_Text_Name_HomeBasesPage = w.until(EC.presence_of_element_located((By.XPATH, text_FirstName_HomeBasesPageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "New Home Bases SAVED - DELETE Function"
    condition1 = input_LocationName_HomeBase_ChildPageVar
    condition2 = read_Text_Name_HomeBasesPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Home Bases SAVED - DELETE Function"
    print_Information_Var = read_Text_Name_HomeBasesPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    # Delete New Home Base
    w.until(EC.element_to_be_clickable((By.XPATH, button_Delete_Action_HomeBasePageAdr))).click()
    time.sleep(0.5)
    # Delete Check New Home bases saved
    read_Text_Name_HomeBasesPage = w.until(EC.presence_of_element_located((By.XPATH, text_FirstName_HomeBasesPageAdr))).text
    #       Assert Test and print if assert is fail
    test_Name = "New Home Bases SAVED is DELETED - DELETE Function"

    print(input_LocationName_HomeBase_ChildPageVar)
    print(read_Text_Name_HomeBasesPage)

    if read_Text_Name_HomeBasesPage == input_LocationName_HomeBase_ChildPageVar:
        condition1 = "1"
        condition2 = read_Text_Name_HomeBasesPage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "New Home Bases SAVED is DELETED - DELETE Function"
    print_Information_Var = read_Text_Name_HomeBasesPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "New Home Bases SAVED is DELETED - DELETE Function"
    time.sleep(0.5)
    tc_reports.screenshot(driver, driver_Name, test_Name)



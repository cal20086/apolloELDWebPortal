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
    import os
    import re
    import test_Global_Variables_apolloWebPortal
    from selenium.webdriver import ActionChains
    import test_Global_Variables_apolloWebPortal
    import openpyxl
    from pathlib import Path


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
    dropdown_HomeBase_DriversChilPageId = "homebase"
    dropdown_Ruleset_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[6]/select"
    dropdown_Ruleset_DriversChilPageId = "ruleset"
    dropdown_24PeriodeStartingTime_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[7]/select"
    dropdown_24PeriodeStartingTime_DriversChilPageId = "startingTime"
    dropdown_RegistrationState_DriversChilPageId = "state"
    dropdown_Units_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[12]/select"
    dropdown_Units_DriversChilPageId = "fuelUnitCode"
    dropdown_LicenseState_DriversChilPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[13]/select"
    dropdown_LicenseState_DriversChilPageId = "state"
    input_LicenseNumber_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[15]/input"

    button_Driver_SAVE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]/button[1]"
    button_Driver_CLOSE_DriversChildPageAdr = "/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[2]/button[3]"
    driverName_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[1]/div"
    userNameName_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]"
    licenseNumber_Drivers_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-driver-list/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[3]"



#   Global variables
    input_DriverName_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverName_DriversChildPage_Global
    input_DriverLastName_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverLastName_DriversChildPage_Global
    input_DriverUserName_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverUserName_DriversChildPage_Global
    input_DriverPassword_DriversChildPageVar = test_Global_Variables_apolloWebPortal.input_DriverPassword_DriversChildPage_Global
    #Excel
    workbookMANAGEDB = test_Global_Variables_apolloWebPortal.workbookMANAGEDB_Global
    worksheetMANAGEDB = test_Global_Variables_apolloWebPortal.worksheetMANAGEDB_Global


    #   Read excel Variables
    excell_pointer = Path(workbookMANAGEDB)
    # Read excel value not formula
    workbookMANAGEDB_Read = openpyxl.load_workbook(excell_pointer, data_only=True)
    worksheetMANAGEDB_Read = workbookMANAGEDB_Read.active

#   Local variables
    date = datetime.now()
    input_LicenseNumberFull_DriversChildPageVar = "Lic" + date.strftime(" %b%d%Y") + date.strftime("%H:%M:%S")
    input_LicenseNumber_DriversChildPageVar = re.sub('\W+','', input_LicenseNumberFull_DriversChildPageVar)
    excel_RuleSetTotal_cellValue = worksheetMANAGEDB_Read['A2'].value
    excel_24PeriodeTotal_cellValue = worksheetMANAGEDB_Read['C2'].value
    excel_StateTotal_cellValue = worksheetMANAGEDB_Read['E2'].value
    w = WebDriverWait(driver, 30)

    #Excel
    excel_DB_line = 4
    excel_DB_line_LogicTest = 2
    colum_Manage_RuleSetTotal = "A"
    colum_Manage_RuleSets = "B"








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

    print(input_driverName_Drivers_ManagePage)
    print(input_userNameName_Drivers_ManagePage)
    print(input_licenseNumber_Drivers_ManagePage)

    # Drivers details page
    button_DriversDetails_DriversChildPage = w.until(EC.element_to_be_clickable((By.XPATH, button_DriversDetails_DriversChildPageAdr)))
    #time.sleep(0.5)
    button_DriversDetails_DriversChildPage.click()


    #   Driver Child Page test:
    #######################################################################################################################################
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
    input_DriverName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH,input_DriverName_DriversChildPageAdr))).get_attribute('value')
    input_DriverLastName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr))).get_attribute('value')
    input_DriverUserName_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_DriverUserName_DriversChildPageAdr))).get_attribute('value')


    #########################################################################################################################################################################

    # TEST NAME FIELD RULES
    input_DriverName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr))))
    input_DriverName_DriversChildPage.clear()
    input_DriverName_DriversChildPage.send_keys("T")
    input_DriverName_DriversChildPageClass = w.until((EC.presence_of_element_located((By.XPATH, input_DriverName_DriversChildPageAdr)))).get_attribute('class')
    # Assert
    test_Name = "Name < 2 -> ERROR"
    condition1 = input_DriverName_DriversChildPageClass
    condition2 = "form-control ng-invalid is-invalid ng-touched ng-dirty"
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Child Page field NAME < 2 -> ! "
    print_Information_Var = input_DriverName_DriversChildPageClass
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    # TEST LAST NAME FIELD RULES
    input_DriverLastName_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr))))
    input_DriverLastName_DriversChildPage.clear()
    input_DriverLastName_DriversChildPage.send_keys("T")
    input_DriverLastName_DriversChildPageClass = w.until((EC.presence_of_element_located((By.XPATH, input_DriverLastName_DriversChildPageAdr)))).get_attribute('class')
    # Assert
    test_Name = "Last Name < 2 -> ERROR"
    condition1 = input_DriverLastName_DriversChildPageClass
    condition2 = "form-control ng-invalid is-invalid ng-touched ng-dirty"
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Child Page field LAST NAME < 2 -> ! "
    print_Information_Var = input_DriverLastName_DriversChildPageClass
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #Home Base options
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_HomeBase_DriversChilPageId))))
    dropdown_HomeBase_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_HomeBase_DriversChilPage_List):
        dropdown_HomeBase_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_HomeBase_DriversChilPage_List[n])
        dropdown_HomeBase_DriversChilPage_Read = dropDown.first_selected_option.text
        print(dropdown_HomeBase_DriversChilPage_Read)
        n = n + 1

    #Rule Set options
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_Ruleset_DriversChilPageId))))
    dropdown_Ruleset_DriversChilPage_List = [x.text for x in dropDown.options]
    # Assert
    test_Name = "Rule Set Options quantities"
    condition1 = str(len(dropdown_Ruleset_DriversChilPage_List))
    condition2 = str(excel_RuleSetTotal_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Rule Set Options quantities: "
    print_Information_Var = str(len(dropdown_Ruleset_DriversChilPage_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    n = 0
    while n < len(dropdown_Ruleset_DriversChilPage_List):
        dropdown_Ruleset_DriversChilPage = dropDown.select_by_visible_text(dropdown_Ruleset_DriversChilPage_List[n])
        dropdown_Ruleset_DriversChilPage_Read = dropDown.first_selected_option.text
        indice = "B" + str(n+2)
        ruleSet_Excel = worksheetMANAGEDB_Read[indice].value


        # Assert
        test_Name = "Rule Set Options"
        condition1 = str(ruleSet_Excel)
        condition2 = str(dropdown_Ruleset_DriversChilPage_Read)
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Rule Set Options: "
        print_Information_Var = str(ruleSet_Excel)
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1


    #24-Period Starting Time
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_24PeriodeStartingTime_DriversChilPageId))))
    dropdown_24PeriodeStartingTime_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    # Assert
    test_Name = "24-Periode Starting Time Options quantities"
    condition1 = str(len(dropdown_24PeriodeStartingTime_DriversChilPage_List))
    condition2 = str(excel_24PeriodeTotal_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "24-Periode Starting Time quantities: "
    print_Information_Var = str(len(dropdown_24PeriodeStartingTime_DriversChilPage_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    print(f'Celula C2 = {excel_RuleSetTotal_cellValue} x {len(dropdown_Ruleset_DriversChilPage_List)}')
    while n < len(dropdown_24PeriodeStartingTime_DriversChilPage_List):
        dropdown_24PeriodeStartingTime_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_24PeriodeStartingTime_DriversChilPage_List[n])
        dropdown_24PeriodeStartingTime_DriversChilPage_Read = dropDown.first_selected_option.text
        print(dropdown_24PeriodeStartingTime_DriversChilPage_Read)
        n = n + 1


    # Move page down to License field - page Scroll down
    input_LicenseNumber_DriversChildPage = w.until(EC.presence_of_element_located((By.XPATH,"/html/body/ngb-modal-window/div/div/app-driver-form/div[2]/form/div[1]/div[18]/div/label")))
    actions = ActionChains(driver)
    actions.move_to_element(input_LicenseNumber_DriversChildPage)
    actions.perform()
    #browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    """
    #Registration State
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropdown_RegistrationState_DriversChilPageId))))
    dropdown_RegistrationState_DriversChilPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_RegistrationState_DriversChilPage_List):
        dropdown_RegistrationState_DriversChilPage_Selected = dropDown.select_by_visible_text(dropdown_RegistrationState_DriversChilPage_List[n])
        dropdown_RegistrationState_DriversChilPage_Read = dropDown.first_selected_option.text
        print(dropdown_RegistrationState_DriversChilPage_Read)
        n = n + 1
    """

    # TEST LICENSE NUMBER FIELD RULES
    input_LicenseNumber_DriversChildPage = w.until((EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr))))
    input_LicenseNumber_DriversChildPage.clear()
    input_LicenseNumber_DriversChildPage.send_keys("T")
    input_LicenseNumber_DriversChildPageClass = w.until((EC.presence_of_element_located((By.XPATH, input_LicenseNumber_DriversChildPageAdr)))).get_attribute('class')
    # Assert
    test_Name = "License Number < 2 -> ERROR"
    condition1 = input_LicenseNumber_DriversChildPageClass
    condition2 = "form-control ng-touched is-invalid ng-dirty ng-invalid"
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Driver Child Page field License Number < 2 -> ! "
    print_Information_Var = input_LicenseNumber_DriversChildPageClass
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
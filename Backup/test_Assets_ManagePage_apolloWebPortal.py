#               Apollo Web Portal - Manage - Assets


def carrierAssets_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from datetime import datetime
    import tc_reports
    import re
    from  selenium.webdriver import ActionChains

#       Carrier details Page Address & Variables
#       Fields Address

    button_Carrier_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[4]"
    title_Assets_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-asset-list/div/div/div[1]/h3"
    button_PlussNew_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-asset-list/div/div/div[1]/div/button"





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

    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)

    #####################################################################################################################################
    #                                                       ASSETS Main functions                                                       #
    #####################################################################################################################################

  #   Page Title on TCReport
    function_Name = "Carriers ASSETS Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # Home Page button
    button_Carrier_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Assets_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Assets_ManagePage.click()

    #   Home Bases Page Open test:
    title_Assets_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Assets_Assets_ManagePageAdr)))).text
    print(title_Assets_Assets_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Assets Page Open"
    condition1 = "Assets"
    condition2 = title_Assets_Assets_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Assets Page Open"
    print_Information_Var = title_Assets_Assets_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Assets Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Assets_ManagePageAdr))).click()
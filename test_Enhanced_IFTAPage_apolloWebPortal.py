#               Apollo Web Portal - IFTA

def EnhancedIFTA_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support.ui import Select
    import tc_reports
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.select import Select
    import os
    import glob
    import openpyxl
    from pathlib import Path
    from pathlib import Path
    from os import path
    from datetime import datetime, timedelta
    from selenium.common.exceptions import NoSuchElementException
    import test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal
    import test_Global_Variables_apolloWebPortal

    #               DVIR Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"
    button_EnhancedIFTA_ManagePageAdr = '//a[contains(@href,"/enhancedifta")]'
    dropbox_Year_EnhancedIFTAPageID = "yearSelector"
    dropbox_Quarter_EnhancedIFTAPageID = "quarterSelector"
    dropbox_Month_EnhancedIFTAPageID = "monthSelector"
    dropbox_Carrier_EnhancedIFTAPageID = "carrierSelector"
    dropbox_Region_EnhancedIFTAPageID = "carrierCountry"
    dropbox_Vehicle_EnhancedIFTAPageID = "vehicleSelector"
    title_EnhancedIFTA_EnhancedIFTAPageAdr = "/html/body/app-root/app-main/div/div/app-ifta-reporting/section[1]/div/div/div[1]/h1"

    button_Execute_EnhancedIFTAPageAdr = "/html/body/app-root/app-main/div/div/app-ifta-reporting/section[2]/div/app-search-panel/div/div/div/div[7]/div/button"


    #   Global Variables

    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global

    #       Variables
    w = WebDriverWait(driver, 30)


    #       #######################################     Enhanced IFTA Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "Enhanced IFTA"
    tc_reports.function_Init_Page(function_Name, driver_Name)
    print("Enhanced IFTA module")


#       Function Enhanced IFTA side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_EnhancedIFTA_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.XPATH, button_EnhancedIFTA_ManagePageAdr))).click()


#       Title of the right page
    title_EnhancedIFTA_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, title_EnhancedIFTA_EnhancedIFTAPageAdr))).text
    test_Name = "Enhanced IFTA page open"
    condition1 = "Enhanced IFTA"
    condition2 = title_EnhancedIFTA_DVIRPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Enhanced IFTA Page - Enhanced IFTA page open:"
    print_Information_Var = title_EnhancedIFTA_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)
    print(title_EnhancedIFTA_DVIRPage)





    print("TEST YEAR %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#       Year - Dropdown %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropbox_Year_EnhancedIFTAPageID))))
    dropbox_Year_EnhancedIFTAPage_List = [x.text for x in dropDown.options]
#    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropbox_Year_EnhancedIFTAPage_List):
        dropbox_Year_EnhancedIFTAPageSelected = dropDown.select_by_visible_text(dropbox_Year_EnhancedIFTAPage_List[n])
        dropBox_Year_EnhancedIFTAPageRead = dropDown.first_selected_option.text
        print(f'Selected: {dropbox_Year_EnhancedIFTAPage_List[n]}')
        print(f'leitura: {dropBox_Year_EnhancedIFTAPageRead}')
        n = n + 1
    dropDown.select_by_index(0)


    print("TEST QUARTER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#       Quarter - Dropdown %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropbox_Quarter_EnhancedIFTAPageID))))
    dropbox_Quarter_EnhancedIFTAPage_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropbox_Quarter_EnhancedIFTAPage_List):
        dropbox_Quarter_EnhancedIFTAPageSelected = dropDown.select_by_visible_text(dropbox_Quarter_EnhancedIFTAPage_List[n])
        dropBox_Quarter_EnhancedIFTAPageRead = dropDown.first_selected_option.text
        print(f'Selected: {dropbox_Quarter_EnhancedIFTAPage_List[n]}')
        print(f'leitura: {dropBox_Quarter_EnhancedIFTAPageRead}')
        n = n + 1

    print("TEST MONTH %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#       Month - Dropdown %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropbox_Month_EnhancedIFTAPageID))))
    dropbox_Month_EnhancedIFTAPage_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropbox_Month_EnhancedIFTAPage_List):
        dropbox_Month_EnhancedIFTAPageSelected = dropDown.select_by_visible_text(dropbox_Month_EnhancedIFTAPage_List[n])
        dropBox_Month_EnhancedIFTAPageRead = dropDown.first_selected_option.text
        print(f'Selected: {dropbox_Month_EnhancedIFTAPage_List[n]}')
        print(f'leitura: {dropBox_Month_EnhancedIFTAPageRead}')
        n = n + 1


    print("TEST CARRIER %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#       Carrier - Select    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropbox_Carrier_EnhancedIFTAPageID))))
    dropbox_Carrier_EnhancedIFTAPage_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropbox_Carrier_EnhancedIFTAPage_List):
        dropbox_Carrier_EnhancedIFTAPageSelected = dropDown.select_by_visible_text(dropbox_Carrier_EnhancedIFTAPage_List[n])
        dropBox_Carrier_EnhancedIFTAPageRead = dropDown.first_selected_option.text
        print(f'Selected: {dropbox_Carrier_EnhancedIFTAPage_List[n]}')
        print(f'leitura: {dropBox_Carrier_EnhancedIFTAPageRead}')
        n = n + 1

    print("TEST REGION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#       Region - Dropdown %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropbox_Region_EnhancedIFTAPageID))))
    dropbox_Region_EnhancedIFTAPage_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropbox_Region_EnhancedIFTAPage_List):
        dropbox_Region_EnhancedIFTAPageSelected = dropDown.select_by_visible_text(dropbox_Region_EnhancedIFTAPage_List[n])
        dropBox_Region_EnhancedIFTAPageRead = dropDown.first_selected_option.text
        print(f'Selected: {dropbox_Region_EnhancedIFTAPage_List[n]}')
        print(f'leitura: {dropBox_Region_EnhancedIFTAPageRead}')
        n = n + 1

    print("TEST VEHICLE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Vehicle  - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropbox_Vehicle_EnhancedIFTAPageID))))
    dropbox_Vehicle_EnhancedIFTAPage_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropbox_Vehicle_EnhancedIFTAPage_List):
        dropbox_Vehicle_EnhancedIFTAPageSelected = dropDown.select_by_visible_text(dropbox_Vehicle_EnhancedIFTAPage_List[n])
        dropBox_Vehicle_EnhancedIFTAPageRead = dropDown.first_selected_option.text
        print(f'Selected: {dropbox_Vehicle_EnhancedIFTAPage_List[n]}')
        print(f'leitura: {dropBox_Vehicle_EnhancedIFTAPageRead}')
        n = n + 1

    button_EXECUTE = w.until(EC.element_to_be_clickable((By.XPATH, button_Execute_EnhancedIFTAPageAdr))).click()

#**************************************
# Tractor Properties Child Page opened
#**************************************

    title_FuelTypePrimary_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[1]/div[1]/div/div[1]/label"
    dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId = "FuelTypePrimary"
    text_Make_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[1]/div[2]/input"
    text_Model_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[1]/div[3]/input"
    text_Year_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[1]/div[4]/input"
    dropBox_Type_TractorProperties_EnhanceIFTApageId = "Type"
    text_BodyClass_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[1]/div[6]/input"
    dropBox_GVWR_TractorProperties_EnhanceIFTApageId = "GVWR"
    button_SAVE_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[2]/button[1]"
    button_CLOSE_TractorProperties_EnhanceIFTApageAdr = "/html/body/ngb-modal-window/div/div/app-property-modal-form/div[2]/form/div[2]/button[2]"

    text_Make_TractorProperties_EnhanceIFTApageVar = "Freightliner"
    text_Model_TractorProperties_EnhanceIFTApageVar = "Cascadia"
    text_Year_TractorProperties_EnhanceIFTApageVar = "2022"
    text_BodyClass_TractorProperties_EnhanceIFTApageVar = "Heavy truck"

    print("TEST FUEL TYPE PRIMARY %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Fuel Type Primary  - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId))))
    dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_List):
        dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_ListSelected = dropDown.select_by_visible_text(dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_List[n])
        dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_ListRead = dropDown.first_selected_option.text
        print(f'Selected: {dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_List[n]}')
        print(f'leitura: {dropBox_FuelTypePrimary_TractorProperties_EnhanceIFTApageId_ListRead}')
        n = n + 1


    print("TEST MAKE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Make - Select

    text_Make_TractorProperties_EnhanceIFTApage = w.until(EC.presence_of_element_located((By.XPATH, text_Make_TractorProperties_EnhanceIFTApageAdr)))
    text_Make_TractorProperties_EnhanceIFTApage.send_keys(text_Make_TractorProperties_EnhanceIFTApageVar)
    text_Make_TractorProperties_EnhanceIFTApageRead = w.until(EC.presence_of_element_located((By.XPATH, text_Make_TractorProperties_EnhanceIFTApageAdr))).get_property('value')

    print(f'leitura {text_Make_TractorProperties_EnhanceIFTApageRead}')


    print("TEST MODEL %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Model - Select

    text_Model_TractorProperties_EnhanceIFTApage = w.until(EC.presence_of_element_located((By.XPATH, text_Model_TractorProperties_EnhanceIFTApageAdr)))
    text_Model_TractorProperties_EnhanceIFTApage.send_keys(text_Model_TractorProperties_EnhanceIFTApageVar)
    text_Model_TractorProperties_EnhanceIFTApageRead = text_Model_TractorProperties_EnhanceIFTApage.get_property('value')

    print(f'leitura {text_Model_TractorProperties_EnhanceIFTApageRead}')

    print("TEST YEAR %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Make - Select

    text_Year_TractorProperties_EnhanceIFTApage = w.until(EC.presence_of_element_located((By.XPATH, text_Year_TractorProperties_EnhanceIFTApageAdr)))
    text_Year_TractorProperties_EnhanceIFTApage.send_keys(text_Year_TractorProperties_EnhanceIFTApageVar)
    text_Year_TractorProperties_EnhanceIFTApageRead = text_Year_TractorProperties_EnhanceIFTApage.get_property('value')

    print(f'leitura {text_Year_TractorProperties_EnhanceIFTApageRead}')


    print("TEST TYPE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Type  - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Type_TractorProperties_EnhanceIFTApageId))))
    dropBox_Type_TractorProperties_EnhanceIFTApageId_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropBox_Type_TractorProperties_EnhanceIFTApageId_List):
        dropBox_Type_TractorProperties_EnhanceIFTApageId_ListSelected = dropDown.select_by_visible_text(dropBox_Type_TractorProperties_EnhanceIFTApageId_List[n])
        dropBox_Type_TractorProperties_EnhanceIFTApageId_ListRead = dropDown.first_selected_option.text
        print(f'Selected: {dropBox_Type_TractorProperties_EnhanceIFTApageId_List[n]}')
        print(f'leitura: {dropBox_Type_TractorProperties_EnhanceIFTApageId_ListRead}')
        n = n + 1

    print("TEST Body Class %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       Model - Select

    text_BodyClass_TractorProperties_EnhanceIFTApage = w.until(EC.presence_of_element_located((By.XPATH, text_BodyClass_TractorProperties_EnhanceIFTApageAdr)))
    text_BodyClass_TractorProperties_EnhanceIFTApage.send_keys(text_BodyClass_TractorProperties_EnhanceIFTApageVar)
    text_BodyClass_TractorProperties_EnhanceIFTApageRead = text_BodyClass_TractorProperties_EnhanceIFTApage.get_property('value')

    print(f'leitura {text_BodyClass_TractorProperties_EnhanceIFTApageRead}')

    print("GVWR TYPE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    #       GVWR  - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_GVWR_TractorProperties_EnhanceIFTApageId))))
    dropBox_GVWR_TractorProperties_EnhanceIFTApageId_List = [x.text for x in dropDown.options]
    #    print(f'List: {dropbox_Year_EnhancedIFTAPage_List}')
    n = 0
    while n < len(dropBox_GVWR_TractorProperties_EnhanceIFTApageId_List):
        dropBox_GVWR_TractorProperties_EnhanceIFTApageId_ListSelected = dropDown.select_by_visible_text(dropBox_GVWR_TractorProperties_EnhanceIFTApageId_List[n])
        dropBox_GVWR_TractorProperties_EnhanceIFTApageId_ListRead = dropDown.first_selected_option.text
        print(f'Selected: {dropBox_GVWR_TractorProperties_EnhanceIFTApageId_List[n]}')
        print(f'leitura: {dropBox_GVWR_TractorProperties_EnhanceIFTApageId_ListRead}')
        n = n + 1

    button_SAVE_TractorProperties_EnhanceIFTApage = w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_TractorProperties_EnhanceIFTApageAdr))).click()



    return()
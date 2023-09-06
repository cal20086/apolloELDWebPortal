#               Apollo Web Portal - DVIR

def DVIR_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList):

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
    import openpyxl
    from pathlib import Path
    from pathlib import Path
    from os import path
    from datetime import datetime, timedelta
    from selenium.common.exceptions import NoSuchElementException

    #               DVIR Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"
    button_DVIR_ManagePageAdr = '//a[contains(@href,"/dvir")]'
    title_DVIR_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[1]/div/div/div[1]/h1"
    dropBox_Carrier_DVIRPageAdrID = "carrierSelector"
    dropBox_Carrier_DVIRPageReadAdr = "/html/body/app-root/app-main/div/div/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[1]/div/span/span[1]/span/span[1]"
    dropBox_Status_DVIRPageAdrID = "driversStatus"
    dropBox_Status_DVIRPageReadAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[2]/div/span/span[1]/span/span[1]"
    dropBox_Drivers_DVIRPageID = "driversSelect"
    dropBox_Drivers_DVIRPageReadAdr = "/html/body/app-root/app-main/div/div/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[3]/div/span/span[1]/span/span[1]"
    date_SatrtEndDate_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    button_Execute_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[5]/div/button"
    checkbox_MoreFilters_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[2]/label[1]/span"
    title_TractorNumber_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[1]/div[1]/div/label"

    text_TractorNumber_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[1]/div[1]/div/input"
    text_TrailerNumber_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[1]/div[2]/div/input"
    dropBox_VehicleCondition_DVIRPageID = "vehicleCondition"
    dropBox_VehicleCondition_DVIRPageReadAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[2]/div[4]/div/span/span[1]/span/span[1]"

    dropBox_Report_DVIRPageID = "report"
    dropBox_Categories_DVIRPageID = "category"
    read_Defects_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[2]/div[3]/div/span/span[1]/span/ul/li[1]"

    input_Defects_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[2]/div[3]/div/span/span[1]/span/ul/li/input"
    read_Defects_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[2]/div[3]/div/span/span[1]/span/ul/li[1]"
    input_Defects_RemoveAllItems_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[3]/div[2]/div[3]/div/span/span[1]/span/ul/span"

    button_Manage_DVIRPageAdr = '//a[contains(@href,"/")]'
    button_calendar_StartEndDate_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    calendar_Month_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[1]"
    calendar_Year_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[2]"
    calendar_DayStart_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[3]/div[1]/span"
    calendar_DayEnd_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[5]/div[7]/span"
    header_Driver_DVIRReport_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[2]/dx-data-grid/div/div[5]/div[1]/table/tbody/tr/td[1]/div[2]"
    download_ReportBigDVIR_DVIRPageAdr = "/html/body/app-root/app-main/div/div/app-dvir/section[2]/div/div/div/div[1]/div/a/i"
    title_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[1]/div/div/div"

    #       Variables

    Ref_DVIR_DVIRPage = "DVIR"
    tractorNumber_DVIRPageVar = "112233445566778899"
    trailerNumber_DVIRPageVar = "101010101010101010"

    month_AbreviationList = ["Jan", "Feb", "Mar", "Apr", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    download_ReportBigDVIR_DVIRPagePath = "C:/Users/Carlos/Downloads/report_big_dvir.pdf"
    workbookDB = "C:/apollo QA Reports/Support test DB/apolloPortalDVIRReportDB.xlsx"
    worksheetDB = "PortalDVIRReportsDB"

    excel_DB_line = 2
    colum_Report_ID = "D"
    colum_Report_Name = "E"
    colum_Categories_ID = "F"
    colum_Categories_Name = "G"
    colum_Defects_ID = "H"
    colum_Defects_Name = "I"
    colum_Parent_ID = "J"

    w = WebDriverWait(driver, 10)

    #       #######################################     DVIR Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "DVIR Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)


#       Function DVIR side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_DVIR_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.XPATH, button_DVIR_ManagePageAdr))).click()


#       Title of the right page
    title_DVIR_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, title_DVIR_DVIRPageAdr))).text
    test_Name = "DVIR page open"
    condition1 = "DVIR"
    condition2 = title_DVIR_DVIRPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - DVIR page open:"
    print_Information_Var = title_DVIR_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)
    print(title_DVIR_DVIRPage)


#       Carrier - Select    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Carrier_DVIRPageAdrID))))
    dropdown_Import_Carrier_DVIR_DVIRPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Carrier_DVIR_DVIRPage_List):
        dropBox_Carrier_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_Carrier_DVIR_DVIRPage_List[n])
        dropBox_Carrier_DVIRPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Status element DVIR page"
        condition1 = dropdown_Import_Carrier_DVIR_DVIRPage_List[n]
        condition2 = dropBox_Carrier_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "DVIR Page - Carrier element:"
        print_Information_Var = dropBox_Carrier_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


#       Status - Select %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Status_DVIRPageAdrID))))
    dropdown_Import_Status_DVIR_DVIRPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Status_DVIR_DVIRPage_List):
        dropBox_Status_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_Status_DVIR_DVIRPage_List[n])
        dropBox_Status_DVIRPageRead = dropDown.first_selected_option.text
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
        test_Name = "Status element DVIR page"
        condition1 = dropdown_Import_Status_DVIR_DVIRPage_List[n]
        condition2 = dropBox_Status_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
        print_Information_Fix = "DVIR Page - Status element:"
        print_Information_Var = dropBox_Status_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        dropDown.select_by_visible_text("All")
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

#       Driver - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Drivers_DVIRPageID))))
    dropdown_Import_Driver_DVIR_DVIRPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Driver_DVIR_DVIRPage_List):
        dropBox_Drivers_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_Driver_DVIR_DVIRPage_List[n])
        dropBox_Drivers_DVIRPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Drivers element DVIR page"
        condition1 = dropdown_Import_Driver_DVIR_DVIRPage_List[n]
        condition2 = dropBox_Drivers_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "DVIR Page - Drivers element:"
        print_Information_Var = dropBox_Drivers_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        dropDown.select_by_visible_text("All")
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


#       Calendar Start-End date


    date_now = datetime.now()
    td = timedelta(30)
    date_now = date_now - td
    date_LastMonth = str(date_now)
    year_LastMonth = date_LastMonth[:4]
    month_LastMonth = date_LastMonth[5:-19]
    month_LastMonth = int(month_LastMonth) + 1
    month_Abreviation_LastMonth = month_AbreviationList[month_LastMonth]
    calendar_Month_DVIRPageVar = month_Abreviation_LastMonth
    calendar_Year_DVIRPageVar = year_LastMonth


    button_calendar_StartEndDate_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_calendar_StartEndDate_DVIRPageAdr)))
    button_calendar_StartEndDate_DVIRPage.click()
    calendar_Month_DVIRPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Month_DVIRPageAdr))))
    calendar_Month_DVIRPage.select_by_visible_text(calendar_Month_DVIRPageVar)
    calendar_Year_DVIRPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Year_DVIRPageAdr))))
    calendar_Year_DVIRPage.select_by_visible_text(calendar_Year_DVIRPageVar)
    calendar_DayStart_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, calendar_DayStart_DVIRPageAdr)))
    calendar_DayStart_DVIRPage.click()
    calendar_DayEnd_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, calendar_DayEnd_DVIRPageAdr)))
    calendar_DayEnd_DVIRPage.click()
    #       Print Assert OK
    date_Selected_DVIRPage = calendar_Month_DVIRPageVar+", "+calendar_Year_DVIRPageVar
    test_Name = "Star-End Date DVIR Reports"
    print_Information_Fix = "Start-End Date selected: "
    print_Information_Var = date_Selected_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

#       More Filter:
    checkbox_MoreFilters_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, checkbox_MoreFilters_DVIRPageAdr )))
    webdriver.ActionChains(driver).move_to_element(checkbox_MoreFilters_DVIRPage).click(checkbox_MoreFilters_DVIRPage).perform()

#       Verify More filters works
    title_TractorNumber_DVIRPage = w.until((EC.presence_of_element_located((By.XPATH, title_TractorNumber_DVIRPageAdr)))).text
    test_Name = "More Filtes CheckBox"
    condition1 = "Tractor Number"
    condition2 = title_TractorNumber_DVIRPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - More Filtes CheckBox:"
    print_Information_Var = title_TractorNumber_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


#       Tractor Number:
    text_TractorNumber_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, text_TractorNumber_DVIRPageAdr)))
    text_TractorNumber_DVIRPage.send_keys(tractorNumber_DVIRPageVar)
    tractorNumber_DVIRPageRead = text_TractorNumber_DVIRPage.get_property('value')
    test_Name = "Tractor Number element"
    condition1 = tractorNumber_DVIRPageVar
    condition2 = tractorNumber_DVIRPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - Tractor Number element:"
    print_Information_Var = tractorNumber_DVIRPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


#       Trailer Number:
    text_TrailerNumber_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, text_TrailerNumber_DVIRPageAdr)))
    text_TrailerNumber_DVIRPage.send_keys(trailerNumber_DVIRPageVar)

    trailerNumber_DVIRPageRead = text_TrailerNumber_DVIRPage.get_property('value')
    test_Name = "Trailer Number element"
    condition1 = trailerNumber_DVIRPageVar
    condition2 = trailerNumber_DVIRPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR Page - Trailer Number element:"
    print_Information_Var = trailerNumber_DVIRPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)


#       Vehicle Condition - Select
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_VehicleCondition_DVIRPageID))))
    dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List):
        dropBox_VehicleCondition_DVIRPageSelected = dropDown.select_by_visible_text(dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List[n])
        dropBox_VehicleCondition_DVIRPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Vehicle Condition element DVIR page"
        condition1 = dropdown_Import_VehicleCondition_DVIR_DVIRPageMoreFilters_List[n]
        condition2 = dropBox_VehicleCondition_DVIRPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "DVIR page - Vehicle Condition element:"
        print_Information_Var = dropBox_VehicleCondition_DVIRPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        dropDown.select_by_visible_text("All")
    #       Screenshot
    test_Name = "DVIR Page Fille up"
    tc_reports.screenshot(driver, driver_Name, test_Name)

#   Clear Tractor & Trailler fields
    text_TractorNumber_DVIRPage.clear()
    text_TrailerNumber_DVIRPage.clear()
# Delete all old report_big_dvir.pdf files created by the DVIR page
    if os.path.isfile(download_ReportBigDVIR_DVIRPagePath):
        os.remove(download_ReportBigDVIR_DVIRPagePath)


#       Execute button
    button_Execute_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_Execute_DVIRPageAdr)))
    webdriver.ActionChains(driver).move_to_element(button_Execute_DVIRPage).click().perform()
#               DVIR Report Available?

    try:
        a = w.until(EC.presence_of_element_located((By.XPATH, header_Driver_DVIRReport_DVIRPageAdr)))
        print('DVIR report is available')
        #       There is DVIR Data - verify is a DVIR file is in the download directory
        # Download report_big_dvir.pdf file
        w.until(EC.element_to_be_clickable((By.XPATH, download_ReportBigDVIR_DVIRPageAdr))).click()
        time.sleep(1.5)
        if os.path.exists(download_ReportBigDVIR_DVIRPagePath):
            #       PASSED - The report_big_dvir.pdf file was saved.
            test_Name = "report_big_dvir.pdf - DVIR Reports download"
            print_Information_Fix = "report_big_dvir.pdf was downloaded"
            print_Information_Var = ""
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            n = n + 1
            #       Screenshot
            tc_reports.screenshot(driver, driver_Name, test_Name)
        else:
            #       ERROR - The report_big_dvir.pdf file was not saved.
            print("Error file not downloaded")
            test_Name = "report_big_dvir.pdf - DVIR Reports download"
            condition1 = 1
            condition2 = 2
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    except:
        print('DVIR Data is NOT available')
        # There is NO DVIR Data
        #       Print Assert OK
        test_Name = "No DVIR Data Available"
        print_Information_Fix = "DVIR Page - Execute button -> PopUp toast message"
        print_Information_Var = "There is no data"
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

# ########################################################################################### NOVA PARTE ########################################################################################################

        # Report x Categories X Defects

#   Read excel
    excell_pointer = Path(workbookDB)
    #Read ecel value not formula
    workbookDB_Read = openpyxl.load_workbook(excell_pointer, data_only=True)
    worksheetDB_Read = workbookDB_Read.active

    excel_ReportsTypes_cellValue = worksheetDB_Read['A2'].value
    excel_CategoriesTypes_cellValue = worksheetDB_Read['B2'].value
    excel_DefectsTypes_cellValue = worksheetDB_Read['C2'].value


#   Check the options/quantities per list based on the excel
    dropBox_Report_DVIRPage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Report_DVIRPageID))))
    dropBox_Report_MoreFilter_DVIR_List = [x.text for x in dropBox_Report_DVIRPage.options]
    # Assert
    test_Name = "Report Items numbers"
    condition1 = str(len(dropBox_Report_MoreFilter_DVIR_List))
    condition2 = str(excel_ReportsTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

#   Check The Categories quantities
    dropBox_Categories_DVIRPage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Categories_DVIRPageID))))
    dropBox_Categories_MoreFilter_DVIR_List = [x.text for x in dropBox_Categories_DVIRPage.options]
    # Assert
    test_Name = "Categories Items numbers"
    condition1 = str(len(dropBox_Categories_MoreFilter_DVIR_List))
    condition2 = str(excel_CategoriesTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    #for combiation ReportCategoriesDefectsVar in range(len(excel_DefectsTypes_cellValue))

    # Positive Test based on the spreadsheet
    try:
        n = 1
        excel_DB_line = excel_DB_line + 2
        #for list_control_Report in range(len(dropBox_Report_MoreFilter_WorkOrder_List)):
        while n < excel_DefectsTypes_cellValue:
            cell_Report_ID = (str(colum_Report_ID) + str(excel_DB_line))
            cell_Report_ID_Value = worksheetDB_Read[cell_Report_ID].value
            cell_Report_Name = (str(colum_Report_Name) + str(excel_DB_line))
            cell_Report_Name_Value = worksheetDB_Read[cell_Report_Name].value
            cell_Categories_ID = (str(colum_Categories_ID) + str(excel_DB_line))
            cell_Categories_ID_Value = worksheetDB_Read[cell_Categories_ID].value
            cell_Categories_Name = (str(colum_Categories_Name) + str(excel_DB_line))
            cell_Categories_Name_Value = worksheetDB_Read[cell_Categories_Name].value
            cell_Defects_ID = (str(colum_Defects_ID) + str(excel_DB_line))
            cell_Defects_ID_Value = worksheetDB_Read[cell_Defects_ID].value
            cell_Defects_Name = (str(colum_Defects_Name) + str(excel_DB_line))
            cell_Defects_Name_Value = worksheetDB_Read[cell_Defects_Name].value
            cell_Parent_ID = (str(colum_Parent_ID) + str(excel_DB_line))
            cell_Parent_ID_Value = worksheetDB_Read[cell_Parent_ID].value


    #            Correto !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if cell_Parent_ID_Value == 0:
                dropBox_Report_DVIRPage.select_by_visible_text(cell_Report_Name_Value)
                dropBox_Item_Report_DVIRPage_Read = dropBox_Report_DVIRPage.first_selected_option.text
                dropBox_Categories_DVIRPage.select_by_visible_text(cell_Categories_Name_Value)
                dropBox_Item_Categories_DVIRPage_Read = dropBox_Categories_DVIRPage.first_selected_option.text
                defects = w.until(EC.presence_of_element_located((By.XPATH, input_Defects_DVIRPageAdr)))
                defects.send_keys(cell_Defects_Name_Value)
                defects.send_keys(Keys.RETURN)

        #       input list field read


                time.sleep(0.25)
                input_Defects_DVIRPage = w.until(EC.presence_of_element_located((By.XPATH, read_Defects_DVIRPageAdr)))
                input_Defects_DVIRPage_Read = input_Defects_DVIRPage.text

                #       input list field read

                # Assert
                test_Name = "Defect items"
                condition1 = cell_Defects_Name_Value
                condition2 = input_Defects_DVIRPage_Read

                print(f'Excell data = {condition1}')
                print(f'Field Read = {condition2}')

                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
                #       Print Assert OK
                print_Information_Fix = "WorkOrder Page - Defect items field:"
                print_Information_Var = cell_Defects_Name_Value
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)

                w.until(EC.element_to_be_clickable((By.XPATH, input_Defects_RemoveAllItems_DVIRPageAdr))).click()
            n = n + 1
            excel_DB_line = excel_DB_line + 1

    except:
        print('!!!!!!!!!!!!!!!!! error !!!!!!!!!!!!!!!!!!!!')
    print(f'Total Report/Categories/Defects combination tested = {n}')


    #       Manage button
    button_Manage_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_Manage_DVIRPageAdr))).click()
    try:
        test_Name = "back to Manage page from DVIR page"
        title_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_ManagePageAdr))).text
        print_Information_Fix = "Manage page - Back to Manage page from DVIR page:"
        print_Information_Var = title_ManagePage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    except:
    # **************** Test and report results at TCReport  ******************************************************************************************************************
    #       Assert Test and print if assert is fail
        test_Name = "back to Manage page from DVIR page"
        condition1 = "Manage"
        condition2 = ""
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
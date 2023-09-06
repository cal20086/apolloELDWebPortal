#               Apollo Web Portal - DVIR Work Order

def DVIR_WorkOrder_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var,
                              client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var,
                              workOrder_Contacts_Var):
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
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

    #               DVIR Work Order Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"
    button_DVIR_ManagePageAdr = '//a[contains(@href,"/dvir")]'
    title_DVIR_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[1]/div/div/div[1]/h1"
    dropBox_Status_DVIRPageAdrID = "driversStatus"
    button_Execute_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[5]/div/button"
    download_ReportBigDVIR_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[1]/div/button"
    download_ReportNormalDVIR_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[5]/div/div/div[1]/button"

    driver_DVIRReport_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div[2]/table/tbody/tr[1]/td[1]"
    header_Timestamp_DVIRReport_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[2]/dx-data-grid/div/div[5]/div[2]/table/tbody/tr/td[2]"
    title_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[1]/h4"
    clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[2]/section/div/div[2]/div[1]/div/div/div/table/tbody/tr[1]/td"
    defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[2]/section/div/div[2]/div[2]/div/div[2]/dx-list"

    clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[2]/section/div/div[2]/div[1]/div/div/div/table/tbody/tr[2]/td"
    button_Action_ManageWorkOrder_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[5]/div/div/div[3]/button"
    title_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[1]/h4"
    input_DefectList_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[2]/form/div[1]/div[1]/span/span[1]/span/ul/li"
    input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[2]/form/div[1]/div[3]/input"
    input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[2]/form/div[1]/div[4]/input"
    button_SAVE_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[2]/form/div[2]/button[1]"
    button_CLOSE_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[2]/form/div[2]/button[2]"
    button_PlusNew_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[2]/section/div/div[2]/div[3]/div/div[1]/div/button"
    input_DefectList_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[2]/form/div[1]/div[1]/span/span[1]/span/ul/li/input"
    button_calendar_StartEndDate_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    calendar_Month_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[1]"
    calendar_Year_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[2]"
    calendar_DayStart_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[3]/div[1]/span"
    calendar_DayEnd_DVIRPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[5]/div[7]/span"
    button_X_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[1]/button"
    driver_DVIRReport_DVIRPagetableAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div[1]/div/div[1]/div/table/tbody/tr[1]/td[2]"
    buttonX_WorkOrder_WorkorderChildPageAdr = "/html/body/ngb-modal-window[2]/div/div/app-workorder-form/div[1]/button"
    buttonX_ManageWorkOrder_WorkorderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-dvir-workorder/div[1]/button"

    #       Variables
    driver_UserName_Var,
    Ref_DVIR_DVIRPage = "DVIR"
    driver_DVIRReport_DVIRPageVar = "Test (sdsd1)"
    download_ReportBigDVIR_DVIRPagePath = "C:/Users/Carlos/Downloads/report_big_dvir.pdf"
    download_Delete_Report_DVIR_DVIRPagePath = "C:/Users/Carlos/Downloads/report_*.pdf"
    clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageVar = client_Name_Var
    clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageVar = client_Adress_Var
    defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList = defect_Vehicle_List_Var
    defectQte_ManageWorkOrder_DVIRManageWorkOrderChildPageListVar = len(defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList)
    input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageVar = workOrder_CreatedBy_Var
    input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageVar = workOrder_Contacts_Var
    month_AbreviationList = ["Jan", "Feb", "Mar", "Apr", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                             "Dec"]
    day_Position_Calendar_DVIRPageStrInit = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div["
    startday_Position_Calendar_DVIRPageRowVar = 2
    day_Position_Calendar_DVIRPageStrMid = "]/div["
    startday_Position_Calendar_DVIRPageColVar = 1
    day_Position_Calendar_DVIRPageStrEnd = "]"
    lastday_Position_Calendar_DVIRPageRow6Var = 6
    lastday_Position_Calendar_DVIRPageRow7Var = 7
    lastday_Position_Calendar_DVIRPageColVar = 7
    w = WebDriverWait(driver, 10)

    #       #######################################     DVIR Work Order Main functions    ########################################################
    #   ###############################################################################################################################
    #   Page Title on TCReport
    function_Name = "DVIR Work Order Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    #       Function DVIR side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(
        EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_DVIR_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_DVIR_ManagePageAdr))).click()

    #       Title of the page
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
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)
    print(title_DVIR_DVIRPage)

    #       Status - Select %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Status_DVIRPageAdrID))))
    dropDown.select_by_visible_text("All")

    #       Calendar Start-End date
    date_now = datetime.now()
    td = timedelta(30)
    date_now = date_now
    date_ActualMonth = str(date_now)
    year_ActualMonth = date_ActualMonth[:4]
    month_ActualMonth = date_ActualMonth[5:-19]
    month_ActualMonth = int(month_ActualMonth) - 1
    month_Abreviation_ActualMonth = month_AbreviationList[month_ActualMonth]
    calendar_Month_DVIRPageVar = month_Abreviation_ActualMonth
    calendar_Year_DVIRPageVar = year_ActualMonth
    button_calendar_StartEndDate_DVIRPage = w.until(
        EC.element_to_be_clickable((By.XPATH, button_calendar_StartEndDate_DVIRPageAdr)))
    button_calendar_StartEndDate_DVIRPage.click()
    calendar_Month_DVIRPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Month_DVIRPageAdr))))
    calendar_Month_DVIRPage.select_by_visible_text(calendar_Month_DVIRPageVar)
    calendar_Year_DVIRPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Year_DVIRPageAdr))))
    calendar_Year_DVIRPage.select_by_visible_text(calendar_Year_DVIRPageVar)
    #       Try if the the last weekday is in the 7th Row of the calendar
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[7]/div[1]"))).click()
        lastday_Position_Calendar_DVIRPageRowVar = str(lastday_Position_Calendar_DVIRPageRow7Var)
    except:
        lastday_Position_Calendar_DVIRPageRowVar = str(lastday_Position_Calendar_DVIRPageRow6Var)
    # Find the 1st weekday of the month
    col = 1
    while col < 8:
        try:
            calendar_StartDay_DVIRPageAdr = day_Position_Calendar_DVIRPageStrInit + str(
                startday_Position_Calendar_DVIRPageRowVar) + day_Position_Calendar_DVIRPageStrMid + str(
                startday_Position_Calendar_DVIRPageColVar) + day_Position_Calendar_DVIRPageStrEnd
            calendar_StartDay_DVIRPage = w.until(
                EC.element_to_be_clickable((By.XPATH, calendar_StartDay_DVIRPageAdr))).click()
            col = 8
        except:
            startday_Position_Calendar_DVIRPageColVar += 1
            col += 1
    # Find the Last weekday of the month
    col = 7
    while col > 0:
        try:
            calendar_LastDay_DVIRPageAdr = day_Position_Calendar_DVIRPageStrInit + str(
                lastday_Position_Calendar_DVIRPageRowVar) + day_Position_Calendar_DVIRPageStrMid + str(
                lastday_Position_Calendar_DVIRPageColVar) + day_Position_Calendar_DVIRPageStrEnd
            calendar_LasttDay_DVIRPage = w.until(
                EC.element_to_be_clickable((By.XPATH, calendar_LastDay_DVIRPageAdr))).click()
            col = 0
        except:
            lastday_Position_Calendar_DVIRPageColVar -= 1
            col -= 1
    #       Print Assert OK
    date_Selected_DVIRPage = calendar_Month_DVIRPageVar + ", " + calendar_Year_DVIRPageVar
    test_Name = "Star-End Date DVIR Reports"
    print_Information_Fix = "Start-End Date selected: "
    print_Information_Var = date_Selected_DVIRPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)

    # Delete all old report_*.pdf files created by the DVIR page
    files = glob.glob(download_Delete_Report_DVIR_DVIRPagePath)
    for f in files:
        os.remove(f)

    #       Execute button
    button_Execute_DVIRPage = w.until(EC.element_to_be_clickable((By.XPATH, button_Execute_DVIRPageAdr)))
    webdriver.ActionChains(driver).move_to_element(button_Execute_DVIRPage).click().perform()

    #   Sort DVIR Reports by clicking on TimeStamp icon
    a = w.until(EC.presence_of_element_located((By.XPATH, header_Timestamp_DVIRReport_DVIRPageAdr)))
    a.click()
    time.sleep(1)
    b = w.until(EC.element_to_be_clickable((By.XPATH, header_Timestamp_DVIRReport_DVIRPageAdr)))
    b.click()

    #   Verify DVIR Report - Driver is corrected: ??????????????????????????????????????????????????????????????????????????????????????????????????
    driver_DVIRReport_DVIRPagetable = w.until(
        EC.presence_of_element_located((By.XPATH, driver_DVIRReport_DVIRPagetableAdr)))

    # Download DVIR reports:

    try:
        w.until(EC.element_to_be_clickable((By.XPATH, download_ReportBigDVIR_DVIRPageAdr))).click()
        w.until((EC.element_to_be_clickable((By.XPATH, download_ReportNormalDVIR_DVIRPageAdr)))).click()
    except:
        print("Report download FAIL")
    #   Action Manage Work Order Call button
    w.until(EC.element_to_be_clickable((By.XPATH, button_Action_ManageWorkOrder_DVIRPageAdr))).click()

    #   Verify if the Downloads are done correctly:
    time.sleep(1.5)
    #   Report "BIG"
    if os.path.exists(download_ReportBigDVIR_DVIRPagePath):
        #       PASSED - The report_big_dvir.pdf file was saved.
        test_Name = "report_big_dvir.pdf - DVIR Reports download"
        print_Information_Fix = "report_big_dvir.pdf was downloaded"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    else:
        #       ERROR - The report_big_dvir.pdf file was not saved.
        print("Error file not downloaded")
        test_Name = "report_big_dvir.pdf - DVIR Reports download"
        condition1 = 1
        condition2 = 2
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #   Report "NORMAL:
    download_ReportNormalDVIR_DVIRPagePath = "C:/Users/Carlos/Downloads/report_normal_*.pdf"
    file = glob.glob(download_ReportNormalDVIR_DVIRPagePath)
    file = str(file)
    file_ReportNormal_FileName = file[29:]
    file_ReportNormal_FilePath = "C:/Users/Carlos/Downloads/"
    file_ReportNormal = file_ReportNormal_FilePath + file_ReportNormal_FileName
    file_ReportNormal = file_ReportNormal.replace("'", "")
    file_ReportNormal = file_ReportNormal.replace("]", "")
    if os.path.exists(file_ReportNormal):
        #       PASSED - The report_big_dvir.pdf file was saved.
        test_Name = "report_normal_dvir.pdf - DVIR Reports download"
        print_Information_Fix = "report_Normal_*.pdf - DVIR Reports download"
        print_Information_Var = file_ReportNormal
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)
    else:
        #       ERROR - The report_big_dvir.pdf file was not saved.
        print("Error file NORMAL not downloaded")
        test_Name = "report_Normal_*.pdf - DVIR Reports download"
        condition1 = 1
        condition2 = 2
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

    #       Title of the Manage Work Order Child page
    title_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(
        EC.presence_of_element_located((By.XPATH, title_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr))).text
    test_Name = "DVIR - Manage Work Order Child page opened"
    condition1 = "Manage Work Order"
    condition2 = title_ManageWorkOrder_DVIRManageWorkOrderChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "DVIR - Manage Work Order Child page opened:"
    print_Information_Var = title_ManageWorkOrder_DVIRManageWorkOrderChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   Client Name
    clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageRead = w.until(
        EC.presence_of_element_located((By.XPATH, clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr))).text
    test_Name = "Client Name - DVIR - Manage Work Order Child"
    #   clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageVar is a standart, define on the main module for all test
    condition1 = clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageVar
    condition2 = clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Client Name is correct - DVIR - Manage Work Order Child!"
    print_Information_Var = clientName_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)

    #   Client Address
    clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageRead = w.until(
        EC.presence_of_element_located((By.XPATH, clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr))).text
    test_Name = "Client Address - DVIR - Manage Work Order Child"
    #   clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageVar is a standart, define on the main module for all test
    condition1 = clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageVar
    condition2 = clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Client Address is correct - DVIR - Manage Work Order Child!"
    print_Information_Var = clientAdr_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)

    #   Defect List
    #   Defect types
    defectList_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(EC.presence_of_all_elements_located((By.XPATH, defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr)))
    for defect in defectList_ManageWorkOrder_DVIRManageWorkOrderChildPage:
        defect = defect.text
    #   defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList is a standart, define on the main module for all test
    for x in defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList:
        test_Name = "List of Defects - DVIR - Manage Work Order Child"
        condition1 = x
        condition2 = defect
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "List of Defect - DVIR - Manage Work Order Child page"
        print_Information_Var = x
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)

    #   Defect quantities
    defect_lines = defect.count('\n')
    # The defects numbers = number of new lines (\n) on the string + 1
    # 1 defect  = 0 \n => +1 = 1
    # 2 defects = 1 \n => +1 = 2
    defect_lines = defect_lines + 1
    test_Name = "Number of Defects listed - DVIR - Manage Work Order Child"
    condition1 = str(defectQte_ManageWorkOrder_DVIRManageWorkOrderChildPageListVar)
    condition2 = str(defect_lines)
    print(f'Defects qte = {condition1}')
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Number of Defects listed - DVIR - Manage Work Order Child"
    print_Information_Var = defect_lines
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)

    #   +New button - Create Work Order
    try:
        plusNewbutton = driver.find_element(By.XPATH, button_PlusNew_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr)
        actions = ActionChains(driver)
        actions.move_to_element(plusNewbutton).perform()

        w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr))).click()
        #   Work Order PAGE / Manage Work Order
        #       Title of the Work Order - Manage Work Order Child page
        title_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(EC.presence_of_element_located((By.XPATH, title_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr))).text
        test_Name = "Work Order - Manage Work Order DVIR Child page opened"
        condition1 = "Work Order"
        condition2 = title_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Work Order - Manage Work Order DVIR Child page opened"
        print_Information_Var = title_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)
        #       Screenshot
        tc_reports.screenshot(driver, driver_Name, test_Name)

        #   Defect List
        n = 0
        for x in defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList:
            print(n)
            if x[0] != "(":
                input_DefectList_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(
                    EC.presence_of_element_located(
                        (By.XPATH, input_DefectList_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr)))
                input_DefectList_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage.send_keys(
                    defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList[n])
                input_DefectList_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage.send_keys(Keys.RETURN)

                #   Created By
                input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(
                    EC.presence_of_element_located(
                        (By.XPATH, input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr)))
                input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage.send_keys(
                    input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageVar)
                input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageRead = input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage.get_attribute('value')
                test_Name = "Created By - Work Order - Manage Work Order DVIR Child page opened"
                condition1 = input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageVar
                condition2 = input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
                #       Print Assert OK
                print_Information_Fix = "Created By - Work Order - Manage Work Order DVIR Child page opened"
                print_Information_Var = input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var,
                                            test_Case_Type,
                                            driver_Name, driver_Version)

                #   Contacts
                input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(
                    EC.presence_of_element_located(
                        (By.XPATH, input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr)))
                input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage.send_keys(
                    input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageVar)
                input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageRead = input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPage.get_attribute(
                    'value')
                test_Name = "Contacts - Work Order - Manage Work Order DVIR Child page opened"
                condition1 = input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageVar
                condition2 = input_Contacts_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
                #       Print Assert OK
                print_Information_Fix = "Contacts - Work Order - Manage Work Order DVIR Child page opened"
                print_Information_Var = input_CreatedBy_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageRead
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var,
                                            test_Case_Type,
                                            driver_Name, driver_Version)

                #       SAVE button
                w.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_Work_Order_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr))).click()
                time.sleep(4)
                try:
                    plusNewbutton = driver.find_element(By.XPATH, button_PlusNew_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr)
                    actions = ActionChains(driver)
                    actions.move_to_element(plusNewbutton).perform()
                    w.until(EC.element_to_be_clickable((By.XPATH, button_PlusNew_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr))).click()
                except:
                    print("Last Defect")
                n += 1
            else:
                n += 1


        #       Title of the Manage Work Order Child page


        #w.until(EC.element_to_be_clickable((By.XPATH, buttonX_WorkOrder_WorkorderChildPageAdr))).click()
        w.until(EC.element_to_be_clickable((By.XPATH, buttonX_ManageWorkOrder_WorkorderChildPageAdr))).click()
        w.until((EC.element_to_be_clickable((By.XPATH, button_Action_ManageWorkOrder_DVIRPageAdr)))).click()
        newDefectList_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(EC.presence_of_all_elements_located((By.XPATH, defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr)))

        # Check the WORK ORDER # on the Manage Work Order - Defect List
        n = 0
        for x in defectList_ManageWorkOrder_DVIRManageWorkOrderChildPageList:
            try:
                assert newDefectList_ManageWorkOrder_DVIRManageWorkOrderChildPage[n].text in defectList_ManageWorkOrder_DVIRManageWorkOrderChildPage[n].text
                # defect list are iguals -> WO# was NOT created
                #       Print Assert OK
                print_Information_Fix = " *** Test FAILED ***:  ERROR !!!   => Work Order was NOT Created from DVIR"
                print_Information_Var = newDefectList_ManageWorkOrder_DVIRManageWorkOrderChildPage[n].text
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            except:
                # defect list are diferent -> WO# was created
                #       Print Assert OK
                print_Information_Fix = "Work Order # Creat from DVIR"
                print_Information_Var = newDefectList_ManageWorkOrder_DVIRManageWorkOrderChildPage[n].text
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            n = n + 1
        title_ManageWorkOrder_DVIRManageWorkOrderChildPage = w.until(
            EC.presence_of_element_located((By.XPATH, title_ManageWorkOrder_DVIRManageWorkOrderChildPageAdr))).text
        test_Name = "DVIR - Manage Work Order Child page opened"
        condition1 = "Manage Work Order"
        condition2 = title_ManageWorkOrder_DVIRManageWorkOrderChildPage
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Returned to DVIR - Manage Work Order Child page opened:"
        print_Information_Var = title_ManageWorkOrder_DVIRManageWorkOrderChildPage
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)
        print_Information_Fix = "NEW Work Order was created"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)

    except:
        print("There is No NEW Work Order to be Process")
        w.until(EC.presence_of_element_located((By.XPATH, button_X_ManageWorkOrder_DVIRManageWorkOrderChildPageListAdr))).click()
        print_Information_Fix = "There is No NEW Work Order to be Process"
        print_Information_Var = ""
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                    driver_Name, driver_Version)
    #       Screenshot
    test_Name = "New Work Order - DVIR page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    return ()
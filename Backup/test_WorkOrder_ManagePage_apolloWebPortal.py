#               Apollo Web Portal - Work Order

def WorkOrder_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var):

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

    #               Work Order Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"
    button_WorkOrder_ManagePageAdr = '//a[contains(@href,"/workorder")]'
    title_WorkOrder_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[1]/div/div/div[1]/h1"
    dropBox_Carrier_WorkOrderPageAdrID = "carrierSelector"
    dropBox_Status_WorkOrderPageAdrID = "Status"
    input_WorkOrderNumber_WorkOrderPageID = "workorderNumber"
    button_calendar_WorkOrderPage = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    date_SatrtEndDate_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-dvir/section[2]/div/app-search-panel/div/div/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    button_calendar_StartEndDate_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    calendar_Month_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[1]"
    calendar_Year_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[2]"
    calendar_DayStart_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[3]/div[1]/span"
    calendar_DayEnd_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[5]/div[7]/span"
    input_Defects_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[2]/div[3]/div/span/span[1]/span/ul/li/input"
    button_EXECUTE_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[2]/div[4]/div/button"
    read_Defects_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[2]/div[3]/div/span/span[1]/span/ul/li[1]"
    dropBox_Report_WorkOrderPageID = "report"
    dropBox_Categories_WorkOrderPageID = "category"
    input_Defects_RemoveAllItems_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[2]/div[3]/div/span/span[1]/span/ul/span"
    button_ACTIONSDetails_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[5]/div/div[1]/button"
    sort_WorkOrderNumber_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]"
    input_WorkOrderNumer_WorkOrder_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"
    button_ViewItems_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[1]/div/button"
    input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td"
    input_CreatedBy_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td"
    input_Status_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td"
    input_AssignedTo_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[5]/td"
    input_WorkOrderSentTo_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[6]/td"
    list_DefectList_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[2]/div[2]/dx-list"
    input_WorkOrderNumer_WorkOrder_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"
    title_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[1]/h3"
    button_closeX_WorkOrderChildPage = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[1]/button"


    #       Variables

    input_WorkOrderNumber_WorkOrderPageVar = "16"
    month_AbreviationList = ["Jan", "Feb", "Mar", "Apr", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day_Position_Calendar_WorkOrderPageStrInit = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div["
    startday_Position_Calendar_WorkOrderPageRowVar = 2
    day_Position_Calendar_WorkOrderPageStrMid = "]/div["
    startday_Position_Calendar_WorkOrderPageColVar = 1
    day_Position_Calendar_WorkOrderPageStrEnd = "]"
    lastday_Position_Calendar_WorkOrderPageRow6Var = 6
    lastday_Position_Calendar_WorkOrderPageRow7Var = 7
    lastday_Position_Calendar_WorkOrderPageColVar = 7

    download_ReportBigWorkOrder_WorkOrderPagePath = "C:/Users/Carlos/Downloads/report_big_dvir.pdf"
    workbookDB = "C:/apollo QA Reports/Support test DB/apolloPortalDVIRReportDB.xlsx"
    excel_DB_line = 2
    colum_Report_ID = "D"
    colum_Report_Name = "E"
    colum_Categories_ID = "F"
    colum_Categories_Name = "G"
    colum_Defects_ID = "H"
    colum_Defects_Name = "I"
    colum_Parent_ID = "J"
    w = WebDriverWait(driver, 10)



    #       #######################################     Work Order Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "Work Order Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Work Order side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_WorkOrder_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.XPATH, button_WorkOrder_ManagePageAdr))).click()

#       Title of the right page
    title_WorkOrder_WorkOrderPage = w.until(EC.presence_of_element_located((By.XPATH, title_WorkOrder_WorkOrderPageAdr))).text
    test_Name = "Work Order page open"
    condition1 = "Manage Work Order"
    condition2 = title_WorkOrder_WorkOrderPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "WorkOrder Page open:"
    print_Information_Var = title_WorkOrder_WorkOrderPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)
    print(title_WorkOrder_WorkOrderPage)


    #       Carrier - Select    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Carrier_WorkOrderPageAdrID))))
    dropdown_Import_Carrier_WorkOrder_WorkOrderPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Carrier_WorkOrder_WorkOrderPage_List):
        dropBox_Carrier_WorkOrderPageSelected = dropDown.select_by_visible_text(dropdown_Import_Carrier_WorkOrder_WorkOrderPage_List[n])
        dropBox_Carrier_WorkOrderPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Carrier element Work Order page"
        condition1 = dropdown_Import_Carrier_WorkOrder_WorkOrderPage_List[n]
        condition2 = dropBox_Carrier_WorkOrderPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Work Order Page - Carrier element:"
        print_Information_Var = dropBox_Carrier_WorkOrderPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1

    #       Status - Select %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Status_WorkOrderPageAdrID))))
    dropdown_Import_Status_WorkOrder_WorkOrderPage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropdown_Import_Status_WorkOrder_WorkOrderPage_List):
        dropBox_Status_WorkOrderPageSelected = dropDown.select_by_visible_text(dropdown_Import_Status_WorkOrder_WorkOrderPage_List[n])
        dropBox_Status_WorkOrderPageRead = dropDown.first_selected_option.text
        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Status element Work Order page"
        condition1 = dropdown_Import_Status_WorkOrder_WorkOrderPage_List[n]
        condition2 = dropBox_Status_WorkOrderPageRead
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Work Order Page - Status element:"
        print_Information_Var = dropBox_Status_WorkOrderPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1
        dropDown.select_by_visible_text("All")
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

    #       Work Order Numeber - Select %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    input_WorkOrderNumber_WorkOrderPage = w.until(EC.presence_of_element_located((By.ID, input_WorkOrderNumber_WorkOrderPageID)))
    input_WorkOrderNumber_WorkOrderPage.send_keys(input_WorkOrderNumber_WorkOrderPageVar)
    input_WorkOrderNumber_WorkOrderPageRead = input_WorkOrderNumber_WorkOrderPage.get_property('value')
    #       Assert Test and print if assert is fail
    test_Name = "Work Order Number element Work Order page"
    condition1 = input_WorkOrderNumber_WorkOrderPageVar
    condition2 = input_WorkOrderNumber_WorkOrderPageRead
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Work Order Page - Work Order Number element:"
    print_Information_Var = input_WorkOrderNumber_WorkOrderPageVar
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #       Calendar Start-End date
    date_now = datetime.now()
    td = timedelta(30)
    date_now = date_now
    date_ActualMonth = str(date_now)
    year_ActualMonth = date_ActualMonth[:4]
    month_ActualMonth = date_ActualMonth[5:-19]
    month_ActualMonth = int(month_ActualMonth) - 1
    month_Abreviation_ActualMonth = month_AbreviationList[month_ActualMonth]
    calendar_Month_WorkOrderPageVar = month_Abreviation_ActualMonth
    calendar_Year_WorkOrderPageVar = year_ActualMonth
    button_calendar_StartEndDate_WorkOrderPage = w.until(EC.element_to_be_clickable((By.XPATH, button_calendar_StartEndDate_WorkOrderPageAdr)))
    button_calendar_StartEndDate_WorkOrderPage.click()
    calendar_Month_WorkOrderPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Month_WorkOrderPageAdr))))
    calendar_Month_WorkOrderPage.select_by_visible_text(calendar_Month_WorkOrderPageVar)
    calendar_Year_WorkOrderPage = Select(w.until(EC.element_to_be_clickable((By.XPATH, calendar_Year_WorkOrderPageAdr))))
    calendar_Year_WorkOrderPage.select_by_visible_text(calendar_Year_WorkOrderPageVar)
    #       Try if the the last weekday is in the 7th Row of the calendar
    try:
        w.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[7]/div[1]"))).click()

        lastday_Position_Calendar_WorkOrderPageRowVar = str(lastday_Position_Calendar_WorkOrderPageRow7Var)
    except:
        lastday_Position_Calendar_WorkOrderPageRowVar = str(lastday_Position_Calendar_WorkOrderPageRow6Var)


    # Find the 1st weekday of the month
    col = 1
    while col < 8:
        try:
            calendar_StartDay_WorkOrderPageAdr = day_Position_Calendar_WorkOrderPageStrInit + str(startday_Position_Calendar_WorkOrderPageRowVar) + day_Position_Calendar_WorkOrderPageStrMid + str(startday_Position_Calendar_WorkOrderPageColVar) + day_Position_Calendar_WorkOrderPageStrEnd
            calendar_StartDay_WorkOrderPage = w.until(EC.element_to_be_clickable((By.XPATH, calendar_StartDay_WorkOrderPageAdr))).click()
            col = 8
        except:
            startday_Position_Calendar_WorkOrderPageColVar += 1
            col += 1
    # Find the Last weekday of the month
    col = 7
    while col > 0:
        try:
            calendar_LastDay_WorkOrderPageAdr = day_Position_Calendar_WorkOrderPageStrInit + str(lastday_Position_Calendar_WorkOrderPageRowVar) + day_Position_Calendar_WorkOrderPageStrMid + str(lastday_Position_Calendar_WorkOrderPageColVar) + day_Position_Calendar_WorkOrderPageStrEnd
            calendar_LasttDay_WorkOrderPage = w.until(EC.element_to_be_clickable((By.XPATH, calendar_LastDay_WorkOrderPageAdr))).click()
            col = 0
        except:
            lastday_Position_Calendar_WorkOrderPageColVar -= 1
            col -= 1
    w.until((EC.element_to_be_clickable((By.XPATH, button_calendar_WorkOrderPage)))).click()


#    Report x Categories X Defects

#   Read excel
    excell_pointer = Path(workbookDB)
    #Read ecel value not formula
    workbookDB_Read = openpyxl.load_workbook(excell_pointer, data_only=True)
    worksheetDB_Read = workbookDB_Read.active

    excel_ReportsTypes_cellValue = worksheetDB_Read['A2'].value
    excel_CategoriesTypes_cellValue = worksheetDB_Read['B2'].value
    excel_DefectsTypes_cellValue = worksheetDB_Read['C2'].value


#   Check the Report options/quantities per list based on the excel
    dropBox_Report_WorkOrderPage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Report_WorkOrderPageID))))
    dropBox_Report_MoreFilter_WorkOrder_List = [x.text for x in dropBox_Report_WorkOrderPage.options]
    # Assert
    test_Name = "Work Order page - Report Items Qte"
    condition1 = str(len(dropBox_Report_MoreFilter_WorkOrder_List))
    condition2 = str(excel_ReportsTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Work Order page - Report Items Qte"
    print_Information_Var = str(excel_ReportsTypes_cellValue)
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

#   Check The Categories quantities
    dropBox_Categories_WorkOrderPage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Categories_WorkOrderPageID))))
    dropBox_Categories_MoreFilter_WorkOrder_List = [x.text for x in dropBox_Categories_WorkOrderPage.options]
    # Assert
    test_Name = "Work order page - Categories Items Qte"
    condition1 = str(len(dropBox_Categories_MoreFilter_WorkOrder_List))
    condition2 = str(excel_CategoriesTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Work order page - Categories Items Qte"
    print_Information_Var = str(excel_CategoriesTypes_cellValue)
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

#   Check The Defects quantities
    #   Check The Defects quantities
    #for combiation ReportCategoriesDefectsVar in range(len(excel_DefectsTypes_cellValue))
    try:
        n = 1
        excel_DB_line = excel_DB_line + 2
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

            if cell_Parent_ID_Value == 0:
                dropBox_Report_WorkOrderPage.select_by_visible_text(cell_Report_Name_Value)
                dropBox_Item_Report_WorkOrderPage_Read = dropBox_Report_WorkOrderPage.first_selected_option.text

                dropBox_Categories_WorkOrderPage.select_by_visible_text(cell_Categories_Name_Value)
                dropBox_Item_Categories_WorkOrderPage_Read = dropBox_Categories_WorkOrderPage.first_selected_option.text

                defects = w.until(EC.presence_of_element_located((By.XPATH, input_Defects_WorkOrderPageAdr)))
                defects.send_keys(cell_Defects_Name_Value)
                defects.send_keys(Keys.RETURN)

        #       input list field read
                time.sleep(0.25)
                read_Defects_WorkOrderPage = w.until(EC.presence_of_element_located((By.XPATH, read_Defects_WorkOrderPageAdr)))
                read_Defects_WorkOrderPage = read_Defects_WorkOrderPage.text

                #       input list field read
                # Assert
                test_Name = "Defect items"
                condition1 = cell_Defects_Name_Value
                condition2 = read_Defects_WorkOrderPage
                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
                #       Print Assert OK
                print_Information_Fix = "WorkOrder Page - Defect items field:"
                print_Information_Var = cell_Defects_Name_Value
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
                w.until(EC.element_to_be_clickable((By.XPATH, input_Defects_RemoveAllItems_WorkOrderPageAdr))).click()
            n = n + 1
            excel_DB_line = excel_DB_line + 1
    except:
        print('!!!!!!!!!!!!!!!!!Try error !!!!!!!!!!!!!!!!!!!!')

    # Select ALL Work Orders and Execute button
    dropBox_Report_WorkOrderPage.select_by_visible_text("All")
    dropBox_Categories_WorkOrderPage.select_by_visible_text("All")
    input_WorkOrderNumber_WorkOrderPage.clear()
    input_WorkOrderNumber_WorkOrderPage.send_keys(" ")
    button_EXECUTE_WorkOrderPage = w.until(EC.element_to_be_clickable((By.XPATH, button_EXECUTE_WorkOrderPageAdr))).click()
    test_Name = "Manage Work Order Manage Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

#    WorkOrder# Sort and Actions:
    w.until(EC.element_to_be_clickable((By.XPATH, sort_WorkOrderNumber_WorkOrderPageAdr))).click()
    w.until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]"))).click()
    time.sleep(0.5)
    input_WorkOrderNumer_WorkOrder_WorkOrderPage = w.until(EC.presence_of_element_located((By.XPATH, input_WorkOrderNumer_WorkOrder_WorkOrderPageAdr))).text

#   Handling the Work Order Details child Pag
#       Title of the right page
    w.until(EC.presence_of_element_located((By.XPATH, button_ACTIONSDetails_WorkOrderPageAdr))).click()


    title_WorkOrderDetails_WorkOrderChildPage = w.until(EC.presence_of_element_located((By.XPATH, title_WorkOrderDetails_WorkOrderChildPageAdr))).text
    test_Name = "Work Order Details Child page open"
    condition1 = "Work Order Details"
    condition2 = title_WorkOrderDetails_WorkOrderChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Work Order Details Child page:"
    print_Information_Var = title_WorkOrderDetails_WorkOrderChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)

#   Close Work Order Child page:
    w.until(EC.element_to_be_clickable((By.XPATH, button_closeX_WorkOrderChildPage))).click()






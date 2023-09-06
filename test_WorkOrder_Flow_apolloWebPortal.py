#               Apollo Web Portal - Work Order Flow

def WorkOrder_Flow_ManagePage (driverModelTestControl, driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_List):

    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.wait import WebDriverWait
    import tc_reports
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.select import Select
    from datetime import datetime, timedelta
    import test_AssignWorkOrder_Vendor

    #               Work Order Main

    #       Fields Address
    menuRegion_MainSideBar_ManagePageAdrAsideDiv = "/html/body/app-root/app-main/div/main-side-bar/aside/div"
    button_WorkOrder_ManagePageAdr = '//a[contains(@href,"/workorder")]'
    title_WorkOrder_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[1]/div/div/div[1]/h1"
    dropBox_Carrier_WorkOrderPageAdrID = "carrierSelector"
    button_calendar_WorkOrderPage = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    button_calendar_StartEndDate_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/div/button"
    calendar_Month_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[1]"
    calendar_Year_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[1]/ngb-datepicker-navigation/ngb-datepicker-navigation-select/select[2]"
    button_EXECUTE_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[2]/div[4]/div/button"
    sort_WorkOrderNumber_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]"
    input_sort_WorkOrderNumber_WorkOrder_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"
    input_Status_WorkOrder_WorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[2]"
    input_Defects_WorkOrderPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[2]/div[2]/dx-list"
    button_ViewItems_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[1]/div/button"
    input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td"
    input_CreatedBy_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td"
    input_TimeCreated_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td"
    input_Status_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td"
    input_AssignedTo_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[5]/td"
    input_WorkOrderSentTo_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[1]/table/tbody/tr[6]/td"
    list_DefectList_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[2]/div[2]/dx-list"
    title_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[1]/h3"
    button_closeX_WorkOrderDetails_WorkOrderChildPageAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[1]/button"
    action_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[3]"
    description_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[4]"
    sort_CreationDate_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]"
    creationDate_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr = "/html/body/ngb-modal-window/div/div/app-workorder-detail/div[2]/div/div/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"
    buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Init = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr["
    buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_End = "]/td[6]/div/div[1]/button"

    #       Variables
    month_AbreviationList = ["Jan", "Feb", "Mar", "Apr", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    day_Position_Calendar_WorkOrderPageStrInit = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/app-search-panel/div/div/form/div[1]/div[4]/app-date-rangepicker/div/div/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div["
    startday_Position_Calendar_WorkOrderPageRowVar = 2
    day_Position_Calendar_WorkOrderPageStrMid = "]/div["
    startday_Position_Calendar_WorkOrderPageColVar = 1
    day_Position_Calendar_WorkOrderPageStrEnd = "]"
    lastday_Position_Calendar_WorkOrderPageRow6Var = 6
    lastday_Position_Calendar_WorkOrderPageRow7Var = 7
    lastday_Position_Calendar_WorkOrderPageColVar = 7
    w = WebDriverWait(driver, 10)

    #       #######################################     Work Order Main functions    ########################################################
    #   ###############################################################################################################################
#   Page Title on TCReport
    function_Name = "Work Order Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#       Function Work Order side bar button click
    menuRegion_MainSideBar_ManagePageAsideDiv = w.until(EC.presence_of_element_located((By.XPATH, menuRegion_MainSideBar_ManagePageAdrAsideDiv)))
    button_WorkOrder_ManagePage = WebDriverWait(menuRegion_MainSideBar_ManagePageAsideDiv,10).until(EC.element_to_be_clickable((By.XPATH, button_WorkOrder_ManagePageAdr))).click()

#   Verify the if is the Correct page:
    title_WorkOrder_WorkOrderPage = w.until(EC.presence_of_element_located((By.XPATH, title_WorkOrder_WorkOrderPageAdr))).text
    test_Name = "Work Order page open"
    condition1 = "Manage Work Order"
    condition2 = title_WorkOrder_WorkOrderPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "WorkOrder Page open"
    print_Information_Var = title_WorkOrder_WorkOrderPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
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
        print_Information_Fix = "Work Order Page - Carrier element"
        print_Information_Var = dropBox_Carrier_WorkOrderPageRead
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
        n = n + 1

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

#   Execute button:
    button_EXECUTE_WorkOrderPage = w.until(EC.element_to_be_clickable((By.XPATH, button_EXECUTE_WorkOrderPageAdr))).click()

#    WorkOrder# Sort and Actions:
    if driver_Name == "Firefox":
        time.sleep(1)
    w.until(EC.element_to_be_clickable((By.XPATH, sort_WorkOrderNumber_WorkOrderPageAdr))).click()
    w.until(EC.element_to_be_clickable((By.XPATH, sort_WorkOrderNumber_WorkOrderPageAdr))).click()
    time.sleep(0.5)
    input_WorkOrderNumber_WorkOrder_ManageWorkOrderPage_Read = w.until(EC.presence_of_element_located((By.XPATH, input_sort_WorkOrderNumber_WorkOrder_WorkOrderPageAdr))).text

#   Work Order Status:
    input_Status_WorkOrder_WorkOrderPage = w.until((EC.presence_of_element_located((By.XPATH, input_Status_WorkOrder_WorkOrderPageAdr)))).text
    #       Screenshot
    test_Name = "Manage Work Order Work Order"
    tc_reports.screenshot(driver, driver_Name, test_Name)

#   Open the Work Order Detail page  for the Work Order Number check on Work Order Details
    workOrderNumber_ManageWorkOrder_Var = input_WorkOrderNumber_WorkOrder_ManageWorkOrderPage_Read
    buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Row = "1"
    buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr = buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Init + buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Row + buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_End
    w.until(EC.element_to_be_clickable((By.XPATH, buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr))).click()
    input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPageAdr))).text

#   Get the Work Order send to from the Work Order

    try:
        workOrderNumber_ManageWorkOrder_Var == input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPage
        workOrder_Contacts_List = w.until(EC.presence_of_element_located((By.XPATH, input_WorkOrderSentTo_WorkOrderDetails_WorkOrderChildPageAdr))).text
        workOrderSentTo_ManageWorkOrder_List = [workOrder_Contacts_List]
    except:
        print("ERRO Work Order Flow - Work Order Number")
    #       Screenshot
    test_Name = "Work Order Details"
    tc_reports.screenshot(driver, driver_Name, test_Name)
#   Close Work Order Detail child page
    w.until(EC.element_to_be_clickable((By.XPATH, button_closeX_WorkOrderDetails_WorkOrderChildPageAdr))).click()
    print(f'driver antes do email = {driver}')
############################################################
#   Open the ASSIGN WORK ORDER page - out of apollo portal #
############################################################
    print("Open Assign Work Order")
    test_AssignWorkOrder_Vendor.assignWorkOrder_Vendor (driverModelTestControl, driver, driver_Name, driver_Version, workOrderNumber_ManageWorkOrder_Var, workOrderSentTo_ManageWorkOrder_List,  input_Status_WorkOrder_WorkOrderPage)

############################################################
#  Close the ASSIGN WORK ORDER page - out of apollo portal #
############################################################

    print("Back to test Work Order Flow apolloWebPortal")

#  GLOBAL the ASSIGN WORK ORDER page - out of apollo portal #
    workOrderNumber_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.workOrderNumber_AssignWorkOrder_Read
    createdBy_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.createdBy_AssignWorkOrder_Read
    timeCreated_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.timeCreated_AssignWorkOrder_Read
    status_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.status_AssignWorkOrder_Read
    defectList_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.defectList_AssignWorkOrder_Read
    action_WorkOrderHistory_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.action_WorkOrderHistory_AssignWorkOrder_Read
    description_WorkOrderHistory_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.description_WorkOrderHistory_AssignWorkOrder_Read
    creationDate_WorkOrderHistory_AssignWorkOrder_Read_global = test_AssignWorkOrder_Vendor.creationDate_WorkOrderHistory_AssignWorkOrder_Read

# Find the eye button related to the Work Order in test on the Work Order table
    n = 1
    while n > 0:
        workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Init = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[2]/div/div/div/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr["
        workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Row = str(n)
        workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_End = "]/td[1]"
        workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr = workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Init + workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Row + workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_End
        workOrderNumber_InTest_WorkOrder_ManageWorkOrder = w.until(EC.presence_of_element_located((By.XPATH, workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr))).text
        if workOrderNumber_InTest_WorkOrder_ManageWorkOrder == workOrderNumber_AssignWorkOrder_Read_global:
            buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Row = str(n)
            buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr = buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Init + buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_Row + buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr_End
            w.until(EC.element_to_be_clickable((By.XPATH, buttoneye_workOrderNumber_InTest_WorkOrder_ManageWorkOrderAdr))).click()
            n = 0
        else:
            n += 1
    print("WOrk Order child page - opened")
#   Verify the Work Order Information and the information from Assign Work Order got form def test_AssignWorkOrder_Vendor.assignWorkOrder_Vendor

#   Page Title on TCReport
    function_Name = "Compare Information from Assign Work Order with the information on the Work Order Details"
    tc_reports.function_Init_Page(function_Name, driver_Name)

#   Verify the WORK ORDER DETAIL child Pag information
#       Title of the right page
    title_WorkOrderDetails_WorkOrderChildPage = w.until(EC.presence_of_element_located((By.XPATH, title_WorkOrderDetails_WorkOrderChildPageAdr))).text
    test_Name = "Work Order Details Child page open"
    condition1 = "Work Order Details"
    condition2 = title_WorkOrderDetails_WorkOrderChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Work Order Details Child page"
    print_Information_Var = title_WorkOrderDetails_WorkOrderChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    # tc_reports.screenshot(driver, driver_Name, test_Name)

#    Verify WORK ORDER NUMBER from Assign Work Order with Work Order number from Work Order Details:

    test_Name = "Work Order Number"
    condition1 = workOrderNumber_AssignWorkOrder_Read_global
    condition2 = input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Work Order Number (Work Order - Assign x Details)"
    print_Information_Var = input_WorkOrderNumber_WorkOrderDetails_WorkOrderChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #    Verify CREATED BY from Assign Work Order with Work Order number from Work Order Details:
    input_CreatedBy_WorkOrderDetails_WorkOrderChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_CreatedBy_WorkOrderDetails_WorkOrderChildPageAdr))).text
    test_Name = "Created By (Work Order - Assign x Details)"
    condition1 = createdBy_AssignWorkOrder_Read_global
    condition2 = input_CreatedBy_WorkOrderDetails_WorkOrderChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Created By (Work Order - Assign x Details)"
    print_Information_Var = input_CreatedBy_WorkOrderDetails_WorkOrderChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #    Verify TIME CREATED from Assign Work Order with Work Order number from Work Order Details:
    input_TimeCreated_WorkOrderDetails_WorkOrderChildPage = w.until(EC.presence_of_element_located((By.XPATH, input_TimeCreated_WorkOrderDetails_WorkOrderChildPageAdr))).text
    test_Name = "Time Created (Work Order - Assign x Details)"
    condition1 = timeCreated_AssignWorkOrder_Read_global
    condition2 = input_TimeCreated_WorkOrderDetails_WorkOrderChildPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Time Created (Work Order - Assign x Details)"
    print_Information_Var = input_TimeCreated_WorkOrderDetails_WorkOrderChildPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #    Verify STATUS from Assign Work Order with Work Order number from Work Order Details:
    test_Name = "Status (Work Order - Assign x Details)"
    condition1 = status_AssignWorkOrder_Read_global
    condition2 = input_Status_WorkOrder_WorkOrderPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Status (Work Order - Assign x Details)"
    print_Information_Var = input_Status_WorkOrder_WorkOrderPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #    Verify DEFECTS LIST from Assign Work Order with Work Order number from Work Order Details:
    #    defectList_AssignWorkOrder_Read_global
    input_Defects_WorkOrderPage = w.until((EC.presence_of_element_located((By.XPATH, input_Defects_WorkOrderPageAdr)))).text
    test_Name = "Defect List WO Assign x Details"
    condition1 = defectList_AssignWorkOrder_Read_global
    condition2 = input_Defects_WorkOrderPage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Defect WO Assign x Details"
    print_Information_Var = input_Defects_WorkOrderPage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

#   Defect quantities

    #    Verify DEFECTS QUANTITIES from Assign Work Order with Work Order number from Work Order Details:
# The defects numbers = number of new lines (\n) on the string + 1
    # 1 defect  = 0 \n => +1 = 1
    # 2 defects = 1 \n => +1 = 2
    defect_lines_defectList_AssignWorkOrder_Read_global = defectList_AssignWorkOrder_Read_global.count('\n') + 1
    defect_lines_input_Defects_WorkOrderPage = input_Defects_WorkOrderPage.count('\n') + 1

    test_Name = "Number of Defects listed - Assign x Details"
    condition1 = str(defect_lines_defectList_AssignWorkOrder_Read_global)
    condition2 = str(defect_lines_input_Defects_WorkOrderPage)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Number of Defects listed - Assign x Details"
    print_Information_Var = str(defect_lines_defectList_AssignWorkOrder_Read_global)
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


#   Verify the last action status on the Work Order History with the status from Assign Work Order:
#   View Items buttom
    w.until((EC.element_to_be_clickable((By.XPATH, button_ViewItems_WorkOrderDetails_WorkOrderChildPageAdr)))).click()

#   Sort Creation date to get the last update informtion
    w.until(EC.presence_of_element_located((By.XPATH, sort_CreationDate_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr))).click()
    w.until(EC.presence_of_element_located((By.XPATH, sort_CreationDate_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr))).click()
    time.sleep(0.5)


#   Read elements to be check:
    action_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read = w.until(EC.presence_of_element_located((By.XPATH, action_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr))).text


    print(action_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read)
    description_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read = w.until((EC.presence_of_element_located((By.XPATH, description_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr)))).text
    creationDate_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read = w.until((EC.presence_of_element_located((By.XPATH, creationDate_WorkOrderHistory_WorkOrderdetails_WorkOrderAdr)))).text

    #   Scroll to action element
    try:
        #time.sleep(1)
        actions = ActionChains(driver)
        actions.move_to_element(title_WorkOrderDetails_WorkOrderChildPage)
        actions.perform()
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    except:
        print()
#   Compare the information from Assign Work Order with the Work Order History at the apollo Portal
#   Actions status
    test_Name = "Last Action updated Assign x Details"
    condition1 = action_WorkOrderHistory_AssignWorkOrder_Read_global
    condition2 = action_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Last Action updated - Assign x Details"
    print_Information_Var = action_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

#   Description status
    test_Name = "Last Description updated - Assign x Details"
    condition1 = description_WorkOrderHistory_AssignWorkOrder_Read_global
    condition2 = description_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Last Description updated - Assign x Details"
    print_Information_Var = description_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

#   Creation Date status
    test_Name = "Last Creaton Date updated - Assign x Details"
    condition1 = creationDate_WorkOrderHistory_AssignWorkOrder_Read_global
    condition2 = creationDate_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Last Creaton Date updated - Assign x Details"
    print_Information_Var = creationDate_WorkOrderHistory_WorkOrderdetails_WorkOrder_Read
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Work Order Details final inspection"
    tc_reports.screenshot(driver, driver_Name, test_Name)

#   Close Work Order Page

    button_Manage_ManageWorkOrderPageAdr = "/html/body/app-root/app-main/div/div[1]/app-manageworkorder/section[1]/div/div/div[2]/ol/li[1]"
    w.until(EC.element_to_be_clickable((By.XPATH, button_closeX_WorkOrderDetails_WorkOrderChildPageAdr))).click()
    w.until((EC.element_to_be_clickable((By.XPATH, button_Manage_ManageWorkOrderPageAdr)))).click()
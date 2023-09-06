#   Assign Work Order send to Vendor

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

def assignWorkOrder_Vendor (driverModelTestControl, driver, driver_Name, driver_Version, workOrderNumber_ManageWorkOrder_Var, workOrderSentTo_ManageWorkOrder_List, input_Status_WorkOrder_WorkOrderPage):

    # Variaveis Globais:
    global workOrderTitle_AssignWorkOrder_Read
    global clientName_AssignWorkOrder_Read
    global clientAddress_AssignWorkOrder_Read
    global workOrderNumber_AssignWorkOrder_Read
    global createdBy_AssignWorkOrder_Read
    global timeCreated_AssignWorkOrder_Read
    global status_AssignWorkOrder_Read
    global defectList_AssignWorkOrder_Read
    global action_WorkOrderHistory_AssignWorkOrder_Read
    global description_WorkOrderHistory_AssignWorkOrder_Read
    global creationDate_WorkOrderHistory_AssignWorkOrder_Read

    workOrderTitle_AssignWorkOrder_Read = str()
    clientName_AssignWorkOrder_Read = str()
    clientAddress_AssignWorkOrder_Read = str()
    workOrderNumber_AssignWorkOrder_Read = str()
    createdBy_AssignWorkOrder_Read = str()
    timeCreated_AssignWorkOrder_Read = str()
    status_AssignWorkOrder_Read = str()
    defectList_AssignWorkOrder_Read = []
    action_WorkOrderHistory_AssignWorkOrder_Read = str()
    description_WorkOrderHistory_AssignWorkOrder_Read = str()
    creationDate_WorkOrderHistory_AssignWorkOrder_Read = str()

    print("Assign Work Order")
#   Address:
    workOrderTitle_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[1]/div/div/div/h1"

    #workOrderNumber_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td"
    workOrderNumber_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td"

    #clientName_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[1]/div/div/div[1]"
    clientName_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[1]/div/div/div/table/tbody/tr[1]/td"

    #clientAddress_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[1]/div/div/div[2]"
    clientAddress_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[1]/div/div/div/table/tbody/tr[2]/td"

    #createdBy_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td"
    createdBy_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[2]/td"

    #timeCreated_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td"
    timeCreated_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[3]/td"

    #status_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[4]/td"
    status_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr[4]/td"

    #defectList_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/dx-list"
    defectList_AssignWorkOrder_Read_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[2]/div/div[2]/div[2]/div[2]/dx-list/div[1]/div/div[1]/div[2]/div"

    #button_ACCEPT_AssignWorkOrder_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/button[1]"
    button_ACCEPT_AssignWorkOrder_Adr = "/html/body/app-root/app-workorderassign/section[2]/div/div[2]/div/div[2]/button[1]"

    button_DECLINE_AssignWorkOrder_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/button[2]"
    button_VIEWITEMS_AssignWorkOrder_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[1]/div/button"


    button_PLUSNEW_AssignWorkOrder_Adr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/button"
    button_SAVE_WorkOrderItem_AssignWorkOrder_Adr = "/html/body/ngb-modal-window/div/div/app-workorderassign-form/div[2]/form/div[2]/button[1]"
    button_CLOSE_WorkOrderItem_AssignWorkOrder_Adr = "/html/body/ngb-modal-window/div/div/app-workorderassign-form/div[2]/form/div[2]/button[2]"
    action_WorkOrderItem_AssignWorkOrder_Adr = "/html/body/ngb-modal-window/div/div/app-workorderassign-form/div[2]/form/div[1]/div[1]/select"
    description_WorkOrderItem_AssignWorkOrder_Adr = "/html/body/ngb-modal-window/div/div/app-workorderassign-form/div[2]/form/div[1]/div[2]/textarea"
    sort_workOrderHistory_AssignWorkOrderAdr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[5]/div/table/tbody/tr/td[1]"
    action_WorkOrderHistory_AssignWorkOrderAdr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[3]"
    description_WorkOrderHistory_AssignWorkOrderAdr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[4]"
    creationDate_WorkOrderHistory_AssignWorkOrderAdr = "/html/body/app-root/app-workorderassign/section[2]/div[2]/div[2]/div/div[2]/div[3]/div[2]/dx-data-grid/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[1]"

#   Variables:
    assignWorkOrdersiteAddressInit = "http://10.1.10.33:4201/workorderAssign?workorderId="
    assignWorkOrdersiteAddressWorkOrderNumber = str(workOrderNumber_ManageWorkOrder_Var)
    assignWorkOrdersiteAddressMid = "&email="
    assignWorkOrdersiteAddressSendTo = workOrderSentTo_ManageWorkOrder_List[0]
    assignWorkOrdersiteAddressVar = assignWorkOrdersiteAddressInit + assignWorkOrdersiteAddressWorkOrderNumber + assignWorkOrdersiteAddressMid + assignWorkOrdersiteAddressSendTo
    date = datetime.now()
    driverDriverListVar = ["C:\\tools\chromedriver.exe",
                           "C:\\tools\operadriver.exe",
                           "C:\\tools\msedgedriver.exe",
                           "C:\\tools\geckodriver.exe"]

    # Open a new window
    if driverModelTestControl == 0:
        driver_AssgnWorkOrder = webdriver.Chrome(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 1:
        driver_AssgnWorkOrder = webdriver.Opera(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 2:
        driver_AssgnWorkOrder = webdriver.Edge(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 3:
        driver_AssgnWorkOrder = webdriver.Firefox(executable_path=driverDriverListVar[driverModelTestControl])

    driver_AssgnWorkOrder.get(assignWorkOrdersiteAddressVar)
    driver_AssgnWorkOrder.maximize_window()
    w1 = WebDriverWait(driver_AssgnWorkOrder, 10)

#   Page Title on TCReport
    function_Name = "Assign Work Order VENDOR email link"
    tc_reports.function_Init_Page(function_Name, driver_Name)


#   Get All information from Assign Work Order
    workOrderTitle_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, workOrderTitle_AssignWorkOrder_Read_Adr))).text
    clientName_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, clientName_AssignWorkOrder_Read_Adr))).text
    clientAddress_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, clientAddress_AssignWorkOrder_Read_Adr))).text
    workOrderNumber_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, workOrderNumber_AssignWorkOrder_Read_Adr))).text
    createdBy_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH,  createdBy_AssignWorkOrder_Read_Adr))).text
    timeCreated_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, timeCreated_AssignWorkOrder_Read_Adr))).text
    status_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, status_AssignWorkOrder_Read_Adr))).text

    defectList_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, defectList_AssignWorkOrder_Read_Adr))).text


#   Verify the if is the Correct page:
    test_Name = "Assign Work Order page open"
    condition1 = "Assign Work Order"
    condition2 = workOrderTitle_AssignWorkOrder_Read
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Assign WO by email"
    print_Information_Var = workOrderTitle_AssignWorkOrder_Read
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    tc_reports.screenshot(driver, driver_Name, test_Name)
    print(workOrderTitle_AssignWorkOrder_Read)
    #       Screenshot
    test_Name = "Assign Work Order VENDOR email link"
    driver_temp = driver
    driver = driver_AssgnWorkOrder
    tc_reports.screenshot(driver, driver_Name, test_Name)
    driver = driver_temp

# Verify Work Order #
    #       Assert Test and print if assert is fail
    test_Name = "Assign Work Order Work Order Number"
    condition1 = workOrderNumber_ManageWorkOrder_Var
    condition2 = workOrderNumber_AssignWorkOrder_Read
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Assign Work Order page Work Order Number"
    print_Information_Var = workOrderNumber_AssignWorkOrder_Read
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)



#
#   Verify The Assign Work Order STATUS:
# If STATUS = OPEN:
    try:
        if input_Status_WorkOrder_WorkOrderPage == "Open":
            w1.until(EC.element_to_be_clickable((By.XPATH, button_ACCEPT_AssignWorkOrder_Adr))).click()

            print("Button ACCEPT was clicked !!!!!!!!!")
        else:
            w1.until(EC.element_to_be_clickable((By.XPATH, button_VIEWITEMS_AssignWorkOrder_Adr))).click()
            w1.until(EC.element_to_be_clickable((By.XPATH, button_PLUSNEW_AssignWorkOrder_Adr))).click()
            action_WorkOrderItem_AssignWorkOrder = Select(w1.until(EC.presence_of_element_located((By.XPATH, action_WorkOrderItem_AssignWorkOrder_Adr))))
            #action_WorkOrderItem_AssignWorkOrder.select_by_visible_text("Payment request")
            randomAction = date.strftime("%M")
            randomAction = randomAction[1]
            randomAction = int(randomAction)
            print(randomAction)
            if randomAction > 7:
                randomAction = randomAction - 3
            print(randomAction)
            action_WorkOrderItem_AssignWorkOrder.select_by_index(randomAction)
            action_WorkOrderHistory_WorkOrderItem_AssignWorkOrderRead = action_WorkOrderItem_AssignWorkOrder.first_selected_option.text
            description_WorkOrderItem_AssignWorkOrder = w1.until(EC.presence_of_element_located((By.XPATH, description_WorkOrderItem_AssignWorkOrder_Adr)))
            description_WorkOrderItemVar = "QA Test: " + date.strftime("%m/%d/%Y, %H:%M:%S")
            description_WorkOrderItem_AssignWorkOrder.send_keys(description_WorkOrderItemVar)
            description_WorkOrderHistory_WorkOrderItem_AssignWorkOrderRead = description_WorkOrderItem_AssignWorkOrder.text
            w1.until(EC.element_to_be_clickable((By.XPATH, button_SAVE_WorkOrderItem_AssignWorkOrder_Adr))).click()
            w1.until(EC.presence_of_element_located((By.XPATH, sort_workOrderHistory_AssignWorkOrderAdr))).click()
            w1.until(EC.presence_of_element_located((By.XPATH, sort_workOrderHistory_AssignWorkOrderAdr))).click()
            time.sleep(0.5)
            action_WorkOrderHistory_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, action_WorkOrderHistory_AssignWorkOrderAdr))).text
            description_WorkOrderHistory_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, description_WorkOrderHistory_AssignWorkOrderAdr))).text
            creationDate_WorkOrderHistory_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, creationDate_WorkOrderHistory_AssignWorkOrderAdr))).text

    except:
        print("Assign Work Order Item ERROR")

    defectList_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, defectList_AssignWorkOrder_Read_Adr))).text
    driver_AssgnWorkOrder.execute_script("window.scrollTo(0, 900)")
    status_AssignWorkOrder_Read = w1.until(EC.presence_of_element_located((By.XPATH, status_AssignWorkOrder_Read_Adr))).text

    driver_AssgnWorkOrder.close()

    print("Test Assign Work Order Vendor CLOSE")

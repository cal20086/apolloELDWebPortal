#               apollo Web Portal - Test Control page


from selenium import webdriver
import os
import test_Global_Variables_apolloWebPortal
import time
from datetime import datetime

import test_LoginPage_apolloWebPortal
import test_HomePage_apolloWebPortal
import test_ManagePage_apolloWebPortal
import test_CarrierDetails_ManagePage_apolloWebPortal
import test_CarrierDrivers_ManagePage_apolloWebPortal
import test_HomeBases_ManagePage_apolloWebPortal
import test_Notifications_ManagePage_apolloWebPortal
import test_Assets_ManagePage_apolloWebPortal
import test_DVIR_ManagePage_apolloWebPortal
import test_DVIR_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_Flow_apolloWebPortal
import teste_NAO_USAR
import test_Report_Categories_Defects_FIELDSInterchanges_apolloWebPortal
import test_Enhanced_IFTAPage_apolloWebPortal
import test_Global_Variables_apolloWebPortal
import tc_reports




#               Open driver & Explicit:

#               Global Variables
global testCaseCounter_Global
#testCaseCounter_Global = 0


#               Variables
driverModelTestControl = 0

contol_Reportfile = 0
test_Case_Type = "Regression"

carrier = ["Staging Client"]
truckDriversList = ["John Doe"]

siteAddressVar = "http://staging.apolloeld.com/HOS.aspx"

driverListName = ["Chrome",
                  "Opera",
                  "Edge",
                  "Firefox"
                  ]

driverListVersion = ["99.0.4896.20 (Official Build) (64-bit)", "83.0.4254.27 (64-bit)",
                     "98.0.1108.43 (Official build) (64-bit", "94.0.2 (64-bit)"
                     ]

driverDriverListVar = ["C:\\tools\chromedriver.exe",
                       "C:\\tools\operadriver.exe",
                       "C:\\tools\msedgedriver.exe",
                       "C:\\tools\geckodriver.exe"]

user_ApolloWebPortalListVar = ["staging.client"]

password_ApolloWebPortalListVar = ["011demo2"]


carrier = ["Staging Client"]
truckDriversList = ["John (johndoe1)"]
reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"


driver_UserName_Var = "Test (sdsd1)"
client_Name_Var = "Carrier Test"
client_Adress_Var = "11111 NE 11st Doral 33150"
defect_Vehicle_List_Var = ("Refrigeration Unit", "Part 1. Air Brake System", "(b) air loss rate exceeds prescribed limit", "Part 19. Steering", "(b) steering wheel lash(free - play) exceeds prescribed limitd")
workOrder_CreatedBy_Var = "carlos.liguori@assuredtechmatics.com"
workOrder_Contacts_Var = ("vendor@vendor.com")




#####################################################################################################################################
#                                                        Main functions                                                             #
#####################################################################################################################################

dateInit = datetime.now()
# Delete all previous reports files
for f in os.listdir(reportFolder_Path_QAReports):
    os.remove(os.path.join(reportFolder_Path_QAReports, f))


while driverModelTestControl < 1:


    if driverModelTestControl == 0:
        driver = webdriver.Chrome(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 1:
        driver = webdriver.Opera(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 2:
        driver = webdriver.Edge(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 3:
        driver = webdriver.Firefox(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl > 3:
        breack(1)

    dateInitbyDriver = datetime.now()
    driver_Name = driverListName[driverModelTestControl]
    driver_Version = driverListVersion[driverModelTestControl]
    user_ApolloWebPortalVar = user_ApolloWebPortalListVar[driverModelTestControl]
    password_ApolloWebPortalVar = password_ApolloWebPortalListVar[driverModelTestControl]

    print(driverModelTestControl)
    print(driver_Name)

# Call Functions:

    test_Global_Variables_apolloWebPortal.global_Variables()
    test_LoginPage_apolloWebPortal.login_apolloWebPortal(contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, siteAddressVar, test_Case_Type)
    test_HomePage_apolloWebPortal.homePage(driver, driver_Name, driver_Version)
    test_ManagePage_apolloWebPortal.managePage(driver, driver_Name, driver_Version)


#    test_CarrierDetails_ManagePage_apolloWebPortal.carrierDetail_ChildMenu_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var)
    test_CarrierDrivers_ManagePage_apolloWebPortal.carrierDrivers_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_HomeBases_ManagePage_apolloWebPortal.carrierHomeBases_ChildMenu_ManagePage (driver, driver_Name, driver_Version)
#    test_Assets_ManagePage_apolloWebPortal.carrierAssets_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_Notifications_ManagePage_apolloWebPortal.carrierNotifications_ChildMenu_ManagePage (driver, driver_Name, driver_Version)
#    test_DVIR_ManagePage_apolloWebPortal.DVIR_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_DVIR_WorkOrder_ManagePage_apolloWebPortal.DVIR_WorkOrder_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_ManagePage_apolloWebPortal.WorkOrder_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_Flow_apolloWebPortal.WorkOrder_Flow_ManagePage (driverModelTestControl, driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_Enhanced_IFTAPage_apolloWebPortal.EnhancedIFTA_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList)
#    teste_NAO_USAR.DVIR_WorkOrder_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)

    #driver.close()

    #def datebyDriver_Calc():
    #    dateEnd = datetime.now()
    #    datebyDriver = dateEnd - dateInitbyDriver
    #    return datebyDriver

    dateEnd = datetime.now()
    datebyDriver = dateEnd - dateInitbyDriver
    test_Execution_Time_By_Driver_Global = datebyDriver

    print()
    print(f"{driver_Name} - Test executing time TOTAL = {datebyDriver}")

    tc_reports.summaryPerformance_by_Driver(driver, driver_Name, datebyDriver)


    #       Print Preformance Summary
    #tc_reports.summaryPerformance_by_Driver(driver, driver_Name)


    driverModelTestControl = driverModelTestControl + 1

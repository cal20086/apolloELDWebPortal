#               apollo Web Portal - Test Control page


from selenium import webdriver
import os
import time
from datetime import datetime
import test_Global_Variables_apolloWebPortal
import test_LoginPage_apolloWebPortal
import test_HomePage_apolloWebPortal
import test_ManagePage_apolloWebPortal
import test_CarrierDetails_ManagePage_apolloWebPortal
import test_CarrierDrivers_ManagePage_apolloWebPortal
import test_HomeBases_ManagePage_apolloWebPortal
import test_Assets_ManagePage_apolloWebPortal
import test_DVIR_ManagePage_apolloWebPortal
import test_DVIR_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_ManagePage_apolloWebPortal
import test_WorkOrder_Flow_apolloWebPortal
import teste_NAO_USAR



#               Open driver & Explicit:

#               Variables
driverModelTestControl = 0
contol_Reportfile = 0
test_Case_Type = "Regression"

carrier = ["QATest1"]
truckDriversList = ["All",
                    "QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)"]

siteAddressVar = "http://10.1.10.33/Login.aspx?ReturnUrl=%2fDefault.aspx"

driverListName = ["Chrome",
                  "Opera",
                  "Edge",
                  "Firefox"
                  ]

driverListVersion = ["96.0.4664.45 (Official Build) (64-bit)", "81.0.4196.37 (64-bit)",
                     "96.0.1054.41 (Official build) (64-bit", "92.0 (64-bit)"
                     ]

driverDriverListVar = ["C:\\tools\chromedriver.exe",
                       "C:\\tools\operadriver.exe",
                       "C:\\tools\msedgedriver.exe",
                       "C:\\tools\geckodriver.exe"]

user_ApolloWebPortalListVar = ["qauser1",
                               "qauser2",
                               "qauser3",
                               "qauser4",
                               "qauser5"]

password_ApolloWebPortalListVar = ["qauser1",
                                   "qauser2",
                                   "qauser3",
                                   "qauser4",
                                   "qauser5"]


carrier = ["QATest1"]
truckDriversList = ["QADriver1 (qadriver1)",
                    "QADriver2 (qadriver2)",
                    "QADriver3 (qadriver3)",
                    "All"]
reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"

driver_UserName_Var = "Test (sdsd1)"
client_Name_Var = "Carrier Test"
client_Adress_Var = "11111 NE 11st Doral 33150"
defect_Vehicle_List_Var = ("Refrigeration Unit", "Part 1. Air Brake System", "(b) air loss rate exceeds prescribed limit", "Part 19. Steering", "(b) steering wheel lash(free - play) exceeds prescribed limitd")
workOrder_CreatedBy_Var = "carlos.liguori@assuredtechmatics.com"
workOrder_Contacts_Var = ("carlos.liguori@assuredtechmatics.com", "vendor@vendor.com")




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
#    test_CarrierDrivers_ManagePage_apolloWebPortal.carrierDrivers_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_HomeBases_ManagePage_apolloWebPortal.carrierHomeBases_ChildMenu_ManagePage (driver, driver_Name, driver_Version)
#    test_Assets_ManagePage_apolloWebPortal.carrierAssets_ChildMenu_ManagePage(driver, driver_Name, driver_Version)
#    test_DVIR_ManagePage_apolloWebPortal.DVIR_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)
#    test_DVIR_WorkOrder_ManagePage_apolloWebPortal.DVIR_WorkOrder_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_ManagePage_apolloWebPortal.WorkOrder_ManagePage (driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
#    test_WorkOrder_Flow_apolloWebPortal.WorkOrder_Flow_ManagePage (driverModelTestControl, driver, driver_Name, driver_Version, carrier, truckDriversList, driver_UserName_Var, client_Name_Var, client_Adress_Var, defect_Vehicle_List_Var, workOrder_CreatedBy_Var, workOrder_Contacts_Var)
    teste_NAO_USAR.DVIR_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)

    driver.close()
    driverModelTestControl = driverModelTestControl + 1

dateEnd = datetime.now()
date = dateEnd-dateInit
print()
print(f"Test executing time = {date}")
print()
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  TEST PASSED %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

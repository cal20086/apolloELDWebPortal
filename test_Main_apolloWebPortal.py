#               apollo Web Portal - Test Control page


from selenium import webdriver

import test_CarrierDetails_ManagePage_apolloWebPortal
import test_DVIR_ManagePage_apolloWebPortal
import test_HomePage_apolloWebPortal
import test_Login_apolloWebPortal
import tc_reports
import test_ManagePage_apolloWebPortal

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
                  "Firefox",
                  "Edge",
                  "Opera"]

driverListVersion = ["96.0.4664.45 (Official Build) (64-bit)",
                     "92.0 (64-bit)",
                     "96.0.1054.41 (Official build) (64-bit",
                     "81.0.4196.37 (64-bit)"]

driverDriverListVar = ["C:\\tools\chromedriver.exe",
                       "C:\\tools\geckodriver.exe",
                       "C:\\tools\msedgedriver.exe",
                       "C:\\tools\operadriver.exe"]

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

while driverModelTestControl < 3:



    if driverModelTestControl == 0:
        driver = webdriver.Chrome(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 1:
        driver = webdriver.Firefox(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 2:
        driver = webdriver.Edge(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl == 3:
        driver = webdriver.Opera(executable_path=driverDriverListVar[driverModelTestControl])
    if driverModelTestControl > 3:
        breack(1)

    driver_Name = driverListName[driverModelTestControl]
    driver_Version = driverListVersion[driverModelTestControl]
    user_ApolloWebPortalVar = user_ApolloWebPortalListVar[driverModelTestControl]
    password_ApolloWebPortalVar = password_ApolloWebPortalListVar[driverModelTestControl]

    print(driverModelTestControl)
    print(driver_Name)

# Call Functions:

    test_Login_apolloWebPortal.login_apolloWebPortal(contol_Reportfile, driver, driver_Name, driver_Version, user_ApolloWebPortalVar, password_ApolloWebPortalVar, siteAddressVar, test_Case_Type)
    test_HomePage_apolloWebPortal.homePage(driver, driver_Name, driver_Version)
    test_ManagePage_apolloWebPortal.managePage(driver, driver_Name, driver_Version)
#    test_CarrierDetails_ManagePage_apolloWebPortal.carrierDetail_ChildMenu_ManagePage(driver, driverName, driverVersion)
    test_DVIR_ManagePage_apolloWebPortal.buttonDVIR_ManagePage(driver, driver_Name, driver_Version, carrier, truckDriversList)

    driver.close()
    driverModelTestControl = driverModelTestControl + 1


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  TEST PASSED %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

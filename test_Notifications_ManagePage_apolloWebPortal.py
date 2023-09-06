#               Apollo Web Portal - Manage - Notifications


def carrierNotifications_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

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

#       Notifications Page Address & Variables
#       Fields Address

    button_Notifications_Carrier_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[5]"
    title_Notifications_Carrier_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[1]/h3"
    button_PlussNew_Notification_ManagePageAdr = "/html/body/app-root/app-main/div/div/app-manage/section[2]/div/div[2]/div/notification-list/div/div/div[1]/div/button"

    title_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[1]"
    input_Name_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[1]/input"
    drpBox_Type_Notification_Notifications_ManagePageId = "type"
    input_Emails_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[3]/input"
    input_SearchAssets_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[4]/app-items-table/div/div/dx-data-grid/div/div[4]/div/div/div[3]/div/div/div/div/div[1]/input"
    checkBox_Assets_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[1]/div[4]/app-items-table/div/div/dx-data-grid/div/div[6]/div/table/tbody/tr[1]/td[1]/div/div"
    button_SAVE_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[2]/button[1]"
    button_CLOSE_Notification_Notifications_ManagePageAdr = "/html/body/ngb-modal-window/div/div/notification-modal/div[2]/notification-form/form/div[2]/button[2]"

    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)

    input_Name_Notification_Notifications_ManagePageVar = "Notification Automation Test"
    input_Emails_Notification_Notifications_ManagePageVar = "carlos.liguori@assuredtechmatics.com"
    input_SearchAssets_Notification_Notifications_ManagePageVar = "TRUCKATEST1000001"

    #####################################################################################################################################
    #                                                       NOTIFICATIONS Main functions                                                       #
    #####################################################################################################################################

    button_Notifications_Carrier_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,button_Notifications_Carrier_ManagePageAdr))).click()

  #   Page Title on TCReport
    function_Name = "Carriers NOTIFICATIONS Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    title_Notifications_Carrier_ManagePage = w.until(EC.presence_of_element_located((By.XPATH, title_Notifications_Carrier_ManagePageAdr))).text
    # print(title_Assets_Assets_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Notifictions Page Open"
    condition1 = "Notifications"
    condition2 = title_Notifications_Carrier_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Notifications Page Open"
    print_Information_Var = title_Notifications_Carrier_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Notifications Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #****************************************************
    # Create a New Notification - Notification Child page
    #****************************************************

    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH,button_PlussNew_Notification_ManagePageAdr))).click()

    #   Notification Child Page:
    title_Notification_Notifications_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Notification_Notifications_ManagePageAdr)))).text
    # print(title_Assets_Assets_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Notifiction Page Open"
    condition1 = "Notification"
    condition2 = title_Notification_Notifications_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Notification Page Open"
    print_Information_Var = title_Notification_Notifications_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,
                                driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Notification Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Create a new Notification

    # Name
    input_Name_Notification_Notifications_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,input_Name_Notification_Notifications_ManagePageAdr))))
    input_Name_Notification_Notifications_ManagePage.send_keys(input_Name_Notification_Notifications_ManagePageVar)
    # Type
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,drpBox_Type_Notification_Notifications_ManagePageId))))
    drpBox_Type_Notification_Notifications_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(drpBox_Type_Notification_Notifications_ManagePage_List):
        drpBox_Type_Notification_Notifications_ManagePage_Selected = dropDown.select_by_visible_text(drpBox_Type_Notification_Notifications_ManagePage_List[n])
        drpBox_Type_Notification_Notifications_ManagePage_Read = dropDown.first_selected_option.text
        print(drpBox_Type_Notification_Notifications_ManagePage_Read)
        n = n + 1
    #Emails
    input_Emails_Notification_Notifications_ManagePage = w.until(EC.presence_of_element_located((By.XPATH,input_Emails_Notification_Notifications_ManagePageAdr)))
    input_Emails_Notification_Notifications_ManagePage.send_keys(input_Emails_Notification_Notifications_ManagePageVar)
    #Assets Search
    input_SearchAssets_Notification_Notifications_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,input_SearchAssets_Notification_Notifications_ManagePageAdr))))
    input_SearchAssets_Notification_Notifications_ManagePage.send_keys(input_SearchAssets_Notification_Notifications_ManagePageVar)
    #Check Box Assets
    checkBox_Assets_Notification_Notifications_ManagePage = w.until((EC.element_to_be_clickable((By.XPATH,checkBox_Assets_Notification_Notifications_ManagePageAdr))))
    checkBox_Assets_Notification_Notifications_ManagePage.click()
    #SAVE
    w.until(EC.element_to_be_clickable((By.XPATH,button_SAVE_Notification_Notifications_ManagePageAdr))).click()

    # Search and test the New Notification

    # Edit Notification


    # Delete the Notification



    #   NotificationS Child Page:






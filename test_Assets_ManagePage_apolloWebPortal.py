#               Apollo Web Portal - Manage - Assets


def carrierAssets_ChildMenu_ManagePage (driver, driver_Name, driver_Version):

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

#       Carrier details Page Address & Variables
#       Fields Address

    button_Carrier_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[1]/div/carrier-list/div/div/div[2]/table/tbody/tr/td[3]/div/button[4]"
    title_Assets_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-asset-list/div/div/div[1]/h3"
    button_PlussNew_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-asset-list/div/div/div[1]/div/button"

    title_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[1]/h4"
    button_PlussNew_Asset_Assets_ManagePageAdr = "/html/body/app-root/app-main/div/div[1]/app-manage/section[2]/div/div[2]/div/app-asset-list/div/div/div[1]/div/button"

    dropBox_AssetType_Asset_Assets_ManagePageId = "assetType"
    text_Number_Asset_Assets_ManagePageId = "assetNumber"
    text_VIN_Asset_Assets_ManagePageId = "assetVIN"
    text_Plate_Asset_Assets_ManagePageId = "assetPlate"
    dropBox_RegistrationState_Asset_Assets_ManagePageId = "assetRegState"
    text_Description_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[1]/form/div/div[6]/textarea"
    text_ECMIdentifier_Asset_Assets_ManagePageId = "ecmidentified"
    text_AdditionalECMIdentifier_Asset_Assets_ManagePageId = "addecmidentified"

    checkBox_Active_Asset_Assets_ManagePageId = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[1]/form/div/div[9]/div/input"

    dropBox_FuelTypePrimary_Asset_Assets_ManagePageId = "FuelTypePrimary"
    text_Make_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div[2]/input"
    text_Model_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div[3]/input"
    text_Year_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div[4]/input"
    dropBox_Type_Asset_Assets_ManagePageId = "Type"
    text_BodyClass_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div[6]/input"
    dropBox_GVWR_Asset_Assets_ManagePageId = "GVWR"

    button_SAVE_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[2]/button[1]"
    button_CLOSE_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[2]/button[2]"

    textTractor_Number_Asset_Assets_ManagePageVar = "TRUCK01"
    textTractor_VIN_Asset_Assets_ManagePageVar = "TRUCK000000000001"
    textTractor_Plate_Asset_Assets_ManagePageVar = "TRUCK01"
    textTractor_Description_Asset_Assets_ManagePageVar = "TEST TRUCK 1"
    dropBox_RegistrationState_Asset_Assets_ManagePageVar = "ID"
    textTractor_ECMIdentifier_Asset_Assets_ManagePageVar = "012345678901"
    textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar = "55555"
    textTractor_FuelTypePrimary_Asset_Assets_ManagePageVar = "Biodiesel"
    textTractor_Make_Asset_Assets_ManagePageVar = "Peterbilt"
    textTractor_Model_Asset_Assets_ManagePageVar = "579"
    textTractor_Year_Asset_Assets_ManagePageVar = "2022"
    textTractor_Type_Asset_Assets_ManagePageVar = "TRUCK"
    textTractor_BodyClass_Asset_Assets_ManagePageVar = "Heavy-Duty"
    dropBox_Tractor_GVWR_Asset_Assets_ManagePageVar = "Class 8:33,001 lb and above (14,969 kg and above)"

    textTrailer_Number_Asset_Assets_ManagePageVar = "TRAILER01"
    textTrailer_VIN_Asset_Assets_ManagePageVar = "TRAILER0000000001"
    textTrailer_Plate_Asset_Assets_ManagePageVar = "TRAILER01"
    textTrailer_Description_Asset_Assets_ManagePageVar = "TEST TRAILER 01"


    #       Variables:
    date = datetime.now()
    w = WebDriverWait(driver, 30)

    #####################################################################################################################################
    #                                                       ASSETS Main functions                                                       #
    #####################################################################################################################################

  #   Page Title on TCReport
    function_Name = "Carriers ASSETS Function"
    tc_reports.function_Init_Page(function_Name, driver_Name)

    # Assets Page button
    button_Carrier_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH, button_Carrier_Assets_ManagePageAdr)))
    time.sleep(0.5)
    button_Carrier_Assets_ManagePage.click()

    #   Assets Page Open test:
    title_Assets_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Assets_Assets_ManagePageAdr)))).text
    #print(title_Assets_Assets_ManagePage)
    #       Assert Test and print if assert is fail
    test_Name = "Assets Page Open"
    condition1 = "Assets"
    condition2 = title_Assets_Assets_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Assets Page Open"
    print_Information_Var = title_Assets_Assets_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Assets Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Assets_ManagePageAdr))).click()

    # Test Asset type: Tractor page
    #   Asset Page Open test:
    title_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, title_Asset_Assets_ManagePageAdr)))).text
    #print(title_Asset_Assets_ManagePageAdr)
    #       Assert Test and print if assert is fail
    test_Name = "Asset Page Open"
    condition1 = "Asset"
    condition2 = title_Asset_Assets_ManagePage
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Asset Page Open"
    print_Information_Var = title_Asset_Assets_ManagePage
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
    #       Screenshot
    test_Name = "Asset Page"
    tc_reports.screenshot(driver, driver_Name, test_Name)





    #Test Asset Type
    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_AssetType_Asset_Assets_ManagePageId))))
    dropBox_AssetType_Asset_Assets_ManagePage = dropDown
    dropBox_AssetType_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_AssetType_Asset_Assets_ManagePage_List):
        dropBox_AssetType_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_AssetType_Asset_Assets_ManagePage_List[n])
        dropBox_AssetType_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text

        # **************** Test and report results at TCReport  ******************************************************************************************************************
        #       Assert Test and print if assert is fail
        test_Name = "Asset Type"
        condition1 = dropBox_AssetType_Asset_Assets_ManagePage_List[n]
        condition2 = dropBox_AssetType_Asset_Assets_ManagePage_Read
        tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
        #       Print Assert OK
        print_Information_Fix = "Asset Page - Asset Type element:"
        print_Information_Var = dropBox_AssetType_Asset_Assets_ManagePage_Read
        test_Case_Type = ""
        contol_Reportfile = 1
        tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type,driver_Name, driver_Version)
        n = n + 1
    #       Screenshot
    #tc_reports.screenshot(driver, driver_Name, test_Name)

    #Select Asset Type = Tractor

    dropBox_AssetType_Asset_Assets_ManagePage = dropBox_AssetType_Asset_Assets_ManagePage.select_by_visible_text("Tractor")

    # Test Asset type: Tractor page
    #******************************

    text_Number_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.ID,text_Number_Asset_Assets_ManagePageId)))
    text_Number_Asset_Assets_ManagePage.send_keys(textTractor_Number_Asset_Assets_ManagePageVar)
    text_VIN_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID,text_VIN_Asset_Assets_ManagePageId))))
    text_VIN_Asset_Assets_ManagePage.send_keys(textTractor_VIN_Asset_Assets_ManagePageVar)
    text_Plate_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID,text_Plate_Asset_Assets_ManagePageId))))
    text_Plate_Asset_Assets_ManagePage.send_keys(textTractor_Plate_Asset_Assets_ManagePageVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_RegistrationState_Asset_Assets_ManagePageId))))
    dropDown.select_by_visible_text(dropBox_RegistrationState_Asset_Assets_ManagePageVar)

    text_Description_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_Description_Asset_Assets_ManagePageAdr))))
    text_Description_Asset_Assets_ManagePage.send_keys(textTractor_Description_Asset_Assets_ManagePageVar)

    text_ECMIdentifier_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_ECMIdentifier_Asset_Assets_ManagePageId))))
    text_ECMIdentifier_Asset_Assets_ManagePage.send_keys(textTractor_ECMIdentifier_Asset_Assets_ManagePageVar)

    text_AdditionalECMIdentifier_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_AdditionalECMIdentifier_Asset_Assets_ManagePageId))))
    text_AdditionalECMIdentifier_Asset_Assets_ManagePage.send_keys(textTractor_AdditionalECMIdentifier_Asset_Assets_ManagePageVar)

    #   Scroll to action element - "Fuel Type Primary
    label_FuelTypePrimary_Asset_Assets_ManagePageAdr = "/html/body/ngb-modal-window/div/div/app-asset-form/div[2]/div[1]/div[2]/form/div/div[1]/div/div[1]/label"
    label_FuelTypePrimary_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,label_FuelTypePrimary_Asset_Assets_ManagePageAdr))))
    actions = ActionChains(driver)
    actions.move_to_element(label_FuelTypePrimary_Asset_Assets_ManagePage)
    actions.perform()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropBox_FuelTypePrimary_Asset_Assets_ManagePageId))))
    dropBox_FuelTypePrimary_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_FuelTypePrimary_Asset_Assets_ManagePage_List):
        dropBox_FuelTypePrimary_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_FuelTypePrimary_Asset_Assets_ManagePage_List[n])
        dropBox_FuelTypePrimary_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text
        n = n + 1

    text_Make_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_Make_Asset_Assets_ManagePageAdr))))
    text_Make_Asset_Assets_ManagePage.send_keys(textTractor_Make_Asset_Assets_ManagePageVar)

    text_Make_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_Model_Asset_Assets_ManagePageAdr))))
    text_Make_Asset_Assets_ManagePage.send_keys(textTractor_Model_Asset_Assets_ManagePageVar)

    text_Year_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_Year_Asset_Assets_ManagePageAdr))))
    text_Year_Asset_Assets_ManagePage.send_keys(textTractor_Year_Asset_Assets_ManagePageVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropBox_Type_Asset_Assets_ManagePageId))))
    dropBox_Type_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_Type_Asset_Assets_ManagePage_List):
        dropBox_Type_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_Type_Asset_Assets_ManagePage_List[n])
        dropBox_Type_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text
        n = n + 1

    text_BodyClass_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH,text_BodyClass_Asset_Assets_ManagePageAdr))))
    text_BodyClass_Asset_Assets_ManagePage.send_keys(textTractor_BodyClass_Asset_Assets_ManagePageVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID,dropBox_GVWR_Asset_Assets_ManagePageId))))
    dropBox_GVWR_Asset_Assets_ManagePage_List = [x.text for x in dropDown.options]
    n = 0
    while n < len(dropBox_GVWR_Asset_Assets_ManagePage_List):
        dropBox_GVWR_Asset_Assets_ManagePage_Selected = dropDown.select_by_visible_text(dropBox_GVWR_Asset_Assets_ManagePage_List[n])
        dropBox_GVR_Asset_Assets_ManagePage_Read = dropDown.first_selected_option.text
        n = n + 1
    #dropDown.send_keys(textTractor_GVWR_Asset_Assets_ManagePageVar)


    button_CLOSE_Asset_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH,button_CLOSE_Asset_Assets_ManagePageAdr)))
    button_CLOSE_Asset_Assets_ManagePage.click()



    # Test Asset page -> Trailer Asset
    #*********************************
    #   + New button
    w.until(EC.element_to_be_clickable((By.XPATH, button_PlussNew_Assets_ManagePageAdr))).click()
    dropBox_AssetType_Asset_Assets_ManagePage = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_AssetType_Asset_Assets_ManagePageId))))
    dropBox_AssetType_Asset_Assets_ManagePage.select_by_visible_text("Trailer")

    text_Number_Asset_Assets_ManagePage = w.until(EC.presence_of_element_located((By.ID, text_Number_Asset_Assets_ManagePageId)))
    text_Number_Asset_Assets_ManagePage.send_keys(textTrailer_Number_Asset_Assets_ManagePageVar)
    text_VIN_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_VIN_Asset_Assets_ManagePageId))))
    text_VIN_Asset_Assets_ManagePage.send_keys(textTrailer_VIN_Asset_Assets_ManagePageVar)
    text_Plate_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.ID, text_Plate_Asset_Assets_ManagePageId))))
    text_Plate_Asset_Assets_ManagePage.send_keys(textTrailer_Plate_Asset_Assets_ManagePageVar)

    dropDown = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_RegistrationState_Asset_Assets_ManagePageId))))
    dropDown.select_by_visible_text("ID")

    text_Description_Asset_Assets_ManagePage = w.until((EC.presence_of_element_located((By.XPATH, text_Description_Asset_Assets_ManagePageAdr))))
    text_Description_Asset_Assets_ManagePage.send_keys(textTrailer_Description_Asset_Assets_ManagePageVar)



    button_CLOSE_Asset_Assets_ManagePage = w.until(EC.element_to_be_clickable((By.XPATH,button_CLOSE_Asset_Assets_ManagePageAdr)))
    button_CLOSE_Asset_Assets_ManagePage.click()
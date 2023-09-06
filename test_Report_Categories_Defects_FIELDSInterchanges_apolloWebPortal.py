#               Apollo Web Portal - Report Categories Defects Interchanges fields
import re


def Report_Categories_Defects_Interchanges (driver, driver_Name, driver_Version, dropBox_Report_PageID, dropBox_Categories_PageID, dropBox_Defects_PageID, read_Defects_PageAdr, input_Defects_PageAdr, input_Defects_RemoveAllItems_PageAdr, source_Function):

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
    import glob
    import openpyxl
    from pathlib import Path
    from os import path
    from datetime import datetime, timedelta
    from selenium.common.exceptions import NoSuchElementException
    import test_Global_Variables_apolloWebPortal


#   Address


    #   Global Variables
    workbookDB = test_Global_Variables_apolloWebPortal.workbookDB_Global
    worksheetDB = test_Global_Variables_apolloWebPortal.worksheetDB_Global

    # Local variables
    w = WebDriverWait(driver, 10)
    excel_DB_line = 4
    excel_DB_line_LogicTest = 2
    colum_Report_ID = "D"
    colum_Report_Name = "E"
    colum_Categories_ID = "F"
    colum_Categories_Name = "G"
    colum_Defects_ID = "H"
    colum_Defects_Name = "I"
    colum_Parent_ID = "J"
    colum_ReportType = "P"
    colum_CategoryByReportType = "Q"
    colum_CategoryOptions = "R"
    colum_DefectByReportDVIRType = "S"
    colum_DefectByReportWOType = "T"
    colum_reportConditionsTestQte = "U"
    colum_ReportbyCategorieDVIRType = "V"
    colum_ReportbyCategorieWOType = "W"
    colum_CategoryType = "X"
    colum_DefectByCategoryType = "Y"
    colum_CategoryDefectTestQte = "Z"


#                   MAIN                **********************************

    #   Page Title on TCReport
    function_Name = "Test REPORT, CATEGORIES and DEFECTS fields from " + source_Function
    tc_reports.function_Init_Page(function_Name, driver_Name)

    #       Screenshot
    test_Name = "R,C,D Filters Logic"
    tc_reports.screenshot(driver, driver_Name, test_Name)

    # Report x Categories X Defects Test

    #   Read excel
    excell_pointer = Path(workbookDB)
    # Read excel value not formula
    workbookDB_Read = openpyxl.load_workbook(excell_pointer, data_only=True)
    worksheetDB_Read = workbookDB_Read.active

    excel_ReportsTypes_cellValue = worksheetDB_Read['A2'].value
    excel_CategoriesTypes_cellValue = worksheetDB_Read['B2'].value
    excel_DefectsTypes_cellValue = worksheetDB_Read['C2'].value
    if source_Function == "WorkOrder":
        excel_ReportsTypes_cellValue = excel_ReportsTypes_cellValue - 1
        excel_CategoriesTypes_cellValue =  excel_CategoriesTypes_cellValue - 1

    #   Check the options/quantities per list based on the excel
    # Report
    dropBox_Report_Page = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Report_PageID))))
    dropBox_Report_MoreFilter_List = [x.text for x in dropBox_Report_Page.options]
    # Assert
    test_Name = "Report Items numbers"
    condition1 = str(len(dropBox_Report_MoreFilter_List))
    condition2 = str(excel_ReportsTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Report options available: "
    print_Information_Var = str(len(dropBox_Report_MoreFilter_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Check The Categories quantities
    dropBox_Categories_Page = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Categories_PageID))))
    dropBox_Categories_MoreFilter_List = [x.text for x in dropBox_Categories_Page.options]
    # Assert
    test_Name = "Categories Items numbers"
    condition1 = str(len(dropBox_Categories_MoreFilter_List))
    condition2 = str(excel_CategoriesTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Categories options available: "
    print_Information_Var = str(len(dropBox_Categories_MoreFilter_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    # Test selecting Report verify the other field
    #   Test    ReportIdDesc	    CategoryIdDesc	    Category Qte.	DefectIdDesc
    #   1       --None--	            --None--	        6	        --None--
    #   2       All	                    All	                5	        All
    #   3       United States	        All	                3
    #   4       Canada Schedule 1	    General	            1
    #   5       List 1 - Heavy vehicle	General	            1
    #   6       List 2 - Bus	        General	            1
    #   7       List 3 - Motor Coach	General	            1
    #   8       Crane	                Crane	            1
    # 	9                               Tractor
    # 	10                              Trailer

    reportConditionsTest = (str(colum_reportConditionsTestQte) + str("2"))
    reportConditionsTestQte = worksheetDB_Read[reportConditionsTest].value

    # Test LOGIC based on REPORT options and verify Categories and Defects
    try:
        n = 1
        x = excel_DB_line_LogicTest
        if source_Function == "WorkOrder":
            x = x + 1
            reportConditionsTestQte = reportConditionsTestQte - 1

        while n <= reportConditionsTestQte:
            report_Type_excel = (str(colum_ReportType) + str(x))
            report_excel = worksheetDB_Read[report_Type_excel].value
            dropBox_Report_Page.select_by_visible_text(report_excel)
            #print(f'Report excel = {report_excel}')
            report_Read = dropBox_Report_Page.first_selected_option.text
            # Assert
            test_Name = "Report selected - Logic Interrelated "
            condition1 = str(report_excel)
            condition2 = str(report_Read)
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

            #   Check The Categories quantities for the selected Report
            categoriebyReport_Type_excel = (str(colum_CategoryOptions) + str(x))
            categorie_excel = worksheetDB_Read[categoriebyReport_Type_excel].value
            dropBox_Categories_Page = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Categories_PageID))))
            dropBox_Categories_MoreFilter_List = [x.text for x in dropBox_Categories_Page.options]
            # Assert
            test_Name = "Categories Items numbers"
            condition1 = str(categorie_excel)
            condition2 = str(len(dropBox_Categories_MoreFilter_List))
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

        #   Read Categorie after selecting Report and compare with Excel expected value
            categoriebyReport_Type_excel = (str(colum_CategoryByReportType) + str(x))
            categorie_excel = worksheetDB_Read[categoriebyReport_Type_excel].value
            categorie_Read = dropBox_Categories_Page.first_selected_option.text
            #print(f'Categories Excel = {categorie_excel}')
            # Assert
            test_Name = "Categories read auto-selected - Logic Interrelated "
            condition1 = str(categorie_excel)
            condition2 = str(categorie_Read)
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

            #   Read Defect after selecting Report and compare with Excel expected value


            if source_Function == "WorkOrder":
                defectbyReport_Type_excel = (str(colum_DefectByReportWOType) + str(x))
                defect_excel = worksheetDB_Read[defectbyReport_Type_excel].value
                print(defect_excel)
                if defect_excel == 1:
                    defect_excel = ""
            else:
                defectbyReport_Type_excel = (str(colum_DefectByReportDVIRType) + str(x))
                defect_excel = worksheetDB_Read[defectbyReport_Type_excel].value

            input_Defects_Page = w.until(EC.presence_of_element_located((By.XPATH, read_Defects_PageAdr)))
            input_Defects_Page_Read = str(input_Defects_Page.text)
            #input_Defects_Page_Read.replace(" ", "")
            input_Defects_Page_Read = input_Defects_Page_Read.replace("×", "")
            input_Defects_Page_Read = input_Defects_Page_Read.replace('\n', "")
            input_Defects_Page_Read = input_Defects_Page_Read.replace(" ", "")
            # Assert
            test_Name = "Defect read auto-selected - Logic Interrelated "
            condition1 = str(defect_excel)
            condition2 = str(input_Defects_Page_Read)
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
            #       Print Assert OK
            print_Information_Fix = "Report selected -> Categories & Defect auto-selected - Logic Interrelated "
            print_Information_Var = report_Read + " / " + categorie_Read + " / " + input_Defects_Page_Read + " => # Categories available = " + str(len(dropBox_Categories_MoreFilter_List))
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)
            x = x + 1
            n = n + 1
    except:
        print("ERROR - Report, Categories and Defects LOGIC TESTE - Excel colum P,Q,R,S,T")

        #       Screenshot
        test_Name = "Report selected"
        tc_reports.screenshot(driver, driver_Name, test_Name)

    categoriesConditionsTest = (str(colum_CategoryDefectTestQte) + str("2"))
    categoriesConditionsTestQte = worksheetDB_Read[categoriesConditionsTest].value

    # Test LOGIC based on CATEGORIES options and verify Report and Defects
    try:
        n = 1
        x = excel_DB_line_LogicTest
        if source_Function == "WorkOrder":
            x = x + 1
            categoriesConditionsTestQte = categoriesConditionsTestQte - 1

        while n <= categoriesConditionsTestQte:
            #Reset all field to "--None--"
            if source_Function == "WorkOrder":
                dropBox_Report_Page.select_by_visible_text("All")
            else:
                dropBox_Report_Page.select_by_visible_text("--None--")
            #Reset Defect to "Engine"
            defects = w.until(EC.presence_of_element_located((By.XPATH, input_Defects_PageAdr)))
            defects.send_keys("Engine")
            defects.send_keys(Keys.RETURN)

            # Set Categories
            categorie_Type_excel = (str(colum_CategoryType) + str(x))
            categorie_excel = worksheetDB_Read[categorie_Type_excel].value
            dropBox_Categories_Page.select_by_visible_text(categorie_excel)
            time.sleep(0.3)
            categorie_Read = dropBox_Categories_Page.first_selected_option.text
            # print(f'Categories Excel = {categorie_excel}')
            # Assert
            test_Name = "Categories auto-selected - Logic Interrelated "
            condition1 = str(categorie_excel)
            condition2 = str(categorie_Read)
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

            # Read Report
            if source_Function == "WorkOrder":
                report_Type_excel = (str(colum_ReportbyCategorieWOType) + str(x))
            else:
                report_Type_excel = (str(colum_ReportbyCategorieDVIRType) + str(x))

            report_excel = worksheetDB_Read[report_Type_excel].value
            report_Read = dropBox_Report_Page.first_selected_option.text
            # Assert
            test_Name = "Report selected - Logic Interrelated "
            condition1 = str(report_excel)
            condition2 = str(report_Read)
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

            #   Read Defect after selecting Report and compare with Excel expected value


            if source_Function == "WorkOrder":
                defectbyReport_Type_excel = (str(colum_DefectByReportWOType) + str(x))
                defect_excel = worksheetDB_Read[defectbyReport_Type_excel].value
                if defect_excel == 1:
                    defect_excel = ""
            else:
                defectbyReport_Type_excel = (str(colum_DefectByReportDVIRType) + str(x))
                defect_excel = worksheetDB_Read[defectbyReport_Type_excel].value

            #print(f'Defect excel = {defect_Read_excel}')
            time.sleep(0.25)
            input_Defects_Page = w.until(EC.presence_of_element_located((By.XPATH, read_Defects_PageAdr)))
            input_Defects_Page_Read = str(input_Defects_Page.text)
            #input_Defects_Page_Read.replace(" ", "")
            input_Defects_Page_Read = input_Defects_Page_Read.replace("×", "")
            input_Defects_Page_Read = input_Defects_Page_Read.replace('\n', "")
            input_Defects_Page_Read = input_Defects_Page_Read.replace(" ", "")
            # Assert
            test_Name = "Defect auto-selected - Logic Interrelated "
            condition1 = str(defect_excel)
            condition2 = str(input_Defects_Page_Read)
            tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)

            #       Print Assert OK
            print_Information_Fix = "Categories selected -> Report & Defect auto-selected - Logic Interrelated "
            print_Information_Var = categorie_Read + " / " + report_Read + " / " + input_Defects_Page_Read
            test_Case_Type = ""
            contol_Reportfile = 1
            tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

            #Reset categorie and Defect fields to --None--
            if source_Function == "WorkOrder":
                dropBox_Categories_Page.select_by_visible_text("All")
            else:
                dropBox_Categories_Page.select_by_visible_text("--None--")
            x = x + 1
            n = n + 1
    except:
        print("ERROR - Categories set -> Report and Defect auto set")

    #       Screenshot
    test_Name = "Categories selected"
    tc_reports.screenshot(driver, driver_Name, test_Name)


    #       input list field read from Excel

    #   Check The Report quantities
    dropBox_Report_Page = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Report_PageID))))
    dropBox_Report_MoreFilter_List = [x.text for x in dropBox_Report_Page.options]
    # Assert
    test_Name = "Report Items numbers"
    condition1 = str(len(dropBox_Report_MoreFilter_List))
    condition2 = str(excel_ReportsTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Report options available: "
    print_Information_Var = str(len(dropBox_Report_MoreFilter_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)

    #   Check The Categories quantities
    dropBox_Categories_Page = Select(w.until(EC.presence_of_element_located((By.ID, dropBox_Categories_PageID))))
    dropBox_Categories_MoreFilter_List = [x.text for x in dropBox_Categories_Page.options]
    # Assert
    test_Name = "Categories Items numbers"
    condition1 = str(len(dropBox_Categories_MoreFilter_List))
    condition2 = str(excel_CategoriesTypes_cellValue)
    tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
    #       Print Assert OK
    print_Information_Fix = "Categories options available: "
    print_Information_Var = str(len(dropBox_Categories_MoreFilter_List))
    test_Case_Type = ""
    contol_Reportfile = 1
    tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version)


    # for combiation Report/Categories/DefectsVar in range(len(excel_DefectsTypes_cellValue))
    # Positive Test based on the EXCEL DB
    try:
        n = 1
        # for list_control_Report in range(len(dropBox_Report_MoreFilter_WorkOrder_List)):
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

    # Only Parent Defect can be selected (ParentId = 0) !!!!!!!!!!!!
            if cell_Parent_ID_Value == 0:
                dropBox_Report_Page.select_by_visible_text(cell_Report_Name_Value)
                dropBox_Item_Report_Page_Read = dropBox_Report_Page.first_selected_option.text
                dropBox_Categories_Page.select_by_visible_text(cell_Categories_Name_Value)
                dropBox_Item_Categories_Page_Read = dropBox_Categories_Page.first_selected_option.text
                defects = w.until(EC.presence_of_element_located((By.XPATH, input_Defects_PageAdr)))
                defects.send_keys(cell_Defects_Name_Value)
                defects.send_keys(Keys.RETURN)

                #       input list field read
                time.sleep(0.25)
                input_Defects_Page = w.until(EC.presence_of_element_located((By.XPATH, read_Defects_PageAdr)))
                input_Defects_Page_Read = input_Defects_Page.text

                #       input list field read
                #       Assert
                test_Name = "Defect items"
                condition1 = cell_Defects_Name_Value
                condition2 = input_Defects_Page_Read
                #                print(f'Excell data = {condition1}')
                #                print(f'Field Read = {condition2}')
                tc_reports.assert_test_reportfile(test_Name, condition1, condition2, driver, driver_Name)
                #       Print Assert OK
                print_Information_Fix = "WorkOrder Page - Defect items field:"
                reportCategoriesDefect = dropBox_Item_Report_Page_Read + " / " + dropBox_Item_Categories_Page_Read + " / " + cell_Defects_Name_Value
                print_Information_Var = reportCategoriesDefect
                test_Case_Type = ""
                contol_Reportfile = 1
                tc_reports.write_reportfile(contol_Reportfile, print_Information_Fix, print_Information_Var,test_Case_Type, driver_Name, driver_Version)
                w.until(EC.element_to_be_clickable((By.XPATH, input_Defects_RemoveAllItems_PageAdr))).click()
            n = n + 1
            excel_DB_line = excel_DB_line + 1

    except:
        print('!!!!!!!!!!!!!!!!! error !!!!!!!!!!!!!!!!!!!!')
    print(f'Total Report/Categories/Defects combination tested = {n}')

    return ()



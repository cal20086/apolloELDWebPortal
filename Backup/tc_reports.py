# Reports and tests for test_Create_Order
from datetime import datetime
import os
#from docx import Document
#from docx.shared import RGBColor



# string = informacao a ser gravada
# n = numero da gravacao, se for n=1 deve colocar o cabecalho
# Print paramenters:
#       Test case name
#       Test case type
#       Browser type
#       control_reportfile = print controler
#          control_reportfile = 0 => print Header
#          control_reportfile = 1 => no print Header
#          control_reportfile = others => ERROR message

screenshot_sequence = 0
assert_Condition = 0


def write_reportfile (control_Reportfile, print_Information_Fix, print_Information_Var, test_Case_Type, driver_Name, driver_Version):

    global assert_Condition
    reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"
    TCReport1 = "TCReport"
    TCReport2 = driver_Name
    TCReport3 = ".doc"
    TCReportName = reportFolder_Path_QAReports + TCReport2 + "_" + TCReport1 + TCReport3
    test_Case_Name = "TC_apolloWebPortal_"+driver_Name


    # Verify and/or create a directory to store apollo web portal QA reports
    if os.path.exists(reportFolder_Path_QAReports):
        a = 0
    else:
        os.makedirs(reportFolder_Path_QAReports)


    if control_Reportfile == 0:
        # 'w' = Open a text to file in Python
        TCReport = open(TCReportName, 'w')
        date = datetime.now()
        print('*************************************************************************', file=TCReport)
        print('*************************************************************************', file=TCReport)
        print('*                           Test Case report                            *', file=TCReport)
        print('*************************************************************************\n', file=TCReport)
        print(f'Test Case Date:         {date}\n', file=TCReport)
        print(f'Test Case Name:         {test_Case_Name}\n', file=TCReport)
        print(f'Test Case type:         {test_Case_Type}\n', file=TCReport)
        print(f'Browser:                {driver_Name}\n', file=TCReport)
        print(f'Browser Version:        {driver_Version}\n', file=TCReport)
        print('*************************************************************************', file=TCReport)
        print('*************************************************************************\n', file=TCReport)
        print('\n', file=TCReport)
        TCReport.close()

    else:
        TCReport = open(TCReportName, 'a')
        if control_Reportfile == 1:
            if assert_Condition == 0:
                # 'a' = Append a text to file in Python
                print(f'* Test PASSED: {print_Information_Fix}: {print_Information_Var}\n', file=TCReport)
            else:
                assert_Condition = 0
        else:
            print("ERRO reportfile n controll")
            print('-------------------------------------------------------------------------\n', file=TCReport)
    TCReport.close()

def assert_test_reportfile (test_Name, condition1, condition2, driver, driver_Name):

    global assert_Condition
    reportFolder_Path_QAReports = "C:/Users/QAReport apollo Web Portal/"
    try:
        assert condition1 in condition2
    except:

        reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"
        TCReport1 = "TCReport"
        TCReport2 = driver_Name
        TCReport3 = ".doc"
        TCReportName = reportFolder_Path_QAReports + TCReport2 + "_" + TCReport1 + TCReport3
        TCReport = open(TCReportName, 'a')
        print('', file=TCReport)
        print(f'Driver: {driver_Name} \n', file=TCReport)
        print(f' *** Test FAILED ***:  ERROR !!!   => {test_Name}   Condition 1 = {condition1} :   Condition 2 = {condition2}  \n', file=TCReport)
        print('-------------------------------------------------------------------------\n', file=TCReport)
        print('', file=TCReport)
        TCReport.close()
        driver_Name_str = str(driver_Name)
        driver_Name = "Fail" + driver_Name_str
        screenshot (driver, driver_Name, test_Name)
        assert_Condition = 1


def function_Init_Page(function_Name, driver_Name):
    # Create a header for each function tested

    reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"
    TCReport1 = "TCReport"
    TCReport2 = driver_Name
    TCReport3 = ".doc"
    TCReportName = reportFolder_Path_QAReports + TCReport2 + "_" + TCReport1 + TCReport3
    TCReport = open(TCReportName, 'a')
    print('', file=TCReport)
    print('*************************************************************************', file=TCReport)
    print(f'{function_Name}', file=TCReport)
    print('*************************************************************************\n', file=TCReport)
    print('', file=TCReport)

def screenshot (driver, driver_Name, test_Name):
    reportFolder_Path_QAReports = "C:/apollo QA Reports/apollo Web Portal/"
    filetype = '.png'
    screenshot_name = test_Name.replace(" ","")
    screenshot_name = reportFolder_Path_QAReports + driver_Name + "_" + screenshot_name + filetype
    driver.save_screenshot(screenshot_name)












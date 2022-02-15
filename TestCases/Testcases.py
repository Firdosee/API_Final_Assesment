import time

import openpyxl
from openpyxl.styles import Alignment

from Application.Task import Test_API_Task
from Application.User import Test_API_User
from Data_Config.Excel import Excel_Data
from TestCases.Base_Logger import abc_test_Base


def test_Create_user():
    log = abc_test_Base.getLogger()
    tes = Test_API_User()
    tes.register_a_user("Register")
    token = tes.log_in("Login")
    user = tes.get_logged_in_user_viatoken(token)
    e1 = Excel_Data()
    data_dict_1 = e1.getAPIData("Login")
    user_from_excel = data_dict_1["name"]
    assert user == user_from_excel
    print(user)
    print(user_from_excel)
    log.info("User is successfully validated")
    tes2 = Test_API_Task()
    tes2.add_task(token)


def test_backup_tasks():
    log = abc_test_Base.getLogger()
    tes = Test_API_User()
    token = tes.log_in("Login")
    tes2 = Test_API_Task()
    # tes2.add_task(token)
    # tes2.add_additional_task(token, "cooking classes")
    id = tes2.get_task(token)
    log.info(id)
    log.info(type(id))
    id = id['data']
    id = id[0]
    id = str(id)
    log.info(id)
    log.info("Taking the backup...")
    wb = openpyxl.load_workbook('../Backup_Data.xlsx')
    sheet = wb.active
    sheet['A1'] = id
    wb.save('../Backup_Data.xlsx')
    log.info("Backup is successfully taken into excel.")


def test_twenty_tasks():
    log = abc_test_Base.getLogger()
    tes = Test_API_User()
    tes.register_a_user("Adding_20_tasks")
    token = tes.log_in("Adding_20_tasks")
    tes2 = Test_API_Task()
    e1 = Excel_Data()
    task_dict = e1.gettaskData("Add20Tasks")
    count = 1
    for key in task_dict:
        try:
            log.info("inside for loop")
            print(key, 'corresponds to', task_dict[key])
            tes2.add_additional_task(token, task_dict[key])
            if (count == 3) or (count == 5) or (count == 7):
                log.info("inside pagination")
                tes2.get_task_pagination(token)
            count = count + 1
            log.info(count)
        except Exception as e:
            log.info("Exception occurred")
            log.error(e)
    id = tes2.get_task(token)
    log.info(type(id))
    id = str(id)
    log.info(id)
    id = id.split("count", 1)[1]
    id = id.split("data", 1)[0]
    log.info("id extracted is....")
    log.info(id)
    s = ''.join(x for x in id if x.isdigit())
    print(int(s))
    s = int(s)
    try:
        assert 20 == s
        log.info("All 20 tasks are added successfully")
    except Exception as e:
        log.info("Exception occurred")
        log.error(e)
        assert False

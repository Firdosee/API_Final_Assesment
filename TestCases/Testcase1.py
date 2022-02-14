import openpyxl
from openpyxl.styles import Alignment

from Application.Task import Test_API_Task
from Application.User import Test_API_User
from Data_Config.Excel import Excel_Data
from TestCases.Base_Logger import abc_test_Base


def test_Create_user():
    tes = Test_API_User()
    tes.register_a_user()
    token = tes.log_in()
    tes2 = Test_API_Task()
    tes2.add_task(token)


def test_backup_tasks():
    log = abc_test_Base.getLogger()
    tes = Test_API_User()
    token = tes.log_in()
    tes2 = Test_API_Task()
    # tes2.add_task(token)
    tes2.add_additional_task(token, "cooking classes")
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
    wb = openpyxl.load_workbook('../Backup_Data.xlsx')
    sheet = wb.active
    sheet['A1'] = id
    wb.save('../Backup_Data.xlsx')


def test_twenty_tasks():
    log = abc_test_Base.getLogger()
    tes = Test_API_User()
    token = tes.log_in()
    tes2 = Test_API_Task()
    e1 = Excel_Data()
    task_dict = e1.gettaskData("Add20Tasks")
    for key in task_dict:
        try:
            print(key, 'corresponds to', task_dict[key])
            tes2.add_additional_task(token, task_dict[key])
        except Exception as e:
            log.info("Exception occured")
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


def test_1():
    my_string = "hello python world , i'm a beginner "
    print(my_string.split("world", 1)[0])

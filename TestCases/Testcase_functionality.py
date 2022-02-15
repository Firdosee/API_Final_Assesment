import time

import openpyxl
from openpyxl.styles import Alignment

from Application.Task import Test_API_Task
from Application.User import Test_API_User
from Data_Config.Excel import Excel_Data
from TestCases.Base_Logger import abc_test_Base

log = abc_test_Base.getLogger()
tes = Test_API_User()
tes2 = Test_API_Task()


def test_register_functionality():
    global tes
    tes.register_a_user("Register_f")


def test_login_functionality():
    global tes
    tes.log_in("Login_f")


def test_logout_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.log_out(token)


def test_get_logged_in_user_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)


def test_update_profile_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes.update_user(token)


def test_upload_img_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes.upload_image(token)


def test_delete_user_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes.delete_user(token)


def test_add_task_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes2.add_task(token)


def test_get_all_task_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes2.add_task(token)
    d = tes2.get_task(token)
    d = d['data']
    d = d[0]
    d = str(d)
    log.info(d)


def test_get_taskid_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    d = tes2.get_task(token)
    d = d['data']
    d = d[0]
    log.info(d)
    task_id_1 = d['_id']
    log.info(task_id_1)


def test_task_pagination_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes2.get_task_pagination(token)


def test_task_update_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    d = tes2.get_task(token)
    d = d['data']
    d = d[0]
    log.info(d)
    task_id = d['_id']
    tes2.update_task_id(token, task_id)


def test_completed_task_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    tes2.get_completed_task(token)


def test_delete_task_functionality():
    global tes
    token = tes.log_in("Login_f")
    tes.get_logged_in_user_viatoken(token)
    d = tes2.get_task(token)
    d = d['data']
    d = d[0]
    log.info(d)
    task_id = d['_id']
    tes2.del_task_id(token, task_id)

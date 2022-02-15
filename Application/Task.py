import json

import requests

from Application.User import Test_API_User
from Data_Config.Excel import Excel_Data
from TestCases.Base_Logger import abc_test_Base

log = abc_test_Base.getLogger()


class Test_API_Task:
    def add_task(self, bearer):
        try:
            log = abc_test_Base.getLogger()
            # t1 = Test_API_User()
            # t1.register_a_user()
            # bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/task'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Getting data for add task payload")
            task_dict = e1.getAPIData("Addtask")
            task_1 = task_dict['description']
            payload = {
                "description": "" + task_1 + ""
            }
            log.info("Add task payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            assert code == 201, "Invalid status"
            log.info("Task creation is done Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def add_additional_task(self, bearer, task):
        try:
            global log
            # t1 = Test_API_User()
            # t1.register_a_user()
            # bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/task'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            # e1 = Excel_Data()
            log.info("Getting data for add task payload")
            # task_dict = e1.getAPIData("Addtask")
            # task_1 = task_dict['description']
            task_1 = task
            payload = {
                "description": "" + task_1 + ""
            }
            log.info("Add task payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            assert code == 201, "Invalid status"
            log.info("Task creation is done Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_task(self, bearer):
        try:
            log = abc_test_Base.getLogger()
            # t1 = Test_API_User()
            # bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/task'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Getting data for get_task payload")
            task_dict = e1.getAPIData("Addtask")
            task_1 = task_dict['description']
            payload = {
                "description": "" + task_1 + ""
            }
            log.info("Getting list of tasks...")
            log.info(payload)
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data_1 = resp.json()
            log.info("Getting json response..")
            log.info(data_1)
            id = data_1['data']
            id = id[0]
            # task_id_1 = id['_id']
            # log.info(task_id_1)
            assert code == 200, "Invalid status"
            log.info("Task id's are successfully obtained")
            # return task_1
            return data_1
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_completed_task(self,bearer):
        try:
            log = abc_test_Base.getLogger()
            #t1 = Test_API_User()
            #bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/task?completed=true'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Getting list of completed  tasks...")
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data_1 = resp.json()
            log.info("Getting json response..")
            log.info(data_1)
            try:
                id = data_1['data']
                id = id[0]
                task_id_1 = id['_id']
                log.info(task_id_1)
            except Exception as e:
                log.info("No completed tasks exists")
            assert code == 200, "Invalid status"
            log.info("Completed Tasks are successfully obtained")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_incompleted_task(self):
        try:
            log = abc_test_Base.getLogger()
            t1 = Test_API_User()
            bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/task?completed=false'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Getting list of completed  tasks...")
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data_1 = resp.json()
            log.info("Getting json response..")
            log.info(data_1)
            try:
                id = data_1['data']
                id = id[0]
                task_id_1 = id['_id']
                log.info(task_id_1)
            except Exception as e:
                log.info("No completed tasks exists")
            assert code == 200, "Invalid status"
            log.info("Completed Tasks are successfully obtained")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_task_pagination(self, bearer):
        try:
            global log
            # t1 = Test_API_User()
            # bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/task?'
            e1 = Excel_Data()
            log.info("Getting Pagination details....")
            task_dict = e1.getAPIData("Pagination")
            lim = str(task_dict['limit'])
            sk = str(task_dict['skip'])
            param = {"limit": "" + lim + "", "skip": "" + sk + ""}
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            resp = requests.get(url, params=param, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data_1 = resp.json()
            log.info("Getting json response..")
            log.info(data_1)

            assert code == 200, "Invalid status"
            log.info("Pagination is completed")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def update_task_id(self,bearer, taskid):
        try:

            #bearer = t1.log_in()
            log.info(bearer)
            baseUrl = 'https://api-nodejs-todolist.herokuapp.com'
            url = baseUrl + "/task/" + taskid
            e1 = Excel_Data()
            log.info("Updating task id  details....")
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            payload = {
                "completed": True
            }
            resp = requests.put(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data_1 = resp.json()
            log.info("Getting json response..")
            log.info(data_1)
            assert code == 200, "Invalid status"
            log.info("Task updation is completed")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def del_task_id(self,bearer, taskid):
        try:
            log = abc_test_Base.getLogger()
            #t1 = Test_API_User()
            #bearer = t1.log_in()
            log.info(bearer)
            baseUrl = 'https://api-nodejs-todolist.herokuapp.com'
            url = baseUrl + "/task/" + taskid
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            log.info("Deleting task....")
            resp = requests.delete(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data_1 = resp.json()
            log.info("Getting json response..")
            log.info(data_1)
            assert code == 200, "Invalid status"
            log.info("Task deletion is completed")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

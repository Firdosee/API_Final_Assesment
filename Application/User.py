import json

import requests

from Data_Config.Excel import Excel_Data
from TestCases.Base_Logger import abc_test_Base


class Test_API_User:

    def register_a_user(self):
        try:
            log = abc_test_Base.getLogger()
            url = 'https://api-nodejs-todolist.herokuapp.com/user/register'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("Getting data for registration payload")
            register_dict = e1.getAPIData("Register")
            name = str(register_dict['name'])
            email = str(register_dict['email'])
            password = str(register_dict['password'])
            age = int(register_dict['age'])
            payload = {
                "name": "" + name + "",
                "email": "" + email + "",
                "password": "" + password + "",
                "age": age
            }
            log.info("Registration payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            assert code == 201, "Invalid status"
            log.info("Registration is done Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def log_in(self):
        try:
            log = abc_test_Base.getLogger()
            # t1 = Test_API_User()
            # t1.register_a_user()
            url = 'https://api-nodejs-todolist.herokuapp.com/user/login'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("Getting data for Login payload")
            login_dict = e1.getAPIData("Login")
            email = str(login_dict['email'])
            password = str(login_dict['password'])
            payload = {
                "email": "" + email + "",
                "password": "" + password + ""
            }
            log.info("Login payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            print("fetching bearer token")
            bearer_token = data['token']
            print(bearer_token)
            log.info("The bearer_token is mentioned above")
            assert code == 200, "Invalid status"
            log.info("User is logged in Successfully")
            return bearer_token
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def log_out(self, bearer):
        try:
            t1 = Test_API_User()
            # bearer = t1.log_in()
            log = abc_test_Base.getLogger()
            log.info("User is about to logout...")
            url = 'https://api-nodejs-todolist.herokuapp.com/user/logout'
            headers2 = {
                'Authorization': 'Bearer ' + bearer
            }
            resp = requests.post(url, headers=headers2)
            code = resp.status_code
            print(code)
            log.info(code)
            assert code == 200, "Invalid status"
            log.info("User is logged out Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_logged_in_user_viatoken(self, bearer):
        try:
            log = abc_test_Base.getLogger()
            # t1 = Test_API_User()
            # bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/user/me'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            log.info(bearer)
            log.info("The bearer_token is mentioned above")
            data = resp.json()
            print("User information is obtained and mentioned below...")
            username = str(data['name'])
            assert code == 200, "Invalid status"
            log.info("logged in Successfully obtained via get user by token and is user is mentioned below...")
            log.info(username)

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def update_user(self, bearer):
        try:
            log = abc_test_Base.getLogger()
            # t1 = Test_API_User()
            # bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/user/me'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Getting data for updating payload")
            login_dict = e1.getAPIData("Update")
            age = int(login_dict['age'])
            payload = {
                "age": age
            }

            response = requests.post(url, data=payload, headers=headers)
            resp = requests.get(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            log.info(code)
            assert code == 200, "Invalid status"
            log.info("User details are updated Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def upload_image(self,bearer):
        try:
            log = abc_test_Base.getLogger()
            #t1 = Test_API_User()
            #bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/user/me/avatar'
            headers = {'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Getting file for upload")

            files = [
                ('avatar', (
                    'smileyy.png', open('../smileyy.png',
                                       'rb'), 'image/png'))
            ]
            resp = requests.post(url, headers=headers, files=files)
            etag = resp.headers.get("ETag")
            log.info("etag")
            log.info(etag)
            code = resp.status_code
            log.info(code)
            assert code == 200, "Invalid status"
            log.info("Image is uploaded Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_upload_image(self):
        try:
            log = abc_test_Base.getLogger()
            #t1 = Test_API_User()
            #bearer = t1.log_in()
            #headers = {'Authorization': 'Bearer ' + bearer}
            files = [
                ('avatar', (
                    'smileyy.png', open('../smileyy.png',
                                        'rb'), 'image/png'))
            ]
            url = 'https://api-nodejs-todolist.herokuapp.com/user/5ddccbec6b55da001759722c/avatar'
            Picture_request = requests.get(url)
            log.info(Picture_request.status_code)
            if Picture_request.status_code == 200:
                log.info("Inside forloop")
                with open("Users/firdi/Downloads/image.png", 'wb') as f:
                    f.write(Picture_request.content)
            log.info("Getting uploaded file from api...")
            log.info("Image is obtained Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def del_img(self):
        try:
            log = abc_test_Base.getLogger()
            #t1 = Test_API_User()
            #bearer = t1.log_in()
            #headers = {'Authorization': 'Bearer ' + bearer}
            files = [
                ('avatar', (
                    'smileyy.png', open('../smileyy.png',
                                        'rb'), 'image/png'))
            ]
            payload = {}
            url = 'https://api-nodejs-todolist.herokuapp.com/user/me/avatar'

            #headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            resp= requests.delete(url, data=json.dumps(files))
            #resp = requests.get(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            log.info(code)
            assert code == 200, "Invalid status"
            log.info("User details are updated Successfully")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def delete_user(self,bearer):
        try:
            log = abc_test_Base.getLogger()
            #t1 = Test_API_User()
            #bearer = t1.log_in()
            url = 'https://api-nodejs-todolist.herokuapp.com/user/me'
            headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + bearer}
            e1 = Excel_Data()
            log.info("Deleting user...")
            resp = requests.delete(url, headers=headers)
            code = resp.status_code
            log.info(code)
            assert code == 200, "Invalid status"
            log.info("User is deleted Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False





'''
Author : Suman Suddala
Created Date : 12-Feb-2021
Purpose : To Automate API calls using python
Last Modified Date: 15-Feb-2021
'''

# Import statements
import requests
import sys
sys.path.append('..')
from utils import read_excel
from utils import generate_report
from utils import generate_apikey
import datetime
import logging

# Validates the HTTP status code and to validate whether expected response parameters available in the response
def validate(expected_statuscode,validate_params,response):
    # Validates HTTP Status code
    if response.status_code == expected_statuscode:
        result = "PASS"
    else:
        result = 'FAIL'
        return result
    reponsedata = response.json() # Converts response to json format
    # Reads all the expected response parameters and check if the parameters existed in response
    for params in validate_params.split(';'):
        if str(reponsedata).find(params) ==-1: # Checks if the expected parameter is not part of response
            result = 'FAIL'
            print (params, ' not existed in response')
            return result
    return result

def run():
    # Creates a log file to writes logs for each run
    logging.basicConfig(filename="../logs/alphavantage_service_test_execution_logs.log", level=logging.INFO,
                        format='[%(levelname)s]:''%(asctime)s:''%(funcName)s:''%(lineno)d:\t''%(message)s')
    # Returns timestamp to print on the console
    now = lambda:datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f : ")
    # Test data file
    filepath = '../testdata/Alphavantage_testdata.xlsx'
    # Assinging sheetname captured from commandline argument
    sheetname = sys.argv[1].upper()
    df = read_excel.read_file(filepath, sheetname)
    # Passing argument and emailid to generate apikey
    apikey = generate_apikey.gen_apikey(sys.argv[2], sys.argv[3])

    print('\n=======================Alphavantage services execution has started =======================\n')
    for index in df.index:
        # Executes the tests case if Execute? = Yes only
        if df['Execute?'][index] == 'Yes':
            if 'datatype=csv' in df['Url'][index]:
                print("Need to handle this")
                continue
            URL = df['Url'][index]
            URL = URL.replace('<<apikey>>', apikey)
            response = requests.get(url=URL)
            data = response.json()

            print('-------- Test case execution has started ----------')
            print(now(),'Test case Id: ',df['TestcaseID'][index])
            logging.info('Test case Id: {}'.format(df['TestcaseID'][index]))
            print(now(),'Test case description: ',df['Description'][index])
            logging.info('Test case description: {}'.format(df['Description'][index]))
            print(now(),'Request Url:', URL)
            logging.info('Request Url:{}'.format(URL))
            print(now(),'Raw Response : ', data)
            logging.info('Raw Response : {}'.format(data))
            # Validates the response
            result = validate(df['ExpectedHTTPStatus_code'][index],df['ValidateParams'][index],response)
            logging.info('Result: {}'.format(result))
            print(now(),"Result: ", result)
            print('-------- Test case execution has completed ----------\n')

            # Writing Results to dataframe to generate HTML report
            df.loc[index,'Result'] = result
            df.loc[index,'HTTP Request'] = URL
            df.loc[index,'HTTP Response'] = str(data)
        else:
            df.drop(index, inplace=True)
    # Generates HTML report
    generate_report.gen_report(df)


if __name__ == '__main__':
    run()



# python main.py servicename(Sheetname) organization emailid
# python main.py TIME_SERIES_DAILY deshaw ssuman.testengineer@gmail.com
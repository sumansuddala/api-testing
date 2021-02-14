import time
import datetime

def gen_report(df):
    # Timestamp
    ts = str(time.time())[:10]
    # Returns timestamp to print on the console
    now = lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f : ")
    print(now(),'Reading report template')
    # Reading existing HTML Report template
    html_report = open('../reports/ReportTemplate/HTMLReportTemplate.html', 'r').read()
    # Creating a new HTML file with timestamp
    f = open('../reports/TestReport'+ts+'.html','w')
    report = ''
    print(now(),'Report preparation is in progress ...')
    # To replace the HTML body with the results
    for index in df.index:
        report = report + ''' <tr class="test-result-step-row test-result-step-row-altone">
                    <td class="test-result-step-testcaseid-cell">
                       '''+ str(df['TestcaseID'][index]) +'''
                    </td>
                    <td class="test-result-step-description-cell">
                        '''+ str(df['Description'][index]) +'''
                    </td>
                    <td class="test-result-step-httprequest-cell">
                       '''+ str(df['HTTP Request'][index]) +'''
                    </td>
                    <td class="test-result-step-httpresponse-cell">
                        '''+ str(df['HTTP Response'][index]) +'''
                    </td>
                    <td class="test-result-step-result-cell-'''+str(df['Result'][index]).lower()+'''">
                        '''+ str(df['Result'][index]) +'''
                    </td>
                </tr> '''

    html_report = html_report.replace('ActualReport', report)
    print(now(),'HTML Report has been generated successfully. Check the reports in /reports location')

    f.write(html_report)
    f.close()

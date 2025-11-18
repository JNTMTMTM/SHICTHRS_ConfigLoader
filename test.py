import SHICTHRSConfigLoader.SHICTHRSConfigLoader as s

try:
    s.SHRConfigLoader_write_ini_file({'SHRLogCore': {'isOutputLogsInConsole': 'True',
                                                                    'isOutputFunctionLoggerName': 'True',
                                                                        'isAutoClearOutdatedLogs': 'True'},
                                                        'SHRLogCore_LogColor': {'DEBUG': 'white', 'INFO': 'white', 'WARNING': 'white',
                                                                                'ERROR': 'white', 'CRITICAL': 'white'}} , '1.ini')
except Exception as e:

    print(e)
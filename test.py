import SHICTHRSConfigLoader.SHICTHRSConfigLoader as s

try:
    s.SHRConfigLoader_read_ini_file('README.md')
except Exception as e:

    print(e)
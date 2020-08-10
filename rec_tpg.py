import signal, time, sys, platform
from datetime import datetime
from pfeiffer import TPG262

# parameters
filename = 'out.dat'
waittime = 10

# get the Python version
is_python2 = 0
is_python3 = 0
ver = platform.python_version_tuple()
if ver[0] == '2':
    is_python2 = 1
    print 'Python version 2'

if ver[0] == '3':
    is_python3 = 1
    print('Python version 3')

# make a connection to TPG
tpg = TPG262(port='/dev/ttyUSB0')

# define signal handler
def handler(signal, frame):
    if is_python2 == 1:
        print '\nDetect interrupt. Exiting the program.\n'
    if is_python3 == 1:
        print('\nDetect interrupt. Exiting the program.\n')

    sys.exit(0)
signal.signal(signal.SIGINT, handler)    

# main routine
while True:
    # get pressure and unix time
    press, (status_code, status_string) = tpg.pressure_gauge(1)
    unixtime = time.time()

    # write to file
    outfile = open(filename, 'a')
    outfile.write(str(int(unixtime)) + ' ' +  str(press) + '\n')
    outfile.close()

    # print to screen
    datetime = datetime.fromtimestamp(int(unixtime))
    if is_python2 == 1:
        print datetime, ' ', press, 'Pa'
    if is_python3 == 1:
        print(datetime, ' ', press, 'Pa')

    # wait
    time.sleep(waittime)


import subprocess
import platform
import os
import sys
cmd1 = 'dataload_test.py'
cmd2 = 'augmentation_test.py'
cmd3 = 'models_test.py'
cmd4 = 'loss_test.py'
cmd5 = 'ssl_test.py'

print('\nSTARTING SELF EEG LIBRARY TEST')
print('')
msg= """
The following test will execute each function or class
using different combinations of input arguments. This may 
take some minutes. Also, if the script detects a cuda device,
it will use it to test functions.\n 
NOTE that some warnings may be 
launched during the test, this is due to few bad combinations of input
arguments generated by the grid search. \n
"""
print(msg)

return_code = subprocess.run(['python', cmd1]).returncode
if return_code != 0:
    print('TEST FAILED: Something appened in the dataload module')
    exit(0)
return_code = subprocess.run(['python', cmd2]).returncode
if return_code != 0:
    print('TEST FAILED: Something appened in the augmentation module')
    exit(0)
return_code = subprocess.run(['python', cmd3]).returncode
if return_code != 0:
    print('TEST FAILED: Something appened in the models module')
    exit(0)
return_code = subprocess.run(['python', cmd4]).returncode
if return_code != 0:
    print('TEST FAILED: Something appened in the losses module')
    exit(0)
return_code = subprocess.run(['python', cmd5]).returncode
if return_code != 0:
    print('TEST FAILED: Something appened in the ssl module')
    exit(0)



# rmdir /Q /S nonemptydir
print('removing generated residual directories (Simulated_EEG, tmpsave)')
try: 
    if platform.system() == 'Windows':
        os.system('rmdir /Q /S Simulated_EEG')
        os.system('rmdir /Q /S tmpsave')
    else:
        os.system('rm -r Simulated_EEG')
        os.system('rm -r tmpsave')
except:
    print('Failed to delete \"Simulated_EEG\" and \"tmpsave\" folders.'
          ' Please don\'t hate me and do it manually')
print('\nTEST COMPLETE. DON\'T WORRY, BE HAPPY!')
sys.exit()
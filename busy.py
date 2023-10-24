import pyinputplus as pyip
flag = 1

while(flag):   #loops the input method.
    answer = pyip.inputYesNo(prompt="Do you want to be kept busy?:")
#takes either yes or no as input else keeps repating for other inputs.
    if(answer.lower() == "yes"):
        flag=1  #if the input is "yes" set's the flag equal to 1 so it continues looping.
    elif(answer.lower() == "no"):
        flag=0  # if the input is "no" set's flag is equal to 0 so it exit's the loop.


        



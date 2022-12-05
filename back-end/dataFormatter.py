import json


def dataFormatter(dataToSend):
    temp = dataToSend
    mydict = {}
    while temp != '\0':
        timestamp = temp[0:temp.find("\r\n")]
        temp = temp[temp.find("\r\n")+2:]
        idx = temp.find("\r\n")
        if(idx == -1):
            idx = len(temp)
            transcript = temp[0:idx]
            temp = '\0'
        else:
            transcript = temp[0:idx]
            temp = temp[temp.find("\r\n")+2:]
        mydict[timestamp] = transcript
    # print(mydict)
    json_object = json.dumps(mydict, indent = 4) 
    # print(json_object)
    return(json_object)
    

# print(dataFormatter("0:06\r\neverything we're doing up in space\r\n0:08\r\nis to benefit humanity or benefit human\r\n0:10\r\nexploration\r\n0:14\r\nwe are natural explorers we want to"))





# // data: {
# //     video1: [transcript1: ,
# //              timestamp1: ,

# //             transcript2: ,
# //             timestamp2: ,]
    
# // }


# //{"message":"0:06\r\neverything we're doing up in space
# //        \r\n0:08\r\nis to benefit humanity or benefit human
# //        \r\n0:10\r\nexploration
# //        \r\n0:14\r\nwe are natural explorers we want to
# //        \r\n0:16\r\nexplore our environment whatever small
# //        \r\n0:18\r\narea we start in we always want to push
# //        \r\n0:19\r\nthe boundaries
# //        \r\n0:20\r\n[Music]
# //        \r\n0:25\r\nthe great thing about space travel is"}

# // Not sure why it is not working tho!
# //Probably you are right! I don't it is there in JS!
# // Something like the above example

# // Parse it to JSON from a single string! Probably would be easier in python dictionary
# //Can we use a python function?
# Yeah 

#Yeah Exactly!



def dataFormatter(dataToSend):
    temp = dataToSend
    mydict = {"timestamp": "transcript"}
    idx = temp.find("\r\n")
    timestamp = temp[0:idx]
    print(timestamp)
    temp.replace(temp[0:idx],"")
    transcript = temp[0:temp.find("\r\n")]
    print(transcript)
    temp.replace(temp[0:temp.find("\r\n")],"")


dataFormatter("0:06\r\neverything we're doing up in space\r\n0:08\r\nis to benefit humanity or benefit human")

#Vrush...could you please run this script?


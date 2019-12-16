from bottle import route, run, get, post, request
import mainPredict as mainPred
import mainCreateDS as mainCrea

@get("/name")
def getName():
    '''returns name of the person speaking'''
    #mainPred
    return

@post("/name")
def postName():
    '''updates dataset with a new person'''
    #mainCrea
    return


#run(host='0.0.0.0', port=8080)

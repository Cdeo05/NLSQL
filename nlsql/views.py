from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class webhookTest(APIView):
    def post(self,request):
        query=request.data["queryResult"]
        print(query['parameters'])
        d={
            'equal':'=',
            'equal to':'=',
            'greater\xa0than':'>',
            'less than':'<',
            'last':'ASC',
            'top':' DESC',
            'Top':' DESC',
            'not equal to':'!=',
        }

        # if(query['parameters']['number']!=''):
        if(len(query['parameters']['attributes'])> 0):
            attributes=",".join(query['parameters']['attributes'])
        if(len(query['parameters']['Count'])>0):
            result = "SELECT COUNT(*) from " + query['parameters']['tables'][0] + ";"
        else:
            if(len(query['parameters']['aggregate'])>0):
                result="SELECT " + query['parameters']['aggregate'] + "(" + attributes + ") " + "FROM " + query['parameters']['tables'][0] + ";"
            elif(len(query['parameters']['person'])):
                print(attributes)
                result="SELECT " + query['parameters']['attributes'][0] + " FROM " + query['parameters']['tables'][0] + " WHERE " + query['parameters']['attributes'][-1] + d[query['parameters']['comparison']] + query['parameters']['person']['name'] +";"
            elif(len(query['parameters']['limit'])>0 and len(query['parameters']['attributes'])>0):
                result= "SELECT " + query['parameters']['attributes'][0] + " FROM " + query['parameters']['tables'][0] + " Order by " + attributes + d[query['parameters']['limit'][0]] +" limit "+ str(int((query['parameters']['number'])))+";" 
            elif(len(query['parameters']['comparison']) and query['parameters']['number']):
                result="SELECT " + query['parameters']['attributes'][0] + " FROM " + query['parameters']['tables'][0] + " WHERE " + query['parameters']['attributes'][-1] + d[query['parameters']['comparison']] + str(int(query['parameters']['number'])) +";"
            else:
                result = "SELECT "+ attributes + " from " + query['parameters']['tables'][0] + ";"

        my_result={
    "fulfillmentText": result,
    
    }  
        return Response(my_result)
        
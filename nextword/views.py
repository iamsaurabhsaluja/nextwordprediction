from django.shortcuts import render

def StatusResponse( status_info, status, updated_time = '' ):
    response = {}

    response['status_info'] = status_info;
    response['status'] = status;
    response['updated_time'] = str(updated_time);

    return response;

def genericResponse( obj ):

    return HttpResponse( json.dumps( obj ), content_type="application/json" )

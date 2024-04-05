from django.shortcuts import render
import os
from django.http import HttpResponse

def home(request):
    return HttpResponse("Test")

import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import APICounter
import random
import logging
hs_token = os.environ.get('HS_AUTH_TOKEN')
base_path=os.environ.get('BASE_PATH')
# HS_HOST="https://awse-p-dip-prdhsfde01.aci.is.cl.ssa.gov"

logging.basicConfig(level=logging.INFO,format='%(levelname)s:%(asctime)s%(module)s%(message)s')
@csrf_exempt
@require_http_methods(["POST"])
def filesubmit(request):
    headers = {'Authorization': f'Token {hs_token}'}
    file_paths = request.POST.getlist('file_paths')  
    print(file_paths)
    responses = []  
    file_to_send=[]
    data=[]
    for file_path in file_paths:
        try:
            print(file_path)

            file_loc = str(base_path)+str(file_path)
            print(file_loc)
            file=('document', open(file_loc, 'rb'))
            file_to_send.append(file)
            logging.info(f'file uploaded successfully')
            doc_meta = f'{{"custom": "{file_path}"}}'
            data.append(('document_metadata', doc_meta),)
        except FileNotFoundError:
            logging.error("file not found")
            responses.append({'file_path': file_path, 'error': 'File not found', 'details': f'No file found at {file_loc}', 'status': 404})
    data.append(('external_id', random.randint(1000, 9999)))
    data.append(('metadata', '{"submission": "md"}'))
    print(file_to_send)
    print("reached")
    response = requests.post(os.environ.get('HS_HOST') + os.environ.get('SUBMIT_URL'),
                                    files=file_to_send, data=data, headers=headers, timeout=300,verify=os.environ.get('CA_CERT_BUNDLE'))
    if response.status_code == 201:
        responses.append({'file_path': file_paths, 'message': 'Created', 'status': 201})
    else:
        responses.append({'file_path': file_paths, 'error': 'Failed to create', 'status_code': response.status_code, 'details': response.text})

    return JsonResponse({'responses': responses})






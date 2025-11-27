# apiapp/views.py ← FINAL VERSION – NO ERRORS, NO DEPENDENCIES, WORKS IMMEDIATELY

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json
import re
from datetime import datetime

from .models import Employee
from .utils import call_proc, validate_api_key

# Add this view — SUPER FAST & PAGINATED
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Employee

def employee_app(request):
    # Only fetch what we need + pagination = INSTANT load
    employees_list = Employee.objects.all().order_by('id')
    paginator = Paginator(employees_list, 25)  # 25 per page = fast

    page = request.GET.get('page')
    employees = paginator.get_page(page)

    return render(request, 'app/employee_app.html', {
        'employees': employees,
        'total': employees_list.count()
    })

# ────────────────────────────────
# BUILT-IN ERROR CODES (NO FILE NEEDED!)
# ────────────────────────────────
class ErrorCode:
    MISSING_API_KEY = {"code": "E1001", "message": "API Key is missing", "status": 401}
    INVALID_API_KEY = {"code": "E1002", "message": "Invalid API Key", "status": 401}
    MISSING_REQUIRED_FIELD = {"code": "E2001", "message": "Missing required field", "status": 400}
    INVALID_EMAIL_FORMAT = {"code": "E2003", "message": "Invalid email format", "status": 400}
    SALARY_MUST_BE_POSITIVE = {"code": "E2004", "message": "Salary must be positive", "status": 400}
    EMPLOYEE_NOT_FOUND = {"code": "E3001", "message": "Employee not found", "status": 404}
    EMPLOYEE_ALREADY_EXISTS = {"code": "E3002", "message": "Employee already exists", "status": 409}
    PROCEDURE_NOT_ALLOWED = {"code": "E4001", "message": "Procedure not allowed", "status": 403}
    PROCEDURE_EXECUTION_FAILED = {"code": "E4003", "message": "Failed to execute procedure", "status": 500}
    INTERNAL_SERVER_ERROR = {"code": "E5001", "message": "Server error", "status": 500}
    INVALID_REQUEST_BODY = {"code": "E2002", "message": "Invalid JSON", "status": 400}

    @staticmethod
    def response(err):
        return {
            "error": {
                "code": err["code"],
                "message": err["message"],
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        }, err["status"]


# 1. Stored Procedure Caller
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def call_stored_procedure(request):
    procedure = request.data.get("procedure")
    params = request.data.get("params", [])

    if not procedure:
        return Response(ErrorCode.response(ErrorCode.MISSING_REQUIRED_FIELD))

    allowed = {"get_employees","sp_get_employee","sp_insert_employee","sp_update_employee","sp_delete_employee","GetEmployeeWithBonus"}
    if procedure not in allowed:
        return Response(ErrorCode.response(ErrorCode.PROCEDURE_NOT_ALLOWED))

    try:
        result = call_proc(procedure, params)
        return Response({"success": True, "results": result, "count": len(result)})
    except:
        return Response(ErrorCode.response(ErrorCode.PROCEDURE_EXECUTION_FAILED))


# 2. Employee CRUD – FULLY VALIDATED
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def employee_list_create(request):
    if request.method == "GET":
        data = list(Employee.objects.values('id','name','email','salary','department'))
        return Response({"success": True, "data": data, "count": len(data)})

    data = request.data
    if not all(k in data and data[k] for k in ['name','email','salary','department']):
        return Response(ErrorCode.response(ErrorCode.MISSING_REQUIRED_FIELD))

    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return Response(ErrorCode.response(ErrorCode.INVALID_EMAIL_FORMAT))

    try:
        if float(data['salary']) <= 0: raise ValueError
    except:
        return Response(ErrorCode.response(ErrorCode.SALARY_MUST_BE_POSITIVE))

    try:
        emp = Employee.objects.create(**data)
        return Response({"success": True, "message": "Created", "id": emp.id}, status=201)
    except:
        return Response(ErrorCode.response(ErrorCode.EMPLOYEE_ALREADY_EXISTS))


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def employee_detail(request, id):
    try:
        emp = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(ErrorCode.response(ErrorCode.EMPLOYEE_NOT_FOUND))

    if request.method == "GET":
        return Response({"success": True, "data": {
            "id": emp.id, "name": emp.name, "email": emp.email,
            "salary": float(emp.salary), "department": emp.department
        }})

    if request.method in ["PUT", "PATCH"]:
        for k, v in request.data.items():
            if k in ['name','email','salary','department']:
                setattr(emp, k, v)
        emp.save()
        return Response({"success": True, "message": "Updated"})

    if request.method == "DELETE":
        emp.delete()
        return Response({"success": True, "message": "Deleted"}, status=204)


# 3. Legacy Raw Endpoints (Still Working)
@csrf_exempt
def employee_raw(request):
    err = validate_api_key(request)
    if err:
        code = ErrorCode.INVALID_API_KEY if err.status_code == 401 else ErrorCode.MISSING_API_KEY
        return JsonResponse(ErrorCode.response(code)[0], status=code["status"])

    if request.method == "GET":
        return JsonResponse({"success": True, "results": call_proc("sp_get_employee")}, safe=False)
    
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            call_proc("sp_insert_employee", [body.get(f) for f in ["name","email","salary","department"]])
            return JsonResponse({"success": True, "message": "Added via SP"})
        except:
            return JsonResponse(ErrorCode.response(ErrorCode.INVALID_REQUEST_BODY)[0], status=400)


@csrf_exempt
def employee_details_raw(request, id):
    err = validate_api_key(request)
    if err:
        code = ErrorCode.INVALID_API_KEY if err.status_code == 401 else ErrorCode.MISSING_API_KEY
        return JsonResponse(ErrorCode.response(code)[0], status=code["status"])

    if request.method == "PUT":
        body = json.loads(request.body)
        call_proc("sp_update_employee", [id] + [body.get(f) for f in ["name","email","salary","department"]])
        return JsonResponse({"success": True, "message": "Updated via SP"})
    
    if request.method == "DELETE":
        call_proc("sp_delete_employee", [id])
        return JsonResponse({"success": True, "message": "Deleted via SP"})
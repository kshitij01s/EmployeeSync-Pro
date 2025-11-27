# apiapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # New clean RESTful ORM endpoints
    path('employee/', views.employee_list_create),           # GET list + POST
    path('employee/<int:id>/', views.employee_detail),       # GET, PUT, DELETE by id
    path('app/', views.employee_app, name='employee_app'),
    # Your old raw stored procedure endpoints (kept working
    path('employee-proc/', views.employee_raw),
    path('employee-proc/<int:id>/', views.employee_details_raw),

    # Powerful generic stored procedure caller
    path('stored-proc/', views.call_stored_procedure),

    # Legacy: old single function (optional – you can delete if not needed)
    # path('old-employee/', views.old_employee_api),
]
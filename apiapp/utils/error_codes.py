# apiapp/utils/error_codes.py → CREATE THIS FILE NOW!

from datetime import datetime

class ErrorCode:
    # Authentication
    MISSING_API_KEY = {"code": "E1001", "message": "API Key is missing", "status": 401}
    INVALID_API_KEY = {"code": "E1002", "message": "Invalid or inactive API Key", "status": 401}

    # Validation
    MISSING_REQUIRED_FIELD = {"code": "E2001", "message": "Missing required field", "status": 400}
    INVALID_REQUEST_BODY = {"code": "E2002", "message": "Invalid JSON in request body", "status": 400}
    INVALID_EMAIL_FORMAT = {"code": "E2003", "message": "Invalid email format", "status": 400}
    SALARY_MUST_BE_POSITIVE = {"code": "E2004", "message": "Salary must be positive", "status": 400}

    # Resource
    EMPLOYEE_NOT_FOUND = {"code": "E3001", "message": "Employee not found", "status": 404}
    EMPLOYEE_ALREADY_EXISTS = {"code": "E3002", "message": "Employee with this email already exists", "status": 409}

    # Stored Procedure
    PROCEDURE_NOT_ALLOWED = {"code": "E4001", "message": "Stored procedure not allowed", "status": 403}
    PROCEDURE_EXECUTION_FAILED = {"code": "E4003", "message": "Failed to execute stored procedure", "status": 500}

    # Server
    INTERNAL_SERVER_ERROR = {"code": "E5001", "message": "Internal server error", "status": 500}

    @staticmethod
    def response(error):
        return {
            "error": {
                "code": error["code"],
                "message": error["message"],
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        }, error["status"]
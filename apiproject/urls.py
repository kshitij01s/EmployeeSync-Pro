"""
URL configuration for apiproject project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# ------------------------------------------------------------------
# PyMySQL → MySQLdb shim (must be at the very top, before any Django imports)
# ------------------------------------------------------------------
import pymysql
pymysql.install_as_MySQLdb()


from django.views.generic import TemplateView
path('app/', TemplateView.as_view(template_name='web/index.html')),

# Simple welcome page for the root URL
# apiproject/urls.py  (only replace the home function, keep the rest)

from django.http import HttpResponse
from django.utils.html import format_html
from datetime import datetime

def home(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EmployeeSync Pro • Enterprise System</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary: #667eea;
                --secondary: #764ba2;
                --glow: #00f5ff;
            }}
            body {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Poppins', sans-serif;
                color: white;
                overflow-x: hidden;
            }}
            .glass {{
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(15px);
                border-radius: 25px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 20px 50px rgba(0,0,0,0.3);
            }}
            .hero-title {{
                font-family: 'Orbitron', sans-serif;
                font-size: 4.5rem;
                background: linear-gradient(45deg, #fff, #00f5ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 30px rgba(0,245,255,0.5);
            }}
            .glow-btn {{
                background: linear-gradient(45deg, #00f5ff, #667eea);
                border: none;
                padding: 18px 60px;
                border-radius: 50px;
                font-size: 1.6rem;
                font-weight: bold;
                box-shadow: 0 15px 35px rgba(102,126,234,0.6);
                transition: all 0.4s;
                position: relative;
                overflow: hidden;
            }}
            .glow-btn:hover {{
                transform: translateY(-10px) scale(1.05);
                box-shadow: 0 25px 50px rgba(102,126,234,0.8);
            }}
            .glow-btn::before {{
                content: '';
                position: absolute;
                top: 0; left: -100%;
                width: 100%; height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
                transition: 0.7s;
            }}
            .glow-btn:hover::before {{ left: 100%; }}
            .feature-card {{
                background: rgba(255,255,255,0.15);
                border-radius: 20px;
                padding: 30px;
                transition: all 0.4s;
                border: 1px solid rgba(255,255,255,0.1);
            }}
            .feature-card:hover {{
                transform: translateY(-15px);
                background: rgba(255,255,255,0.25);
                box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            }}
            .pulse-badge {{
                animation: pulse 2s infinite;
                background: #ff006e !important;
            }}
            @keyframes pulse {{ 0%,100% {{ transform: scale(1); }} 50% {{ transform: scale(1.15); }} }}
            .status-dot {{
                width: 15px; height: 15px; background: #00ff88; border-radius: 50%;
                box-shadow: 0 0 20px #00ff88; animation: blink 2s infinite;
            }}
            @keyframes blink {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        </style>
    </head>
    <body>
        <div class="container py-5">
            <!-- Hero Section -->
            <div class="text-center mb-5">
                <h1 class="hero-title mb-3">EmployeeSync Pro</h1>
                <p class="lead fs-3 opacity-90">Enterprise-Grade • Real-Time • Secure • Production Ready</p>
                <div class="my-4">
                    <span class="status-dot d-inline-block me-2"></span>
                    <strong>All Systems Operational</strong> • {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                </div>
            </div>

            <!-- Main Action Button -->
            <div class="text-center my-5">
                <a href="/app/" class="btn glow-btn text-white shadow-lg">
                    Launch Management Portal
                </a>
            </div>

            <!-- Feature Cards -->
            <div class="row g-4 mt-4">
                <div class="col-lg-4">
                    <div class="feature-card text-center h-100">
                        <i class="bi bi-laptop display-1 mb-3 text-cyan"></i>
                        <h3>Web Dashboard</h3>
                        <p>Full-featured CRUD interface with live data sync</p>
                        <a href="/app/" class="btn btn-outline-light btn-sm">Open →</a>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="feature-card text-center h-100">
                        <i class="bi bi-shield-lock display-1 mb-3 text-warning"></i>
                        <h3>Admin Control</h3>
                        <p>Manage employees, API keys & system settings</p>
                        <a href="/admin/" class="btn btn-warning btn-sm">Enter Admin →</a>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="feature-card text-center h-100">
                        <i class="bi bi-cloud-check display-1 mb-3 text-success"></i>
                        <h3>REST API</h3>
                        <p>Secure endpoints with stored procedure support</p>
                        <a href="/employee/" class="btn btn-success btn-sm">Test API →</a>
                    </div>
                </div>
            </div>

            <!-- Latest Updates -->
            <div class="glass mt-5 p-5">
                <h2 class="text-center mb-4">
                    <i class="bi bi-stars"></i> Latest Features 
                    <span class="badge pulse-badge ms-3 fs-6">LIVE NOW</span>
                </h2>
                <div class="row text-center">
                    <div class="col-md-3"><i class="bi bi-shield-check text-success fs-1"></i><br>Enterprise Security</div>
                    <div class="col-md-3"><i class="bi bi-lightning-charge text-warning fs-1"></i><br>Real-Time Sync</div>
                    <div class="col-md-3"><i class="bi bi-database-check text-info fs-1"></i><br>Stored Proc Ready</div>
                    <div class="col-md-3"><i class="bi bi-phone-vibrate text-cyan fs-1"></i><br>Fully Responsive</div>
                </div>
            </div>

            <!-- Footer -->
            <div class="text-center mt-5 opacity-75">
                <p>Header for API testing: <code class="bg-dark px-3 py-2 rounded">X-API-Key: YOUR_KEY_HERE</code></p>
                <small>© 2025 EmployeeSync Pro • Built with Django + Love</small>
            </div>
        </div>
    </body>
    </html>
    """)


urlpatterns = [
    path('', home, name='home'),                    # Root URL → welcome page
    path('admin/', admin.site.urls),

    # Your actual API app (check the folder name!)
    # Most common names are: apiapp, employees, api, core, etc.
    path('', include('apiapp.urls')),               # this gives you /employee/, /employee-proc/, etc.
    # If the folder is named differently, change 'apiapp' to the correct name
    path('app/', TemplateView.as_view(template_name='web/index.html'), name='web_app'),
]
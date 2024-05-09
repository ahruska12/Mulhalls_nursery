import subprocess
import os
from django.conf import settings
from django.http import HttpResponse

from django.http import FileResponse

from .models import Employee


def backup_database():
    """Create a backup of the PostgreSQL database."""
    backup_file = os.path.join(settings.MEDIA_ROOT, 'db_backup.sql')
    command = [
        'pg_dump',
        '--dbname=d3pg1kk1uaoje9',  # Replace with your database name
        '--host=ceu9lmqblp8t3q.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com',  # Your database host
        '--port=5432',  # Your database port
        '--username=u9ke3i88bug1j0',  # Your database username
        '--password=pfb9297a72793d298aea744e4a2eb1b28c9a70703b9deb358bf56457ca0879073',  # Remove if password is needed
        '--file=' + backup_file,
        '--format=custom'  # You can choose plain for SQL text file or custom for compressed
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"Backup failed: {result.stderr.decode()}")

    return backup_file


def backup_database_view(request, emp_id):
    try:
        usr = Employee.objects.get(employee_id=emp_id)
        print(usr)
    except Employee.DoesNotExist:
        return HttpResponse("Forbidden", status=403)

    if usr:
        try:
            print("inside if statement")
            backup_file = backup_database()
            response = FileResponse(open(backup_file, 'rb'), as_attachment=True, filename='db_backup.sql')
            return response
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

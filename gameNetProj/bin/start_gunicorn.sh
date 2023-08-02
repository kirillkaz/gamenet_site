source /home/debian/projects/venv/bin/activate    
exec gunicorn -c "../gunicorn_config.py" bistro_site.wsgi 

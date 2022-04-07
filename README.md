This is my project defence for SoftUni -> Django web framework.

I want to highlight some issues I had while deploying with heroku.

First  I could not use os.getenv('$VARIABLE_NAME'). It could not read the variables.
Instead I used python-decouple package, and then it all worked fine.

Second I was getting error for building wheel while deploying for backports.zoneinfo==0.2.1.
It turned out that I need to specify the python version I am using in a runtime.txt file.

Third was the error "FATAL: no pg_hba.conf entry for host, no encryption" when deploying
after database maintenance on the heroku side.
That was fixed by installing dj-database-urls and specifying variables in settings.py:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
I guess that is because my PostgreSQL is installed on Docker. Not absolutely sure about that one.

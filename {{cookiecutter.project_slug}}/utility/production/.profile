alias activateenv="source /home/{{ cookiecutter.project_user }}/{{ cookiecutter.project_user }}_env/bin/activate"
alias apprestart="sudo supervisorctl restart {{ cookiecutter.project_user }}_gunicorn"
alias nginxrestart="sudo supervisorctl restart {{ cookiecutter.project_user }}_nginx"

alias app="activateenv && cd /home/{{ cookiecutter.project_user }}/{{ cookiecutter.project_slug }}"
alias pull="git pull origin master"
alias migrate="python manage.py migrate"
alias collectstatic="python manage.py collectstatic"

alias updateapp="app; pull; migrate; collectstatic; apprestart"

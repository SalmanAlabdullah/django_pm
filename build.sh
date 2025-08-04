if [[ $CREATE_SUPERUSER ]];
then
  python projects_management/manage.py createsuperuser --no-input
fi

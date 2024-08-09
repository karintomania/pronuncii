## Set up nvim
```
source workspace.vim
```

## Run Black on the file
```
!black %

!pylint %
```

## Run tests
```
python manage.py test
docker exec pronuncii-py python manage.py test 
python manage.py test main.tests.test_session_service
```

## Show Dependencies

## TODO:
- add redis for session
- add job to remove old recordings


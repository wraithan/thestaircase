from fabric.api import task, local


s3 = {
    'bucket': 'media.thestaircase.org',
    'key': 'static',
}


@task
def deploy():
    local('git push heroku')
    local('heroku run ./manage.py migrate')
    media()


@task
def media():
    local('./manage.py collectstatic --noinput')
    local('s3sync.rb -r --progress --public-read static/ '
          '%(bucket)s:%(key)s' % s3)

from app import app

app.config.update(
    DEBUG=True,
    SERVER_NAME='dtable.dev',
    STATIC_SERVER_NAME='static.dtable.dev'
)
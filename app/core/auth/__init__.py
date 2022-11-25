from fastapi import FastAPI


def include_auth_routers(app: FastAPI):
    from app.core.auth.view import auth_router
    from app.core.auth.oauth.view import oauth_router

    app.include_router(auth_router)
    app.include_router(oauth_router)

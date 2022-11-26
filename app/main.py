from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from fastapi.responses import RedirectResponse

#routes
from app.api_v1.categories.route import router as router_categories
from app.api_v1.users.route import router as router_users
from app.api_v1.auth.route import router as router_auth
from app.api_v1.sub_categories.route import router as router_sub_categories
from app.api_v1.products.route import router as router_products
from app.api_v1.home.route import router as router_home


app = FastAPI(
    title='Muebles Saldana API'
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')

app.include_router(router_categories, prefix=settings.API_V1)
app.include_router(router_users, prefix=settings.API_V1)
app.include_router(router_auth, prefix=settings.API_V1)
app.include_router(router_sub_categories, prefix=settings.API_V1)
app.include_router(router_products, prefix=settings.API_V1)
app.include_router(router_home, prefix=settings.API_V1)
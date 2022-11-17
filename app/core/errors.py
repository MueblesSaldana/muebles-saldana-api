from fastapi.responses import JSONResponse

response = {
    "ERROR_SERVER" :                    JSONResponse(status_code=400, content={"message": "Error en el servidor", "data": None}),
    "ERROR_CREATE_CATEGORY":            JSONResponse(status_code=400, content={"message": "Error al crear una categoria", "data": None}),
    "ERROR_CREATE_USER":                JSONResponse(status_code=400, content={"message": "Error al crear un usuario", "data": None}),
    "ERROR_CREATE_SUB_CATEGORY":        JSONResponse(status_code=400, content={"message": "Error al crear una sub-categoria", "data": None}),
    "ERROR_GET_CATEGORY":               JSONResponse(status_code=400, content={"message": "Error al obtener categoria", "data": None}),
    "ERROR_GET_SUB_CATEGORY":           JSONResponse(status_code=400, content={"message": "Error al obtener sub-categoria", "data": None}),
}
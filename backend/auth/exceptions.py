from fastapi import HTTPException, status


def generic_exception(e: Exception):
    # Create log for generic exception
    print(e)
    raise HTTPException(
        status_code=status.HTTP_406_NOT_ACCEPTABLE,
        detail={"message": "Não foi possível criar o usuário", "error": e},
    ) from e

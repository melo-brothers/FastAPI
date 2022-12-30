from collections import defaultdict

from fastapi import HTTPException, status


ERROR_MESSAGES = {
    4001: {
        "code": 4001,
        "status_code": status.HTTP_400_BAD_REQUEST,
        "type": "Alerta",
        "category": "Negocial",
        "name": "Parâmetro incorreto",
        "description": "Verifique os dados da requisição",
        "message": "Algum valor foi passado incorretamente verifique os campos do tipo data",
        "action": "correct_data",
    },
    4002: {
        "code": 4002,
        "status_code": status.HTTP_400_BAD_REQUEST,
        "type": "Alerta",
        "category": "Negocial",
        "name": "Este usuário já existe na base ({})",
        "description": "Verifique o username ou email do usuário",
        "message": "Algum valor foi passado incorretamente verifique os campos do tipo data",
        "action": "correct_data",
    },
}

DEFAULT_MSG = {
    "code": 5000,
    "status_code": status.HTTP_503_SERVICE_UNAVAILABLE,
    "type": "Alert",
    "category": "System",
    "subcategory": "Internal",
    "name": "Erro ao processar",
    "description": "Erro ao processar a operação",
    "message": "Erro ao processar a operação",
    "action": "Por favor registre uma...",
}

ERROR_MESSAGES = defaultdict(lambda: DEFAULT_MSG, ERROR_MESSAGES)


def raise_message(msg_code: int, preview=False, **kwargs):
    msg = ERROR_MESSAGES[msg_code]
    if msg["code"] != 5000 and kwargs:
        for k, v in kwargs.items():
            msg[k] = msg[k].format(v)

    status_code = msg["status_code"]
    del msg["status_code"]
    exc = HTTPException(status_code=status_code, detail=msg)
    if preview:
        return exc

    raise exc

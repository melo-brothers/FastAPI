from collections import defaultdict

error_messages = {
    4001: {
        "code": 4001,
        "http_status": 400,
        "type": "Alerta",
        "category": "Negocial",
        "name": "Parâmetro incorreto",
        "description": "Verifique os dados da requisição",
        "message": "Algum valor foi passado incorretamente verifique os campos do tipo data",
        "action": "correct_data",

    },
}

DEFAULT_MSG = {
    "code": 5000,
    "http_status": 500,
    "type": "Alert",
    "category": "System",
    "subcategory": "Internal",
    "name": "Erro ao processar",
    "description": "Erro ao processar a operação",
    "message": "Erro ao processar a operação",
    "action": "Por favor registre uma...",
}

error_messages = defaultdict(lambda: DEFAULT_MSG, error_messages)


def raise_message(msg):
    raise NotImplementedError

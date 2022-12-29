from backend.core.errors import raise_message, HTTPException
import pytest


def test_raise_existent_message_without_format():
    expected = {
        "code": 4001,
        "type": "Alerta",
        "category": "Negocial",
        "name": "Parâmetro incorreto",
        "description": "Verifique os dados da requisição",
        "message": "Algum valor foi passado incorretamente verifique os campos do tipo data",
        "action": "correct_data",
    }
    assert raise_message(4001, preview=True).detail == expected

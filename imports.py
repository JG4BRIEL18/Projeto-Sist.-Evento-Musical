import os
from datetime import date
from config.db import criar_conexao
from services.loginadm import login_admin
from services.evento_lista import listar_eventos
from services.ingressos import listar_ingressos
from services.cadastro import cadastrar_participante
from services.participantes import listar_participantes
from services.participantes import editar_participante
from services.excluir_partic import (
    excluir_participante_por_email,
    excluir_participante_por_cpf
)

from django.core.management.base import BaseCommand
from curriculum.models import Category

CATEGORIES = [
    # Administração Pública
    "Administração",
    "Gestão de Pessoas",
    "Licitações e Compras",
    "Contabilidade Pública",
    "Controladoria",
    "Planejamento e Orçamento",

    # Tecnologia e Dados
    "Tecnologia da Informação",
    "Infraestrutura de TI",
    "Suporte Técnico",
    "Desenvolvimento de Sistemas",
    "Banco de Dados",
    "Análise de Dados",
    "Segurança da Informação",

    # Educação
    "Educação Básica",
    "Pedagogia",
    "Apoio Escolar",

    # Saúde
    "Saúde Pública",
    "Vigilância Sanitária",
    "Atenção Básica",
    "Enfermagem",
    "Saúde Mental",

    # Assistência Social
    "Assistência Social",
    "Proteção Social Básica",
    "Proteção Social Especial",
    "CRAS",
    "CREAS",

    # Obras e Infraestrutura
    "Obras Públicas",
    "Infraestrutura Urbana",
    "Engenharia Civil",
    "Manutenção Predial",
    "Transporte",

    # Meio Ambiente
    "Meio Ambiente",
    "Sustentabilidade",
    "Agricultura",
    "Recursos Hídricos",
    "Resíduos Sólidos",

    # Jurídico
    "Assessoria Jurídica",
    "Procuradoria",
    "Ouvidoria",

    # Finanças
    "Finanças",
    "Tributação",
    "Arrecadação",

    # Outros
    "Cultura",
    "Esporte e Lazer",
    "Comunicação Social",
    "Turismo",
    "Logística",
    "Patrimônio Público",
]


class Command(BaseCommand):
    help = "Popula a tabela Category com as áreas de aplicação"

    def handle(self, *args, **kwargs):
        created_count = 0

        for category in CATEGORIES:
            obj, created = Category.objects.get_or_create(name=category)
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f"{created_count} categorias cadastradas com sucesso!"
        ))

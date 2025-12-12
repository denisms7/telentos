from django.core.management.base import BaseCommand
from skills.models import System


class Command(BaseCommand):
    help = "Pré-cadastra sistemas institucionais"

    SYSTEMS = [
        {"name": "SCP-550", "description": "Sistema de Contabilidade, Licitação, Compras e Patrimonio"},
        {"name": "eProcessos", "description": "Sistema eletrônico de processos municipais."},
        {"name": "Sys-Saude", "description": "Sistema de gestão da saúde municipal."},
        {"name": "Sys-Frotas", "description": "Gerenciamento de veículos e frotas."},
        {"name": "Sys-RH", "description": "Sistema de Recursos Humanos."},
        {"name": "GMS", "description": "Gestão de Materiais e Serviços."},
        {"name": "SEFANET", "description": "Sistema de Nota Fiscal de Produtor Rural."},
        {"name": "UMC-INCRA", "description": "Acesso ao portal UMC do INCRA."},
        {"name": "AMP (Diário Oficial)", "description": "Publicações oficiais da AMP."},
        {"name": "eProtocolo", "description": "Sistema de protocolo Estadual."},
        {"name": "TCE-PR", "description": "Acesso aos sistemas do Tribunal de Contas do Paraná."},
        {"name": "Pagina Institucional", "description": "Portal institucional oficial do Municipio."},
        {"name": "Leis Municipais", "description": "Sistema de consulta de legislação municipal."},
        {"name": "SIM-AM", "description": "Sistema de Informações Municipais – SIM/AM (TCE)."},
    ]

    def handle(self, *args, **options):
        created_count = 0

        for item in self.SYSTEMS:
            name = item["name"]
            description = item["description"]

            obj, created = System.objects.get_or_create(
                name=name,
                defaults={
                    "active": True,
                    "description": description,
                },
            )

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Sistema criado: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Sistema já existe: {name}"))

        self.stdout.write(
            self.style.NOTICE(
                f"Processo finalizado. {created_count} sistema(s) criado(s)."
            )
        )

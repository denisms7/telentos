from django.core.management.base import BaseCommand
from skills.models import System


class Command(BaseCommand):
    help = "Pré-cadastra sistemas institucionais"

    SYSTEMS = [
        "SCP-550",
        "eProcessos",
        "Sys-Saude",
        "Sys-Frotas",
        "Sys-RH",
        "GMS",
        "SEFANET",
        "UMC INCRA",
        "AMP (Diário Oficial dos Municípios)",
        "eProtocolo",
        "TCE-PR",
        "Pagina Institucional",
        "Leis Municipais",
        "SIM-AM",
    ]

    def handle(self, *args, **options):
        created_count = 0

        for system_name in self.SYSTEMS:
            obj, created = System.objects.get_or_create(
                name=system_name,
                defaults={
                    "active": True,
                },
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Sistema criado: {system_name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Sistema já existe: {system_name}")
                )

        self.stdout.write(
            self.style.NOTICE(
                f"Processo finalizado. {created_count} sistema(s) criado(s)."
            )
        )

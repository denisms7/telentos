from django.core.management.base import BaseCommand

from skills.models import Skill, SkillType


class Command(BaseCommand):
    help = "Cria skills administrativas padrões no sistema."

    def handle(self, *args, **options):
        skills = [
            # Pacote Microsoft
            ("Microsoft Excel", SkillType.HARD),
            ("Microsoft Word", SkillType.HARD),
            ("Microsoft PowerPoint", SkillType.HARD),
            ("Microsoft Outlook", SkillType.HARD),
            ("Microsoft Access", SkillType.HARD),
            ("Microsoft Publisher", SkillType.HARD),
            ("Microsoft Teams", SkillType.HARD),

            ("Uso e Manutenção Básica de Impressoras", SkillType.HARD),

            # Design e engenharia
            ("AutoCAD", SkillType.HARD),
            ("Revit", SkillType.HARD),
            ("Adobe Photoshop", SkillType.HARD),
            ("Adobe Premiere", SkillType.HARD),
            ("Illustrator", SkillType.HARD),
            ("CorelDRAW", SkillType.HARD),
            ("Design Gráfico", SkillType.HARD),
            ("Fotografia e Vídeo", SkillType.HARD),

            # Tecnologia da informação
            ("Programação", SkillType.HARD),
            ("Redes de Computadores", SkillType.HARD),
            ("Segurança da Informação", SkillType.HARD),
            ("Análise de Dados ou Banco de Dados", SkillType.HARD),
            ("Big Data", SkillType.HARD),
            ("Cloud Computing", SkillType.HARD),
            ("Suporte Técnico", SkillType.HARD),
            ("Desenvolvimento Web", SkillType.HARD),

            # Administração pública e gestão
            ("Processos Administrativos (PAD)", SkillType.HARD),
            ("Compras e Licitações", SkillType.HARD),
            ("Planejamento Estratégico", SkillType.HARD),
            ("Finanças Públicas", SkillType.HARD),
            ("Nota Fiscal e Tributos", SkillType.HARD),
            ("Redação Oficial", SkillType.HARD),
            ("Elaboração de Relatórios", SkillType.HARD),
            ("Arquivologia", SkillType.HARD),

            # Sustentabilidade
            ("Sustentabilidade", SkillType.HARD),
            ("Gestão de Resíduos Sólidos", SkillType.HARD),
            ("Gestão Hídrica", SkillType.HARD),

            # Comunicação e marketing institucional
            ("Comunicação Institucional", SkillType.HARD),
            ("Marketing", SkillType.HARD),
            ("Produção de Conteúdo", SkillType.HARD),
            ("Mídias Sociais", SkillType.HARD),
            ("Assessoria de Imprensa", SkillType.HARD),
            ("Retórica", SkillType.SOFT),

            # Competências comportamentais
            ("Conduta Profissional", SkillType.SOFT),
            ("Flexibilidade e Adaptação", SkillType.SOFT),
            ("Liderança", SkillType.SOFT),
            ("Resiliência", SkillType.SOFT),
            ("Comunicação", SkillType.SOFT),
            ("Gestão de Pessoas", SkillType.SOFT),
            ("Gestão do Tempo", SkillType.SOFT),
            ("Atendimento ao Público", SkillType.SOFT),
        ]

        created_count  = 0

        for name, skill_type in skills:
            obj, created = Skill.objects.get_or_create(
                name=name,
                skill_type=skill_type,
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Skill criada: {obj}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Skill já existe: {obj}")
                )

        self.stdout.write(
            self.style.NOTICE(
                f"Processo finalizado. {created_count} skill(s) criadas."
            )
        )
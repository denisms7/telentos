from django.core.management.base import BaseCommand
from skills.models import Function


class Command(BaseCommand):
    help = "Cadastra cargos iniciais na tabela Function"

    def handle(self, *args, **options):
        functions = [
            {
                "name": "Agente Administrativo",
                "description": """
                <p>- Executa serviços de apoio nas áreas técnicas da Administração Pública;<br />
                - Executa serviços técnicos relativos a sua área de atuação;<br />
                - Executa pesquisas de interesse da Administração;<br />
                - Elabora relatórios de atividades administrativas;<br />
                - Redige expedientes administrativos em geral;<br />
                - Examina processos relacionados com assuntos gerais da repartição;<br />
                - Elabora ou verifica documentos de receitas e despesas, empenhos e balancetes;<br />
                - Supervisiona tarefas de rotina administrativa;<br />
                - Assessora o superior hierárquico em assuntos técnicos e administrativos;<br />
                - Coleta e elabora dados visando a melhoria das atividades;<br />
                - Viabiliza convênios para captação de recursos;<br />
                - Presta assessoria técnica em planos, programas e projetos;<br />
                - Elabora relatórios, planilhas, informações e pareceres;<br />
                - Acompanha e avalia políticas e diretrizes administrativas;<br />
                - Participa de programas de treinamento quando convocado;<br />
                - Executa demais tarefas pertinentes à área de atuação.</p>
                """,
            },

            {
                "name": (
                    "Agente de Serviços Administrativos - Recepcionista"
                ),
                "description": """
                <p>
                - Organiza e mantém o controle e guarda de documentos;<br />
                - Atende telefones e transmite recados;<br />
                - Transporta documentos entre unidades;<br />
                - Preenche requerimentos e documentos diversos;<br />
                - Atende ao público fornecendo informações;<br />
                - Presta serviços de digitação;<br />
                - Redige expedientes sumários;<br />
                - Distribui e encaminha correspondências;<br />
                - Executa atividades auxiliares administrativas;<br />
                - Zela pelos equipamentos sob sua guarda;<br />
                - Realiza busca de dados e pesquisa documental;<br />
                - Coleta informações para metas institucionais;<br />
                - Elabora textos profissionais e documentos oficiais;<br />
                - Aplica técnicas secretariais;<br />
                - Controla protocolos e arquivamentos;<br />
                - Opera equipamentos de digitalização e cópia;<br />
                - Executa demais funções administrativas correlatas.
                </p>
                """,
            },

            {
                "name": "Agente de Serviços Administrativos - Telefonista",
                "description": """
                <p>
                - Faz ligações telefônicas;<br />
                - Atende telefones, procede anotações e transmite recados aos demais servidores;<br />
                - Fornece informações sobre endereços e telefones quando solicitado;<br />
                - Faz relatórios sobre as ligações efetuadas;<br />
                - Solicita atendimento para reparo quando necessário nos equipamentos;<br />
                - Zela pelos equipamentos colocados sob sua responsabilidade;<br />
                - Efetua todas as demais funções inerentes ao cargo.
                </p>
                """,
            },

            {
                "name": "Agente de Fiscalização",
                "description": """
                <p>
                - Fiscaliza pedidos de inscrição no cadastro de contribuintes municipais e licenças de localização e funcionamento;<br />
                - Fiscaliza e mantém atualizados cadastros de contribuintes e de licenças;<br />
                - Fiscaliza a utilização de documentos fiscais e outras obrigações acessórias;<br />
                - Executa inscrições no Cadastro de Contribuintes;<br />
                - Realiza levantamentos de informações junto a órgãos públicos e privados;<br />
                - Atende, orienta e informa servidores e contribuintes sobre legislação e procedimentos legais;<br />
                - Efetua cálculos específicos, croquis e levantamentos de campo para fins fazendários;<br />
                - Comunica irregularidades observadas durante as atividades de fiscalização;<br />
                - Realiza análise comparativa das atividades dos contribuintes;<br />
                - Realiza levantamento socioeconômico para composição da base de cálculo do ISS estimado;<br />
                - Realiza levantamentos cadastrais para análise de encerramento e baixa de ofício;<br />
                - Emite pareceres, notificações e autos de infração, quando autorizado;<br />
                - Presta auxílio na Auditoria Tributária;<br />
                - Presta suporte técnico-administrativo à área tributária;<br />
                - Opera sistemas e equipamentos de informática;<br />
                - Executa fiscalização prevista no Plano Diretor do Município;<br />
                - Atualiza cadastros econômicos e imobiliários fiscais;<br />
                - Realiza fiscalização in loco;<br />
                - Executa fiscalização de Vigilância Sanitária;<br />
                - Emite notificações e autuações fiscais;<br />
                - Executa outras atividades correlatas.
                </p>
                """,
            },

            {
                "name": "Advogado",
                "description": """
                <p>
                - Presta suporte técnico aos órgãos quanto às demandas da comunidade e dos conselhos;<br />
                - Profere palestras, esclarecendo procedimentos legais aos técnicos do serviço;<br />
                - Capacita agentes multiplicadores;<br />
                - Mantém atualizados os registros de todos os atendimentos realizados;<br />
                - Participa de todas as reuniões da equipe;<br />
                - Realiza todas as tarefas inerentes à função de advogado;<br />
                - Atua judicial e extrajudicialmente em situações que não sejam atribuição da Procuradoria Jurídica Municipal.
                </p>
                """,
            },


        ]

        created_count = 0

        for data in functions:
            function, created = Function.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "active": True,
                },
            )

            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Cargo criado: {function.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Cargo já existe: {function.name}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Processo finalizado. {created_count} cargo(s) criado(s)."
            )
        )

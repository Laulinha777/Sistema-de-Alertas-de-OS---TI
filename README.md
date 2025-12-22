# 🔎Sistema de Monitoramento de Ordens de Serviço - TI

Projeto com o objetivo de notificar automaticamente quando suregm novas Ordens de Serviço (OS) destinadas ao setor de TI.

## 🎇Sobre o Projeto:
  A solução foi desenvolvida utilizando Python, com integração a um bot, criado do Telegram, responsável por enviar mensagens de alerta sempre que uma nova OS é identificada para o setor de TI, da empresa onde realizo estágio. 
As notificações das OS’s, contendo ID e a Descrição, são obtidas diretamente do banco de dados do sistema ERP utilizado pela empresa, através de consultas realizadas no MySQL (via MySQL WorkBench).

  O sistema realiza o monitoramento contínuo das novas OS's enquanto o servidor está em execução. Anteriormente, esse processo era feito de forma **manual**, sendo necessário procurar as OS's destinadas ao setor, o que demandava mais tempo e tornava o processo menos eficiente.
Como **melhoria futura**, o projeto poderá ser integrado ao **n8n**, permitindo a automação do fluxo sem a necessidade de manter o servidor Python rodando continuamente no terminal, tornando a solução ainda mais prática, escalável e eficiente.

### Tecnologias utilizadas:
- Python
- MySQL
- Telegram Bot

<p align="center"> 
<img  width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/382d9713-cfab-4b03-af91-3041faad5e22" />
</p>

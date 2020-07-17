.. _about:

Sobre a Central de Erros
========================

Projeto que simula um sistema de logs feito durante o AceleraDev Python Online da Codenation (que hoje em dia é `Trybe <https://www.betrybe.com/>`_) em parceria com a `Stone <https://www.stone.com.br/>`_.

Objetivo
++++++++
Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.

A arquitetura do projeto é formada por:

Backend - API
-------------

* criar endpoints para serem usados pelo frontend da aplicacao.

* criar um endpoint que será usado para gravar os logs de erro em um banco de dados relacional.

* a API deve ser segura, permitindo acesso apenas com um token de autenticação válido.

Para saber mais sobre o projeto, acesse:
++++++++++++++++++++++++++++++++++++++++

:ref:`Documentação sobre a API <swagger>`
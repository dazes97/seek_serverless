Proyecto Todo Backend

Este proyecto es un backend construido con Serverless Framework y Python  

Requisitos

instalados los siguientes componentes en el sistema:

1. Docker: Necesario para la compilación de paquetes Python.
2. Python 3.12.9: Versión de Python requerida para el proyecto.
3. Node.js 22 LTS: Versión de Node.js requerida.
4. Serverless Framework: Instalado globalmente.
   npm install -g osls

Configuración del Proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

1. Clonar el Repositorio
git clone https://github.com/dazes97/seek_serverless.git

cd tu-repositorio

2. Instalar Dependencias
Instala las dependencias de Node.js en la raíz del proyecto:
npm install

Instalar Dependencias en Cada Carpeta de Servicio(auth, authorizer, todos):
npm install

Crear Virtual Env en Cada Carpeta de Servicio(auth, authorizer, todos):
python -m venv venv

3. Configurar Variables de Entorno

Crea un archivo .env en la raíz de cada carpeta de servicio y define las variables de entorno necesarias:

todos:

DYNAMODB_TABLE=nombre-de-la-tabla-nosql-a-crear
PROFILE=nombre-del-perfil-aws-para-desplegar

authorizer:
JWT_SECRET=jwt-secret-generado
PROFILE=nombre-del-perfil-aws-para-desplegar

auth:
JWT_SECRET=jwt-secret-generado(mismo que el authorizer)
PROFILE=nombre-del-perfil-aws-para-desplegar

4.- Configurar credenciales globales

serverless config credentials \
  --provider aws \
  --key TU_KEY \
  --secret TU_SECRET

5.- Desplegar el Proyecto

Para desplegar el proyecto en AWS, ejecuta el siguiente comando en la raiz del proyecto:

sls deploy --stage api

6.- para visualizar la documentacion de la api visita: https://editor-next.swagger.io/
adjunta el archivo swagger.json de la carpeta todos


Comandos Útiles

- Desplegar el proyecto(en cada carpeta o en la raiz del proyecto):
  sls deploy --stage api

- Ejecutar el proyecto localmente (con serverless-offline):
  sls offline

- Eliminar el despliegue(raiz del proyecto):
  sls remove --stage api

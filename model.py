from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from app import get_abstract, read_dir, read_pdf, read_page

template = """
Necesito que califiques los abstracts de cada uno estos artículos científicos que te voy a pasar, por favor.

Aqui te doy el resumen del articulo cientifico que quiero hacer, por lo que los que te vaya a pasar son resumenes de 
articulos cientificos. Estos resumenes son de diferentes temas, por lo que te pido que los leas y me digas si son aptos para ir dentro de la investigacion como 
referencias bibliograficas. Solo di un si o un no, y una pequeña razon por la que crees que si o no.

Contexto:
Este proyecto busca desarrollar un prototipo de orientador virtual para emprendedores de base tecnológica en Perú, 
impulsado por inteligencia artificial generativa. Su objetivo es complementar el trabajo de instituciones 
gubernamentales como CONCYTEC, INNOVATE y el Ministerio de la Producción, que brindan recursos informativos, 
pero con limitaciones en interacción continua y cobertura. El prototipo será una plataforma interactiva que 
ofrezca asesoramiento personalizado, cubriendo el vacío en orientación práctica y seguimiento que dejan estas instituciones.

Entre sus características clave se destacan la interacción bidireccional con el usuario, la presentación de tendencias globales 
en innovación y tecnologías de vanguardia, y la generación de resúmenes personalizados al finalizar cada interacción para 
su posterior consulta. Este enfoque busca fomentar la creación de startups tecnológicas en Perú, facilitando el 
acceso a información relevante de forma dinámica y eficiente.

Los objetivos del proyecto son:

Objetivo general: Desarrollar un orientador virtual interactivo basado en inteligencia artificial generativa, que ofrezca 
asesoramiento personalizado, brinde información sobre tendencias tecnológicas y genere resúmenes.

Objetivo específico 1: Crear un compendio de información sobre emprendimiento tecnológico en Perú, incluyendo tendencias 
globales, normativas locales y recursos de instituciones clave como CONCYTEC, INNOVATE y PRODUCE.

Objetivo específico 2: Desarrollar e integrar un modelo de lenguaje de gran tamaño (LLM) adaptado al ámbito de emprendimiento 
tecnológico, para proporcionar respuestas coherentes y adaptadas al perfil del usuario.

Este proyecto tiene como fin impulsar el ecosistema emprendedor peruano y ayudar a la creación de nuevas empresas tecnológicas 
mediante una herramienta accesible, interactiva e innovadora.

Y aqui el contexto del proyecto: {context}
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def main():
    respuestas = [[] for _ in range(5)] # Poner el numero de archivos en la carpeta pdfs
    

    for index, file in enumerate(read_dir("pdfs")):
        file_path = f"pdfs/{file}"
        pdf_file_obj = read_pdf(file_path)
        
        page_info = read_page(pdf_file_obj, 0)

        abstract = get_abstract(page_info)
        result = chain.invoke({"context":abstract})
        respuestas[index].append(file)
        respuestas[index].append(result)
        
    pdf_file_obj.close()
    print(respuestas)


if __name__ == "__main__":
    main()
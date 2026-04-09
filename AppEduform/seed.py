import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppEduform.settings')
django.setup()

from AppPagina.models import AreaVocacional, Carrera, Pregunta

def seed_data():
    # Crear áreas vocacionales
    areas_data = [
        {'nombre': 'Tecnología e Informática'},
        {'nombre': 'Administración'},
        {'nombre': 'Diseño y Multimedia'},
        {'nombre': 'Salud'},
        {'nombre': 'Turismo'},
        {'nombre': 'Construcción'},
        {'nombre': 'Agroindustria'},
        {'nombre': 'Mecánica'},
    ]

    areas = {}
    for area_data in areas_data:
        area, created = AreaVocacional.objects.get_or_create(**area_data)
        areas[area.nombre] = area
        print(f"Área: {area.nombre} {'creada' if created else 'ya existe'}")

    # Crear carreras con descripciones
    carreras_data = [
        {
            'nombre': 'Desarrollo de Software',
            'tipo': 'Tecnologo',
            'area': areas['Tecnología e Informática'],
            'descripcion': 'Esta carrera forma profesionales capaces de diseñar, desarrollar y mantener aplicaciones de software. Es ideal para personas con habilidades analíticas y creativas, permitiendo trabajar en equipos multidisciplinarios para resolver problemas tecnológicos complejos. Los egresados pueden desempeñarse en empresas de tecnología, startups, consultorías y como freelancers, contribuyendo al avance digital de la sociedad.'
        },
        {
            'nombre': 'Administración de Empresas',
            'tipo': 'Tecnologo',
            'area': areas['Administración'],
            'descripcion': 'Forma líderes en la gestión empresarial, enseñando a organizar recursos, planificar estrategias y dirigir equipos. Es perfecta para individuos con visión emprendedora y habilidades de negociación, abriendo puertas a roles ejecutivos, consultoría y emprendimiento en diversos sectores económicos.'
        },
        {
            'nombre': 'Diseño Gráfico',
            'tipo': 'Tecnico',
            'area': areas['Diseño y Multimedia'],
            'descripcion': 'Esta carrera combina creatividad y tecnología para comunicar ideas visualmente. Los diseñadores gráficos crean identidades corporativas, materiales publicitarios y experiencias digitales. Es perfecta para individuos artísticos con habilidades técnicas, permitiendo expresar creatividad mientras resuelven problemas de comunicación visual.'
        },
        {
            'nombre': 'Enfermería',
            'tipo': 'Tecnico',
            'area': areas['Salud'],
            'descripcion': 'La enfermería es una profesión dedicada al cuidado integral de la salud humana. Prepara a los estudiantes para proporcionar atención médica compasiva y competente, trabajando en hospitales, clínicas y comunidades. Es perfecta para individuos empáticos y dedicados que desean marcar una diferencia en la vida de las personas, ofreciendo apoyo emocional y técnico en momentos críticos.'
        },
        {
            'nombre': 'Turismo y Hotelería',
            'tipo': 'Tecnico',
            'area': areas['Turismo'],
            'descripcion': 'Prepara profesionales para gestionar servicios turísticos, organizando experiencias de viaje y promoviendo destinos. Es ideal para personas extrovertidas y con pasión por los viajes, ofreciendo oportunidades en agencias, hoteles y empresas de eventos, contribuyendo al desarrollo del sector turístico.'
        },
        {
            'nombre': 'Construcción Civil',
            'tipo': 'Tecnico',
            'area': areas['Construcción'],
            'descripcion': 'Enseña a planificar, ejecutar y supervisar proyectos de edificación. Los técnicos en construcción trabajan en obras civiles, asegurando calidad y seguridad. Es adecuada para personas prácticas y con capacidad para trabajar en equipo, contribuyendo al desarrollo urbano sostenible.'
        },
        {
            'nombre': 'Agroindustria',
            'tipo': 'Tecnico',
            'area': areas['Agroindustria'],
            'descripcion': 'Forma especialistas en procesos de transformación de productos agrícolas. Combina conocimientos técnicos con prácticas agrícolas modernas. Es perfecta para individuos interesados en el campo y la innovación, trabajando en industrias alimentarias y mejorando la cadena de suministro agrícola.'
        },
        {
            'nombre': 'Mecánica Automotriz',
            'tipo': 'Tecnico',
            'area': areas['Mecánica'],
            'descripcion': 'Especializa en el mantenimiento y reparación de vehículos y maquinaria. Los técnicos mecánicos diagnostican y solucionan problemas mecánicos. Es ideal para personas con habilidades manuales y interés en la tecnología automotriz, trabajando en talleres, concesionarios y empresas de transporte.'
        },
    ]

    for carrera_data in carreras_data:
        carrera, created = Carrera.objects.get_or_create(
            nombre=carrera_data['nombre'],
            defaults=carrera_data
        )
        if created:
            print(f"Carrera: {carrera.nombre} creada")
        else:
            # Actualizar descripción si no existe
            if not carrera.descripcion:
                carrera.descripcion = carrera_data['descripcion']
                carrera.save()
                print(f"Carrera: {carrera.nombre} descripción actualizada")

    # Crear preguntas de ejemplo
    preguntas_data = [
        {'texto': '¿Te gusta resolver problemas lógicos?', 'area': areas['Tecnología e Informática']},
        {'texto': '¿Te interesa reparar computadores o redes?', 'area': areas['Tecnología e Informática']},
        {'texto': '¿Te gustaría desarrollar software o videojuegos?', 'area': areas['Tecnología e Informática']},
        {'texto': '¿Te interesa trabajar con bases de datos?', 'area': areas['Tecnología e Informática']},
        {'texto': '¿Te gustaría administrar una empresa o negocio?', 'area': areas['Administración']},
        {'texto': '¿Te interesa organizar proyectos empresariales?', 'area': areas['Administración']},
        {'texto': '¿Te gustaría trabajar en contabilidad o finanzas?', 'area': areas['Administración']},
        {'texto': '¿Te interesa emprender tu propio negocio?', 'area': areas['Administración']},
        {'texto': '¿Te gustaría diseñar logotipos o publicidad digital?', 'area': areas['Diseño y Multimedia']},
        {'texto': '¿Te interesa editar videos o contenido multimedia?', 'area': areas['Diseño y Multimedia']},
        {'texto': '¿Te gustaría trabajar con animación digital?', 'area': areas['Diseño y Multimedia']},
        {'texto': '¿Te interesa crear contenido para redes sociales?', 'area': areas['Diseño y Multimedia']},
        {'texto': '¿Te gustaría ayudar en la atención de pacientes?', 'area': areas['Salud']},
        {'texto': '¿Te interesa promover hábitos saludables?', 'area': areas['Salud']},
        {'texto': '¿Te gustaría trabajar en hospitales o clínicas?', 'area': areas['Salud']},
        {'texto': '¿Te interesa cuidar adultos mayores o niños?', 'area': areas['Salud']},
        {'texto': '¿Te gustaría guiar turistas o mostrar lugares?', 'area': areas['Turismo']},
        {'texto': '¿Te interesa organizar viajes o eventos?', 'area': areas['Turismo']},
        {'texto': '¿Te gustaría trabajar en hoteles o turismo?', 'area': areas['Turismo']},
        {'texto': '¿Te interesa promover destinos turísticos?', 'area': areas['Turismo']},
        {'texto': '¿Te gustaría construir casas o edificios?', 'area': areas['Construcción']},
        {'texto': '¿Te interesa interpretar planos de construcción?', 'area': areas['Construcción']},
        {'texto': '¿Te gustaría supervisar obras?', 'area': areas['Construcción']},
        {'texto': '¿Te interesa trabajar con herramientas de construcción?', 'area': areas['Construcción']},
        {'texto': '¿Te gustaría trabajar con cultivos o alimentos?', 'area': areas['Agroindustria']},
        {'texto': '¿Te interesa procesar productos agrícolas?', 'area': areas['Agroindustria']},
        {'texto': '¿Te gustaría mejorar la producción agrícola?', 'area': areas['Agroindustria']},
        {'texto': '¿Te interesa trabajar en el campo?', 'area': areas['Agroindustria']},
        {'texto': '¿Te gustaría reparar motos o carros?', 'area': areas['Mecánica']},
        {'texto': '¿Te interesa trabajar con motores?', 'area': areas['Mecánica']},
        {'texto': '¿Te gustaría diagnosticar fallas mecánicas?', 'area': areas['Mecánica']},
        {'texto': '¿Te interesa mantener vehículos?', 'area': areas['Mecánica']},
    ]

    for pregunta_data in preguntas_data:
        pregunta, created = Pregunta.objects.get_or_create(**pregunta_data)
        print(f"Pregunta: {pregunta.texto[:50]}... {'creada' if created else 'ya existe'}")

if __name__ == '__main__':
    seed_data()
    print("Datos sembrados exitosamente.")
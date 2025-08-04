import os
import sys
from PyQt5.QtCore import Qt, QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizeGrip,QMessageBox,QTableWidgetItem,QLabel,QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from views.agregarUsuario import AgregarUsuario
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from views.session import UserSession
from database.conexion import Database
from error.logger import log
from views.eliminarUsuario import EliminarUsuario
from views.modificarUsuario import ModificarUsuario
from views.agregarPeliculas import AgregarPeliculas
from views.eliminarPeliculas import EliminarPelicula
from views.modificarPelicula import ModificarPelicula
from views.agregarFuncion import AgregarFuncion
from views.eliminarFuncion import EliminarFuncion
from views.modificarFuncion import ModificarFuncion
from datetime import datetime
from views.seleccionarButacas import Cine
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QDate
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt





class MainWindow(QMainWindow):   
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Cargar el archivo .ui que contiene la interfaz gráfica
        loadUi("ui\\menu.ui", self)
        self.db = Database()
        self.carpeta_imagenes = "movies"

        # Eliminar la barra de título de la ventana y ajustar la opacidad
        self.setWindowFlags(Qt.FramelessWindowHint) 
        self.setWindowOpacity(1.0)  # Opacidad completa (1.0 es totalmente opaco)

        # SizeGrip para redimensionar la ventana desde la esquina inferior derecha
        self.gripSize = 10  # Tamaño del QSizeGrip
        self.grip = QSizeGrip(self)  # Crear el QSizeGrip
        self.grip.resize(self.gripSize, self.gripSize)  # Ajustar el tamaño del grip

        # Ocultar el menú lateral al inicio (iniciar con width=0)
        self.frame_lateral.setMinimumWidth(0)

        # Iniciar en la primera página (self.page)
        self.stackedWidget.setCurrentWidget(self.page)

        # Asignar el evento de mover la ventana al arrastrar el frame superior
        self.frame_superior.mouseMoveEvent = self.mover_ventana  
        
        # Configurar los botones para cambiar de páginas dentro de un stackedWidget
        self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))			
        self.bt_uno.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_uno))
        self.bt_dos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_dos))	
        self.bt_tres.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_tres))
        self.bt_cuatro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cuatro))			
        self.bt_cinco.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cinco))	

        #Cartelera
        self.btn_anterior.clicked.connect(self.pelicula_anterior)
        self.btn_siguiente.clicked.connect(self.pelicula_siguiente)


        #Saludo de bienvenida
        session = UserSession()
        saludo = session.username if session.username else "Usuario"  # Valor por defecto "Usuario"

        # Acortar el nombre si es demasiado largo (máximo 10 caracteres)
        max_length = 10
        if len(saludo) > max_length:
            saludo = saludo[:max_length] + "..."  # Truncar el nombre y agregar "..."

        # Actualizar el QLabel con el saludo
        self.label_bienvenida.setText(f"Hola, {saludo}!")



        #Configuracion botones pagina Usuarios
        self.bt_agregar_usuario.clicked.connect(self.abrir_agregar_usuario)
        self.btn_eliminar_usuario.clicked.connect(self.abrir_eliminar_usuarios)
        self.btn_modificar_usuario.clicked.connect(self.abrir_modificar_usuario)

        # Conectar eventos para los filtros
        self.nombre_filtro_usuario.textChanged.connect(self.aplicar_filtros)
        self.fecha_creacion_filtro_usuario.dateChanged.connect(self.aplicar_filtros)


        self.comboBox_filtro_usuario.currentIndexChanged.connect(self.aplicar_filtros)

        self.fecha_creacion_filtro_usuario.setCalendarPopup(True)
        self.fecha_creacion_filtro_usuario.setDisplayFormat("dd/MM/yyyy")  
        self.fecha_creacion_filtro_usuario.setDate(QDate.currentDate())

        # Cargar datos iniciales
        self.cargar_usuarios_en_tabla()
        self.cargar_rol_filtro()


        #Configuracion botones pagina Peliculas
        self.btn_agregar_pelicula.clicked.connect(self.abrir_agregar_pelicula)
        self.btn_eliminar_pelicula.clicked.connect(self.abrir_eliminar_pelicula)
        self.btn_modificar_pelicula.clicked.connect(self.abrir_modificar_pelicula)
        self.btn_informacion_pelicula.clicked.connect(self.mostrar_informacion_pelicula)
        self.btn_calcular_peliculas.clicked.connect(self.calcular_estadisticas_pelicula)

        # Conectar el botón al método
        # self.btn_buscar_pelicula.clicked.connect(self.aplicar_filtros_pelicula)
        # Conectar el campo de texto al método para actualizar el filtro de nombre
        self.filtro_nombre_pelicula.textChanged.connect(self.cargar_peliculas_en_tabla)

        # Conectar los cambios en las fechas al método para activar el filtro de fechas
        self.fecha_inicio_pelicula.dateChanged.connect(self.activar_filtro_fecha_peliculas)
        self.fecha_fin_pelicula.dateChanged.connect(self.activar_filtro_fecha_peliculas)

        self.btn_todo_peliculas.clicked.connect(self.mostrar_todas_las_peliculas)

        self.fecha_inicio_pelicula.setCalendarPopup(True)
        self.fecha_inicio_pelicula.setDisplayFormat("dd/MM/yyyy")  
        self.fecha_inicio_pelicula.setDate(QDate.currentDate())

        self.fecha_fin_pelicula.setCalendarPopup(True)
        self.fecha_fin_pelicula.setDisplayFormat("dd/MM/yyyy")  
        self.fecha_fin_pelicula.setDate(QDate.currentDate())

        #Configuracion botones pagina funciones
        self.filtro_fecha_activado = False  # Configuración inicial del filtro de fecha

        # Configuración inicial de botones y fechas
        self.btn_agregar_funcion.clicked.connect(self.abrir_agregar_funcion)
        self.btn_eliminar_funcion.clicked.connect(self.abrir_eliminar_funcion)
        self.btn_modificar_funcion.clicked.connect(self.abrir_modificar_funcion)
        self.btn_actualizar.clicked.connect(self.actualizar_cartelera)
        self.btn_comprar.clicked.connect(self.abrir_seleccionar_butacas)
        self.btn_mostrar_todo_funcion.clicked.connect(self.mostrar_todas_las_funciones)
        self.comboBox_idfunciones.currentTextChanged.connect(self.cargar_Funciones_en_tabla)
        self.btn_actualizar_funcion.clicked.connect(self.mostrar_todas_las_funciones)
        # Configuración inicial de la tabla, ComboBox y fechas por defecto
        try:
            self.mostrar_todas_las_funciones()  # Mostrar todas las funciones al iniciar
            self.cargar_id_funciones_en_comboBox()  # Cargar IDs en el comboBox al iniciar
        except Exception as e:
            log(e, "error")

        # Configurar fechas de filtro por defecto a hoy
        hoy = QDate.currentDate()
        
        self.fecha_filtro_inicio_f.setCalendarPopup(True)
        self.fecha_filtro_inicio_f.setDate(hoy)
        self.fecha_filtro_fin_f.setCalendarPopup(True)
        self.fecha_filtro_fin_f.setDate(hoy)

        # Conectar señales de cambio de fecha para activar filtro solo si cambian
        self.fecha_filtro_inicio_f.dateChanged.connect(self.activar_filtro_fecha)
        self.fecha_filtro_fin_f.dateChanged.connect(self.activar_filtro_fecha)

        


        
                        
        #Configuracion botones pagina Historial
        self.fecha_historial.setCalendarPopup(True)
        self.fecha_historial.setDate(datetime.today())
        self.comboBox_historial_usuario.currentIndexChanged.connect(self.actualizar_comboBox)
        self.fecha_historial.editingFinished.connect(self.actualizar_tabla_fecha)
        self.fecha_seleccionada = False
        self.btn_filtrar.clicked.connect(self.filtrar_peliculas)






        # Control de los botones de la barra de títulos (minimizar, maximizar/restaurar, cerrar)
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(lambda: self.close())

        # Ocultar el botón de restaurar por defecto, ya que no está maximizada
        self.bt_restaurar.hide()

        # Asignar el evento al botón del menú lateral para animarlo
        self.bt_menu.clicked.connect(self.mover_menu)
        
        

        

        # Llenar tabla de usuarios al iniciar
        self.cargar_usuarios_en_tabla()
        # Llenar la tabla de Pelis al iniciar
        self.cargar_peliculas_en_tabla()
        # Llenar la tabla de historial al iniciar
        self.cargar_datos_historial()
        # Llenar la tabla de funciones al iniciar
        #Actualizar Cartelera
        self.actualizar_cartelera()
        self.cargar_usuarios_en_comboBox()
        self.estadistica_pelicula()
        self.estadisticas_individual()
        self.cargar_funciones_tabla_estadisticas()
        self.inicializar_tabla_estadisticas()

        
        self.btn_actualizar_estadisticas_peliculas.clicked.connect(self.estadistica_pelicula)
        
        
        # Conectar el botón de actualizar con el método cargar_usuarios_en_tabla
        self.btn_actualizarUsuario.clicked.connect(self.cargar_usuarios_en_tabla)
        self.btn_todo_filtro_usuario.clicked.connect(self.cargar_usuarios_en_tabla)
        # Conectar el botón de actualizar con el método cargar_pelis_en_tabla
        self.btn_actualizar_pelicula.clicked.connect(self.cargar_peliculas_en_tabla)
        # Conectar el botón de actualizar con el método cargar_datos_historial
        self.btn_regenerar_Todo.clicked.connect(self.mostrar_todos_los_datos_historial)
        # Conectar el botón de actualizar con el método cargar_Funciones_en_tabla
        self.btn_actualizarH.clicked.connect(self.cargar_datos_historial)

        self.comboBox_historial_usuario.currentIndexChanged.connect(self.filtrar_por_usuario)
        self.fecha_historial.dateChanged.connect(self.filtrar_por_fecha)


        self.btn_todo_funciones.clicked.connect(self.mostrar_todas_las_funciones_estadisticas)
        
        self.btn_actualizar_estadisticas_f.clicked.connect(self.actualizar_funciones_estadisticas)
        self.filtro_fecha_funcion_esta.dateChanged.connect(self.activar_filtro_fecha_estadisticas) 
        self.filtro_fecha_funcion_esta.setCalendarPopup(True)
        self.filtro_fecha_funcion_esta.setDisplayFormat("dd/MM/yyyy")  
        self.filtro_fecha_funcion_esta.setDate(QDate.currentDate())
        self.tableWidget_estadisticas_funciones.itemClicked.connect(self.mostrar_resumen_funcion_seleccionada)
        self.filtro_fecha_activado = False  






        

        self.grafico_funciones(self.layout_grafico)
        





#==============================================================================================================
#Venta de Entradas

    def actualizar_cartelera(self):
        """Carga las funciones desde hoy en adelante y actualiza las imágenes de la cartelera."""
        # Obtener la fecha actual y todas las funciones en adelante
        fecha_actual = datetime.now().date()
        funciones = self.db.obtener_funciones()
        funciones_futuras = [f for f in funciones if f[2].date() >= fecha_actual]  # Filtra funciones desde hoy en adelante

        # Cargar imágenes asociadas a las funciones
        if funciones_futuras:
            self.funciones_detalladas = []  # Lista para almacenar cada función individualmente
            peliculas_bd = self.db.obtener_peliculas()

            for funcion in funciones_futuras:
                id_funcion = funcion[0]  # Asegúrate de que el ID de la función sea el primer elemento
                id_pelicula = funcion[1]
                pelicula_data = next((p for p in peliculas_bd if p[0] == id_pelicula), None)

                if pelicula_data:
                    nombre_pelicula = pelicula_data[1]
                    nombre_imagen = pelicula_data[3]
                    ruta_imagen = os.path.join(self.carpeta_imagenes, nombre_imagen)

                    # Calcular las butacas disponibles
                    asientos_reservados = self.db.obtener_asientos_reservados(id_funcion)
                    butacas_disponibles = 30 - len(asientos_reservados)  # 30 es el número máximo de butacas

                    # Guardar cada función como una entrada única en funciones_detalladas, incluyendo el id_funcion
                    self.funciones_detalladas.append({
                        "id_funcion": id_funcion,
                        "titulo": nombre_pelicula,
                        "ruta_imagen": ruta_imagen,
                        "descripcion": pelicula_data[2],
                        "fecha_hora": funcion[2],
                        "sala": funcion[3],
                        "precio": funcion[4],
                        "butacas_disponibles": butacas_disponibles  # Agregar el número de butacas disponibles
                    })

            self.indice_pelicula = 0
        else:
            # print("No hay funciones programadas a partir de hoy.")
            self.funciones_detalladas = []
            self.indice_pelicula = -1
            self.Imagen_cartelera.setText("No hay funciones programadas.")
            self.Imagen_cartelera.setAlignment(Qt.AlignCenter)
            font = self.Imagen_cartelera.font()
            font.setPointSize(14)
            self.Imagen_cartelera.setFont(font)
            return  # No llamar a mostrar_pelicula si no hay funciones

        # Llama a mostrar_pelicula con un pequeño retraso al iniciar
        QTimer.singleShot(100, self.mostrar_pelicula)

    def mostrar_pelicula(self):
        """Muestra la información de la función actual en el QLabel Imagen_cartelera, LineEdit_nombre y textEdit_descripcion."""
        if self.funciones_detalladas and 0 <= self.indice_pelicula < len(self.funciones_detalladas):
            funcion_actual = self.funciones_detalladas[self.indice_pelicula]

            # Cargar y mostrar la imagen de la función actual
            ruta_imagen = funcion_actual["ruta_imagen"]
            pixmap = QPixmap(ruta_imagen)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(
                    self.Imagen_cartelera.size(),
                    Qt.IgnoreAspectRatio,
                    Qt.SmoothTransformation
                )
                self.Imagen_cartelera.setPixmap(pixmap)
            else:
                print(f"No se pudo cargar la imagen: {ruta_imagen}")

            # Mostrar título y detalles de la función actual
            self.lineEdit_nombre.setText(funcion_actual["titulo"])
            self.lineEdit_nombre.setReadOnly(True)  # Hacer el campo de solo lectura

            # Construir el texto descriptivo
            detalles = (
                # f"Descripción: {funcion_actual['descripcion']}\n"
                f"Fecha y Hora: {funcion_actual['fecha_hora']}\n"
                f"Sala: {funcion_actual['sala']}\n"
                f"Precio: ${funcion_actual['precio']}"
            )
            self.textEdit_descripion.setPlainText(detalles)
            self.textEdit_descripion.setReadOnly(True)  # Hacer el campo de solo lectura

            # Actualizar las butacas disponibles
            self.Butacas_disponibles.setText(f"Butacas disponibles: {funcion_actual['butacas_disponibles']}")
            self.Butacas_disponibles.setReadOnly(True)  # Hacer el campo de solo lectura
        else:
            # Limpiar la interfaz si no hay funciones disponibles o índice no válido
            self.Imagen_cartelera.clear()
            self.Imagen_cartelera.setText("No hay funciones disponibles para hoy.")
            self.Imagen_cartelera.setAlignment(Qt.AlignCenter)
            font = self.Imagen_cartelera.font()
            font.setPointSize(14)
            self.Imagen_cartelera.setFont(font)
            self.lineEdit_nombre.clear()
            self.textEdit_descripcion.clear()
            self.Butacas_disponibles.clear()

    def resizeEvent(self, event):
        """Se llama cada vez que la ventana o el QLabel cambia de tamaño."""
        self.mostrar_pelicula()
        super().resizeEvent(event)

    def pelicula_anterior(self):
        """Cambia a la función anterior en el carrusel y actualiza la imagen."""
        if self.funciones_detalladas:
            self.indice_pelicula = (self.indice_pelicula - 1) % len(self.funciones_detalladas)
            self.mostrar_pelicula()

    def pelicula_siguiente(self):
        """Cambia a la siguiente función en el carrusel y actualiza la imagen."""
        if self.funciones_detalladas:
            self.indice_pelicula = (self.indice_pelicula + 1) % len(self.funciones_detalladas)
            self.mostrar_pelicula()


    #==============================================================================================================
    
    # Configuracion Pagina Usuario
    def abrir_agregar_usuario(self):
        self.agregar_usuario = AgregarUsuario(self)
        self.agregar_usuario.show()
        
    def abrir_eliminar_usuarios(self):
        self.eliminar_usuario = EliminarUsuario()
        self.eliminar_usuario.show()
    
    def abrir_modificar_usuario(self):
        self.modificar_usuario = ModificarUsuario()
        self.modificar_usuario.show()
    

    # Configuracion Pagina Peliculas
    def abrir_agregar_pelicula(self):
        self.agregar_pelicula = AgregarPeliculas()
        self.agregar_pelicula.show()
    
    def abrir_eliminar_pelicula(self):
        self.eliminar_pelicula = EliminarPelicula()
        self.eliminar_pelicula.show()
    
    def abrir_modificar_pelicula(self):
        self.modificar_pelicula = ModificarPelicula()
        self.modificar_pelicula.show()
    
    
    # Configuracion Pagina Funciones
    def abrir_agregar_funcion(self):
        self.agregar_funcion = AgregarFuncion()
        self.agregar_funcion.show()
    
    def abrir_eliminar_funcion(self):
        self.eliminar_funcion = EliminarFuncion()
        self.eliminar_funcion.show()
    
    def abrir_modificar_funcion(self):
        self.modificar_funcion = ModificarFuncion()
        self.modificar_funcion.show()

    def abrir_seleccionar_butacas(self):
        if self.funciones_detalladas and 0 <= self.indice_pelicula < len(self.funciones_detalladas):
            id_funcion = self.funciones_detalladas[self.indice_pelicula]['id_funcion']  # Asegúrate de que este campo contenga el ID correcto
            self.seleccionar_butacas = Cine(id_funcion)
            self.seleccionar_butacas.show()
        

    #==============================================================================================================
    # Configuracion Pagina Usuarios 

    def cargar_usuarios_en_tabla(self, filtros=None):
        """
        Carga los usuarios de la base de datos con filtros opcionales.
        El filtro de nombre tiene la mayor prioridad.
        """
        try:
            # Consultar usuarios con filtros
            usuarios = self.db.obtener_usuarios(filtros)

            # Limpiar la tabla antes de cargar nuevos datos
            self.tableWidget_usuarios.setRowCount(0)

            # Llenar la tabla con los datos obtenidos
            for row_number, row_data in enumerate(usuarios):
                self.tableWidget_usuarios.insertRow(row_number)

                nombre_usuario = row_data[1]       # NombreUsuario
                grupo = row_data[3]                # Grupo
                fecha_creacion = row_data[4]       # FechaCreacion
                fecha_modificacion = row_data[5]   # FechaModificacion

                # Insertar datos en la tabla
                self.tableWidget_usuarios.setItem(row_number, 0, QTableWidgetItem(str(nombre_usuario)))
                self.tableWidget_usuarios.setItem(row_number, 1, QTableWidgetItem(str(grupo)))
                self.tableWidget_usuarios.setItem(row_number, 2, QTableWidgetItem(str(fecha_creacion)))
                self.tableWidget_usuarios.setItem(row_number, 3, QTableWidgetItem(str(fecha_modificacion)))

            # Ajustar el tamaño de las columnas
            self.tableWidget_usuarios.resizeColumnsToContents()
            self.tableWidget_usuarios.resizeRowsToContents()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al cargar usuarios: {str(e)}')

    def cargar_rol_filtro(self):
        """
        Carga la lista de roles únicos en el combo box de filtro.
        """
        try:
            # Obtener todos los usuarios
            usuarios = self.db.obtener_usuarios()

            # Limpiar y configurar el comboBox
            self.comboBox_filtro_usuario.clear()
            self.comboBox_filtro_usuario.addItem("Seleccionar Categoría")  # Opción predeterminada

            # Extraer roles únicos y añadirlos al comboBox
            roles_unicos = {usuario[3] for usuario in usuarios}  # Columna de roles
            for rol in sorted(roles_unicos):
                self.comboBox_filtro_usuario.addItem(rol)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'No se pudo cargar la lista de roles. Error: {str(e)}')

    def aplicar_filtros(self):
        """
        Aplica los filtros a la tabla. Prioriza el filtro por nombre sobre los demás.
        Los filtros solo se aplican al presionar el botón 'btn_buscar_usuario'.
        """
        # Obtener el texto del campo de nombre
        nombre = self.nombre_filtro_usuario.text().strip()

        # Verificar si el filtro por nombre tiene prioridad
        if nombre:  
            # Si hay un nombre, se desactivan los otros filtros
            filtros = {"nombre": nombre}
        else:
            # Si no hay filtro por nombre, considerar grupo y fecha
            grupo = self.comboBox_filtro_usuario.currentText()
            if grupo == "Seleccionar Categoría":  # Si no se seleccionó un grupo específico
                grupo = None

            fecha_creacion = self.fecha_creacion_filtro_usuario.date().toString("yyyy-MM-dd") \
                if self.fecha_creacion_filtro_usuario.date().isValid() else None

            # Crear diccionario de filtros sin nombre
            filtros = {
                "fecha_creacion": fecha_creacion,
                "grupo": grupo,
            }

        # Recargar la tabla con los filtros aplicados
        self.cargar_usuarios_en_tabla(filtros=filtros)


    #==============================================================================================================
    # Configuracion Pagina Historial
    
    def cargar_usuarios_en_comboBox(self):
        """Carga todos los usuarios en el comboBox_historial_usuario."""
        try:
            usuarios = self.db.obtener_usuarios()  # Obtener todos los usuarios de la base de datos

            # Limpiar el comboBox antes de cargar los usuarios
            self.comboBox_historial_usuario.clear()

            # Añadir opción de selección general (opcional)
            self.comboBox_historial_usuario.addItem("Todos los usuarios", None)

            # Añadir cada usuario al comboBox
            for usuario in usuarios:
                id_usuario = usuario[0]  # Asumiendo que el ID del usuario está en la primera columna
                nombre_usuario = usuario[1]  # Asumiendo que el nombre del usuario está en la segunda columna
                self.comboBox_historial_usuario.addItem(nombre_usuario, id_usuario)

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar los usuarios en el comboBox.')

    def mostrar_todos_los_datos_historial(self):
        """Muestra todos los registros del historial sin filtros."""
        try:
            # Desactivar el filtro de fecha si estaba activado
            self.filtro_fecha_activado = False

            # Reiniciar el comboBox a "Todos los usuarios"
            self.comboBox_historial_usuario.setCurrentIndex(0)

            # Cargar todos los registros sin filtro
            historial = self.db.obtener_historial()

            # Ordenar por fecha en orden descendente
            historial_ordenado = sorted(historial, key=lambda x: x[2], reverse=True)

            # Limpiar y cargar los datos en la tabla
            self.tableWidget_historial.setRowCount(0)
            for row_number, row_data in enumerate(historial_ordenado):
                id_usuario = row_data[1]
                usuario = self.db.obtener_usuario_por_id(id_usuario)
                nombre_usuario = usuario[1] if usuario else "Desconocido"
                fecha_hora = row_data[2]
                accion = row_data[3]

                # Insertar fila en la tabla
                self.tableWidget_historial.insertRow(row_number)
                self.tableWidget_historial.setItem(row_number, 0, QTableWidgetItem(nombre_usuario))
                self.tableWidget_historial.setItem(row_number, 1, QTableWidgetItem(str(fecha_hora)))
                self.tableWidget_historial.setItem(row_number, 2, QTableWidgetItem(accion))

            # Ajustar las columnas y filas
            self.tableWidget_historial.resizeColumnsToContents()
            self.tableWidget_historial.resizeRowsToContents()

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar la tabla de historial sin filtros.')

    def cargar_datos_historial(self):
        """Carga y filtra los registros del historial según el comboBox y la fecha."""
        try:
            # Obtener todos los registros del historial
            historial = self.db.obtener_historial()

            # Filtro por usuario seleccionado
            id_usuario_seleccionado = self.comboBox_historial_usuario.currentData()
            # print(f"ID usuario seleccionado: {id_usuario_seleccionado}")
            if id_usuario_seleccionado is not None:
                historial = [registro for registro in historial if registro[1] == id_usuario_seleccionado]
            # print(f"Historial filtrado por usuario: {historial}")

            # Filtro por fecha seleccionada
            if self.filtro_fecha_activado:
                fecha_seleccionada = self.fecha_historial.date().toPyDate()
                # print(f"Fecha seleccionada: {fecha_seleccionada}")
                historial = [registro for registro in historial if registro[2].date() == fecha_seleccionada]
            # print(f"Historial filtrado por fecha: {historial}")

            # Ordenar por fecha en orden descendente
            historial_ordenado = sorted(historial, key=lambda x: x[2], reverse=True)
            # print(f"Historial ordenado final: {historial_ordenado}")

            # Limpiar y cargar los datos en la tabla
            self.tableWidget_historial.setRowCount(0)
            for row_number, row_data in enumerate(historial_ordenado):
                id_usuario = row_data[1]
                usuario = self.db.obtener_usuario_por_id(id_usuario)
                nombre_usuario = usuario[1] if usuario else "Desconocido"
                fecha_hora = row_data[2]
                accion = row_data[3]

                # Insertar fila en la tabla
                self.tableWidget_historial.insertRow(row_number)
                self.tableWidget_historial.setItem(row_number, 0, QTableWidgetItem(nombre_usuario))
                self.tableWidget_historial.setItem(row_number, 1, QTableWidgetItem(str(fecha_hora)))
                self.tableWidget_historial.setItem(row_number, 2, QTableWidgetItem(accion))

            # Ajustar las columnas y filas
            self.tableWidget_historial.resizeColumnsToContents()
            self.tableWidget_historial.resizeRowsToContents()

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar la tabla de historial.')
    
    def actualizar_comboBox(self):
        """Actualiza la tabla según la selección del comboBox."""
        self.cargar_datos_historial()

    def filtrar_por_usuario(self):
        """Filtra los registros del historial según el usuario seleccionado."""
        # print("Método filtrar_por_usuario llamado")
        self.cargar_datos_historial()

    def filtrar_por_fecha(self):
        """Filtra los registros del historial según la fecha seleccionada."""
        # print("Método filtrar_por_fecha llamado")
        self.filtro_fecha_activado = True
        self.cargar_datos_historial()







    
    #==============================================================================================================
    # Configuracion Pagina Funciones

    def cargar_id_funciones_en_comboBox(self):
        """Carga todos los IDs de funciones en el comboBox_idfunciones con nombre de película (o mensaje si fue eliminada)."""
        try:
            funciones = self.db.obtener_funciones()

            self.comboBox_idfunciones.clear()
            self.comboBox_idfunciones.addItem("Todas las funciones", None)  # Opción general

            for funcion in funciones:
                id_funcion = funcion[0]
                nombre_pelicula = funcion[1] if funcion[1] is not None else "Película eliminada"
                texto_mostrado = f"{id_funcion} - {nombre_pelicula}"
                self.comboBox_idfunciones.addItem(texto_mostrado, id_funcion)

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar los IDs de funciones en el comboBox.')


    def actualizar_tabla_comboBox(self):
        """Actualiza la tabla según la selección del comboBox de funciones."""
        self.cargar_Funciones_en_tabla()

    def actualizar_tabla_fecha(self):
        """Actualiza la tabla al confirmar la selección de una fecha."""
        self.cargar_Funciones_en_tabla()


    def activar_filtro_fecha(self):
        """Activa el filtro de fecha cuando se cambia una fecha de filtro."""
        self.filtro_fecha_activado = True
        self.cargar_Funciones_en_tabla()

    def cargar_Funciones_en_tabla(self):
        """Carga las funciones en la tabla aplicando filtros de ID y fechas solo si están activados."""
        try:
            if not self.db:
                return

            funciones = self.db.obtener_funciones()  # Obtener funciones desde la base de datos

            # Filtrar por ID si hay uno seleccionado
            id_funcion_seleccionado = self.comboBox_idfunciones.currentData()
            if id_funcion_seleccionado:
                funciones = [funcion for funcion in funciones if funcion[0] == id_funcion_seleccionado]

            # Aplicar filtro de fecha solo si está activado
            if getattr(self, 'filtro_fecha_activado', False):
                fecha_inicio = self.fecha_filtro_inicio_f.date().toPyDate()
                fecha_fin = self.fecha_filtro_fin_f.date().toPyDate()
                funciones = [funcion for funcion in funciones if fecha_inicio <= funcion[2].date() <= fecha_fin]

            self.tableWidget_funciones.setRowCount(0)  # Limpiar la tabla

            for row_number, row_data in enumerate(funciones):
                self.tableWidget_funciones.insertRow(row_number)

                id_funcion = row_data[0]
                asientos_reservados = self.db.obtener_asientos_reservados(id_funcion)
                total_butacas = 30
                butacas_vendidas = len(asientos_reservados)
                porcentaje_vendido = (butacas_vendidas / total_butacas) * 100

                color = QColor("red") if porcentaje_vendido <= 40 else QColor("orange") if porcentaje_vendido <= 60 else QColor("lightgreen") if porcentaje_vendido <= 80 else QColor("darkgreen")

                # Verificar si la película fue eliminada
                pelicula = row_data[1] if row_data[1] is not None else "Película eliminada"

                datos_visibles = [row_data[0], pelicula, row_data[2], row_data[3], row_data[4], butacas_vendidas]

                for column_number, data in enumerate(datos_visibles):
                    item = QTableWidgetItem(str(data))
                    if column_number == 0:
                        item.setData(Qt.UserRole, id_funcion)
                    item.setBackground(color)
                    self.tableWidget_funciones.setItem(row_number, column_number, item)

            self.tableWidget_funciones.setColumnHidden(0, True)
            self.tableWidget_funciones.resizeColumnsToContents()

        except Exception as e:
            if getattr(self, 'filtro_fecha_activado', False) or id_funcion_seleccionado:
                log(e, "error")
                QMessageBox.critical(self, 'Error', 'No se pudo cargar la tabla de funciones.')

    def mostrar_todas_las_funciones(self):
        """Muestra todas las funciones en la tabla sin aplicar filtros."""
        try:
            funciones = self.db.obtener_funciones()
            self.tableWidget_funciones.setRowCount(0)

            for row_number, row_data in enumerate(funciones):
                self.tableWidget_funciones.insertRow(row_number)

                id_funcion = row_data[0]
                asientos_reservados = self.db.obtener_asientos_reservados(id_funcion)
                total_butacas = 30
                butacas_vendidas = len(asientos_reservados)
                porcentaje_vendido = (butacas_vendidas / total_butacas) * 100

                color = QColor("red") if porcentaje_vendido <= 40 else QColor("orange") if porcentaje_vendido <= 60 else QColor("lightgreen") if porcentaje_vendido <= 80 else QColor("darkgreen")

                # Verificar si la película fue eliminada
                pelicula = row_data[1] if row_data[1] is not None else "Película eliminada"

                datos_visibles = [row_data[0], pelicula, row_data[2], row_data[3], row_data[4], butacas_vendidas]

                for column_number, data in enumerate(datos_visibles):
                    item = QTableWidgetItem(str(data))
                    if column_number == 0:
                        item.setData(Qt.UserRole, id_funcion)
                    item.setBackground(color)
                    self.tableWidget_funciones.setItem(row_number, column_number, item)

            self.tableWidget_funciones.setColumnHidden(0, True)
            self.tableWidget_funciones.resizeColumnsToContents()

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo mostrar todas las funciones en la tabla.')


    #==============================================================================================================
    # Configuracion Estadisticas Funciones

    def inicializar_tabla_estadisticas(self):
        """Inicializa la tabla de estadísticas desactivando el filtro de fecha y mostrando todas las funciones."""
        self.filtro_fecha_activado = False  # Desactivar el filtro al inicio
        self.filtro_fecha_funcion_esta.setDate(QDate.currentDate())  # Configurar la fecha actual en el filtro
        self.cargar_funciones_tabla_estadisticas()  # Cargar todas las funciones sin filtros
    
    def activar_filtro_fecha_estadisticas(self):
        """Activa el filtro de fecha cuando se cambia la fecha en el filtro."""
        self.filtro_fecha_activado = True
        self.cargar_funciones_tabla_estadisticas()  # Cargar funciones con el filtro activado

    def mostrar_todas_las_funciones_estadisticas(self):
        self.filtro_fecha_activado = False
        self.cargar_funciones_tabla_estadisticas()
        # print("Filtro desactivado. Mostrando todas las funciones.")

    def cargar_funciones_tabla_estadisticas(self):
        """Carga las funciones en la tabla de estadísticas, aplicando o no los filtros según corresponda."""
        try:
            if not self.db:
                # print("No se encontró la conexión a la base de datos.")
                return

            # Obtener todas las funciones de la base de datos
            funciones = self.db.obtener_funciones_con_nombre_peliculas()

            # Si no hay funciones, limpiar la tabla y salir
            if not funciones:
                # print("No se encontraron funciones para cargar.")
                self.tableWidget_estadisticas_funciones.setRowCount(0)
                return

            # Filtrar las funciones si el filtro de fecha está activado
            if self.filtro_fecha_activado:
                fecha_seleccionada = self.filtro_fecha_funcion_esta.date().toPyDate()
                funciones = [funcion for funcion in funciones if funcion[2].date() == fecha_seleccionada]

            # Limpiar la tabla antes de cargar datos
            self.tableWidget_estadisticas_funciones.setRowCount(0)

            # Si no hay funciones después del filtro, dejar la tabla vacía
            if not funciones:
                # print("No hay funciones para mostrar después del filtro.")
                return

            # Insertar funciones en la tabla
            for row_number, row_data in enumerate(funciones):
                self.tableWidget_estadisticas_funciones.insertRow(row_number)

                id_funcion = row_data[0]
                nombre_pelicula = row_data[1]
                fecha_hora = row_data[2]

                # Crear los items de la tabla
                item_nombre_pelicula = QTableWidgetItem(str(nombre_pelicula))
                item_fecha_hora = QTableWidgetItem(str(fecha_hora))
                item_id_funcion = QTableWidgetItem()

                # Guardar el ID como dato interno usando UserRole
                item_nombre_pelicula.setData(Qt.UserRole, id_funcion)

                # Insertar los items en las columnas respectivas
                self.tableWidget_estadisticas_funciones.setItem(row_number, 0, item_nombre_pelicula)
                self.tableWidget_estadisticas_funciones.setItem(row_number, 1, item_fecha_hora)
                self.tableWidget_estadisticas_funciones.setItem(row_number, 2, item_id_funcion)

            # Ocultar la columna del ID de la función
            self.tableWidget_estadisticas_funciones.setColumnHidden(2, True)

            # Ajustar el ancho de las columnas
            self.tableWidget_estadisticas_funciones.resizeColumnsToContents()

            # print(f"Se cargaron {len(funciones)} funciones en la tabla.")

        except Exception as e:
            # print(f"Error general al cargar la tabla: {e}")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar la tabla de funciones.')

    def mostrar_resumen_funcion_seleccionada(self, item):
        """Muestra un resumen de la función seleccionada en la tabla."""
        try:
            row = item.row()
            funcion_id = self.tableWidget_estadisticas_funciones.item(row, 0).data(Qt.UserRole)
            # print(f"Función seleccionada, ID: {funcion_id}")  # Depuración
            self.mostrar_informacion_funcion(funcion_id)
        except Exception as e:
            # print(f"Error al mostrar el resumen: {e}")  # Depuración
            QMessageBox.critical(self, "Error", f"Ocurrió un error al mostrar el resumen: {e}")

    def mostrar_informacion_funcion(self, funcion_id):
        """Muestra un QMessageBox con la información de una función específica."""
        try:
            asientos_reservados = self.db.obtener_asientos_reservados(funcion_id)
            butacas_vendidas = len(asientos_reservados)

            funcion_info = self.db.obtener_funcion_por_id(funcion_id)
            if funcion_info:
                id_sala, precio_funcion, fecha_hora_funcion = funcion_info[3], funcion_info[4], funcion_info[2]

                sala_info = self.db.obtener_sala_por_id(id_sala)
                if not sala_info:
                    QMessageBox.warning(self, "Advertencia", "No se encontró información de la sala asociada.")
                    return

                total_butacas = sala_info['NumeroButacas']
                butacas_restantes = total_butacas - butacas_vendidas
                dinero_recaudado = precio_funcion * butacas_vendidas

                mensaje = (
                    f"ID de la función: {funcion_id}\n"
                    f"Butacas vendidas: {butacas_vendidas}\n"
                    f"Butacas restantes: {butacas_restantes}\n"
                    f"Dinero recaudado: ${dinero_recaudado:.2f}\n"
                )

                if fecha_hora_funcion < datetime.now():
                    porcentaje_ocupacion = (butacas_vendidas / total_butacas) * 100 if total_butacas > 0 else 0
                    mensaje += f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%"

                self.textEdit_info_funciones.setText(mensaje)
            else:
                QMessageBox.warning(self, "Advertencia", "No se encontró información para la función seleccionada.")

        except Exception as e:
            # print(f"Error al mostrar información de la función: {e}")  # Depuración
            QMessageBox.critical(self, 'Error', f'No se pudo obtener la información de la función: {e}')

    def grafico_funciones(self, layout=None):
        """
        Genera un gráfico de barras con la recaudación total por día y lo agrega al layout especificado.
        Si no se especifica un layout, se utiliza el layout predeterminado `self.layout_grafico`.

        :param layout: Layout de PyQt donde se agregará el gráfico.
        """
        if layout is None:
            layout = self.layout_grafico  

        # Limpiar el layout antes de agregar un nuevo gráfico
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        try:
            # Obtener datos de la base de datos
            datos = self.db.obtener_recaudacion_por_dia()
            if not datos:
                # print("No hay datos disponibles para la recaudación.")
                return

            # Procesar datos
            fechas = [dato[0].strftime('%Y-%m-%d') for dato in datos]
            recaudaciones = [dato[1] for dato in datos]

            # Crear la figura del gráfico
            fig, ax = plt.subplots(dpi=100, figsize=(3.8, 2.5), tight_layout=True, facecolor='white')
            ax.bar(fechas, recaudaciones, color='blue')
            ax.set_title('Recaudación Total por Día', fontsize=8)
            ax.set_xlabel('Fecha', fontsize=7)
            ax.set_ylabel('Recaudación ($)', fontsize=7)
            ax.tick_params(axis='x', labelsize=6, rotation=45)
            ax.tick_params(axis='y', labelsize=6)

            # Ajustar márgenes
            plt.subplots_adjust(bottom=0.35)

            # Crear el canvas de matplotlib y agregarlo al layout
            canvas = FigureCanvas(fig)
            layout.addWidget(canvas)

        except Exception as e:
            print(f"Error al generar el gráfico: {e}")

    def actualizar_funciones_estadisticas(self):
        """
        Actualiza las estadísticas y gráficos relacionados con las funciones.
        """
        self.mostrar_todas_las_funciones_estadisticas()  # Actualiza otras estadísticas
        self.grafico_funciones()  # Genera y muestra el gráfico






    #==============================================================================================================
    # Configuracion Pagina Pelis

    def inicializar_tabla_peliculas(self):
        """Inicializa la tabla de películas mostrando todas las películas sin filtros."""
        self.filtro_fecha_activado = False  # Desactiva el filtro de fechas al inicio
        hoy = QDate.currentDate() 
        self.fecha_inicio_pelicula.setDate(hoy)  # Fecha mínima inicial
        self.fecha_fin_pelicula.setDate(QDate.currentDate())  # Fecha actual como límite
        self.filtro_nombre_pelicula.clear()  # Limpia el filtro de nombre
        self.cargar_peliculas_en_tabla()  # Cargar todas las películas sin filtros

    def cargar_peliculas_en_tabla(self):
        """Carga las películas en la tabla aplicando los filtros automáticamente."""
        try:
            if not self.db:
                QMessageBox.critical(self, "Error", "No se encontró la conexión a la base de datos.")
                return

            # Obtener todas las películas desde la base de datos
            peliculas = self.db.obtener_peliculas()

            # Prioridad: Si hay un filtro por nombre, desactivar el filtro de fechas
            filtro_nombre = self.filtro_nombre_pelicula.text().strip()
            if filtro_nombre:
                self.filtro_fecha_activado = False  # Desactiva el filtro de fechas
                peliculas = [
                    p for p in peliculas if filtro_nombre.lower() in p[1].lower()
                ]
            elif getattr(self, "filtro_fecha_activado", False):
                # Filtrar por rango de fechas si no hay filtro por nombre
                fecha_inicio_pelicula = self.fecha_inicio_pelicula.date().toPyDate()
                fecha_fin_pelicula = self.fecha_fin_pelicula.date().toPyDate()
                peliculas = [
                    p for p in peliculas if fecha_inicio_pelicula <= p[6] <= fecha_fin_pelicula
                ]

            # Limpiar la tabla antes de cargar los datos
            self.tableWidget_pelis.setRowCount(0)

            # Insertar las películas en la tabla
            for row_number, pelicula in enumerate(peliculas):
                id_pelicula = pelicula[0]
                nombre = pelicula[1]
                fecha_inicio_pelicula = pelicula[6]
                fecha_fin_pelicula = pelicula[7]
                duracion = pelicula[8]
                clasificacion = pelicula[9]

                # Insertar cada dato en su respectiva columna
                self.tableWidget_pelis.insertRow(row_number)
                self.tableWidget_pelis.setItem(row_number, 0, QTableWidgetItem(str(nombre)))
                self.tableWidget_pelis.setItem(row_number, 1, QTableWidgetItem(str(fecha_inicio_pelicula)))
                self.tableWidget_pelis.setItem(row_number, 2, QTableWidgetItem(str(fecha_fin_pelicula)))
                self.tableWidget_pelis.setItem(row_number, 3, QTableWidgetItem(str(duracion)))
                self.tableWidget_pelis.setItem(row_number, 4, QTableWidgetItem(str(clasificacion)))

                # Guardar el ID de la película en UserRole
                self.tableWidget_pelis.item(row_number, 0).setData(Qt.UserRole, id_pelicula)

            # Ajustar el tamaño de las columnas al contenido
            self.tableWidget_pelis.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cargar la tabla: {str(e)}")

    def activar_filtro_fecha_peliculas(self):
        """Activa el filtro de fechas al cambiar las fechas si no hay un filtro por nombre."""
        if not self.filtro_nombre_pelicula.text().strip():  # Solo activar si no hay filtro de nombre
            self.filtro_fecha_activado = True
            self.cargar_peliculas_en_tabla()

    def desactivar_filtros(self):
        """Desactiva todos los filtros y muestra todas las películas."""
        self.filtro_fecha_activado = False
        self.filtro_nombre_pelicula.clear()
        self.inicializar_tabla_peliculas()

    def mostrar_todas_las_peliculas(self):
        """Muestra todas las películas sin aplicar ningún filtro (botón 'Ver todo')."""
        self.filtro_nombre_pelicula.clear()  # Limpia el filtro de nombre
        self.filtro_fecha_activado = False  # Desactiva el filtro de fechas
        self.inicializar_tabla_peliculas()


    def mostrar_informacion_pelicula(self):
        # Verificar si hay una película seleccionada
        pelicula_id = self.obtener_pelicula_seleccionada()

        if pelicula_id is None:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una película.")
            return

        # Obtener los datos de la película
        datos_pelicula = self.db.obtener_datos_pelicula(pelicula_id)
        if datos_pelicula is None:
            QMessageBox.critical(self, "Error", "No se pudo obtener la información de la película.")
            return

        # Obtener los géneros de la película
        generos = self.db.obtener_generos_pelicula(pelicula_id)
        generos_texto = ", ".join(generos) if generos else "Sin géneros"

        # Preparar el mensaje de la información de la película con el formato solicitado
        mensaje = (
            f"- Nombre:\n      {datos_pelicula['nombre']}\n"
            f"- Descripción:\n      {datos_pelicula['resumen']}\n"
            f"- País de Origen:\n      {datos_pelicula['pais_origen']}\n"
            f"- Fecha de Estreno:\n      {datos_pelicula['fecha_estreno']}\n"
            f"- Fecha de Inicio:\n      {datos_pelicula['fecha_inicio']}\n"
            f"- Fecha de Fin:\n      {datos_pelicula['fecha_fin']}\n"
            f"- Duración:\n      {datos_pelicula['duracion']} minutos\n"
            f"- Clasificación:\n      {datos_pelicula['clasificacion']}\n"
            f"- Géneros:\n      {generos_texto}\n"
        )

        # Mostrar el mensaje en un QMessageBox
        QMessageBox.information(self, "Información de la Película", mensaje)
        
    #==============================================================================================================
    # Configuracion Estadisticas Pelis

    def actualizar_estadisticas(self, id_pelicula):
        try:
            # Obtener datos desde la base de datos considerando todas las funciones
            porcentaje_asistencia, capacidad_total, total_vendidos = self.db.calcular_porcentaje_asistencia(id_pelicula)

            # Imprimir resultados para depuración
            # print(f"ID Película: {id_pelicula}")
            # print(f"Capacidad Total: {capacidad_total}, Total Vendidos: {total_vendidos}")

            # Actualizar los elementos de la interfaz con los datos calculados
            self.lineEdit_porcentaje_asistencia.setText(f"{porcentaje_asistencia:.2f}%")
            self.lineEdit_capacidad_total.setText(str(capacidad_total))
            self.lineEdit_total_vendidos.setText(str(total_vendidos))

            # print(f"Porcentaje calculado: {porcentaje_asistencia:.2f}%")
        except Exception as e:
            print(f"Error al actualizar estadísticas: {e}")

    def estadistica_pelicula(self): 
        """Carga estadísticas generales de las películas."""
        try:
            # Cantidad de Películas
            peliculas = self.db.obtener_peliculas()
            total_peliculas = len(peliculas)
            
            # Top 10 de películas más vistas
            peliculas_mas_vistas = self.db.obtener_peliculas_mas_vistas()
            peliculas_vistas_texto = "\n".join(
                [f"{pelicula['NombrePelicula']} (ID: {pelicula['IdPelicula']}), Ventas: {pelicula['CantidadVentas']}" 
                for pelicula in peliculas_mas_vistas]
            )
            
            # Top 5 géneros más rentables
            generos_mas_rentables = self.db.obtener_generos_mas_rentables()
            generos_rentables_texto = "\n".join(
                [f"{genero['Genero']}, Ingresos Totales: ${genero['IngresosTotales']}" 
                for genero in generos_mas_rentables]
            )
            
            # Crear el mensaje completo
            mensaje1 = f"{total_peliculas}\n\n"
            mensaje2 = f"{peliculas_vistas_texto}\n\n"
            mensaje3 = f"{generos_rentables_texto}"

            # Mostrar mensajes
            self.total_peliculas.setText(mensaje1)  # LineEdit
            self.textEdit_top10_peliculas.setText(mensaje2)  # TextEdit
            self.textEdit_top5_generos.setText(mensaje3)  # TextEdit
            
            # Bloquear edición en TextEdit
            self.textEdit_top10_peliculas.setReadOnly(True)
            self.textEdit_top5_generos.setReadOnly(True)

            # Cargar estadísticas individuales
            self.estadisticas_individual()

        except Exception as e:
            print(f"Ocurrió un error al cargar estadísticas generales: {str(e)}")

    def estadisticas_individual(self):
        """Carga las estadísticas de todas las películas en la tabla."""
        try:
            peliculas = self.db.obtener_peliculas()
            self.tabla_estadistica_peli.setRowCount(0)  # Limpia la tabla antes de insertar datos

            for row_number, pelicula in enumerate(peliculas):
                id_pelicula = pelicula[0]  # ID de la película
                nombre = pelicula[1]       # Nombre de la película

                # Insertar una nueva fila en la tabla
                self.tabla_estadistica_peli.insertRow(row_number)

                # Crear un QTableWidgetItem para la columna de ID
                item_id = QTableWidgetItem(str(id_pelicula))
                item_id.setData(Qt.UserRole, id_pelicula)  # Almacena el ID en UserRole
                self.tabla_estadistica_peli.setItem(row_number, 0, item_id)

                # Crear un QTableWidgetItem para el nombre de la película
                item_nombre = QTableWidgetItem(str(nombre))
                self.tabla_estadistica_peli.setItem(row_number, 1, item_nombre)

                # Verificar que el ID esté correctamente almacenado
                almacenado_id = self.tabla_estadistica_peli.item(row_number, 0).data(Qt.UserRole)

            # Ajustar el ancho de las columnas al contenido
            self.tabla_estadistica_peli.resizeColumnsToContents()

        except Exception as e:
            print(f"Ocurrió un error al cargar estadísticas individuales: {str(e)}")

    def calcular_estadisticas_pelicula(self):
        """Calcula y actualiza las estadísticas de la película seleccionada en la tabla."""
        try:
            # Obtener la fila seleccionada
            row = self.tabla_estadistica_peli.currentRow()

            if row == -1:
                return

            # Validar que la celda contenga un elemento válido
            item = self.tabla_estadistica_peli.item(row, 0)
            if not item:
                return

            # Recuperar el ID de la película desde el UserRole
            id_pelicula = item.data(Qt.UserRole)

            if not id_pelicula:
                return

            # Realizar consultas y cálculos
            porcentaje_asistencia, _, _ = self.db.calcular_porcentaje_asistencia(id_pelicula)
            horario_mas_exitoso, max_butacas = self.db.obtener_horario_mas_exitoso(id_pelicula)
            recaudacion_total = self.db.obtener_recaudacion_total(id_pelicula)

            # Formatear los resultados
            porcentaje = f"{porcentaje_asistencia:.2f}%" if porcentaje_asistencia > 0 else "0.00%"
            horario = (
                f"{horario_mas_exitoso} (Butacas llenas: {max_butacas})"
                if max_butacas > 0
                else "No disponible"
            )
            recaudacion = f"${recaudacion_total:.2f}" if recaudacion_total > 0 else "$0.00"

            # Actualizar los campos de la interfaz
            self.lineEdit_porcentaje_asistencia.setText(porcentaje)
            self.lineEdit_horario_mas_exitoso.setText(horario)
            self.lineEdit_recaudadcion_historica.setText(recaudacion)

        except Exception as e:
            print(f"Ocurrió un error al calcular las estadísticas: {str(e)}")

    def filtrar_peliculas(self):
        """Filtra las películas por nombre basado en el texto ingresado en filtro_nombre_estadistica."""
        try:
            # Obtener el texto del filtro
            texto_filtro = self.filtro_nombre_estadistica.text().strip().lower()

            # Si no hay texto en el filtro, recargar todas las películas
            if not texto_filtro:
                self.estadisticas_individual()
                return

            # Obtener todas las películas
            peliculas = self.db.obtener_peliculas()

            # Limpiar la tabla
            self.tabla_estadistica_peli.setRowCount(0)

            # Recorre las películas y filtra las que coinciden con el texto
            row_number = 0
            for pelicula in peliculas:
                id_pelicula = pelicula[0]
                nombre = pelicula[1]

                # Verificar si el nombre contiene el texto del filtro
                if texto_filtro in nombre.lower():
                    self.tabla_estadistica_peli.insertRow(row_number)

                    # Crear los items para cada celda
                    item_id = QTableWidgetItem(str(id_pelicula))
                    item_id.setData(Qt.UserRole, id_pelicula)  # Almacenar el ID en UserRole
                    self.tabla_estadistica_peli.setItem(row_number, 0, item_id)

                    item_nombre = QTableWidgetItem(nombre)
                    self.tabla_estadistica_peli.setItem(row_number, 1, item_nombre)

                    row_number += 1

            # Ajustar el ancho de las columnas al contenido
            self.tabla_estadistica_peli.resizeColumnsToContents()

        except Exception as e:
            print(f"Ocurrió un error al filtrar las películas: {str(e)}")

    def obtener_pelicula_seleccionada(self):
        """
        Obtiene el ID de la película seleccionada en la tabla `tableWidget_pelis`.
        """
        try:
            # Obtener la fila seleccionada
            selected_row = self.tableWidget_pelis.currentRow()

            if selected_row == -1:
                return None

            # Recuperar el elemento de la columna correspondiente (ID de la película)
            pelicula_id_item = self.tableWidget_pelis.item(selected_row, 0)
            
            if not pelicula_id_item:
                return None

            # Recuperar el ID desde UserRole
            pelicula_id = pelicula_id_item.data(Qt.UserRole)
            
            if not pelicula_id:
                return None

            return pelicula_id

        except Exception as e:
            print(f"Ocurrió un error al obtener la película seleccionada: {str(e)}")
            return None

    #==============================================================================================================
    #                         Configuracion - [] X

    # Método para minimizar la ventana
    def control_bt_minimizar(self):
        self.showMinimized()		

    # Método para restaurar la ventana a tamaño normal (si estaba maximizada)
    def control_bt_normal(self): 
        self.showNormal()		
        self.bt_restaurar.hide()  # Ocultar botón restaurar
        self.bt_maximizar.show()  # Mostrar botón maximizar

    # Método para maximizar la ventana
    def control_bt_maximizar(self): 
        self.showMaximized()
        self.bt_maximizar.hide()  # Ocultar botón maximizar
        self.bt_restaurar.show()  # Mostrar botón restaurar

    # Método para mover el menú lateral con una animación
    def mover_menu(self):
        width = self.frame_lateral.width()  # Obtener el ancho actual del menú lateral
        normal = 0  # Ancho mínimo del menú cuando está colapsado
        extender = 200 if width == 0 else normal  # Extender a 200 si está colapsado, si no, reducir a 0
        
        # Animación para cambiar el tamaño del menú lateral
        self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
        self.animacion.setDuration(300)  # Duración de la animación en milisegundos
        self.animacion.setStartValue(width)  # Valor inicial (ancho actual)
        self.animacion.setEndValue(extender)  # Valor final (colapsado o extendido)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)  # Tipo de animación

        self.animacion.start()  # Iniciar la animación

    
    ## SizeGrip: Reposicionar el grip cuando la ventana se redimensiona
    def resizeEvent(self, event):
        rect = self.rect()  # Obtener el rectángulo actual de la ventana
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)  # Mover el grip a la esquina inferior derecha
    
    ## Mover la ventana al hacer clic en la parte superior y arrastrar
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()  # Capturar la posición del cursor al hacer clic

    def mover_ventana(self, event):
        if not self.isMaximized():  # Solo permitir mover la ventana si no está maximizada
            if event.buttons() == Qt.LeftButton:  # Si se arrastra con el botón izquierdo
                self.move(self.pos() + event.globalPos() - self.clickPosition)  # Mover la ventana
                self.clickPosition = event.globalPos()  # Actualizar la posición del cursor
                event.accept()  # Aceptar el evento

        # Si se arrastra hacia la parte superior de la pantalla, maximizar la ventana
        if event.globalPos().y() <= 20:  
            self.showMaximized()
        else:
            self.showNormal()

    

def main():
    app = QApplication(sys.argv)  
    ventana = MainWindow()  
    ventana.show()  
    sys.exit(app.exec_())  

if __name__ == "__main__":
    main()


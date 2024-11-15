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

        #Configuracion botones pagina Peliculas
        self.btn_agregar_pelicula.clicked.connect(self.abrir_agregar_pelicula)
        self.btn_eliminar_pelicula.clicked.connect(self.abrir_eliminar_pelicula)
        self.btn_modificar_pelicula.clicked.connect(self.abrir_modificar_pelicula)
        self.btn_informacion_pelicula.clicked.connect(self.mostrar_informacion_pelicula)


        #Configuracion botones pagina funciones
        self.filtro_fecha_activado = False  # Configuración inicial del filtro de fecha

        # Configuración inicial de botones y fechas
        self.btn_agregar_funcion.clicked.connect(self.abrir_agregar_funcion)
        self.btn_eliminar_funcion.clicked.connect(self.abrir_eliminar_funcion)
        self.btn_modificar_funcion.clicked.connect(self.abrir_modificar_funcion)
        self.btn_actualizar.clicked.connect(self.actualizar_cartelera)
        self.btn_comprar.clicked.connect(self.abrir_seleccionar_butacas)
        self.btn_resumen_funcion.clicked.connect(self.mostrar_resumen_funcion_seleccionada)
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
        self.comboBox_historial_usuario.currentIndexChanged.connect(self.actualizar_tabla_comboBox)
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
        self.cargar_Historial_en_tabla()
        # Llenar la tabla de funciones al iniciar
        #Actualizar Cartelera
        self.actualizar_cartelera()
        self.cargar_usuarios_en_comboBox()
        self.estadistica_pelicula()
        self.estadisticas_individual()

        
        # Conectar el botón de actualizar con el método cargar_usuarios_en_tabla
        self.btn_actualizarUsuario.clicked.connect(self.cargar_usuarios_en_tabla)
        # Conectar el botón de actualizar con el método cargar_pelis_en_tabla
        self.btn_actualizar_pelicula.clicked.connect(self.cargar_peliculas_en_tabla)
        # Conectar el botón de actualizar con el método cargar_Historial_en_tabla
        self.btn_actualizarH.clicked.connect(self.cargar_Historial_en_tabla)
        # Conectar el botón de actualizar con el método cargar_Funciones_en_tabla




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
            print("No hay funciones programadas a partir de hoy.")
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
                f"Descripción: {funcion_actual['descripcion']}\n"
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
    def cargar_usuarios_en_tabla(self):
        """Carga los usuarios de la base de datos y muestra solo NombreUsuario, Grupo, FechaCreacion y FechaModificacion en tableWidget_usuarios, adaptando el contenido al tamaño de la tabla."""

        try:
            usuarios = self.db.obtener_usuarios()
            self.tableWidget_usuarios.setRowCount(0)
            
            for row_number, row_data in enumerate(usuarios):
                self.tableWidget_usuarios.insertRow(row_number)

                # Asignar solo los datos de las columnas deseadas
                nombre_usuario = row_data[1]       # NombreUsuario (índice 1)
                grupo = row_data[3]                # Grupo (índice 3)
                fecha_creacion = row_data[4]       # FechaCreacion (índice 4)
                fecha_modificacion = row_data[5]   # FechaModificacion (índice 5)

                # Insertar los datos en la tabla
                self.tableWidget_usuarios.setItem(row_number, 0, QTableWidgetItem(str(nombre_usuario)))
                self.tableWidget_usuarios.setItem(row_number, 1, QTableWidgetItem(str(grupo)))
                self.tableWidget_usuarios.setItem(row_number, 2, QTableWidgetItem(str(fecha_creacion)))
                self.tableWidget_usuarios.setItem(row_number, 3, QTableWidgetItem(str(fecha_modificacion)))

            # Ajustar el tamaño de las columnas y filas al contenido
            self.tableWidget_usuarios.resizeColumnsToContents()
            self.tableWidget_usuarios.resizeRowsToContents()

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar la tabla de usuarios.')


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

    def actualizar_tabla_comboBox(self):
        """Actualiza la tabla según la selección del comboBox."""
        self.cargar_Historial_en_tabla()

    def actualizar_tabla_fecha(self):
        """Actualiza la tabla solo cuando se confirma la selección de una fecha."""
        self.fecha_seleccionada = True
        self.cargar_Historial_en_tabla()

    def cargar_Historial_en_tabla(self):
        """Carga y filtra los registros del historial según la selección del comboBox y la fecha, y ajusta el contenido de la tabla."""
        try:
            historial = self.db.obtener_historial()  # Obtener todos los registros del historial

            # Obtener el usuario seleccionado del comboBox
            id_usuario_seleccionado = self.comboBox_historial_usuario.currentData()

            # Aplicar filtro por usuario si se seleccionó uno específico
            if id_usuario_seleccionado:
                historial = [registro for registro in historial if registro[1] == id_usuario_seleccionado]

            # Solo filtrar por la fecha si la fecha fue seleccionada manualmente
            if self.fecha_seleccionada:
                fecha_seleccionada = self.fecha_historial.date().toPyDate()
                historial = [registro for registro in historial if registro[2].date() == fecha_seleccionada]

            # Ordenar el historial en orden descendente por la fecha y hora (índice 2)
            historial_ordenado = sorted(historial, key=lambda x: x[2], reverse=True)

            self.tableWidget_historial.setRowCount(0)  # Limpiar la tabla

            for row_number, row_data in enumerate(historial_ordenado):
                id_usuario = row_data[1]  # Asumiendo que el ID del usuario está en la segunda columna (índice 1)
                usuario = self.db.obtener_usuario_por_id(id_usuario)  # Obtener los datos del usuario por ID

                nombre_usuario = usuario[1] if usuario else "Desconocido"  # Asumiendo que el nombre del usuario está en el índice 1
                fecha_hora = row_data[2]  # Fecha y hora en el índice 2
                accion = row_data[3]  # Acción en el índice 3

                self.tableWidget_historial.insertRow(row_number)
                self.tableWidget_historial.setItem(row_number, 0, QTableWidgetItem(str(nombre_usuario)))
                self.tableWidget_historial.setItem(row_number, 1, QTableWidgetItem(str(fecha_hora)))
                self.tableWidget_historial.setItem(row_number, 2, QTableWidgetItem(str(accion)))

            # Ajustar el ancho de las columnas y la altura de las filas al contenido
            self.tableWidget_historial.resizeColumnsToContents()
            self.tableWidget_historial.resizeRowsToContents()

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo cargar la tabla de historial.')

    
    #==============================================================================================================
    # Configuracion Pagina Funciones

    
    
    def cargar_id_funciones_en_comboBox(self):
        """Carga todos los IDs de funciones en el comboBox_idfunciones."""
        try:
            funciones = self.db.obtener_funciones()  # Obtener todas las funciones

            self.comboBox_idfunciones.clear()
            self.comboBox_idfunciones.addItem("Todas las funciones", None)  # Opción de selección general

            for funcion in funciones:
                id_funcion = funcion[0]
                self.comboBox_idfunciones.addItem(str(id_funcion), id_funcion)

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

            # Insertar datos en la tabla (incluyendo el ID de la función, pero ocultándolo)
            for row_number, row_data in enumerate(funciones):
                self.tableWidget_funciones.insertRow(row_number)

                id_funcion = row_data[0]
                asientos_reservados = self.db.obtener_asientos_reservados(id_funcion)
                total_butacas = 30
                butacas_vendidas = len(asientos_reservados)
                porcentaje_vendido = (butacas_vendidas / total_butacas) * 100

                # Seleccionar color según porcentaje de butacas vendidas
                color = QColor("red") if porcentaje_vendido <= 40 else QColor("orange") if porcentaje_vendido <= 60 else QColor("lightgreen") if porcentaje_vendido <= 80 else QColor("darkgreen")

                # Agregar datos a la tabla (incluyendo el ID, pero ocultándolo visualmente)
                datos_visibles = [row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], butacas_vendidas]

                for column_number, data in enumerate(datos_visibles):
                    item = QTableWidgetItem(str(data))
                    if column_number == 0:
                        item.setData(Qt.UserRole, id_funcion)  # Guardar el ID en UserRole
                    item.setBackground(color)
                    self.tableWidget_funciones.setItem(row_number, column_number, item)

            # Ocultar la columna del ID de la función para que no sea visible
            self.tableWidget_funciones.setColumnHidden(0, True)

            # Ajustar el ancho de las columnas al contenido
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

            # Insertar funciones en la tabla (incluyendo el ID de la función, pero ocultándolo visualmente)
            for row_number, row_data in enumerate(funciones):
                self.tableWidget_funciones.insertRow(row_number)

                id_funcion = row_data[0]
                asientos_reservados = self.db.obtener_asientos_reservados(id_funcion)
                total_butacas = 30
                butacas_vendidas = len(asientos_reservados)
                porcentaje_vendido = (butacas_vendidas / total_butacas) * 100

                # Seleccionar color según porcentaje de butacas vendidas
                color = QColor("red") if porcentaje_vendido <= 40 else QColor("orange") if porcentaje_vendido <= 60 else QColor("lightgreen") if porcentaje_vendido <= 80 else QColor("darkgreen")

                # Agregar datos a la tabla (incluyendo el ID, pero ocultándolo visualmente)
                datos_visibles = [row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], butacas_vendidas]

                for column_number, data in enumerate(datos_visibles):
                    item = QTableWidgetItem(str(data))
                    if column_number == 0:
                        item.setData(Qt.UserRole, id_funcion)  # Guardar el ID en UserRole
                    item.setBackground(color)
                    self.tableWidget_funciones.setItem(row_number, column_number, item)

            # Ocultar la columna del ID de la función para que no sea visible
            self.tableWidget_funciones.setColumnHidden(0, True)

            # Ajustar el ancho de las columnas al contenido
            self.tableWidget_funciones.resizeColumnsToContents()

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', 'No se pudo mostrar todas las funciones en la tabla.')

    def mostrar_resumen_funcion_seleccionada(self):
        """Muestra el resumen de la función seleccionada en la tabla."""
        selected_items = self.tableWidget_funciones.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una función en la tabla primero.")
            return

        selected_row = selected_items[0].row()
        id_funcion = self.tableWidget_funciones.item(selected_row, 0).data(Qt.UserRole)  # Recuperar el ID desde UserRole
        self.mostrar_informacion_funcion(id_funcion)

    def mostrar_informacion_funcion(self, funcion_id):
        """Muestra un QMessageBox con la información de una función específica, incluyendo su ID."""
        try:
            asientos_reservados = self.db.obtener_asientos_reservados(funcion_id)
            butacas_vendidas = len(asientos_reservados)
            
            funcion_info = self.db.obtener_funcion_por_id(funcion_id)
            if funcion_info:
                id_sala, precio_funcion, fecha_hora_funcion = funcion_info[3], funcion_info[4], funcion_info[2]
                
                sala_info = self.db.obtener_sala_por_id(id_sala)
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

                QMessageBox.information(self, "Información de la función", mensaje)
            else:
                QMessageBox.warning(self, "Advertencia", "No se encontró información para la función seleccionada.")

        except Exception as e:
            log(e, "error")
            QMessageBox.critical(self, 'Error', f'No se pudo obtener la información de la función: {e}')


    


    
    #==============================================================================================================
    # Configuracion Pagina Pelis

    def cargar_peliculas_en_tabla(self):
        try:
            peliculas = self.db.obtener_peliculas()  # Obtiene todas las películas
            self.tableWidget_pelis.setRowCount(0)

            # Filas de la tabla: NombrePelicula, FechaInicio, FechaFin, Duracion, Clasificacion
            for row_number, pelicula in enumerate(peliculas):
                # Asigna cada campo de la base de datos a una columna específica
                id_pelicula = pelicula[0]  # ID de la película
                nombre = pelicula[1]
                fecha_inicio = pelicula[6]
                fecha_fin = pelicula[7]
                duracion = pelicula[8]
                clasificacion = pelicula[9]

                # Insertamos los datos en la tabla, sin incluir el ID en la columna visible
                self.tableWidget_pelis.insertRow(row_number)
                self.tableWidget_pelis.setItem(row_number, 0, QTableWidgetItem(str(nombre)))
                self.tableWidget_pelis.setItem(row_number, 1, QTableWidgetItem(str(fecha_inicio)))
                self.tableWidget_pelis.setItem(row_number, 2, QTableWidgetItem(str(fecha_fin)))
                self.tableWidget_pelis.setItem(row_number, 3, QTableWidgetItem(str(duracion)))
                self.tableWidget_pelis.setItem(row_number, 4, QTableWidgetItem(str(clasificacion)))

                # Almacenar el ID de la película como "UserRole" en el primer elemento de la fila
                self.tableWidget_pelis.item(row_number, 0).setData(Qt.UserRole, id_pelicula)

            # Ajusta el ancho de las columnas al contenido
            self.tableWidget_pelis.resizeColumnsToContents()
            self.estadistica_pelicula()

        except Exception as e:
            log(e, "error")




    def estadistica_pelicula(self): 
        # Cantidad de Peliculas
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
        mensaje2 = f"\n{peliculas_vistas_texto}\n\n"
        mensaje3 = f"\n{generos_rentables_texto}"

        # Mostrar Mensajes
        self.total_peliculas.setText(mensaje1)  # LineEdit
        self.textEdit_top10_peliculas.setText(mensaje2)  # TextEdit
        self.textEdit_top5_generos.setText(mensaje3)  # TextEdit

        # Bloquear edición en TextEdit
        self.textEdit_top10_peliculas.setReadOnly(True)
        self.textEdit_top5_generos.setReadOnly(True)
        self.estadisticas_individual()

    
    def estadisticas_individual(self):
        """Carga las estadísticas de todas las películas en la tabla."""
        try:
            peliculas = self.db.obtener_peliculas()
            self.tabla_estadistica_peli.setRowCount(0)
            for row_number, pelicula in enumerate(peliculas):
                id_pelicula = pelicula[0]  
                nombre = pelicula[1]
                self.tabla_estadistica_peli.insertRow(row_number)
                self.tabla_estadistica_peli.setItem(row_number, 0, QTableWidgetItem(str(id_pelicula)))
                self.tabla_estadistica_peli.setItem(row_number, 1, QTableWidgetItem(str(nombre)))
            self.tabla_estadistica_peli.resizeColumnsToContents()
        except Exception as e:
            log(e, "error")


    def filtrar_peliculas(self):
        """Filtra las películas por nombre basado en el texto ingresado en filtro_nombre_estadistica."""
        try:
            # Obtiene el texto de filtro
            texto_filtro = self.filtro_nombre_estadistica.text().strip().lower()
            
            # Si el filtro está vacío, llama a estadisticas_individual para cargar todas las películas
            if not texto_filtro:
                self.estadisticas_individual()
                return
            
            # Obtiene todas las películas
            peliculas = self.db.obtener_peliculas()
            
            # Limpia la tabla
            self.tabla_estadistica_peli.setRowCount(0)

            # Recorre las películas y solo inserta las que coinciden con el filtro
            row_number = 0  # Controla el índice de las filas en la tabla filtrada
            for pelicula in peliculas:
                id_pelicula = pelicula[0]
                nombre = pelicula[1]

                # Aplica el filtro: verifica si el nombre contiene el texto de filtro
                if texto_filtro in nombre.lower():
                    self.tabla_estadistica_peli.insertRow(row_number)
                    self.tabla_estadistica_peli.setItem(row_number, 0, QTableWidgetItem(str(id_pelicula)))
                    self.tabla_estadistica_peli.setItem(row_number, 1, QTableWidgetItem(nombre))
                    row_number += 1  # Incrementa solo si una película fue añadida

            # Ajusta el ancho de las columnas al contenido
            self.tabla_estadistica_peli.resizeColumnsToContents()

        except Exception as e:
            log(e, "error")



    def obtener_pelicula_seleccionada(self):
        selected_row = self.tableWidget_pelis.currentRow()
        
        if selected_row == -1:
            return None

        # Recuperar el ID almacenado en UserRole en la primera columna de la fila seleccionada
        pelicula_id_item = self.tableWidget_pelis.item(selected_row, 0)
        pelicula_id = pelicula_id_item.data(Qt.UserRole)
        
        return pelicula_id



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


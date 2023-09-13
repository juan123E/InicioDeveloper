from selenium import webdriver

# Iniciar el navegador Chrome
driver = webdriver.Chrome()
correos = ['cdc@iglesiaencasa.co', 'cebco1@iglesiaencasa.co', 'cebcomodelia@iglesiaencasa.co', 'conexion@iglesiaencasa.co', 'bd@iglesiaencasa.co', 'tim.conexion@iglesiaencasa.co', 'audiencia.01@iglesiaencasa.co', 'consolidacion@iglesiaencasa.co', 'constructores@iglesiaencasa.co', 'tim.constructores@iglesiaencasa.co', 'coordinador.316@iglesiaencasa.co', 'tim.decorazon@iglesiaencasa.co', 'decorazon@iglesiaencasa.co', 'dispositivos@iglesiaencasa.co', 'fotos3@iglesiaencasa.co', 'fotos2@iglesiaencasa.co', 'fotos@iglesiaencasa.co', 'fotosiglesia@iglesiaencasa.co', 'liderazgo@iglesiaencasa.co', 'predicas@iglesiaencasa.co', 'lactantes@iglesiaencasa.co', 'tvwall2@iglesiaencasa.co', 'tim.radio@iglesiaencasa.co', 'encasaradio@iglesiaencasa.co', 'radio@iglesiaencasa.co', 'asis1.ensamble@iglesiaencasa.co', 'asis2.ensamble@iglesiaencasa.co', 'tim.ensamble@iglesiaencasa.co', 'bd1.ensamble@iglesiaencasa.co', 'asistente2.ec@iglesiaencasa.co', 'ensamblecreativo@iglesiaencasa.co', 'laantesala@iglesiaencasa.co', 'tim.laantesala@iglesiaencasa.co', 'legado@iglesiaencasa.co', 'tim.legado@iglesiaencasa.co', 'fotosvilla@iglesiaencasa.co', 'vpr-radio@iglesiaencasa.co', 'vpr@iglesiaencasa.co', 'backup@iglesiaencasa.co', 'javapontepersonales@iglesiaencasa.co', 'letras@iglesiaencasa.co', 'secretaria@iglesiaencasa.co', 'info@iglesiaencasa.co', 'admin2@iglesiaencasa.co', 'staff@iglesiaencasa.co', 'tim.staff@iglesiaencasa.co', 'sc@iglesiaencasa.co', 'medios@iglesiaencasa.co', 'tim.sc@iglesiaencasa.co', 'tic@iglesiaencasa.co', 'asistente1.tic@iglesiaencasa.co', 'vencedores@iglesiaencasa.co', 'tim.vencedores@iglesiaencasa.co', 'tim.vida@iglesiaencasa.co', 'vida@iglesiaencasa.co', 'vip@iglesiaencasa.co', 'tim.consolidacion@iglesiaencasa.co', 'tim.tic@iglesiaencasa.co', 'tic.iglencasa.@icloud.com', 'videoclips1@iglesiaencasa.co', 'bd.fotos@iglesiaencasa.co', 'vidaevangelismo@gmail.com', 'n.mayorquin@iglencasa.onmicrosoft.com', 'l.granados@iglencasa.onmicrosoft.com']
nombres = ['Andrés', 'María', 'Camila', 'Luis', 'Sofía', 'Carlos', 'Valentina', 'Pedro', 'Isabella', 'Javier', 'Sara', 'Daniel', 'Valeria', 'Miguel', 'Laura', 'José', 'Alejandra', 'Fernando', 'Lucía', 'Diego', 'Natalia', 'Manuel', 'Juliana', 'Felipe', 'Ana', 'Sebastián', 'Santiago', 'Mateo', 'Paula', 'Alejandro', 'Antonio', 'Victoria', 'Gabriel', 'Daniela', 'Julián', 'Valery', 'Tomás', 'Catalina', 'David', 'Tatiana', 'Christian', 'Giselle', 'Eduardo', 'María José', 'Adrián', 'Mariana', 'Hernán', 'Valeria', 'Rafael', 'Isabel', 'Simón', 'Estefanía', 'Carlos Andrés', 'Johana', 'Germán', 'Vanessa', 'Andrés Felipe', 'Sandra', 'Jairo', 'Lorena', 'Ricardo', 'Elena', 'Mauricio', 'Patricia', 'Diana', 'Paola', 'Rosa', 'Melissa', 'Luisa', 'Juan Pablo', 'Carmen', 'Marcela', 'Santiago', 'María Camila', 'Gustavo', 'Elizabeth', 'Samuel', 'Alejandra', 'Alberto', 'Katherine']
apellidos = ['Rodríguez', 'López', 'Martínez', 'Pérez', 'Gómez', 'Sánchez', 'Fernández', 'Torres', 'Ramírez', 'Vargas', 'Díaz', 'Hernández', 'Silva', 'Mendoza', 'Rojas', 'Jiménez', 'Ortega', 'Soto', 'Castro', 'Romero', 'Álvarez', 'Ruiz', 'Morales', 'Estrada', 'Flores', 'Rivera', 'Santos', 'Delgado', 'Chávez', 'Guerrero', 'Cortés', 'Valencia', 'Acosta', 'Campos', 'Medina', 'Aguilar', 'Arias', 'Pacheco', 'Vega', 'Cruz', 'Peralta', 'Gutiérrez', 'Quintero', 'Luna', 'Mendoza', 'Ochoa', 'Peña', 'Rivas', 'Cabrera', 'Gálvez', 'Salazar', 'Navarro', 'Maldonado', 'Palacios', 'Salcedo', 'Camacho', 'Villarreal', 'Toro', 'Bautista', 'Lara', 'Duque', 'Paredes', 'León', 'Uribe', 'Barrera', 'Paredes', 'Zapata', 'Ferreira', 'Aldana', 'Bustos', 'Castellanos']
x = 59
# Abrir el sitio web con el formulario
driver.get('https://form.jotform.com/232327105179655')

while x < 64:
    # Llenar nombre
    driver.find_element("id",'first_142').send_keys(nombres[x])
    # Llenar apellido
    driver.find_element("id",'last_142').send_keys(apellidos[x])
    # Llenar email
    driver.find_element("id",'input_5').send_keys(correos[x])
    # Orpimir siguiente
    driver.find_element("id",'form-pagebreak-next_135').click()
    # Oprimir siguiente
    driver.find_element("id",'form-pagebreak-next_39').click()
    # Seleccionar Giselle
    driver.find_element("id",'label_input_44_5').click()
    #Seleccionar The crew
    driver.find_element("id",'label_input_48_4').click()
    # Oprimir siguiente
    driver.find_element("id",'form-pagebreak-next_50').click()
    # Seleccionar En casa Radio
    driver.find_element("id",'label_input_54_7').click()
    # Oprimir siguiente
    driver.find_element("id",'form-pagebreak-next_61').click()
    # Seleccionar Juan Aponte
    driver.find_element("id",'label_input_73_0').click()
    # Oprimir siguiente
    driver.find_element("id",'form-pagebreak-next_72').click()
    # Oprimir siguiente
    driver.find_element("id",'form-pagebreak-next_83').click()
    #Oprimir Enviar
    driver.find_element("id",'input_2').click()
    # Recargar la pagina
    driver.close()
    driver = webdriver.Chrome()
    driver.get('https://form.jotform.com/232327105179655')
    x += 1
    print(correos[x], x)


input("Presione una tecla para continuar...")
# Cerrar el navegador
#driver.close()


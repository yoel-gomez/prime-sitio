# Importar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Resultados del formulario
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # obtener la imagen seleccionada
        selected_image = request.form.get('image-selector')

        # Asignación #2. Recepción del texto
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Assignment #3. Receiving the text's positioning
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')
        selected_color = request.form.get('color-selector')

        # Asignación #3. Recepción del posicionamiento del texto
        

        return render_template('index.html', 
                               # Visualización de la imagen seleccionada
                               selected_image=selected_image, 

                               # Asignación #2. Visualización del texto
                                text_top = text_top,
                                text_bottom = text_bottom   ,

                               #  Asignación #3. Visualización del color
                                text_top_y = text_top_y,
                                text_bottom_y = text_bottom_y,
                                selected_color = selected_color

                               
                               # Asignación #3. Visualización de la posición del texto


                               )
    else:
        # Mostrar la primera imagen por defecto
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)

from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import shutil
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'site/static/uploads'

# Carrega o modelo treinado
model = YOLO('runs//detect//train//weights//best.pt')

# Função que faz a predição e retorna a quantidade de gados e o caminho da imagem processada
def analyze_image(filepath):
    # Faz a predição na imagem fornecida
    results = model.predict(
        source=filepath,  # Caminho para a imagem de entrada
        conf=0.30,  # Confiança mínima para considerar uma detecção
        iou=0.7,  # Limite de sobreposição para supressão de não-máximos (NMS)
        imgsz=640,  # Tamanho da imagem de entrada para o modelo
        save=True  # Salva a imagem com as detecções
    )
    
    # Diretório onde a imagem foi salva automaticamente pelo YOLO
    predict_dir = results[0].save_dir

    # Caminho da imagem processada no diretório 'runs/detect/predictX/'
    processed_image_path = os.path.join(predict_dir, os.path.basename(filepath))
    
    # Defina um novo caminho para a imagem processada em 'static/uploads/'
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(filepath))
    
    # Move a imagem processada para o diretório de uploads
    shutil.move(processed_image_path, output_path)
    
    # Conta o número de gados detectados
    total_gados = len(results[0].boxes)
    
    return total_gados, output_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Nenhum arquivo enviado!'
        
        file = request.files['file']
        if file.filename == '':
            return 'Nenhum arquivo selecionado!'
        
        if file:
            # Salva a imagem original no diretório de uploads
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Analisa a imagem e obtém o número de gados e o caminho da imagem processada
            total_gados, processed_image = analyze_image(filepath)
            
            # Renderiza o template com a imagem original, processada e o número de gados
            return render_template('index.html', filename=filename, processed_image=processed_image, total_gados=total_gados)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

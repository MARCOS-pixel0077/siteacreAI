import cohere
from flask import Flask, request, jsonify
from flask_cors import CORS

# Inicialize o cliente Cohere com sua chave de API
co = cohere.Client("NarNig6E0mkhWmrCS9LBAc6g9Xzi7DiimBvhxbiY")

app = Flask(__name__)
CORS(app)  # Permite requisições de outros domínios (CORS)

def gerar_resposta(prompt):
    try:
        # Fazendo a solicitação à API de chat
        response = co.chat(
            model="command-xlarge-nightly",  # Modelo mais avançado
            message=prompt,  # A pergunta enviada para a IA
            temperature=0.7,  # Controla a criatividade da resposta
            max_tokens=150  # Limita o tamanho da resposta
        )
        return response.text.strip()  # Retorna a resposta gerada
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pergunta = data.get('pergunta')

    # Gera a resposta usando o Cohere
    resposta = gerar_resposta(pergunta)

    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)

#Criação de servidor HTTP
from flask import Flask, render_template, request
#Render template utilizado para renderizar arquivos que se encontram na pasta templates
#Pórem podemos passar o paramentro template_folder no Flas() para indicar qual será a nossa pasta de templates

app = Flask(__name__)

#Podemos passar um 2º parametro na função route, os methods que receberá um array definindo o método que será utilizado: GET OU POST. Podemos passar mais de um método
@app.route("/", methods=["GET", "POST"]) #Criação de rota
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        if request.form["val1"] != "" or request.form["val2"] != "":
            if request.form["opc"] == "soma":
                soma = int(request.form["val1"]) + int(request.form["val2"])
                return {
                  "Soma": str(soma)  
                } 

            elif request.form["opc"] == "subt":
                subt = int(request.form["val1"]) - int(request.form["val2"])
                return{ 
                "Subtração": str(subt)
                }

            elif request.form["opc"] == "divi":
                divi = int(request.form["val1"]) / int(request.form["val2"])
                return{ 
                "Divisão": str(divi)
                }

            elif request.form["opc"] == "mult":
                mult = int(request.form["val1"]) * int(request.form["val2"])
                return{ 
                "Multiplicação": str(mult)
                    }
        else:
            return "Informe valores válidos"



@app.errorhandler(404)
def not_found(error):
    return "Página não encontrada"

app.run(debug=True) 
#Podemos passar a porta por meio do parametro port=
#Parametro debug=True atualiza nossa porta automaticamente


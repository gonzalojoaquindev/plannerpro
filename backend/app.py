from flask import Flask, jsonify, request
from flask_cors import CORS

from routes.accounts import accounts
from routes.categories import categories
from routes.subcategories import subcategories
from routes.benefited import benefited
from routes.transactions import transactions


app = Flask(__name__)


app.register_blueprint(accounts)
app.register_blueprint(categories)
app.register_blueprint(subcategories)
app.register_blueprint(benefited)
app.register_blueprint(transactions)



# Aca le digo que permite hacerle peticiones HTTP desde el servidor del fronted React
CORS(app, resources={"*": {"origins": "http://localhost:5173"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404



# Aca le digo que la configuración va avenir desde unn objeto (config)
if __name__ == '__main__':
    app.config["DEBUG"] = True
    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
from dash import Dash

app = Dash(__name__, suppress_callback_exceptions=True)

from layout import create_layout
from callbacks import *

app.layout = create_layout()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=False)
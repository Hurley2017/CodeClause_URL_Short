from serv import ui
app = ui

if "__main__" == __name__:
    # app.run(debug=True)
    from waitress import serve
    serve(app)
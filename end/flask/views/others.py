from main import render_template,app,request
@app.route('/about')
def about():
    return '这是关于页面'


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

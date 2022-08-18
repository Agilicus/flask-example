import flask

app = flask.Flask('app')
app.config["DEBUG"] = True

@app.route('/script.js', methods=['GET'])
def script():
    return """
function showApi(data) {
    const divid = document.getElementById('api-data');
    const value = document.createElement('h2');
    value.innerHTML = "api_result: " + data.status;
    divid.appendChild(value);
}
fetch("http://localhost:5001/api")
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("NETWORK RESPONSE ERROR");
    }
  })
  .then(data => {
    console.log(data);
    showApi(data)
  })
  .catch((error) =>
  {
    console.error("FETCH ERROR:", error)
  });
"""

@app.route('/', methods=['GET'])
def home():
    return """
<html>
 <head><title>Dashboard</title></head>
 <body>
   <h1>This shows some api data</h1>
   <div id="api-data"></div>
   <script src="/script.js"></script>
 </body>
</html>
"""

app.run('0.0.0.0', 5000)

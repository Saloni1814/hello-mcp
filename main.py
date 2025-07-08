from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/.well-known/mcp.json", methods=["GET"])
def mcp_discovery():
    return jsonify({
        "tools": [
            {
                "name": "hello-tool",
                "description": "Returns Hello World",
                "parameters": {}
            }
        ]
    })

@app.route("/invoke/hello-tool", methods=["POST"])
def invoke_hello():
    return jsonify({
        "output": "Hello, MCP World! 🎉"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


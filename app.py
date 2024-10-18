from quart import Quart, send_from_directory
import os

app = Quart(__name__, static_folder='my-react-app/build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
async def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return await send_from_directory(app.static_folder, path)
    else:
        return await send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
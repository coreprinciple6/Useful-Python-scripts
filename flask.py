
''' open postman, run this python file then give the localhost/test address in postman.
Then add input as a dictionary in the body of postman and send to use this api.'''
import json
import base64
import numpy as np
from flask_cors import CORS
from datetime import datetime
from flask import Flask, request, jsonify
import time

app = Flask(__name__)
CORS(app)

# def saved_img(img, path=None):
#     today = datetime.today()
#     d1 = today.strftime("%d/%m/%Y")
#     now =  datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     if path is not None:
#         save_path = path+"/"+str(d1)+"/"+str(current_time)+"/"
#         os.makedirs(save_path, exist_ok=True)
#         img_name = save_path+"image_after_decoding"+".png"
#         cv2.imwrite(img_name, img)
#     return save_path

# def convert_to_im_array(data):
#     arr = base64.b64decode(data)
#     img_arr = np.frombuffer(arr, np.uint8)
#     img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
#     save_path = saved_img(img, "/home/IMAGES")
#     with open(save_path+"string_image.txt","w") as file:
#         file.write(str(data))
#     return img, save_path


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode('utf-8'))
            file = data['file']
            img_bytes = file
            img_bytes, save_path = convert_to_im_array(img_bytes)
            img = np.asarray(img_bytes)

            result = 'random string'
            print(result)
            with open(save_path+'API_RESULT.txt', 'w') as f:
                print(result, file=f)
            return jsonify(result)

        except Exception as e:
           # print(e)
            return jsonify({'status': 500, 'message': "Error! check you input"})
        


if __name__ == '__main__':
    print("SERVER STARTED")
    app.run(host="0.0.0.0",port="8080")
    #app.run()

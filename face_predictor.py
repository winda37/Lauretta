# import library
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import cv2
import json


def get_image(url):
    """ GET image file from url
    Parameters
    ----------
    url : str
          url to get image url from https://hackattic.com/ challenge
    Returns
    -------
    Output: nparray
            Image array size (800,800,3)
    """
    im_url = requests.get(url=url).json()
    im_url = im_url['image_url']
    img = requests.get(im_url)
    return np.asarray(Image.open(BytesIO(img.content)))


def post_answer(url, data):
    """POST the face detection result
    Parameters
    ----------
    url : str
          url to send the answer
    data: dict
          json file of face position
    """
    return requests.post(url=url, data=data)


def fd_haar_cascade(img):
    """Face detection using viola-jones method
    Parameters
    ----------
    img : nparray

    Returns
    -------
    Output  : list
              list of grid position that contains face image
    """
    # change RBG image to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # import the model
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # do prediction
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    position = []
    for face in faces:
        (startX, startY) = face[0], face[1]
        (endX, endY) = face[2], face[3]
        x = int(startX/100)
        y = int(startY/100)
        position.append([y, x])
    return position


if __name__ == '__main__':
    ACCESS_TOKEN = 'b4099508ab747a74'
    url = 'https://hackattic.com/challenges/basic_face_detection/'

    # GET the image
    im = get_image(url+'problem?access_token='+ACCESS_TOKEN)
    # find the position of grid that contain face image
    position = fd_haar_cascade(im)
    data = {'face_tiles': position}
    json_data = json.dumps(data)
    # POST the answer
    res = post_answer(url+'solve?access_token='+ACCESS_TOKEN, json_data)
    print('Respond: ', res.content)





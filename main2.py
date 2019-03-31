import os
import sys
import io

from flask import Flask, redirect, render_template, request

from google.cloud import firestore
from google.cloud import storage
from google.cloud import vision

hash_table = {"Paper":"compost", "Plastic":"recycle", "Food":"compost", 
                "Plastic bottle":"recycle", "Paper product":"compost", 
                "Potato chip":"recycle", "rubber ducky":"recycle" ,"Tin can":"recycle", "Electronic device":"recycle"
                ,"Battery":"recycle","Textile":"compost"};

def checkGarb(description, hash_tables):
    #print(dir(description));
    temp = str(description)
    if temp in hash_table: 
        classification = hash_table[description]
        classification = classification.lower()
        return classification
    else:
        return "0"

def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    #print('Labels:')

    #for label in labels:
        #print(label.description)

    #rasberry pi display which trashcan to throw to
    for label in labels:
        #print (type(label))
        tCan = str(checkGarb(label.description, hash_table))
        if (tCan == "0"):
            #print("00000000")
            continue
        else:
            #print("11111")
            print(tCan)
	    return tCan
    print ("compost")
    return "compost"
        




if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.

    detect_labels("/home/pi/Desktop/hackPhotos/hackImage.jpg")

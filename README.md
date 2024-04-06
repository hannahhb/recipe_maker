# recipe_maker

Image detection via YoloV8 -> Recipie builder from ingredient -> 

pre-trained weights from https://github.com/lannguyen0910/food-recognition?tab=readme-ov-file


Models	| Image Size | 	Epochs	|  mAP@0.5	| mAP@0.5:0.95
--- | --- | --- | --- |--- 
YOLOv5s	| 640x640 | 172 |	0.907	| 0.671
YOLOv5m	| 640x640 |	112 |	0.897 |	0.666
YOLOv5l	| 640x640 | 118	| 0.94 |	0.73
YOLOv5x |	640x640 | 62 |	0.779 |	0.533
YOLOv8s	| 640x640	| 70 |	0.963 |	0.82

oh no.
oh dear.
run using:
    flask --app app.py run --debug

using tutorial 
https://geekpython.in/flask-app-for-image-recognitio

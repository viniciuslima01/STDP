import os
import dlib
import cv2
import glob

detectorPlaca = dlib.simple_object_detector("recursos/detector_placas.svm")
for imagem in glob.glob(os.path.join("placas_teste", "*.jpg")):
	img = cv2.imread(imagem)
	placasDetectadas = detectorPlaca(img, 2)
	
	for d in placasDetectadas:
		e, t, d, b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))
		cv2.rectangle(img, (e,t), (d, b), (0, 0, 255), 2)
		
	cv2.imshow("Detector de placas", img)
	cv2.waitKey(0)
	
cv2.destroyAllWindows()

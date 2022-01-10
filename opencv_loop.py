import cv2
import argparse

def start(args):

	in_cap = cv2.VideoCapture(0)
	print('read video')
	while True:
		is_in, in_cam    = in_cap.read()
		try:
			in_frame = cv2.cvtColor(in_cam, cv2.COLOR_BGR2RGB)
			cv2.imshow('check',in_frame)
			# cv2.imwrite('help.jpg',in_frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		except Exception as e:
			print(e)
			continue

	in_cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--show",  action="store_true",
                    help="show the faces in this device?")
	parser.add_argument("-v", "--verbose", action="store_true",
                    help="print the response")
	args = parser.parse_args()
	print(args)
	start(args)
    

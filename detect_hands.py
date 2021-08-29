import cv2
import time
from hand_recognitor import handFinder
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=bool, default=False, help='detection / tracking')
parser.add_argument('--count', type=int, default=2, help='maximum number of hands')
parser.add_argument('--detConf', type=float, default=0.5, help='minimum_detection_confidence')
parser.add_argument('--trcConf', type=float, default=0.5, help='minimum_tracking_confidence')
parser.add_argument('--flip', type=bool, default=False, help='image is upside down')
parser.add_argument('--drawlm', type=bool, default=True, help='draw hand landmarks')
parser.add_argument('--drawcn', type=bool, default=True, help='draw hand connections')
args = parser.parse_args()

'''
0-wrist
1:4-thumb(cmc:tip)
5:8-index(mcp:tip)
9:12-middle(mcp:tip)
13:16-ring(mcp:tip)
17:20-pinky(mcp:tip)
'''

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

handDetector = handFinder(args.mode, args.count, args.detConf, args.trcConf)

aTime = 0
bTime = 0

while True:
	ret, frame = cap.read()
	image = frame.copy()

	hand_landmarks, image = handFinder.findHands(img=image, BGR=True, flip=args.flip, drawLandmarks=args.drawlm, drawConnections=args.drawcn)

	aTime = time.time()
	fps = 1/(aTime-bTime)
	bTime = aTime
	print(fps)

	cv2.imshow('window name', image)
	if cv2.waitKey(1) == ord('q'):
		break

cv2.destroyAllWindows()

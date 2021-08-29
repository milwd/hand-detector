import cv2
import mediapipe


class handFinder():
	def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
		self.mode = static_image_mode
		self.maxHands = max_num_hands
		self.detectionConfidence = min_detection_confidence
		self.trackingConfidence = min_tracking_confidence
		self.mpHands = mediapipe.solutions.hands
		self.hands = self.mpHands.Hands(mode, maxHands, detectionConfidencede, trackingConfidence)
		self.mpDraw = mediapipe.solutions.drawing_utils
		self.shape = None
		self.landmarks = None
		# self.handFingers = []

	def findHands(self, img, BGR=True, flip=False, drawLandmarks=True, drawConnections=True):
		self.shape = img.shape
		if BGR:
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		if flip:
			img = cv2.flip(img, 0)
		results = self.hands.process(img)
		self.landmarks = results.multi_hand_landmarks
		self.handFingers = []
		if len(self.landmarks) > 0:
			for hand in self.landmarks:
				if drawLandmarks:
					self.mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS if drawConnections)
				for lmk in hand.landmark:
					lmk.y = int(lmk.y * self.shape[0])
					lmk.x = int(lmk.x * self.shape[1])
				# self.handFingers.append({'thumb':None, 'index':None, 'middle':None, 'ring':None, 'pinky':None})
			return self.landmarks, img
		else:
			return None, img

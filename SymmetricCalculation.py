import math

def rotateAlphaX(x, y):
  magnitude = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
  phase = math.atan2(y, x) + (120.0 * (math.pi / 180.0))
  return magnitude * math.cos(phase)

def rotateAlphaY(x, y):
  magnitude = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
  phase = math.atan2(y, x) + (120.0 * (math.pi / 180.0))
  return magnitude * math.sin(phase)

def cartesian_to_polar(x, y):
    magnitude = math.sqrt(x**2 + y**2)
    angle_rad = math.atan2(y, x)
    angle_degrees = math.degrees(angle_rad)
    return magnitude, angle_degrees


inputOneMag, inputOneAngle = input("Input one vector length, angle ").split(",")
oneMag = float(inputOneMag)
oneAngle = float(inputOneAngle)

inputTwoMag, inputTwoAngle = input("Input second vector length, angle ").split(",")
twoMag = float(inputTwoMag)
twoAngle = float(inputTwoAngle)

inputThreeMag, inputThreeAngle = input("Input third vector length, angle ").split(",")
threeMag = float(inputThreeMag)
threeAngle = float(inputThreeAngle)


oneX = oneMag * math.cos(oneAngle * (math.pi / 180.0))
oneY = oneMag * math.sin(oneAngle * (math.pi / 180.0))

twoX = twoMag * math.cos(twoAngle * (math.pi / 180.0))
twoY = twoMag * math.sin(twoAngle * (math.pi / 180.0))

threeX = threeMag * math.cos(threeAngle * (math.pi / 180.0))
threeY = threeMag * math.sin(threeAngle * (math.pi / 180.0))


posOneX = (oneX + rotateAlphaX(twoX, twoY) + rotateAlphaX(rotateAlphaX(threeX, threeY), rotateAlphaY(threeX, threeY))) / 3.0
posOneY = (oneY + rotateAlphaY(twoX, twoY) + rotateAlphaY(rotateAlphaX(threeX, threeY), rotateAlphaY(threeX, threeY))) / 3.0

posTwoX = rotateAlphaX(posOneX, posOneY)
posTwoY = rotateAlphaY(posOneX, posOneY)

posThreeX = rotateAlphaX(posTwoX, posTwoY)
posThreeY = rotateAlphaY(posTwoX, posTwoY)

posMag, posAngleOne = cartesian_to_polar(posOneX, posOneY)
posMag, posAngleTwo = cartesian_to_polar(posTwoX, posTwoY)
posMag, posAngleThree = cartesian_to_polar(posThreeX, posThreeY)

posVectors = [(posMag, posAngleOne), (posMag, posAngleTwo), (posMag, posAngleThree)]
print('positive component vectors', posVectors)




negOneX = (oneX + rotateAlphaX(rotateAlphaX(twoX, twoY), rotateAlphaY(twoX, twoY)) + rotateAlphaX(threeX, threeY) ) / 3.0
negOneY = (oneY + rotateAlphaY(rotateAlphaX(twoX, twoY), rotateAlphaY(twoX, twoY)) + rotateAlphaY(threeX, threeY) ) / 3.0

negTwoX = rotateAlphaX(negOneX, negOneY)
negTwoY = rotateAlphaY(negOneX, negOneY)

negThreeX = rotateAlphaX(negTwoX, negTwoY)
negThreeY = rotateAlphaY(negTwoX, negTwoY)

negMag, negAngleOne = cartesian_to_polar(negOneX, negOneY)
negMag, negAngleTwo = cartesian_to_polar(negTwoX, negTwoY)
negMag, negAngleThree = cartesian_to_polar(negThreeX, negThreeY)

negVectors = [(negMag, negAngleOne), (negMag, negAngleTwo), (negMag, negAngleThree)]
print('negative component vectors', negVectors)




zeroX = (oneX + twoX + threeX) / 3.0
zeroY = (oneY + twoY + threeY) / 3.0

zeroMag, zeroAngle = cartesian_to_polar(zeroX, zeroY)

zeroVectors = [(zeroMag, zeroAngle)]
print('zero components', zeroVectors)
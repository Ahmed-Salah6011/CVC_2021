from imports_helperfunctions.ImportLib import *
from imports_helperfunctions.HelperFunc import *
from IDNumberParser import *
def CERTMatcher_bottom(InputImage):

    MIN_MATCH_COUNT=2
    detector=cv2.SIFT_create()
    FLANN_INDEX_KDITREE=0
    flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
    flann=cv2.FlannBasedMatcher(flannParam,{})
    trainImg = cv2.imread('ocr/cert_bottom_ref.jpg',0)
    trainKP,trainDesc=detector.detectAndCompute(trainImg,None)
    QueryImgBGR = InputImage
    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.knnMatch(queryDesc,trainDesc,k=2)
    goodMatch=[]

    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)

    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H)
    else:
        raise Exception('Not Enough match found,Make sure its an ID card and recapture the image again')
        
    Edged = four_point_transform(QueryImgBGR, queryBorder.reshape(4, 2))

    return Edged

def CERTMatcher_top(InputImage):
    

    MIN_MATCH_COUNT=2
    detector=cv2.SIFT_create()

    FLANN_INDEX_KDITREE=0
    flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
    flann=cv2.FlannBasedMatcher(flannParam,{})

    trainImg = cv2.imread('ocr/cert_top_ref.jpg',0)
    trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

    QueryImgBGR = InputImage

    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.knnMatch(queryDesc,trainDesc,k=2)
    goodMatch=[]

    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)

    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H)
    else:
        raise Exception('Not Enough match found,Make sure its an ID card and recapture the image again')
        
    Edged = four_point_transform(QueryImgBGR, queryBorder.reshape(4, 2))

    return Edged

def IDMatcher_back(InputImage):
    

    MIN_MATCH_COUNT=2
    detector=cv2.SIFT_create()

    FLANN_INDEX_KDITREE=0
    flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
    flann=cv2.FlannBasedMatcher(flannParam,{})

    trainImg = cv2.imread('ocr/ID_back_Ref.jpeg',0)
    trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

    QueryImgBGR = InputImage

    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.knnMatch(queryDesc,trainDesc,k=2)
    goodMatch=[]

    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)

    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H)
    else:
        raise Exception('Not Enough match found,Make sure its an ID card and recapture the image again')
        
    Edged = four_point_transform(QueryImgBGR, queryBorder.reshape(4, 2))

    return Edged
def IDMatcher(InputImage):
    

    MIN_MATCH_COUNT=2
    detector=cv2.SIFT_create()

    FLANN_INDEX_KDITREE=0
    flannParam=dict(algorithm=FLANN_INDEX_KDITREE,tree=5)
    flann=cv2.FlannBasedMatcher(flannParam,{})

    trainImg = cv2.imread('ocr/atef.jpeg',0)
    trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

    QueryImgBGR = InputImage

    QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
    queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
    matches=flann.knnMatch(queryDesc,trainDesc,k=2)
    goodMatch=[]

    for m,n in matches:
        if(m.distance<0.75*n.distance):
            goodMatch.append(m)

    if(len(goodMatch)>MIN_MATCH_COUNT):
        tp=[]
        qp=[]
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp=np.float32((tp,qp))
        H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)
        h,w=trainImg.shape
        trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder=cv2.perspectiveTransform(trainBorder,H)
    else:
        raise Exception('Not Enough match found,Make sure its an ID card and recapture the image again')
        
    Edged = four_point_transform(QueryImgBGR, queryBorder.reshape(4, 2))

    return Edged
def CERTCutter_bottom(InputImage):
    
    Kernel = np.ones((2,2), np.uint8)
    Kernel_Vertical = np.ones((2,1), np.uint8)
    Kernel_sharpen = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    Edged = CERTMatcher_bottom(InputImage)
    Edged = cv2.resize(Edged,(Edged.shape[1],1000))
    Gaussian=cv2.GaussianBlur(Edged,(7,7),2)
    Edged_Gray = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2GRAY)
    Edged_Gray = cv2.fastNlMeansDenoising(Edged_Gray,10,10,7,21) 
    Edged_Gray = cv2.filter2D(Edged_Gray, -1, Kernel_sharpen)
    Name1   = Edged_Gray[600:,:]

    _,Name1 = cv2.threshold(Name1,180,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Name1 = cv2.filter2D(Name1, -1, Kernel_sharpen)
    Name1   = cv2.erode(Name1,Kernel_Vertical,iterations=1)



    return Name1
def CERTCutter_top(InputImage):
    
    Kernel = np.ones((2,2), np.uint8)
    Kernel_Vertical = np.ones((2,1), np.uint8)
    Kernel_sharpen = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    Edged = CERTMatcher_top(InputImage)
    Edged_Resized = cv2.resize(Edged,(1600,990))
    Gaussian=cv2.GaussianBlur(Edged_Resized,(7,7),2)
    Edged_Gray = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2GRAY)
    Edged_Gray = cv2.fastNlMeansDenoising(Edged_Gray,10,10,7,21) 
    Edged_Gray = cv2.filter2D(Edged_Gray, -1, Kernel_sharpen)

    Name1   = Edged_Gray[210:990,0:1550]

    _,Name1 = cv2.threshold(Name1,180,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Name1 = cv2.filter2D(Name1, -1, Kernel_sharpen)
    Name1   = cv2.erode(Name1,Kernel_Vertical,iterations=1)

   

    return Name1


def IDCutter(InputImage):
    
    Kernel = np.ones((2,2), np.uint8)
    Kernel_Vertical = np.ones((2,1), np.uint8)
    Kernel_sharpen = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])

    Edged = IDMatcher(InputImage)


    Edged_Resized = cv2.resize(Edged,(1600,990))
    Gaussian=cv2.GaussianBlur(Edged_Resized,(7,7),2)
    Edged_Gray = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2GRAY)
    Edged_Gray = cv2.fastNlMeansDenoising(Edged_Gray,10,10,7,21) 
    Edged_Gray = cv2.filter2D(Edged_Gray, -1, Kernel_sharpen)


    ID      = Edged_Gray[740:900,650:1550]
    Name1   = Edged_Gray[250:355,1100:1550]
    Name2   = Edged_Gray[360:475,600:1550]
    Address = Edged_Gray[480:680,600:1550]
    ID_Code = Edged_Gray[870:1060,120:550]


    ID=cv2.erode(ID,Kernel,iterations=3)
    _,ID = cv2.threshold(ID,160,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ID=cv2.dilate(ID,Kernel,iterations=3)


    _,Name1 = cv2.threshold(Name1,180,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Name1 = cv2.filter2D(Name1, -1, Kernel_sharpen)
    Name1   = cv2.erode(Name1,Kernel_Vertical,iterations=1)


    _,Name2 = cv2.threshold(Name2,180,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Name2 = cv2.filter2D(Name2, -1, Kernel_sharpen)
    Name2   = cv2.erode(Name2,Kernel_Vertical,iterations=1)

    _,Address = cv2.threshold(Address,160,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Address   = cv2.dilate(Address,Kernel,iterations=1)
    Address = cv2.filter2D(Address, -1, Kernel_sharpen)
    Address   = cv2.erode(Address,Kernel_Vertical,iterations=1)

    _,ID_Code = cv2.threshold(ID_Code,160,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ID_Code = cv2.morphologyEx(ID_Code, cv2.MORPH_OPEN, Kernel,iterations=3)
    
    return ID,Name1,Name2,Address,ID_Code


def IDCutter_back(InputImage):
    Kernel = np.ones((2,2), np.uint8)
    Kernel_Vertical = np.ones((2,1), np.uint8)
    Kernel_sharpen = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
    Edged = IDMatcher_back(InputImage)
    Edged_Resized = cv2.resize(Edged,(1600,990))
    Gaussian=cv2.GaussianBlur(Edged_Resized,(7,7),2)
    Edged_Gray = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2GRAY)
    Edged_Gray = cv2.fastNlMeansDenoising(Edged_Gray,10,10,7,21) 
    Edged_Gray = cv2.filter2D(Edged_Gray, -1, Kernel_sharpen)

    Name1   = Edged_Gray[120:405,0:1450]
    _,Name1 = cv2.threshold(Name1,160,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Name1 = cv2.filter2D(Name1, -1, Kernel_sharpen)
    Name1   = cv2.erode(Name1,Kernel_Vertical,iterations=1)
#     cv2.imwrite('img.jpg',Name1)
    return Name1


def IDParser(ID,Name1,Name2,Address,ID_Code):
    
    ID_Text = pytesseract.image_to_string(ID,lang='ara_number')
    ID_Text = ''.join(ID_Text.split())
    #print(ID_Text)

    config = '-l ara-amiri-3000 --oem 1 --psm 7'
    Name1_Text = pytesseract.image_to_string(Name1,config=config)
    Name1_Text = re.sub(r'[^\w]', ' ', Name1_Text)
    Name1_Text = re.sub(r'[0-9]+', '', Name1_Text)
    Name1_Text = Name1_Text.replace(' ', '')
    Name1_Text = " ".join(Name1_Text.split())
    #print(Name1_Text)

    config = '-l ara-amiri-3000 --oem 1 --psm 11'
    Name2_Text = pytesseract.image_to_string(Name2,config=config)
    Name2_Text = re.sub(r'[^\w]', ' ', Name2_Text)
    Name2_Text = re.sub(r'[0-9]+', '', Name2_Text)
    Name2_Text = " ".join(Name2_Text.split())
    #print(Name2_Text)

    Name = Name1_Text + " " + Name2_Text
    #print(Name)

    config = '-l Arabic2 --oem 1 --psm 11'
    Address_Text = pytesseract.image_to_string(Address,config=config)
    Address_Text = Address_Text.replace('\n', ' ')
    Address_Text = " ".join(Address_Text.split())
    #print(Address_Text)

    config = '-l eng --oem 1 --psm 7'
    ID_Code_Text = pytesseract.image_to_string(ID_Code,config=config)
    ID_Code_Text = re.sub(r'[^\w]', ' ', ID_Code_Text)
    ID_Code_Text = "".join(ID_Code_Text.split())
    ID_Code_Text = ID_Code_Text.replace('_', '')

    #print(ID_Code_Text)

    iD = ID_Text

    if len(iD)==14:
        DateOfBirth = getDateOfBirth(iD)
        Gender      = getGender(iD)
        GovName     = getGovName(iD)[0]
        DateofRetir = getDateOfRetirement(iD)

    else:
        DateOfBirth = None
        Gender      = None
        GovName     = None
        DateofRetir = None

    return ID_Text,Name,Address_Text,ID_Code_Text,DateOfBirth,Gender,GovName,DateofRetir

def CERTParser_top(Name1):

    config = '-l ara-amiri-3000 --oem 1 --psm 11'
    Name1_Text = pytesseract.image_to_string(Name1,config=config)
    Name1_Text = re.sub(r'[^\w]', ' ', Name1_Text)
    Name1_Text = re.sub(r'[0-9]+', '', Name1_Text)

    return Name1_Text.split()
def CERTParser_bottom(Name1):

    config = '-l ara-amiri-3000 --oem 1 --psm 11'
    Name1_Text = pytesseract.image_to_string(Name1,lang="ara_number")
    # Name1_Text = re.sub(r'[^\w]', ' ', Name1_Text)
    # Name1_Text = re.sub(r'[0-9]+', '', Name1_Text)

    return Name1_Text.split()

def IDParser(ID,Name1,Name2,Address,ID_Code):
    
    ID_Text = pytesseract.image_to_string(ID,lang='ara_number')
    ID_Text = ''.join(ID_Text.split())
    #print(ID_Text)

    config = '-l ara-amiri-3000 --oem 1 --psm 7'
    Name1_Text = pytesseract.image_to_string(Name1,config=config)
    Name1_Text = re.sub(r'[^\w]', ' ', Name1_Text)
    Name1_Text = re.sub(r'[0-9]+', '', Name1_Text)
    Name1_Text = Name1_Text.replace(' ', '')
    Name1_Text = " ".join(Name1_Text.split())
    #print(Name1_Text)

    config = '-l ara-amiri-3000 --oem 1 --psm 11'
    Name2_Text = pytesseract.image_to_string(Name2,config=config)
    Name2_Text = re.sub(r'[^\w]', ' ', Name2_Text)
    Name2_Text = re.sub(r'[0-9]+', '', Name2_Text)
    Name2_Text = " ".join(Name2_Text.split())
    #print(Name2_Text)

    Name = Name1_Text + " " + Name2_Text
    #print(Name)

    config = '-l Arabic2 --oem 1 --psm 11'
    Address_Text = pytesseract.image_to_string(Address,config=config)
    Address_Text = Address_Text.replace('\n', ' ')
    Address_Text = " ".join(Address_Text.split())
    #print(Address_Text)

    config = '-l eng --oem 1 --psm 7'
    ID_Code_Text = pytesseract.image_to_string(ID_Code,config=config)
    ID_Code_Text = re.sub(r'[^\w]', ' ', ID_Code_Text)
    ID_Code_Text = "".join(ID_Code_Text.split())
    ID_Code_Text = ID_Code_Text.replace('_', '')

    #print(ID_Code_Text)

    iD = ID_Text

    if len(iD)==14:
        DateOfBirth = getDateOfBirth(iD)
        Gender      = getGender(iD)
        GovName     = getGovName(iD)[0]
        DateofRetir = getDateOfRetirement(iD)

    else:
        DateOfBirth = None
        Gender      = None
        GovName     = None
        DateofRetir = None

    return ID_Text,Name,Address_Text,ID_Code_Text,DateOfBirth,Gender,GovName,DateofRetir
def IDParser_back(Name1):
    

    # config = '-l ara-amiri-3000 --oem 1 --psm 7'
    config = '-l ara-amiri-3000 --oem 1 --psm 11'
    Name1_Text = pytesseract.image_to_string(Name1,config=config)

    Name1_Text = Name1_Text.replace(' ', '')
    Name1_Text = " ".join(Name1_Text.split())
    #print(Name1_Text)

    return Name1_Text.split()

def IDScanner(InputImage):
    ID,Name1,Name2,Address,ID_Code = IDCutter(InputImage)
    ID_Text,Name,Address_Text,ID_Code_Text,DateOfBirth,Gender,GovName,DateofRetir = IDParser(ID,Name1,Name2,Address,ID_Code)
    if ID_Text and Name and Address_Text and ID_Code_Text and DateOfBirth and Gender and GovName and DateofRetir:
        data={
            "ID":ID_Text,
            "Name":Name,
            "Address":Address_Text,
            "Code":ID_Code_Text,
            "DateOfBirth":DateOfBirth,
            "Gender":Gender,
            "Governament":GovName,
            "DateofRetirement":DateofRetir,
        }
    else:
        data = {}
    return data
def CERTScanner_bottom(InputImage):
    Name1 = CERTCutter_bottom(InputImage)
    status = CERTParser_bottom(Name1)
    if status:
        return {'المجموع':status[0]}
    else:
        return {}

def IDScanner_back(InputImage):
    Name1 = IDCutter_back(InputImage)
    status = [word for word in IDParser_back(Name1) if word in ['انثى','ذكر','أنثى','مسلم','مسيحى','طالب','دكر']]
    data = ""
    print(status)
    if len(status) >= 3:
        
        data={
            "Gender":status[1],
            "Job":status[0],
            "Religion":status[2],
        }
    else:
        data = {}

    return data
def CERTScanner_top(InputImage):
    Name1 = CERTCutter_top(InputImage)
    status = CERTParser_top(Name1) 
    data = {}
    if status:
        for i in range(len(status)):
            if status[i] == 'اسم' and status[i+1] == 'الطالب':
                data[status[i] + ' '+status[i+1]] = " ".join(status[i+2:status.index('المديرية')])
            if status[i] == 'المديرية':
                data[status[i]] = status[i+1]
            if status[i] == 'المدرسة':
                data[status[i]] = " ".join(status[i+1:])
            if status[i] == 'اللغة' and status[i+1] == 'الأولى':
                data[status[i] + ' ' + status[i+1]] = status[i+2]
            if status[i] == 'اللغة' and status[i+1] == 'الثانية':
                data[status[i] + ' ' + status[i+1]] = status[i+2]
            if status[i] == 'الإدارة' and status[i+1] == 'التعليمية':
                data[status[i] + ' ' + status[i+1]] = status[i+2]
    else:
        data = {}
    return data

class Account:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def resetInfo(self, total, rewardName, rewardPoints, pcCurrent, pcTotal, mobileCurrent, mobileTotal, edgeCurrent, edgeTotal):
        self.total = total         
        self.rewardName = rewardName    
        self.rewardPoints = rewardPoints  
        self.pcCurrent = pcCurrent     
        self.pcTotal = pcTotal       
        self.mobileCurrent = mobileCurrent 
        self.mobileTotal = mobileTotal   
        self.edgeCurrent = edgeCurrent   
        self.edgeTotal = edgeTotal     

    def getAccountInfo(self):
        return self.total, self.rewardName, self.rewardPoints

    def getPCInfo(self):
        return self.pcCurrent, self.pcTotal
    
    def checkPCInfo(self):
        if self.pcCurrent == self.pcTotal:
            return True
        else:
            return False

    def getMobileInfo(self):
        return self.mobileCurrent, self.mobileTotal
    
    def checkMobileInfo(self):
        if self.mobileCurrent == self.mobileTotal:
            return True
        else:
            return False

    def getEdgeInfo(self):
        return self.edgeCurrent, self.edgeTotal

    def checkEdgeInfo(self):
        if self.edgeCurrent == self.edgeTotal:
            return True
        else:
            return False
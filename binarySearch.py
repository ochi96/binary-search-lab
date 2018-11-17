
import math

class Array:    
    def __init__(self,length,step):
        self.length=length
        self.step=step

    def create_Array(self):
        step=self.step
        length=self.length
        created_Array=([])
        for i in range(step,(length*step)+1,step):
            created_Array.append(i)
        return created_Array
        

    @staticmethod        
    def toTwenty():####
        return Array(20,1).create_Array()

    @staticmethod        
    def toForty(): #####
        return Array(20,2).create_Array()

    @staticmethod
    def toOneThousand():  #####
        return Array(100,10).create_Array()


class binarySearch:
    def __init__(self,length,step):
        self.binarySearch=Array(length,step)
        self.length=self.binarySearch.length
        self.step=self.binarySearch.step
        self.array=self.binarySearch.create_Array()
        self.count=0
        self.index=0

    def __getitem__(self,index):
        return self.array[index]


    def search(self,item):
        self.array.sort()
        first=0
        last=self.length-1
        first_item=self.array[first]
        last_item=self.array[last]

        if item<first_item or item>last_item:
            self.count=0
            return {"count":self.count,"index":-1}

        while True:

            if item==first_item or item==last_item:
                if item==first_item:
                    return {'count':self.count,'index':first}
                else:
                    return {'count':self.count,'index':last}

            if not(((item-first_item)%self.step==0) and ((last_item-item)%self.step==0)):
                return {'count':self.count,'index':-1}

        
            if (item-first_item)>(last_item-item):
                first=math.ceil((first+last)/2)
            elif (item-first_item)<(last_item-item):
                last=math.ceil((first+last)/2)
            else:
                return {"count":self.count,"index":int((first+last)/2)}

            first_item=self.array[first]
            last_item=self.array[last]
            self.count+=1
            
                        
        
        
        
        
        
                
            
    
        
            
            
    
    
    
    

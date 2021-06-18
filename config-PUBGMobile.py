
import struct
import os
import time
import androidhelper

__version__="1.2"
__author__="uche.sumarna"
__description__="""
setting config for pubg mobile support v.19
"""

# level available 4,5,6,7
FPSLevel=7 #level info 4=30fps 5=40fps 6=60fps 7=90fps
android=androidhelper.Android()
maps=[
 '00101111','01110011','01100100', 
 '01100011', '01100001', '01110010', 
 '01100100', '00101111', '01000001', 
 '01101110', '01100100', '01110010', 
 '01101111', '01101001', '01100100', 
 '00101111', '01100100', '01100001', 
 '01110100', '01100001', '00101111', 
 '01100011', '01101111', '01101101', 
 '00101110', '01110100', '01100101', 
 '01101110', '01100011', '01100101', 
 '01101110', '01110100', '00101110', 
 '01101001', '01100111', '00101111', 
 '01100110', '01101001', '01101100', 
 '01100101', '01110011', '00101111', 
 '01010101', '01000101', '00110100', 
 '01000111', '01100001', '01101101', 
 '01100101', '00101111', '01010011', 
 '01101000', '01100001', '01100100', 
 '01101111', '01110111', '01010100', 
 '01110010', '01100001', '01100011', 
 '01101011', '01100101', '01110010', 
 '01000101', '01111000', '01110100', 
 '01110010', '01100001', '00101111', 
 '01010011', '01101000', '01100001', 
 '01100100', '01101111', '01110111', 
 '01010100', '01110010', '01100001', 
 '01100011', '01101011', '01100101', 
 '01110010', '01000101', '01111000', 
 '01110100', '01110010', '01100001', 
 '00101111', '01010011', '01100001', 
 '01110110', '01100101', '01100100', 
 '00101111', '01010011', '01100001', 
 '01110110', '01100101', '01000111', 
 '01100001', '01101101', '01100101', 
 '01110011', '00101111', '01000001', 
 '01100011', '01110100', '01101001', 
 '01110110', '01100101', '00101110', 
 '01110011', '01100001', '01110110']
def settings(path,value):
  if not os.path.isfile(path):
      print 'pubg mobile not install'
      return
  fp=open(path,'rb+')
  data=fp.read()
  result=data.find('FPS')
  if result!=-1:
    fp.seek(result)
    a,b,c,d,e,f,g,h,i,j=config=struct.unpack("<8sh3B11s2iHi",fp.read(38))
    if a=="FPSLevel":
        if b==3072:
            if f=="IntProperty":
                sets=struct.pack("<8sh3B11s2iHi",a,b,c,d,e,f,g,h,i,value)
                fp.seek(result)
                fp.write(sets)
                fp.close()
                return True, "settings to level %s success"%(value)
    return False,""
conv=[int(x,2) for x in maps]

class PUBGMobileGFX(dict):
    
    def __init__(self):
        self.DEBUG=False
        self.data="181B1A1D1C1F1E111013121514171609080B0A0D0C0F0E010003383B3A3D3C3F3E313033323534373629282B2A2D2C2F2E21202349484B4A4D4C4F4E41405744"
        dpath=''.join([chr(i) for i in [47,115, 100, 99, 97, 114, 100, 47, 65, 110, 100, 114, 111, 105, 100, 47, 100, 97, 116, 97, 47, 99, 111, 109, 46, 116, 101, 110, 99, 101, 110, 116, 46, 105, 103, 47, 102, 105, 108, 101, 115, 47, 85, 69, 52, 71, 97, 109, 101, 47, 83, 104, 97, 100, 111, 119, 84, 114, 97, 99, 107, 101, 114, 69, 120, 116, 114, 97, 47, 83, 104, 97, 100, 111, 119, 84, 114, 97, 99, 107, 101, 114, 69, 120, 116, 114, 97, 47, 83, 97, 118, 101, 100, 47, 67, 111, 110, 102, 105, 103, 47, 65, 110, 100, 114, 111, 105, 100]])
        self.vars=''.join([chr(i) for i in (43,67,86,97,114,115)])
        self.path="%s/UserCustom.ini"%dpath
        self.fData={}
        self.get_keys()
        self.load()
        if not os.path.isfile("/sdcard/tmp/UserCustom.ini"):
            if not os.path.isdir("/sdcard/tmp"):
                os.mkdir("/sdcard/tmp")
            open("/sdcard/tmp/%s"%os.path.basename(self.path),"wb").write(open(self.path).read())
            if self.DEBUG:
                print "backup original file"
        self.fps_var=''.join([chr(x) for x in [114, 46, 80, 85, 66, 71, 68, 101, 118, 105, 99, 101, 70, 80, 83]])
        self.LOW=[76, 111, 119]
        self.MID=[77, 105, 100]
        self.HIGH=[72, 105, 103, 104]
        self.HDR=[72, 68, 82]
        self.FPS=30
        
    def __call__(self,value,data):
        if value=="unpack":
            attr,v=self.unpack(data).split("=")
            att=attr.split(".")
            name=att[len(att)-1]
            setattr(self,name,v)
            self["config"][name]="%s=%s"%(attr,v)
            if not "%s=%s"%(attr,v) in self["data"]:
                self["data"].append("%s=%s"%(attr,v))
            
    def get_keys(self):
        if (self.fData):
            return self.fData
        pos=0
        fData={}
        for x in range(97,123):
            fData[chr(x)]=self.data[pos:pos+2]
            pos+=2
        for y in range(65,91):
            fData[chr(y)]=self.data[pos:pos+2]
            pos+=2
        for z in range(48,58):
            fData[chr(z)]=self.data[pos:pos+2]
            pos+=2
        for c in (46,61):
            fData[chr(c)]=self.data[pos:pos+2]
            pos+=2
        self.fData=fData
        return fData
        
    def conv(self,list):
        return "".join([chr(x) for x in list])
        
    def get_last(self,data):
        return data[len(data)-1]
        
    def restore_settings(self):
        if os.path.isfile(self.path):
            open(self.path,"wb").write(open("/sdcard/tmp/%s"%os.path.basename(self.path)).read())
            if self.DEBUG:
                print "restore success"
            return True
        return False
        
    def get_values(self):
        dk={}
        for k,v in self.fData.items():
            dk[v]=k
        return dk
        
    def equals(self,orig):
        for fps in (self.LOW,self.MID,self.HIGH,self.HDR):
            var="%s="%(self.fps_var+''.join([chr(x) for x in fps]))
            result="%s\n"%var
            if orig.find(var)!=-1:
                return True
        return False
        
    def get_settings(self):
        return "\n".join((self["config"].keys()))
        
    def get_value(self,name):
        return getattr(self,name)
        
    def save_config(self):
        cfg=self["data"]
        bck=self["backup"]
        base="[UserCustom DeviceProfile]\n"
        for f in cfg:
            k,v=f.split("=")
            attr=self.get_last(k.split("."))
            value=self.get_value(attr)
            dt="%s=%s"%(k,value)
            base+="%s\n"%(self.pack("%s"%(dt)))
        base+="\n"
        base+="[BackUp DeviceProfile]\n"
        for a in bck:
            base+="%s\n"%(self.pack(a))
        try:
            open(self.path,"wb").write(base)
            if self.DEBUG:
                print "config saved"
                print "setting success\n enjoy the game . . ."
            return True,"config saved"
        except:
            if self.DEBUG:
                print("error creating config")
        return False,False
        
       
    def load(self):
        k=open(self.path)
        self["config"]={}
        self["backup"]=[]
        self["data"]=[]
        data=k.readlines()
        for x in range(len(data)):
            st=data[x]
            if not st:
                break
            list_data=st.split("=")
            if len(list_data)==1 and not list_data[0]=="\n":
                self[list_data[0].split()[0][1:]]=[]
            elif len(list_data)==2:
                if self.has_key("UserCustom"):
                    if not self["backup"]:
                        self("unpack",list_data[1][:-1])
                    
                if self.has_key("BackUp"):
                    self["backup"].append(self.unpack(list_data[1][:-1]))
                    
    def set_fps_all(self,value):
        result=""
        res=[(x.split("=")[0],x.split("=")[1]) for x in self["data"]]
        keys=[k for k,v in res]
        for fps in (self.LOW,self.MID,self.HIGH,self.HDR):
            var="%s=%s"%(self.fps_var+''.join([chr(x) for x in fps]),value)
            result+="%s\n"%var
            attr,v=var.split("=")
            att=attr.split(".")
            name=att[len(att)-1]
            setattr(self,name,v)
            self["config"][name]="%s=%s"%(attr,v)
            if (not var.split("=")[0] in keys):
                self["data"].append(var)
            else:
                index=-1
                for i in self["data"]:
                    index+=1
                    if (i.split("=")[0]==var.split("=")[0]):
                        self["data"][index]="%s=%s"%(var.split("=")[0],self.get_last(var.split("=")))
            
        return result==[],result
    def set_fps(self,type,fps):
        if type in (self.LOW,self.MID,self.HIGH,self.HDR):
            var="%s=%s"%(self.fps_var+''.join([chr(x) for x in type]),fps)
            attr,v=var.split("=")
            att=attr.split(".")
            name=att[len(att)-1]
            setattr(self,name,fps)
            self["config"][name]=var
            res=[(x.split("=")[0],x.split("=")[1]) for x in self["data"]]
            keys=[k for k,v in res]
            
            if (not var.split("=")[0] in keys):
                self["data"].append(var)
            else:
                index=-1
                for i in self["data"]:
                    index+=1
                    if (i.split("=")[0]==var.split("=")[0]):
                        self["data"][index]="%s=%s"%(var.split("=")[0],self.get_last(var.split("=")))
            return True,fps
        return False,fps
    def unpack(self,data):
        values=self.get_values()
        return "".join([values[data[x:x+2]] for x in range(0,len(data),2)])
        
    def pack(self,data):
        keys=self.get_keys()
        return "%s=%s"%(self.vars,"".join([keys[data[x:x+1]] for x in range(len(data))]))
    
if __name__=="__main__":
    gfx=PUBGMobileGFX()
    gfx.DetailMode=0
    gfx.MobileSimpleShader=0
    gfx.ShadowQuality=0
    gfx.MobileNumDynamicPointLights=0
    gfx.MSAACount=4.0
    gfx.MaterialQualityLevel=0
    gfx.LODDistanceScale=0.8
    gfx.UserVulkanSetting=0
    gfx.DepthOfFieldQuality=0
    gfx.BloomQuality=0
    gfx.PUBGDeviceFPSMid=60
    gfx.SetDecalBakingRTSizeInLobby=1024
    gfx.StaticMeshLODDistanceScale=0.8
    gfx.ParticleLODBias=2
    gfx.AntiAliasing=0.0
    gfx.MinLOD=0
    gfx.MaxCSMResolution=4
    gfx.MobileHDR=0
    gfx.MaxMobileCascades=2
    gfx.UserHDRSetting=4
    gfx.SceneColorFormat=0.0
    gfx.ACESStyle=4
    gfx.PoolSize=250
    gfx.MobileMSAA=0
    gfx.RefractionQuality=0
    gfx.DynamicObjectShadow=1
    gfx.UserQualitySetting=0
    gfx.UserShadowSwitch=0
    gfx.MaxAnisotropy=1
    gfx.EmitterSpawnRateScale=1.0
    gfx.LightShaftQuality=0
    gfx.PUBGLDR=1
    gfx.MobileContentScaleFactor=1.0
    gfx.DistanceScale=0
    gfx.UserMSAASetting=0
    
    def show(msg):
        android.dialogCreateAlert("Info",msg)
        android.dialogShow()
        time.sleep(2)
        android.dialogDismiss()
    def CreateAlert(title,msg):
        android.dialogCreateAlert(title,msg)
        android.dialogSetNegativeButtonText("Cancel")
        android.dialogSetPositiveButtonText("Ok")
        android.dialogShow()
        response=android.dialogGetResponse().result
        android.dialogDismiss()
        
        if(response["which"]=="positive"):
            data=android.getLaunchableApplications()
            for name in data[1]:
                    if name=="PUBG MOBILE":
                        print 'opening pubg mobile'
                        time.sleep(2)
                        android.startActivity("android.intent.action.MAIN", None, None, None, False,"com.tencent.ig", data[1][name])
        if(response["which"]=="negative"):
            show("Launch Cancel")
        
    def createDialog():
        info="                          LEVEL INFO\n\n       4=30fps 5=40fps 6=60fps 7=90fps"
        android.dialogCreateInput("FPS Level",info, defaultText="%s"%FPSLevel,inputType="number")
        android.dialogSetNegativeButtonText("Cancel")
        android.dialogSetPositiveButtonText("Ok")
        android.dialogShow()
        response=android.dialogGetResponse().result
        android.dialogDismiss()
        
        if(response["which"]=="positive"):
           if int(response["value"]) in [4,5,6,7]:
               config=settings(''.join([chr(i) for i in conv]),int(response["value"]))
               gfx.set_fps_all({4:30,5:45,6:60,7:90}[int(response["value"])])
               if (config[0]):
        	          show(config[1])
               save=gfx.save_config()
               if(save[0]):
                   show(save[1])
               CreateAlert("PUBG MOBILE","open pubg mobile ?")

           else:
               android.dialogCreateAlert("Info","please a insert valid Level")
               android.dialogShow()
               time.sleep(2)
               android.dialogDismiss()
               createDialog()
        if(response["which"]=="negative"):
            show("Settings Cancel")
    createDialog()

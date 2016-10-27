import requests
import time
import random
import json
import sys

class movement:
    
    def sample(self):
        url='http://192.168.1.43:4035/gotapi/drive_controller/move?serviceId=68:86:E7:03:CB:BC.35e03745e6edb1d37b2ef4cc9d14e478.localhost.deviceconnect.org&accessToken=null&'
        #全身
        URL=url+'angle=0&speed=0.3'
        requests.post(URL)
        time.sleep(5)
        #後退
        URL=url+'angle=180&speed=0.47'
        requests.post(URL)
        time.sleep(5)
        #左
        URL=url+'angle=270&speed=0.47'
        requests.post(URL)
        time.sleep(5)
        #右
        URL=url+'angle=90&speed=0.47'

        requests.post(URL)
        time.sleep(5)

    def normal(self):
        url='http://192.168.1.43:4035/gotapi/drive_controller/move?serviceId=68:86:E7:03:CB:BC.35e03745e6edb1d37b2ef4cc9d14e478.localhost.deviceconnect.org&accessToken=null&'
        select=random.randint(1,4)
        if select==1:
            #パターン１
            URL=url+'angle=0&speed=0.3'
            requests.post(URL)
            print("normal 前進")
            URL=url+'angle=90&speed=0.3'
            requests.post(URL)
            print("normal 右")
            URL=url+'angle=225&speed=0.3'
            requests.post(URL)
            print("normal 左斜め後ろ")
        elif select==2:
            #パターン２
            URL=url+'angle=90&speed=0.3'
            requests.post(URL)
            print("normal 右")
            URL=url+'angle=0&speed=0.3'
            requests.post(URL)
            print("normal 前進")
            URL=url+'angle=225&speed=0.3'
            requests.post(URL)
            print("normal 左斜め後ろ")
        elif select==3:
            #パターン３
            URL=url+'angle=0&speed=0.3'
            requests.post(URL)
            print("normal 前進")
            URL=url+'angle=180&speed=0.3'
            requests.post(URL)
            print("normal 後退")
        elif select==4:
            #パターン４
            URL=url+'angle=180&speed=0.3'
            requests.post(URL)
            print("normal 後退")
            URL=url+'angle=45&speed=0.3'
            requests.post(URL)
            print("normal 右斜め上")
            URL=url+'angle=315&speed=0.3'
            requests.post(URL)
            print("normal 左斜め上")
            URL=url+'angle=180&speed=0.3'
            requests.post(URL)
            print("normal 後退")

    def tense(self):
        url='http://192.168.1.43:4035/gotapi/drive_controller/move?serviceId=68:86:E7:03:CB:BC.35e03745e6edb1d37b2ef4cc9d14e478.localhost.deviceconnect.org&accessToken=null&'
        select=random.randint(1,4)
        if select==1:
            #パターン１
            URL=url+'angle=0&speed=0.5'
            requests.post(URL)
            print("tense 前進")
            URL=url+'angle=90&speed=0.5'
            requests.post(URL)
            print("tense 右")
            URL=url+'angle=225&speed=0.5'
            requests.post(URL)
            print("tense 左斜め後ろ")
            #sys.exit()
        elif select==2:
            #パターン２
            URL=url+'angle=90&speed=0.5'
            requests.post(URL)
            print("tense 右")
            URL=url+'angle=0&speed=0.5'
            requests.post(URL)
            print("tense 前進")
            URL=url+'angle=225&speed=0.5'
            requests.post(URL)
            print("tense 左斜め後ろ")
        elif select==3:
            #パターン３
            URL=url+'angle=0&speed=0.5'
            requests.post(URL)
            print("tense 前進")
            URL=url+'angle=180&speed=0.5'
            requests.post(URL)
            print("tense 後退")
        elif select==4:
            #パターン４
            URL=url+'angle=180&speed=0.5'
            requests.post(URL)
            print("tense 後退")
            URL=url+'angle=45&speed=0.5'
            requests.post(URL)
            print("tense 右斜め上")
            URL=url+'angle=315&speed=0.5'
            requests.post(URL)
            print("tense 左斜め上")
            URL=url+'angle=180&speed=0.5'
            requests.post(URL)
    def decide(self):
        URL='http://192.168.1.43:4035/gotapi/health/heartrate?serviceId=F3%3A3B%3A15%3A7E%3A29%3ABB.e9484eb5107adfef1af6a0dc65c03232.localhost.deviceconnect.org&accessToken=null'
        s=requests.get(URL).json()
        encode_json_data = json.dumps(s)
        #print (encode_json_data)#for test
        decode_json_data = json.loads(encode_json_data)
        rate=int(decode_json_data['heartRate'])#これが行動決定の基準値
        print(rate)
        if rate >= 90 and rate <= 105:
            requests.post('http://192.168.1.43:4035/gotapi/light?serviceId=68%3A86%3AE7%3A03%3ACB%3ABC.35e03745e6edb1d37b2ef4cc9d14e478.localhost.deviceconnect.org&accessToken=null&lightId=1&name=Sphero%20LED&color=00ff00&brightness=1')
            self.normal()
            print("Action:normal")
        elif rate > 105:
            requests.post('http://192.168.1.43:4035/gotapi/light?serviceId=68%3A86%3AE7%3A03%3ACB%3ABC.35e03745e6edb1d37b2ef4cc9d14e478.localhost.deviceconnect.org&accessToken=null&lightId=1&name=Sphero%20LED&color=ff0000&brightness=1')
            self.tense()
            print("Action:tense")
        else:
            requests.post('http://192.168.1.43:4035/gotapi/light?serviceId=68%3A86%3AE7%3A03%3ACB%3ABC.35e03745e6edb1d37b2ef4cc9d14e478.localhost.deviceconnect.org&accessToken=null&lightId=1&name=Sphero%20LED&color=0000ff&brightness=1')
            print("NoAction")
        time.sleep(3)
        self.decide()



def main():
    move=movement()
    move.decide()

if __name__ == "__main__":
   main()

        
        
            
            




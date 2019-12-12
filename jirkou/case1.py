import requests

uri = "http://backend.paas.env"

def test_02(self):
    '获取face_id'
    URL = "/api/one_image/create/v3"
    url = self.uri + URL
    body = {
        "face_url":"https://pic.igengmei.com/2019/10/23/1503/caab087dc836-s"
         #"face_url":Case.seven_url
    }
    result = requests.post(url=url,data=body)
    res = result.json()
    face_url = res.get("data").get("face_url")
    if face_url is None:
        raise RuntimeError('face_url:为空')
    face_id = res.get("data").get("face_id")
    if face_id is None:
        raise RuntimeError('face_id:为空')
    #获取面部 face_id
    print(face_id)



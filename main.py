from flask import Flask, render_template, request, jsonify
from utils import isStartWithF

#Flask 객체 인스턴스 생성
app = Flask(__name__)
hashtag = "name"
users = []
users.append({
  "user_id":"joon",
  "name":"minjoon",
  "password":"12345",
  "age":15,
  "height":175
})
@app.route("/users", methods=["GET"])
def getUser():
    if 'min' in users[2] :
        return users['name']

    return users
    # 1. age, height, name을 쿼리파라미터로 받기
    #2. users에서 age 이상, height 이상, name in 조건 filtering
    #3. 필터링된 모든 결과를 리턴


@app.route('/users', methods=['POST'])
def createUser():
   bodyParams = request.get_json()
   name_receive = bodyParams["name_give"]
   password_receive = bodyParams["password_give"]
   user_id = bodyParams["user_id"]
   age = bodyParams["age_give"]
   height = bodyParams["height_give"]
   users.append({
       "user_id":user_id,
       "name":name_receive,
       "password":password_receive,
       "age":age,
       "height":height
   })
   return jsonify({'result':'success', 'msg': 'POST 요청!'})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
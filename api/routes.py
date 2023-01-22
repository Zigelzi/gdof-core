from flask import make_response, jsonify

from api import app

# Status message descriptions
status_msg_fail = "fail"
status_msg_success = "success"

likes = []


@app.get("/likes/<string:article_id>")
def get_likes(article_id):
    response = {"status": status_msg_success, "article_id": article_id}
    print(response)
    response_json = jsonify(response)

    return make_response(response_json, 200)


@app.post("/likes/<string:article_id>")
def add_like(article_id):
    response = {"status": status_msg_success, "article_id": article_id}
    likes.append({"article_id": article_id})
    response["likes"] = likes

    response_json = jsonify(response)
    print(likes)

    return make_response(response_json, 200)

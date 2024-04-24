from flask import Flask
import facility_dao as facility
import comments_dao as comments
import post_dao as post
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

# facility
app.add_url_rule('/get_facility/<int:id>', view_func=facility.get_facility, methods=['GET'])
app.add_url_rule('/get_all_facility/', view_func=facility.get_all_facility, methods=['GET'])

#post
app.add_url_rule('/add_post/<int:id>', view_func=post.add_post, methods=['POST'])
app.add_url_rule('/get_post/<int:id>', view_func=post.get_post, methods=['GET'])
app.add_url_rule('/get_all_post', view_func=post.get_all_post, methods=['GET'])
app.add_url_rule('/delete_post/<int:id>', view_func=post.delete_post, methods=['DELETE'])

#comments
app.add_url_rule('/add_comments/<int:id>', view_func=comments.add_comments, methods=['POST'])
app.add_url_rule('/get_comments/<int:id>', view_func=comments.get_comments, methods=['GET'])
app.add_url_rule('/get_all_comments/', view_func=comments.get_all_comments, methods=['GET'])
app.add_url_rule('/delete_comments/<int:id>', view_func=comments.delete_comments, methods=['DELETE'])

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
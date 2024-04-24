from flask import request, jsonify, render_template
import db_connection as db


def add_post():
    connection = db.create_connection()
    cursor = connection.cursor()
    id = request.json.get('id')
    title = request.json.get('title')
    content = request.json.get('content')
    create_at = request.json.get('create_at')
    username = request.json.get('username')
    facility_id = request.json.get('facility_id')
    cursor.callproc('post_pkg.addpost', [id, title, content,create_at,username,facility_id])
    cursor.close()
    connection.commit()
    return jsonify(message="post added"), 201


def get_post(id):
    connection = db.create_connection()
    cursor = connection.cursor()
    result = cursor.callfunc('post_pkg.Getpost', db.CURSOR, [id])
    post = [dict(zip([column[0] for column in result.description], row)) for row in result]
    cursor.close()
    return jsonify(post=post)

def get_all_post():
    connection = db.create_connection()
    cursor = connection.cursor()
    result = cursor.callfunc('post_pkg.Getallpost', db.CURSOR)
    posts = [dict(zip([column[0] for column in result.description], row)) for row in result]
    cursor.close()
    return jsonify(posts=posts)

def delete_post(id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('post_pkg.deletepost', [id])
    cursor.close()
    connection.commit()
    return jsonify(message="post deleted"), 200
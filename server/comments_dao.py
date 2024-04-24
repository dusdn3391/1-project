from flask import request, jsonify, render_template
import db_connection as db


def add_comments():
    connection = db.create_connection()
    cursor = connection.cursor()
    id = request.json.get('id')
    create_at = request.json.get('create_at')
    comments = request.json.get('comments')
    username = request.json.get('username')
    facility_id = request.json.get('facility_id')
    cursor.callproc('comments_pkg.addcomments', [id,comments,create_at,username,facility_id])
    cursor.close()
    connection.commit()
    return jsonify(message="post added"), 201


def get_comments(id):
    connection = db.create_connection()
    cursor = connection.cursor()
    result = cursor.callfunc('comments_pkg.Getcomments', db.CURSOR, [id])
    comments = [dict(zip([column[0] for column in result.description], row)) for row in result]
    cursor.close()
    return jsonify(comments=comments)

def get_all_comments():
    connection = db.create_connection()
    cursor = connection.cursor()
    result = cursor.callfunc('comments_pkg.GetAllcomments', db.CURSOR)
    commentss = [dict(zip([column[0] for column in result.description], row)) for row in result]
    cursor.close()
    return jsonify(commentss=commentss)

def delete_comments(id):
    connection = db.create_connection()
    cursor = connection.cursor()
    cursor.callproc('comments_pkg.Getcomments', [id])
    cursor.close()
    connection.commit()
    return jsonify(message="post deleted"), 200
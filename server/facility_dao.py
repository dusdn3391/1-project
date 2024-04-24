from flask import request, jsonify, render_template
import db_connection as db

def get_facility(id):
    connection = db.create_connection()    
    cursor = connection.cursor()
    facility_cursor = cursor.callfunc('facility_pkg.Getfacility', db.CURSOR, [id])
    facility = [dict(zip([column[0] for column in facility_cursor.description], row)) for row in facility_cursor]
    return jsonify(facility), 200

def get_all_facility():
    connection = db.create_connection()    
    cursor = connection.cursor()
    facilitys_cursor = cursor.callfunc('facility_pkg.GetAllfacility', db.CURSOR)
    facilitys = [dict(zip([column[0] for column in facilitys_cursor.description], row)) for row in facilitys_cursor]
    return jsonify(facilitys=facilitys), 200


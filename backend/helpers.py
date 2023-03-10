from flask import jsonify
def validate_skills(skills):
    if skills == []:
        return False
    if type(skills) != list:
        return False
    for skill in skills:
        if skill == "":
            return False
    return skills


def api_response(data, status_code, err=None):
    if err:
        return jsonify({"error": err}), status_code
    return jsonify(data), status_code

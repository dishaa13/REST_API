from flask import Flask, jsonify
todo = Flask('__name__')

students = [
    {
        'id':1,
        'name':'Disha',
        'age':20
    },
    {
        'id':2,
        'name':'Anjana',
        'age':20
    },
    {
        'id':3,
        'name':'Mahesh',
        'age':20
    },
]

@todo.route('/students-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_students_by_id(id):
    print(id)
    for std in students:
        if std['id']==id:
            return jsonify(std)
        print(std)

    return jsonify('not found')


if __name__ == '__main__':
    todo.run(

        debug=True
    )
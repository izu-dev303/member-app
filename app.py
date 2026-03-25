from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

# 起動時にDBを初期化
database.init_db()

# メンバー一覧
# メンバー一覧
@app.route('/')
def list_members():
    keyword = request.args.get('keyword', '')
    members = database.get_all_members()
    if keyword:
        members = [m for m in members if keyword in m[1]]
    return render_template('list.html', members=members, keyword=keyword)

# メンバー追加
@app.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        database.add_member(name, email)
        return redirect(url_for('list_members'))
    return render_template('add.html')

# メンバー編集
@app.route('/edit/<int:member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    members = database.get_all_members()
    member = next((m for m in members if m[0] == member_id), None)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        database.update_member(member_id, name, email)
        return redirect(url_for('list_members'))
    return render_template('edit.html', member=member)

# メンバー削除
@app.route('/delete/<int:member_id>')
def delete_member(member_id):
    database.delete_member(member_id)
    return redirect(url_for('list_members'))

if __name__ == '__main__':
    app.run(debug=True)
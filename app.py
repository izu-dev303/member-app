from member import load_members, add_member, delete_member, find_member, update_member
from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)

# 一覧表示
@app.route('/')
def index():
    keyword = request.args.get('keyword', '')
    members = load_members()
    if keyword:
        members = [m for m in members if keyword in m['name']]
    return render_template('list.html', members=members, keyword=keyword)

# 追加
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        add_member(name)
        return redirect('/')
    return render_template('add.html')

# 削除
@app.route('/delete/<int:member_id>')
def delete(member_id):
    delete_member(member_id)
    return redirect('/')

# 編集
@app.route('/edit/<int:member_id>', methods=['GET', 'POST'])
def edit(member_id):
    member = find_member(member_id)
    if request.method == 'POST':
        new_name = request.form['name']
        update_member(member_id, new_name)
        return redirect('/')
    return render_template('edit.html', member=member)

# CSVダウンロード
@app.route('/download')
def download():
    return send_file('members.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
 

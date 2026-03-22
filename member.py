import csv
import os

FILE_NAME = 'members.csv'

def load_members():
    members = []
    if not os.path.exists(FILE_NAME):
        return members
    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            members.append(row)
    return members

def save_members(members):
    with open(FILE_NAME, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(members)

def add_member(name):
    members = load_members()
    if members:
        new_id = str(max(int(m['id']) for m in members) + 1)
    else:
        new_id = '1'
    members.append({'id': new_id, 'name': name})
    save_members(members)

def delete_member(member_id):
    members = load_members()
    members = [m for m in members if m['id'] != str(member_id)]
    save_members(members)

def find_member(member_id):
    members = load_members()
    for m in members:
        if m['id'] == str(member_id):
            return m
    return None

def update_member(member_id, new_name):
    members = load_members()
    for m in members:
        if m['id'] == str(member_id):
            m['name'] = new_name
    save_members(members)
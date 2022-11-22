import sqlite3 as lite
from dict_factory import dict_factory
db = lite.connect("mic_plot.db")

# arr = ["Theo","Ms Sheinkopf","Hannah","Will Tackley","Noah","Felix","Louis","Amelia","Gabe","Lucy","Ashwin","Harry","Rosie","Emma","Leah"]
#
# for name in arr:
#     cur = db.execute(f"INSERT INTO characters(character_name) VALUES ('{name}')")
#     db.commit()
# #
#
# arr = []
# scene = 26
# vals = [13,1,6,5,11,9,20,15,7]
# for val in vals:
#     arr.append([scene,val])
# print(arr)
# #
# for record in arr:
#     cur = db.execute(f"INSERT INTO characters_in_scenes(scene_id,character_id) VALUES (?,?)",(record[0],record[1]))
#     db.commit()


#

def query_db(query, args=(), one=False):
    cur = db.execute(query, args)
    cur.row_factory = dict_factory
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

scenes = query_db("SELECT scene_id,scene_name FROM scenes")
arr = []
for scene in scenes:
    scene_id = scene["scene_id"]
    characters = query_db(f"SELECT character_name FROM characters c JOIN characters_in_scenes s ON c.character_id = s.character_id WHERE s.scene_id = {scene_id}")
    row = [char["character_name"] for char in characters]
    arr.append(row)

print(arr)

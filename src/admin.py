import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import pyperclip as pc

# Fetch the service account key JSON file contents
cred = credentials.Certificate('/home/manoj/Desktop/Clipy/src/sample-52c33-firebase-adminsdk-61fgt-8655212f66.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sample-52c33-default-rtdb.firebaseio.com'
})

ref = db.reference('/data/')

def paste_data(): # paste data into the database.

# As an admin, the app has access to read and write all data, regradless of Security Rules

    textp = pc.paste()
    # ref.set(textp)
    data  = {
        'text' : textp
    }
    json_object = json.dumps(data, indent = 1)
    ref.push(json_object)
    # print(json_object)



def copy_data(): # copy data from database.
    copied = []
    # copied = ref.child('data')
    try:
        copy = ref.order_by_child('text').limit_to_last(3).get()
        for key, val in copy.items():
            temp = val
            x = len(temp) - 3
            textc = temp[12:x]
            if(x > 50):
                textc = textc[:50] + '...'
                copied.append(textc)
            else:
                copied.append(textc)
        return (copied)

        # pc.copy(textc)

    except AttributeError:
        pass


# copy_data()
# paste_data()

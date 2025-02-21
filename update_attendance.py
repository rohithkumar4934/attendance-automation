import firebase_admin
from firebase_admin import credentials, firestore
import os

# Absolute path to the service account file
service_account_path = os.path.abspath("serviceAccountKey.json")

if not os.path.exists(service_account_path):
    print(f"❌ Firebase credentials file '{service_account_path}' is missing!")
    exit(1)

try:
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    attendance_ref = db.collection("attendance")
    docs = attendance_ref.get()
    
    for doc in docs:
        attendance_ref.document(doc.id).update({"attendance": "absent"})
    
    print("✅ All attendance records marked as absent!")

except Exception as e:
    print(f"❌ Error updating attendance: {e}")

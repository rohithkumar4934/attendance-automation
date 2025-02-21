import firebase_admin
from firebase_admin import credentials, firestore
import os

# Check if service account file exists
if not os.path.exists("serviceAccountKey.json"):
    print("❌ Firebase credentials file 'serviceAccountKey.json' is missing!")
    exit(1)

try:
    # Initialize Firebase with service account JSON
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Update attendance collection: Mark all records as "absent"
    attendance_ref = db.collection("attendance")
    
    docs = attendance_ref.get()
    for doc in docs:
        attendance_ref.document(doc.id).update({"attendance": "absent"})
    
    print("✅ All attendance records marked as absent!")

except Exception as e:
    print(f"❌ Error updating attendance: {e}")

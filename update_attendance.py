import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase with service account JSON
cred = credentials.Certificate("serviceAccountKey.json")  # 🔹 Your Firebase JSON key
firebase_admin.initialize_app(cred)
db = firestore.client()

# Update attendance collection: Mark all records as "absent"
attendance_ref = db.collection("attendance")

try:
    docs = attendance_ref.get()
    for doc in docs:
        attendance_ref.document(doc.id).update({"attendance": "absent"})
    
    print("✅ All attendance records marked as absent!")

except Exception as e:
    print(f"❌ Error updating attendance: {e}")

from supabase import create_client
import bcrypt
import re

# ==========================
# SUPABASE CONFIG
# ==========================

SUPABASE_URL = "https://watfqsymkyigszyqpqiv.supabase.co"
SUPABASE_KEY = "sb_publishable_nTX9vsAK5xGPO-RIrXCI8A_4NiY9ph7"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==========================
# EMAIL VALIDATION FUNCTION
# ==========================

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

# ==========================
# REGISTER USER
# ==========================

def register_user(email, password):

    # ---- Email Validation ----
    if not is_valid_email(email):
        return False, "Invalid email format"

    # ---- Password Validation ----
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    # ---- Check if user exists ----
    existing = supabase.table("users").select("*").eq("email", email).execute()

    if existing.data:
        return False, "User already exists"

    # ---- Hash Password ----
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # ---- Insert User ----
    response = supabase.table("users").insert({
        "email": email,
        "password": hashed_pw
    }).execute()

    if response.data:
        return True, "Registered successfully"
    else:
        return False, "Registration failed"


# ==========================
# LOGIN USER
# ==========================

def login_user(email, password):

    # ---- Basic Validation ----
    if not is_valid_email(email):
        return False, "Invalid email format"

    response = supabase.table("users").select("*").eq("email", email).execute()

    if not response.data:
        return False, "User not found"

    user = response.data[0]
    stored_password = user["password"]

    if bcrypt.checkpw(password.encode(), stored_password.encode()):
        return True, "Login successful"
    else:
        return False, "Incorrect password"
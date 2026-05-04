import re
import asyncio

# -----------------------------------------------
# Code Quality Demo File
# Contains deliberate issues for Aikido scanning
# -----------------------------------------------

MAX_RETRIES = 3
USER_ROLES = ["admin", "editor", "viewer"]


# Issue 1: Dead code after return
def get_user_role(user_id):
    if user_id == 1:
        return "admin"
    return "viewer"
    print("User role retrieved")  # Dead code — unreachable


# Issue 2: Magic number — should be a named constant
def calculate_timeout(requests):
    return requests * 42


# Issue 3: Regex compiled inside loop — wastes CPU on every iteration
def find_emails(text_list):
    results = []
    for text in text_list:
        pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
        matches = pattern.findall(text)
        results.extend(matches)
    return results


# Issue 4: Filtering inside a loop — inefficient
def process_active_users(users):
    results = []
    for user in users:
        active = [u for u in users if u.get("active")]
        if user in active:
            results.append(user)
    return results


# Issue 5: Inner await serialising work — should use asyncio.gather
async def fetch_all(urls):
    results = []
    for url in urls:
        result = await fetch(url)
        results.append(result)
    return results


async def fetch(url):
    await asyncio.sleep(0.1)
    return f"response from {url}"


# Issue 6: Unused variable
def calculate_discount(price, discount):
    tax_rate = 0.2  # Assigned but never used
    final_price = price - (price * discount)
    return final_price


# Issue 7: Missing return in conditional branch
def get_status_code(status):
    if status == "active":
        return 200
    elif status == "inactive":
        return 404
    # Missing else — returns None implicitly


# Issue 8: Mutable default argument — classic Python anti-pattern
def add_user(name, roles=[]):
    roles.append(name)
    return roles


# Issue 9: Bare except — swallows all errors silently
def load_config(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except:
        pass

import customtkinter as ctk
from tkinter import messagebox

# ---------- Logic (copied from your script) ----------
def calculate_fake_score(account):
    score = 0

    if len(account['username']) > 15:
        score += 1

    if not account['has_profile_photo']:
        score += 2

    ratio = account['following_count'] / (account['followers_count'] + 1)
    if ratio > 30:
        score += 6

    if account['post_count'] < 3:
        score += 3

    if account['post_count'] > 1000:
        score += 4

    if account['verified']:
        score -= 10

    return score


# ---------- GUI Part ----------
def check_account():
    try:
        username = username_entry.get().strip()
        has_photo = photo_switch.get()
        followers = int(followers_entry.get())
        following = int(following_entry.get())
        posts = int(posts_entry.get())
        verified = verified_switch.get()

        account = {
            'username': username,
            'has_profile_photo': has_photo,
            'followers_count': followers,
            'following_count': following,
            'post_count': posts,
            'verified': verified
        }

        score = calculate_fake_score(account)
        FAKE_THRESHOLD = 7

        if score >= FAKE_THRESHOLD:
            result_label.configure(
                text=f"Fake Score: {score}\n⚠️ Likely FAKE Account",
                text_color="red"
            )
        else:
            result_label.configure(
                text=f"Fake Score: {score}\n✅ Likely REAL Account",
                text_color="green"
            )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for counts!")


def reset_fields():
    username_entry.delete(0, "end")
    followers_entry.delete(0, "end")
    following_entry.delete(0, "end")
    posts_entry.delete(0, "end")
    photo_switch.deselect()
    verified_switch.deselect()
    result_label.configure(text="", text_color="white")


# ---------- Window ----------
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Fake Account Detector")
app.geometry("500x600")

title = ctk.CTkLabel(app, text="Fake Account Detector", font=("Arial", 22, "bold"))
title.pack(pady=20)

# Inputs
frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="both", expand=True)

username_label = ctk.CTkLabel(frame, text="Username:")
username_label.pack(anchor="w", padx=10)
username_entry = ctk.CTkEntry(frame, placeholder_text="Enter username")
username_entry.pack(padx=10, pady=5, fill="x")

photo_switch = ctk.CTkSwitch(frame, text="Has Profile Photo?")
photo_switch.pack(pady=5, padx=10)

verified_switch = ctk.CTkSwitch(frame, text="Is Verified?")
verified_switch.pack(pady=5, padx=10)

followers_label = ctk.CTkLabel(frame, text="Followers Count:")
followers_label.pack(anchor="w", padx=10)
followers_entry = ctk.CTkEntry(frame)
followers_entry.pack(padx=10, pady=5, fill="x")

following_label = ctk.CTkLabel(frame, text="Following Count:")
following_label.pack(anchor="w", padx=10)
following_entry = ctk.CTkEntry(frame)
following_entry.pack(padx=10, pady=5, fill="x")

posts_label = ctk.CTkLabel(frame, text="Post Count:")
posts_label.pack(anchor="w", padx=10)
posts_entry = ctk.CTkEntry(frame)
posts_entry.pack(padx=10, pady=5, fill="x")

# Buttons
check_button = ctk.CTkButton(app, text="Check Account", command=check_account)
check_button.pack(pady=10)

reset_button = ctk.CTkButton(app, text="Reset", fg_color="gray", command=reset_fields)
reset_button.pack(pady=5)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

app.mainloop()

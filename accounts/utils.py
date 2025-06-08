from pathlib import Path
import time

def user_profile_upload_handler(instance, filename):
    fpath = Path(filename)
    clean_name = fpath.stem.replace(" ", "_") #the clean name without suffix
    ext = fpath.suffix # the suffix like .jpg

    final_name = str(f"{clean_name}_{int(time.time())}{ext}") #creating a unique name

    upload_path = Path("UserProfilePictures") / f"USER_{instance.user.username}" #the address of the folder we want to save the pics on
    return str(upload_path / final_name)
    
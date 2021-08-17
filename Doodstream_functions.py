import urllib.request
import json

# Api key
api_key = "api_key"

# File code
file_code = "24mo0udvdri7" # 12 Digit file Code

# Folder Code
fld_id = "120134"   # Note - It is folder id no folder code

# ╔══════════════════════════╗
# ║ DOODSTREAM API Functions ║
# ╚══════════════════════════╝

# Account API Links
def account_info(key):
    return data_from_link("https://doodapi.com/api/account/info?key=" + key)

def account_report(key,last = "", from_date = "",to_date = ""):
    return data_from_link("https://doodapi.com/api/account/stats?key=" + key + "&last=" + last + "&from_date=" + from_date + "&to_date=" + to_date)

def dmca_list(key):
    return data_from_link("https://doodapi.com/api/dmca/list?key=" + key)

# Upload API Links
def clone_file(key, file_code, fld_id):
    return "https://doodapi.com/api/file/clone?key=" + key + "&file_code=" + file_code + "&fld_id=" + fld_id

def remote_upload(key, url, fld_id, new_title): # new title solution pending
    return data_from_link("https://doodapi.com/api/upload/url?key=" + key + "&url=" + url + "&fld_id=" + fld_id + "&new_title=" + new_title)

def remote_upload_status(key, file_code):
    return data_from_link("https://doodapi.com/api/urlupload/status?key=" + key + "&file_code=" + file_code)

def remote_upload_actions(key, action): # action must be restart_errors, clear_all, clear_errors
    return data_from_link("https://doodapi.com/api/urlupload/actions?key=" + key + "&" + action)

# Manage Folders API Links
def create_folder(key, name, parent_id):
    return data_from_link("https://doodapi.com/api/folder/create?key=" + key + "&name=" + name + "&parent_id=" + parent_id)

def rename_folder(key, fld_id, name):
    return data_from_link("https://doodapi.com/api/folder/rename?key=" + key + "&fld_id=" + fld_id + "&name=" + name)

def list_folders(key, fld_id, page = "0", per_page = "0"):
    return data_from_link("https://doodapi.com/api/folder/list?key=" + key + "&fld_id=" + fld_id + "&page=" + page + "&per_page=" + per_page)

# Manage Files API Links
def list_files(key, fld_id, page = "",per_page = "", ):
    return data_from_link("https://doodapi.com/api/file/list?key=" + key + "&fld_id=" + fld_id + "&page=" + page + "&per_page=" + per_page)

def file_status(key,file_code):
    return data_from_link("https://doodapi.com/api/file/check?key=" + key + "&file_code=" + file_code)

def file_info(key, file_code):
    return data_from_link("https://doodapi.com/api/file/info?key=" + key + "&file_code=" + file_code)

def file_images(key, file_code):
    return data_from_link("https://doodapi.com/api/file/image?key=" + key + "&file_code=" + file_code)

def file_rename(key, file_code, title):
    return data_from_link("https://doodapi.com/api/file/rename?key=" + key + "&file_code=" + file_code + "&title=" + title)

def file_search(key, search_term):
    return data_from_link("https://doodapi.com/api/search/videos?key=" + key + "&search_term=" + search_term)

# Remote Subtitles
def file_link_with_subtitle(key, file_code, subtitle_link, lable = "English"):
    return "https://dood.so/d/" + file_code +"?c1_file=" + subtitle_link + "&c1_label=" + lable # c1_file(Subtitle URL (srt or vtt)) # c1_label(Subtitle language or any lable)

# Data to Dictionary
def data_from_link(link):
    url = urllib.request.urlopen(link)
    temp = url.read()
    data = temp.decode('UTF-8')
    dict = json.loads(data)
    return dict


# Call Any Function to retive data from doodstream
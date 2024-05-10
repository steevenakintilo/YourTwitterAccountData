from file import *
import json

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from datetime import datetime, timedelta, date

class AccountData():  
  if os.path.exists(r'twitter_data\data\account.js') == False:  
    print("Unziping the file")
    unzip_file()
  
  if os.path.exists(r'twitter_data\data\account.js') == False:  
    print("The file provided is not twitter archive")
    exit()
  f = print_file_info(r'twitter_data\data\account.js').split("\n") 
  AccountId = get_account_data(f,"accountId").replace(",","")
  AccountCreationDate = get_account_creation_date(f)
  AccountAgeInDay = 0
  AccountUsername = str(get_account_data(f,"username").replace(",","").replace(" ",""))
  Nb_of_dm_send = 0
  Nb_of_dm_received = 0
  Nb_of_tweet_total = 0
  Nb_of_rt = 0
  Nb_of_comment = 0
  Nb_of_tweet = 0
  Top5RepliedUser = []
  Top5RepliedUserWithStat = []
  Top5DMedUser = []
  Top5DmUserWithStat = []
  Nb_of_account_blocked = 0
  Nb_of_tweet_liked = 0
  Nb_of_tweet_made_on_average = 0
  Nb_of_rt_made_on_average = 0
  Nb_of_comment_made_on_average = 0
  Nb_of_all_tweet_made_on_average = 0
  Nb_of_dm_send_on_average = 0
  Nb_of_dm_received_on_average = 0
  Nb_of_tweet_liked_on_average = 0
  Nb_of_word = 0
  Nb_of_char = 0
  Nb_of_unique_word = 0
  Nb_of_char_on_average = 0
  Nb_of_word_on_average = 0
  Nb_of_word_linked_to_petit_prince = 0
  Nb_of_char_linked_to_petit_prince = 0
  Nb_of_word_in_the_petit_prince = 14180
  Nb_of_char_in_the_petit_prince = 71595
  
  
  

class SeleniumData():
  options = webdriver.ChromeOptions()
  options.add_argument('--blink-settings=imagesEnabled=false')
  options.add_argument("--log-level=3")  # Suppress all logging levels
  
  # C:\Users\your_usernema\AppData\Local\Google\Chrome\User Data
  #Replace your_username with your username
  #and Profile 3 by your profile number
  
  options.add_argument(r"--user-data-dir=C:\Users\your_username\AppData\Local\Google\Chrome\User Data\Profile 3")
  options.add_argument(r'--profile-directory=Profile 3')
  #options.add_argument('headless')
  driver = webdriver.Chrome(options=options)  # You can change this to whichever browser you prefer and have installed
  username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'  
  button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
  password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
  login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'


def account_age(data):
    date_str = str(data.AccountCreationDate)
    today = datetime.now().date()
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    data.AccountAgeInDay = str(today - date).split(" ")[0].replace(" ","").strip()

def average_stat(data):
  
  age = int(data.AccountAgeInDay)
  data.Nb_of_tweet_made_on_average = round((data.Nb_of_tweet/age),2)
  data.Nb_of_rt_made_on_average = round((data.Nb_of_rt/age),2)
  data.Nb_of_comment_made_on_average = round((data.Nb_of_comment/age),2)
  data.Nb_of_all_tweet_made_on_average = round((data.Nb_of_tweet_total/age),2)
  data.Nb_of_dm_send_on_average = round((data.Nb_of_dm_send/age),2)
  data.Nb_of_dm_received_on_average = round((data.Nb_of_dm_received/age),2)
  data.Nb_of_tweet_liked_on_average = round((data.Nb_of_tweet_liked/age),2)
  
def get_username_from_id(id):
    S = SeleniumData()
    try:
        S.driver.get(f"https://twitter.com/intent/user?user_id={id}")
        time.sleep(1)
        current_url = str(S.driver.current_url)
        return (current_url.split("=")[1])
    except:
        return("error")

def convert_seconds_to_hms(seconds):
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  remaining_seconds = seconds % 60

  return hours, minutes, remaining_seconds

def twitter_account_info():
  data = AccountData()
  number_of_dm(data)
  number_of_tweet(data)
  number_of_block(data)
  number_of_like(data)
  account_age(data)
  average_stat(data)
  number_of_word(data)
  # Print values of attributes
  print("Printing all values")
  print("AccountId:", data.AccountId)
  print("AccountCreationDate:", data.AccountCreationDate)
  print("AccountUsername:", data.AccountUsername)
  print("Nb_of_dm_send:", data.Nb_of_dm_send)
  print("Nb_of_dm_received:", data.Nb_of_dm_received)
  print("Nb_of_tweet_total:", data.Nb_of_tweet_total)
  print("Nb_of_rt:", data.Nb_of_rt)
  print("Nb_of_comment:", data.Nb_of_comment)
  print("Nb_of_tweet:", data.Nb_of_tweet)
  print("Top5RepliedUser:", data.Top5RepliedUser)
  print("Top5RepliedUserWithStat:", data.Top5RepliedUserWithStat)
  print("Top5DMedUser:", data.Top5DMedUser)
  print("Top5DmUserWithStat:", data.Top5DmUserWithStat)
  print("Nb_of_account_blocked:", data.Nb_of_account_blocked)
  print("Nb_of_tweet_liked:", data.Nb_of_tweet_liked)
  print("Account Age:" , data.AccountAgeInDay)
  print("Nb_of_tweet_liked_on_average:" , data.Nb_of_tweet_liked_on_average)
  print("Nb_of_tweet_made_on_average:", data.Nb_of_tweet_made_on_average)
  print("Nb_of_rt_made_on_average:", data.Nb_of_rt_made_on_average)
  print("Nb_of_comment_made_on_average:", data.Nb_of_comment_made_on_average)
  print("Nb_of_all_tweet_made_on_average:", data.Nb_of_all_tweet_made_on_average)
  print("Nb_of_dm_send_on_average:", data.Nb_of_dm_send_on_average)
  print("Nb_of_dm_received_on_average:", data.Nb_of_dm_received_on_average)
  print("Nb_of_char:", data.Nb_of_char)
  print("Nb_of_char_on_average:", data.Nb_of_char_on_average)
  print("Nb_of_word:", data.Nb_of_word)
  print("Nb_of_unique_word:", data.Nb_of_unique_word)
  print("Nb_of_word_on_average:", data.Nb_of_word_on_average)
  print("Nb of word in the petit prince:" , data.Nb_of_word_in_the_petit_prince)
  print("Nb of char in the petit prince:" , data.Nb_of_char_in_the_petit_prince)
  print("number of time you wrote the petit prince by number of word: " , data.Nb_of_word_linked_to_petit_prince)
  print("number of time you wrote the petit prince by number of char: " , data.Nb_of_char_linked_to_petit_prince)
  print("yeah")

def number_of_dm(data):
  f = print_file_info(r'twitter_data\data\direct-messages.js').replace('"',"")
  data.Nb_of_dm_send = f.count(f"senderId : {str(data.AccountId)}")
  data.Nb_of_dm_received = f.count(f"recipientId : {str(data.AccountId)}")
  fr = f.split("recipientId")
  fs = f.split("senderId")
  
  list_of_user = []
  list_of_user_ = []
  count_user = []
  alpha = "abcdefghijlmnopqrstuvwxyz"
  for user, user2 in zip(fs, fr):
    userDm = str(user[0:100].split("\n")[0].replace(",","").replace(":","").replace(" ","")).replace(data.AccountId,"").replace("-","").replace(" ","")
    userDm2 = str(user2[0:100].split("\n")[0].replace(",","").replace(":","").replace(" ","")).replace(data.AccountId,"").replace("-","").replace(" ","")
    if "w" not in userDm and len(userDm) > 3 and data.AccountId not in userDm:
      list_of_user.append(userDm.replace("\n",""))
    if "w" not in userDm2 and len(userDm2) > 3 and data.AccountId not in userDm2:
      list_of_user.append(userDm.replace("\n",""))
        
  f1,f2,f3 = 0,0,0

  for user in list_of_user:
    if user not in list_of_user_ and len(user) > 5:
      list_of_user_.append(user)
      count_user.append(list_of_user.count(user))
      #print(user)
  zipped_lists = zip(count_user, list_of_user_)
  sorted_zipped_lists = sorted(zipped_lists)
  sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)
  
  if len(sorted_list1) >= 6:
    for i in range(1,6):
      od = get_username_from_id(str(sorted_list2[-i]))
      data.Top5DMedUser.append(od)
      #data.Top5DmUserWithStat.append(str((od , sorted_list1[-i] , len(list_of_user) , round(float((sorted_list1[-i]/len(list_of_user)) * 100),2), " %")))
      data.Top5DmUserWithStat.append(str((od , sorted_list1[-i] , len(list_of_user) , round(float((sorted_list1[-i]/len(list_of_user)) * 100),2), " %")))
  
  else:
    for i in range(1,len(sorted_list1)):
      data.Top5DMedUser.append(sorted_list2[-i])
      data.Top5DmUserWithStat.append(str((od , sorted_list1[-i] , len(list_of_user) , round(float((sorted_list1[-i]/len(list_of_user)) * 100),2), " %")))


def number_of_word(data):
  f = print_file_info(r'twitter_data\data\tweets.js').replace('"',"").split("full_text")
  x = 0
  age = int(data.AccountAgeInDay)
  list_of_word_ = []
  list_of_word = []
  list_of_word_bigger_than_5 = []
  count_word = []
  unique_word = []
  for Wrd in f:
    if "RT" not in Wrd[0:5]:
      Tweetword = Wrd[0:400].split("\n")[0].replace(",","").replace(":","")
      words = Tweetword.split(" ")
      for word in words:
        if "@" not in word and "https//t.co/" not in word and "window.YTD.tweets.part0" not in word and len(word) > 0:
          list_of_word.append(word)
          data.Nb_of_char += len(word)
          if word not in unique_word:
            unique_word.append(word)
  
  
  Top5MustUsedWord = []
  Top5MustUsedWordLongerThan5 = []
  Nb_of_char = 0
  Nb_of_char_on_average = 0
 
  # for word in list_of_word:
  #   if word not in list_of_word_:
  #     list_of_word_.append(word)
  #     count_word.append(list_of_word.count(word))
  

  data.Nb_of_word = len(list_of_word)
  data.Nb_of_word_on_average = int(round(data.Nb_of_word/(data.Nb_of_tweet + data.Nb_of_comment),0))
  data.Nb_of_char_on_average = int(round(data.Nb_of_char/(data.Nb_of_tweet + data.Nb_of_comment),0))
  
  data.Nb_of_unique_word = len(unique_word)
  
  
  data.Nb_of_word_linked_to_petit_prince = round((data.Nb_of_word/data.Nb_of_word_in_the_petit_prince),1)
  data.Nb_of_char_linked_to_petit_prince = round((data.Nb_of_char/data.Nb_of_char_in_the_petit_prince),1)
  
  # zipped_lists = zip(count_word, list_of_word_)
  # sorted_zipped_lists = sorted(zipped_lists)
  # sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)
  
  # # j = 0

  # # if len(sorted_list1) >= 6:
  # #   for i in range(1,len(sorted_list1)):
  # #     if len(sorted_list2[-i]) > 12:
  # #       data.Top5MustUsedWord.append((sorted_list2[-i],sorted_list1[-i]))
  # #       j+=1
  # #     if j >= 5:
  # #       break
  # # else:
  # #   for i in range(1,len(sorted_list1)):
  # #     data.Top5MustUsedWord.append(sorted_list2[-i])

  
def number_of_tweet(data):
  f = print_file_info(r'twitter_data\data\tweets.js').replace('"',"")
  
  data.Nb_of_rt = f.count("full_text : RT")
  data.Nb_of_comment = f.count("full_text : @")
  data.Nb_of_tweet_total = f.count("full_text : ")
  data.Nb_of_tweet = data.Nb_of_tweet_total - (data.Nb_of_rt + data.Nb_of_comment)
  list_of_user_replied = f.split("in_reply_to_screen_name")
  list_of_user = []
  list_of_user_ = []
  count_user = []
  for userT in list_of_user_replied:    
    userTweet = userT[0:30].split("\n")[0].replace(",","").replace(":","").replace(" ","")
    if len(userTweet) < 16 and userTweet.lower() != data.AccountUsername.lower():
      list_of_user.append(userTweet)
    
  f1,f2,f3 = 0,0,0

  for user in list_of_user:
    if user not in list_of_user_:
      list_of_user_.append(user)
      count_user.append(list_of_user.count(user))
  
  zipped_lists = zip(count_user, list_of_user_)
  sorted_zipped_lists = sorted(zipped_lists)
  sorted_list1, sorted_list2 = zip(*sorted_zipped_lists)
  
  if len(sorted_list1) >= 6:
    for i in range(1,6):
      data.Top5RepliedUser.append(sorted_list2[-i])
      data.Top5RepliedUserWithStat.append(str((sorted_list2[-i] , sorted_list1[-i] , len(list_of_user) , round(float((sorted_list1[-i]/len(list_of_user)) * 100),2), " %")))
      
  else:
    for i in range(1,len(sorted_list1)):
      data.Top5RepliedUser.append(sorted_list2[-i])
      data.Top5RepliedUserWithStat.append(str((sorted_list2[-i] , sorted_list1[-i] , len(list_of_user) , round(float((sorted_list1[-i]/len(list_of_user)) * 100),2), " %")))

def number_of_block(data):
  data.Nb_of_account_blocked = str(print_file_info(r'twitter_data\data\block.js').replace('"',"")).count("blocking")

def number_of_like(data):
  data.Nb_of_tweet_liked = str(print_file_info(r'twitter_data\data\like.js').replace('"',"")).count("expandedUrl")


def twitter_account_data():
  print("Start")
  start_time = time.time()
  twitter_account_info()
  delete_data()
  end_time = time.time()
  elapsed_time = end_time - start_time
  hours, minutes, remaining_seconds = convert_seconds_to_hms(int(elapsed_time))
  print(f"It tooks {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
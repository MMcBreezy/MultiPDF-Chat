css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn-useast1.kapwing.com/collections/black-girl-wat-meme-template-3sqo0_thumbnail.jpg?Expires=1696737607&GoogleAccessId=dev-sa-videoprocessing%40kapwing-dev.iam.gserviceaccount.com&Signature=oqotqd%2Fjou8nOESmEzP1IzCrookQxMdsIHZ9Q50Mz2vOx2d5UyV6HAShfMeS2q8TqwsCRiy3lo72FAE3w4pQc5IafVps%2FWXlo%2BeXtRGW6PQYOvKmDiDRYnsvBMYnW5xkWQGrzh7yqFYOy%2FUnhzj2M1jktCbs2NPYTJJLyQ%2BvxO0RNjm1XTfGhAUUM%2FdK29g8JM4l%2B26eJcC9iAx%2FoywQ%2FlvGFknfuwezPLp0Dh6yJbBXdusuWt4wniv9FTiDAlkCteb2fOvcX8lO%2BAd0qAO0McVanFMt4jS0sM2FbN7Zo32wdxYRUBwtFEEYX9cbLDmf%2BsGRVwePFr8MofJ4ap%2FizA%3D%3D">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

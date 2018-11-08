# coding=utf-8
################################################
# Nazomi Plurk bot Project
# Produced by Dephilia
################################################
import logger,logging
logger = logging.getLogger(__name__)
from plurk_oauth import PlurkAPI
import util
import os


class PyPlurk_caller:
    def __init__(self,
                CONSUMER_SECRET,
                CONSUMER_KEY,
                ACCESS_TOKEN,
                ACCESS_TOKEN_SECRET):
        self.plurk=PlurkAPI(key=CONSUMER_KEY, secret=CONSUMER_SECRET,
                         access_token=ACCESS_TOKEN, access_secret=ACCESS_TOKEN_SECRET)
    # --Users
    def me(self):
        pass
    def update(self):
        pass
    def updateAvatar():
        pass
    def getKarmaStats():
        pass
    # --Profile
    def getOwnProfile():
        pass
    def getPublicProfile():
        pass
    # --Real time notifications
    def getUserChannel():
        pass
    def getPlurks():
        pass
    def getUnreadCount():
        pass
    # --Timeline
    def getPlurk():
        pass
    def getUnreadPlurks():
        pass
    def getPublicPlurks():
        pass
    def plurkAdd():
        pass
    def plurkDelete():
        pass
    def plurkEdit():
        pass
    def toggleComments():
        pass
    def mutePlurks():
        pass
    def unmutePlurks():
        pass
    def favoritePlurks():
        pass
    def unfavoritePlurks():
        pass
    def replurk():
        pass
    def unreplurk():
        pass
    def markAsRead():
        pass
    def uploadPicture():
        pass
    def reportAbuse():
        pass
    # --Responses
    def get():
        pass
    def responseAdd():
        pass
    def responseDelete():
        pass
    # --Friends and fans
    def getFriendsByOffset():
        pass
    def getFansByOffset():
        pass
    def getFollowingByOffset():
        pass
    def becomeFriend():
        pass
    def removeAsFriend():
        pass
    def becomeFan():
        pass
    def setFollowing():
        pass
    def getCompletion():
        pass
    # --Alerts
    def getActive():
        pass
    def getHistory():
        pass
    def addAsFan():
        pass
    def addAllAsFan():
        pass
    def addAllAsFriends():
        pass
    def addAsFriend():
        pass
    def denyFriendship():
        pass
    def removeNotification():
        pass
    # --Search
    def PlurkSearch():
        pass
    def UserSearch():
        pass
    # --Emoticons
    def get():
        pass
    # --Blocks
    def get():
        pass
    def block():
        pass
    def unblock():
        pass
    # --Cliques
    def getCliques():
        pass
    def getClique():
        pass
    def createClique():
        pass
    def renameClique():
        pass
    def add():
        pass
    def remove():
        pass
    # --OAuth Utilities
    def checkToken():
        pass
    def expireToken():
        pass
    def checkTime():
        pass
    def echo():
        pass

# Check plurk key
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
plurk = PlurkAPI(key=CONSUMER_KEY, secret=CONSUMER_SECRET,
                 access_token=ACCESS_TOKEN, access_secret=ACCESS_TOKEN_SECRET)

# --Users
def getMe(*arg,**kwarg):
    return plurk.callAPI('/APP/Users/me')

def getKarma(*arg,**kwarg):
    return plurk.callAPI('/APP/Users/getKarmaStats')

# --Polling
def getPlurks(offset,limit=None,favorers_detail=None,limited_detail=None,
                replurkers_detail=None,*arg,**kwarg):
    options={'offset':util.dt2pt(offset)}
    if limit:options['limit']=limit
    if favorers_detail:options['favorers_detail']=favorers_detail
    if limited_detail:options['limited_detail']=limited_detail
    if replurkers_detail:options['replurkers_detail']=replurkers_detail
    return plurk.callAPI('/APP/Polling/getPlurks',options=options)

def getUnreadCount(*arg,**kwarg):
    return plurk.callAPI('/APP/Polling/getUnreadCount')

# --Timeline
def plurkAdd(content,qualifier=':',limited_to=None,no_comments=None,lang=None,
                *arg,**kwarg):
    options={
        'content':content,
        'qualifier':qualifier
    }
    if limited_to:options['limited_to']=limited_to
    if no_comments:options['no_comments']=no_comments
    if lang:options['lang']=lang
    return plurk.callAPI('/APP/Timeline/plurkAdd',options=options)

def getUnreadPlurks(offset=None,limit=None,filter=None,favorers_detail=None,limited_detail=None,
                replurkers_detail=None,*arg,**kwarg):
    options={}
    if offset:options['offset']=util.dt2pt(offset)
    if limit:options['limit']=limit
    if filter:options['filter']=filter
    if favorers_detail:options['favorers_detail']=favorers_detail
    if limited_detail:options['limited_detail']=limited_detail
    if replurkers_detail:options['replurkers_detail']=replurkers_detail
    return plurk.callAPI('/APP/Timeline/getUnreadPlurks',options=options)

def markAsRead(ids,note_position=None,*arg,**kwarg):
    if not isinstance(ids,list):raise TypeError("markAsRead only accept id list.")
    options={'ids':ids}
    if note_position:options['note_position']=note_position
    return plurk.callAPI('/APP/Timeline/markAsRead',options=options)

def markAsRead_one(id,note_position=None,*arg,**kwarg):
    """Accept one id version"""
    options={'ids':[str(id)]}
    if note_position:options['note_position']=note_position
    return plurk.callAPI('/APP/Timeline/markAsRead',options=options)

# --Responses
def getResponses(plurk_id,from_response=None,minimal_data=None,count=None,*arg,**kwarg):
    options={
        'plurk_id':plurk_id
    }
    if from_response:options['from_response']=from_response
    if minimal_data:options['minimal_data']=minimal_data
    if count:options['count']=count
    return plurk.callAPI('/APP/Responses/get',options=options)

def responseAdd(plurk_id,content,qualifier,*arg,**kwarg):
    """
    Note: Repeating send something will cause failure
    """
    options={
        'plurk_id':plurk_id,
        'content':content,
        'qualifier':qualifier
    }
    return plurk.callAPI('/APP/Responses/responseAdd',options=options)

# --Friends and fans
def becomeFriend(friend_id,*arg,**kwarg):
    options={
        'friend_id':friend_id
    }
    return plurk.callAPI('/APP/FriendsFans/becomeFriend',options=options)

# --Alerts
def addAllAsFriends(*arg,**kwarg):
    return plurk.callAPI('/APP/Alerts/addAllAsFriends')

# --Other
def checkToken(*arg,**kwarg):
    return plurk.callAPI('/APP/checkToken')

def checkTime(*arg,**kwarg):
    return plurk.callAPI('/APP/checkTime')

def echo(data,*arg,**kwarg):
    return plurk.callAPI('/APP/echo',options={'data':data})

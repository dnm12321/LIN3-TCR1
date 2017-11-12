# -*- coding: utf-8 -*-
# Codding Sunysz edit
# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = LINETCR.LINE()
cl.login(qr=True)

ki = kk = kc = kg = cl

cl

# adm = cl
 
# adm = LINETCR.LINE()
# adm.login(token= "ElAOrOHacrPxYZOzEh3a.YBky8hyF1LROK01iGqOKUG.XwDJRQ3sJQP8KZDWxKem44bNbi4zW4JLbbhoJ5uIhLc=")
# adm.loginResult()
 
# client_id = '511abc94ee71658'
# client_secret = '948a2fcdbf566c04bcce5f990e349ce795ee7460'
# access_token = '30181acf5583ad6a215b4f69e6e5c7bc5c66efdb'
# refresh_token = '4a6b3f983b96714c2e9b581edf86f86e0d681938'
 
# client = ImgurClient(client_id, client_secret, access_token, refresh_token)
 
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
 
album = None
image_path = 'tmp/tmp.jpg'
 
# cl = kk = ki = kc kg
 
helpMessage ="""Sunysz Bot(s) v0.1
 
Use Command With 「Sunysz」 to use the Bot(s)
 
[Gid] - Show Group ID
[Mid all] - Show all the Bot(s) MID
[Bot 1/2/3/4/5] - Shows the specific Bot MID
[Bot all] - Show all the Bot(s) Contact
[Bot 1/2/3/4/5] - Shows the specific Bot Contact
[Yid] - Show your ID
[Contact 「mid」] - Give Contact by MID
[Join on/off] - Auto join group
[Leave on/off] - Allows the bot to leave the group
 
[*] Command in the groups [*]
[Ginfo] - Group Info
[Banlist] - Check Banlist
[Cancel] - Cancel all pending(s) invitation
[Stalk 「ID」] - Upload lastest instagram picture from ID
 
[*] |Admin and Staff Commands| [*]
[Absen] - Check if bot is Online
[Glink on/off] - Turn invitation link for group on/off
[Cancel on/off] - Turn auto cancel invite on/off
[Url on/off] - Turn auto block url on/off
[Gn 「group name」] - Change Group Name
[Sp/Speed all/1/2/3/4/5] - Check bot response speed
[Random:「A」] - Randomize group name A times
[Bc 「text」] - Let the bot send a text
[Kick 「with tag」] - bot kick target from group
[Gift] - Bot a Gift Theme/Sticker
 
 
[*] |Admin only Commands| [*]
[Cleanse] - Clear all members in the group
[Bye all] - Bot Leave
[Ban 「@」] - Ban By Tag
[Unban 「@」] - Unban By Tag
[Ban] - By Sharing Contact
[Unban] - By Sharing Contact
[Kill ban] - Kick all banned contact(s)
[Staff add/remove @] - Add or Remove Staff By Tag
[Add 「@」] - Add friend line By Tag
[Join all ] - Bot Join the groups
[Staff list] - Check Staff
"""
KAC=[cl,ki,kk,kc,kg]
mid = cl.getProfile().mid
Amid = kk.getProfile().mid
Bmid = ki.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kg.getProfile().mid
 
Bots = [mid,Amid,Bmid,Cmid,Dmid]
owner = ["u7a5257b4cd2286f1a225fe44e797dd0f"]
admin = ["u7a5257b4cd2286f1a225fe44e797dd0f","ub1c605507469907e4cabd3ce65eb532f"]
staff = ["u7a5257b4cd2286f1a225fe44e797dd0f","ub1c605507469907e4cabd3ce65eb532f"]
adminMID = "u7a5257b4cd2286f1a225fe44e797dd0f"
 
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"",
    "cName2":"",
    "cName3":"",
    "cName4":"",
    "cName5":"",
    "blacklist":{},
    "backup":True,
    "wblacklist":False,
    "dblacklist":False,
    "protectionAdmin":True,
    "protectionBots":True,
    "protectionOn":True
    }
 
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
 
cancelinvite = {
    'autoCancel':True,
    'autoCancelUrl':True
}
 
bot1_name = {
    "1" : "BOT1",
    "2" : "Bot Creator",
    "3" : "􏿿􀜁􀅔􏿿􀨁􀄆 Assist",
    "4" : "TE̴͗͒̈Ä̵́̋̄M̷̛̓͠",
    "5" : "~~==Admin==~~"
}
bot2_name = {
    "1" : "BOT2",
    "2" : "Bot Creator",
    "3" : "􏿿􀜁􀅔􏿿􀨁􀄆 Assist",
    "4" : "TE̴͗͒̈Ä̵́̋̄M̷̛̓͠",
    "5" : "~~==Admin==~~"
}
 
bot3_name = {
    "1" : "BOT3",
    "2" : "Bot Creator",
    "3" : "􏿿􀜁􀅔􏿿􀨁􀄆 Assist",
    "4" : "TE̴͗͒̈Ä̵́̋̄M̷̛̓͠",
    "5" : "~~==Admin==~~"
}
bot4_name = {
    "1" : "BOT4",
    "2" : "Bot Creator",
    "3" : "􏿿􀜁􀅔􏿿􀨁􀄆 Assist",
    "4" : "TE̴͗͒̈Ä̵́̋̄M̷̛̓͠",
    "5" : "~~==Admin==~~"
}
bot5_name = {
    "1" : "BOT5",
    "2" : "Bot Creator",
    "3" : "􏿿􀜁􀅔􏿿􀨁􀄆 Assist",
    "4" : "TE̴͗͒̈Ä̵́̋̄M̷̛̓͠",
    "5" : "~~==Admin==~~"
}
setTime = {}
setTime = wait2['setTime']
 
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
 
    # Here's the metadata for the upload. All of these are optional, including
    # this config dict itself.
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }
 
    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()
 
    return image
 
 
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
 
def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            try:    
                cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me/ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me/ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me/ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me/ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                kg.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me/ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                print "Like"
            except:
                pass
        else:
             print "Already Liked"
     time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
 
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
   
def bot(op):
    try:
        if op.type == 0:
            return
 
        if op.type == 11:
            if cancelinvite["autoCancelUrl"] == True:
                if cl.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass
       
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"
 
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    kk.acceptGroupInvitation(op.param1)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"
 
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"
 
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    kc.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    kg.acceptGroupInvitation(op.param1)
            else:
                if cancelinvite["autoCancel"] == True:
                    try:
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "invite canceled"
                    except:
                        try:
                            print "Retry canceling invitation"
                            X = random.choice(KAC).getGroup(op.param1)
                            gInviMids = [contact.mid for contact in X.invitee]
                            random.choice(KAC).cancelGroupInvitation(op.param1, gInviMids)
                            print gInviMids + "invite canceled"
                        except:
                            print "Bot can't cancel the invitation"
                            pass
                       
        if op.type == 13:
            if op.param2 not in admin:
                if op.param2 not in admin:
                    if wait["backup"] == True:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.inviteIntoGroup(op.param1[op.param3])
                        ki.inviteIntoGroup(op.param1[op.param3])
                        kk.inviteIntoGroup(op.param1[op.param3])
                        kc.inviteIntoGroup(op.param1[op.param3])
                        kg.inviteIntoGroup(op.param1[op.param3])
           
                       
        if op.type == 15:
            random.choice(KAC).sendText(op.param1, "Good Bye :)\nSee You Again")
            print op.param3 + "has left the group"
 
        if op.type == 19:
            if op.param3 in wait["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1, op.param3)
                except:
                    random.choice(KAC).kickoutFromGroup(op.param1, op.param3)
                   
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 not in admin:
                    if wait["protectionOn"] == True:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.inviteIntoGroup(op.param1[op.param3])
                        ki.inviteIntoGroup(op.param1[op.param3])
                        kk.inviteIntoGroup(op.param1[op.param3])
                        kc.inviteIntoGroup(op.param1[op.param3])
                        kg.inviteIntoGroup(op.param1[op.param3])
                           
        if op.type == 19:
            if op.param2 in Bots:
                try:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    kk.kickoutFromGroup(op.param1,[op.param2])
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    kc.kickoutFromGroup(op.param1,[op.param2])
                    kg.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    cl.inviteIntoGroup(op.param1,Bots)
                    kk.inviteIntoGroup(op.param1,Bots)
                    ki.inviteIntoGroup(op.param1,Bots)
                    kc.inviteIntoGroup(op.param1,Bots)
                    kg.inviteIntoGroup(op.param1,Bots)
                except:
                    pass
                   
        if op.type == 19:
            if wait["protectionAdmin"] == True:
                try:
                    if op.param2 in admin:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            cl.inviteIntoGroup(op.param1,admin)
                            kg.kickoutFromGroup(op.param1,admin)
                        except:
                            pass
                except Exception as e:
                    print e
       
        if op.type == 19:
            print "someone was kicked"
            if admin in op.param3:
                print "Admin has been kicked"
                if op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    kk.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                print "Admin Joined"      
 
            if mid in op.param3:
                print "BOT1 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kk.inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    print "BOT1 Joined"
 
            if Amid in op.param3:
                print "BOT2 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        ki.inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    print "BOT2 Joined"
 
            if Bmid in op.param3:
                print "BOT3 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kc.inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    print "BOT3 Joined"
 
            if Cmid in op.param3:
                print "BOT4 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kg.inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    print "BOT4 Joined"
 
            if Dmid in op.param3:
                print "BOT5 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        kg.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kg.acceptGroupInvitation(op.param1)
                    print "BOT5 Joined"
 
            else:
                cl.kickoutFromGroup(op.param1,[op.param2])
                kk.kickoutFromGroup(op.param1,[op.param2])
                ki.kickoutFromGroup(op.param1,[op.param2])
                kc.kickoutFromGroup(op.param1,[op.param2])
                kg.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
                print "autokick executed"
 
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"
 
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in the Blacklist")
                        wait["wblacklist"] = False
                        print "MID Already in the Blacklist"
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to the Blacklist")
                        print [msg.contentMetadata["mid"]] + " Added to the Blacklist"
 
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted from the Blacklist")
                        wait["dblacklist"] = False
                        print [msg.contentMetadata["mid"]] + " Removed from the Blacklist"
 
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Contact not in Blacklist")
                        print "MID not in blacklist"
               elif wait["contact"] == True:
                    if msg.from_ in admin:
                        msg.contentType = 0
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[Display Name]:\n" + msg.contentMetadata["displayName"] + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            if op.type == 5:
                if wait["autoAdd"] == True:
                    cl.findAndAddContactsByMid(op.param1)
                    if (wait["message"] in [""," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1,str(wait["message"]))
#-----------------------[Help Section]------------------------                
            elif msg.text in ["Helpme!","Helpp","Help Me"]:
                if wait["lang"] == "JP":
                    random.choice(KAC).sendText(msg.to,helpMessage)
                    print "[Command]/help executed"
                else:
                    cl.sendText(msg.to, "you not staff or admin")
#-----------------------[Group Name Section]------------------------
            elif "Sunysz Gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Sunysz Gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
            elif "Sunysz gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Sunysz gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
#-----------------------[Kick Section]------------------------
            elif "Sunysz Kick @" in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Sunysz Kick @","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    kk.kickoutFromGroup(msg.to,[midd])
                    ki.kickoutFromGroup(msg.to,[midd])
                    kc.kickoutFromGroup(msg.to,[midd])
                    kg.kickoutFromGroup(msg.to,[midd])
                    cl.sendText(msg.to,"Good bye.")
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif "Sunysz kick @" in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Sunysz kick @","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    kk.kickoutFromGroup(msg.to,[midd])
                    ki.kickoutFromGroup(msg.to,[midd])
                    kc.kickoutFromGroup(msg.to,[midd])
                    kg.kickoutFromGroup(msg.to,[midd])
                    cl.sendText(msg.to,"Good bye.")
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunysz Kill ban","Sunysz kill ban"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        if matched_list != []:
                            cl.sendText(msg.to,"Blacklisted contact noticed...")
                            cl.sendText(msg.to,"Begin Kicking contact")
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"It looks empty here.")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        print "[Command]Kill ban executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Send Profile Section]------------------------                    
            elif msg.text in ["Sunysz Bot all","Sunysz bot all"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot all executed"
            elif msg.text in ["Sunysz Bot 1","Sunysz bot 1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                print "[Command]Bot 1 executed"
            elif msg.text in ["Sunysz Bot 2","Sunysz bot 2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                print "[Command]Bot 2 executed"
            elif msg.text in ["Sunysz Bot 3","Sunysz bot 3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                print "[Command]Bot 3 executed"
            elif msg.text in ["Sunysz Bot 4","Sunysz bot 4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                print "[Command]Bot 4 executed"
            elif msg.text in ["Sunysz Bot 5","Sunysz bot 5"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot 5 executed"
#-----------------------[Cancel invitation Section]------------------------
            elif msg.text in ["Sunysz cancel","Sunysz Cancel"]:
                if msg.toType == 2:                    
                    X = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Canceling all pending(s) invitation")
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "[Command]Cancel executed"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"This group doesn't have any pending invitation")
                            print "[Command]Group don't have pending invitation"
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "Cancel executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group link Section]------------------------                        
            elif msg.text in ["Sunysz Glink off","Sunysz Link off","Sunysz glink off","Sunysz link off"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned off")
                            print "[Command]Glink off executed"
                        else:
                            cl.sendText(msg.to,"Already turned off")
                            print "[Command]Glink off executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
 
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink off executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sunysz Glink on","Sunysz Link on","Sunysz glink on","Sunysz link on"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned on")
                            print "[Command]Glink on executed"
                        else:
                            cl.sendText(msg.to,"Already turned on")
                            print "[Command]Glink on executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink on executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group info Section]------------------------
            elif msg.text in ["Sunysz Gc","Sunysz gc","Sunysz gcreator"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group Creator]\n" + gCreator)
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': gCreator}
                        cl.sendMessage(msg)
            elif msg.text in ["Sunysz Ginfo","Sunysz ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                        print "[Command]Ginfo executed"
                    else:
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        print "[Command]Ginfo executed"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Ginfo executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Bot/User/Group ID Section]------------------------
            if msg.text == "Me":
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
            elif msg.text == "Mid":
                kk.sendText(msg.to,msg.from_)
            elif msg.text in ["Sunysz Gid","Sunysz gid"]:
                cl.sendText(msg.to,msg.to)
                print "[Command]Gid executed"
            elif msg.text in ["Sunysz Mid all","Sunysz mid all"]:
                cl.sendText(msg.to,"[Sunysz]Bots ID\n\n[Sunysz]-BOT1\n" + mid + "\n\n[Sunysz]-BOT2\n" + Amid + "\n\n[Sunysz]-BOT3\n" + Bmid + "\n\n[Sunysz]-BOT4\n" + Cmid + "\n\n[Sunysz]-BOT5\n" + Dmid)
                print "[Command]Mid executed"
            elif msg.text in ["Sunysz Mid 1","Sunysz mid 1"]:
                cl.sendText(msg.to,mid)
                print "[Command]Mid 1 executed"
            elif msg.text in ["Sunysz Mid 2","Sunysz mid 2"]:
                kk.sendText(msg.to,Amid)
                print "[Command]Mid 2 executed"
            elif msg.text in ["Sunysz Mid 3","Sunysz mid 3"]:
                ki.sendText(msg.to,Bmid)
                print "[Command]Mid 3 executed"
            elif msg.text in ["Sunysz Mid 4","Sunysz mid 4"]:
                kc.sendText(msg.to,Cmid)
                print "[Command]Mid 4 executed"
            elif msg.text in ["Sunysz Mid 5","Sunysz mid 5"]:
                kc.sendText(msg.to,Dmid)
                print "[Command]Mid 5 executed"
            elif msg.text in ["Sunysz Yid","Sunysz yid"]:
                cl.sendText(msg.to,msg.from_)
                print "[Command]Yid executed"
#-----------------------[Send Contact Section]------------------------
            elif "Sunysz Contact " in msg.text:
                mmid = msg.text.replace("Sunysz Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
            elif "Sunysz contact " in msg.text:
                mmid = msg.text.replace("Sunysz contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
#-----------------------[Auto Join Section]------------------------
            elif msg.text in ["Sunysz Join on","Sunysz join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already on")
                        kk.sendText(msg.to,"Auto join already on")
                        ki.sendText(msg.to,"Auto join already on")
                        kc.sendText(msg.to,"Auto join already on")
                        kg.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join already on")
                        kk.sendText(msg.to,"Auto join already on")
                        ki.sendText(msg.to,"Auto join already on")
                        kc.sendText(msg.to,"Auto join already on")
                        kg.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned on")
                        kk.sendText(msg.to,"Auto join turned on")
                        ki.sendText(msg.to,"Auto join turned on")
                        kc.sendText(msg.to,"Auto join turned on")
                        kg.sendText(msg.to,"Auto join turned on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned on")
                        kk.sendText(msg.to,"Auto join turned on")
                        ki.sendText(msg.to,"Auto join turned on")
                        kc.sendText(msg.to,"Auto join turned on")
                        kg.sendText(msg.to,"Auto join turned on")
                        print "Join on executed"
            elif msg.text in ["Sunysz Join off","Sunysz join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already off")
                        kk.sendText(msg.to,"Auto join already off")
                        ki.sendText(msg.to,"Auto join already off")
                        kc.sendText(msg.to,"Auto join already off")
                        kg.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned off")
                        kk.sendText(msg.to,"Auto join turned off")
                        ki.sendText(msg.to,"Auto join turned off")
                        kc.sendText(msg.to,"Auto join turned off")
                        kg.sendText(msg.to,"Auto join turnedy off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
            elif msg.text in ["Sunysz Backup on","Sunysz backup on"]:
                if msg.from_ in admin:
                    wait["backup"] == True
                    cl.sendText(msg.to,"Backup mode already on")
                    kk.sendText(msg.to,"Backup mode already on")
                    ki.sendText(msg.to,"Backup mode already on")
                    kc.sendText(msg.to,"Backup mode already on")
                    kg.sendText(msg.to,"Backup mode already on")
                    print "[Command]Backup on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Sunysz Backup off","Sunysz backup off"]:
                if msg.from_ in admin:
                    wait["backup"] == False
                    cl.sendText(msg.to,"Backup mode already off")
                    kk.sendText(msg.to,"Backup mode already off")
                    ki.sendText(msg.to,"Backup mode already off")
                    kc.sendText(msg.to,"Backup mode already off")
                    kg.sendText(msg.to,"Backup mode already off")
                    print "[Command]Backup off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Protect on","Prt on"]:
                if msg.from_ in admin:
                    wait["protectionOn"] == True
                    cl.sendText(msg.to,"Protect members is now on")
                    print "[Command]Protect on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunprotection off","Sunysz Protection off"]:
                if msg.from_ in admin:
                    wait["Protect off","Prt off"] == False
                    cl.sendText(msg.to,"Protect members is now off")
                    print "[Command]Protect off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Prad on","Protect ad on"]:
                if msg.from_ in admin:
                    wait["protectionAdmin"] == True
                    cl.sendText(msg.to,"Protect admin is now on")
                    print "[Command]Protect admin on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Prad on","Protect ad on"]:
                if msg.from_ in admin:
                    wait["protectionAdmin"] == False
                    cl.sendText(msg.to,"Protect Admin is now off")
                    print "[Command]Protect admin off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#-----------------------[Group Url Section]------------------------
            elif msg.text in ["Gurl","gurl"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                        print "[Command]Gurl executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                        print "[Command]Gurl executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[All bots join group Section]------------------------
            elif msg.text in ["Join all","join all"]:
                if msg.from_ in admin:
                    try:
                        ginfo = cl.getGroup(msg.to)
                        ginfo.preventJoinByTicket = False
                        cl.updateGroup(ginfo)
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ginfo = random.choice(KAC).getGroup(msg.to)
                        ginfo.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(ginfo)
                    except:
                        print "Somethings wrong with the url"
                    print "[Command]Join all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#-----------------------[Bot(s) Leave Section]------------------------
            elif msg.text in ["Bye all","Bye my babies"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            ki.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye all executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunysz Bye bot 1","Sunysz bye bot 1"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 1 executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunysz Bye bot 2","Sunysz bye bot 2"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kk.getGroup(msg.to)
                        try:
                            kk.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 2 executed"
                    else:
                        kk.sendText(msg.to,"Command denied.")
                        kk.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunysz Bye bot 3","Sunysz bye bot 3"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = ki.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 3 executed"
                    else:
                        ki.sendText(msg.to,"Command denied.")
                        ki.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunysz Bye bot 4","Sunysz bye bot 4"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 4 executed"
                    else:
                        kc.sendText(msg.to,"Command denied.")
                        kc.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Sunysz Bye bot 5","Sunysz bye bot 5"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 5 executed"
                    else:
                        kg.sendText(msg.to,"Command denied.")
                        kg.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Cleanse Section (USE AT YOUR OWN RISK!)]------------------------
            elif msg.text in ["Cleanse!!!","cleanse!!!"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Sunysz cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        kk.sendText(msg.to,"Waktunya bersih-bersih")
                        kc.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        # --------------[Bot and Admin MID]----------------
                            targets.remove(admin)
                            targets.remove(mid)
                            targets.remove(Amid)
                            targets.remove(Bmid)
                            targets.remove(Cmid)
                            targets.remove(Dmid)
                        # --------------[Bot and Admin MID]----------------
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    targets.remove(admin)
                                    targets.remove(mid)
                                    targets.remove(Amid)
                                    targets.remove(Bmid)
                                    targets.remove(Cmid)
                                    targets.remove(Dmid)
                                    klist=[ki,kk,kc,cl,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                        print "[Command]Cleanse executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"Not found")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes Kick")
                                    kk.sendText(msg.to,"Fuck You")
#-----------------------[Ban/Unban Section]------------------------
            elif "Ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Ban","ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                    print "[Command]Ban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Unban","unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                    print "[Command]Unban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Banlist","banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, "Blacklisted user(s):\n"+mc)
                    print "[Command]Banlist executed"
            elif msg.text in ["Cek ban","cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
#-----------------------[Bot Speak Section]------------------------
            elif "Bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Bc ","")
                    cl.sendText(msg.to,(bctxt))
                    kk.sendText(msg.to,(bctxt))
                    ki.sendText(msg.to,(bctxt))
                    kc.sendText(msg.to,(bctxt))
                    kg.sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif "bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("bc ","")
                    cl.sendText(msg.to,(bctxt))
                    kk.sendText(msg.to,(bctxt))
                    ki.sendText(msg.to,(bctxt))
                    kc.sendText(msg.to,(bctxt))
                    kg.sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
	
            elif msg.text in ["Ngantuk"]:
                cl.sendText(msg.to,"Tidur bebs")
                kk.sendText(msg.to,"Tidur lah,")
                ki.sendText(msg.to,"ih.. Dasar Jones ô€œô€…”Har Harô¿¿")
            elif msg.text in ["Sayang"]:
                cl.sendText(msg.to,"Sayang ... sayang palalu peang,")
                kk.sendText(msg.to,"Situ kan jomlo")
                ki.sendText(msg.to,"dasar jones ô€œô€…”Har Harô¿¿")
            elif msg.text in ["Bobo ah","Bobo dulu ah"]:
                cl.sendText(msg.to,"Have a nice dream :)")
                ke.sendText(msg.to,"Byee~")
                ki.sendText(msg.to,"ô€œô€…”Har Harô¿¿")
            elif msg.text in ["Cinta"]:
                cl.sendText(msg.to,"Cinta i ususmu minum yak*** tiap hari~~")
                kk.sendText(msg.to,"ô€œô€…”Har Harô¿¿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang")
                kk.sendText(msg.to,"Jangan nakal ya!")
            elif msg.text in ["Bacot","bacod","cod","cot"]:
                ke.sendText(msg.to,"Dasar berisik!")
                ka.sendText(msg.to,"Awas mulut lu dower...")
            elif msg.text in ["Bangsat","bangcat","vangsat"]:
                ko.sendText(msg.to,"Cot")
                ks.sendText(msg.to,"kasar njir")
                ke.sendText(msg.to,"uuwuu..")
            elif msg.text in ["Jam on","jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
 
                    now3 = datetime.now()
                    nowU = datetime.strftime(now3,"(%H:%M)")
                    profile = kk.getProfile()
                    profile.displayName = wait["cName2"] + nowU
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"done")
 
                    now4 = datetime.now()
                    nowV = datetime.strftime(now4,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName3"] + nowV
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"done")
 
                    now5 = datetime.now()
                    nowW = datetime.strftime(now5,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowW
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"done")
 
                    now6 = datetime.now()
                    nowX = datetime.strftime(now6,"(%H:%M)")
                    profile = kg.getProfile()
                    profile.displayName = wait["cName5"] + nowX
                    kg.updateProfile(profile)
                    kg.sendText(msg.to,"done")
            elif msg.text in ["Jam off","jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"oke has ben turn off")
            elif msg.text in ["Change clock to ","change clock to "]:
                n = msg.text.replace("Change clock to ","")
                o = msg.text.replace("Sunysz change clockbto ","")
                p = msg.text.replace("Sunysz change clock to ","")
                q = msg.text.replace("Sunysz change clock to ","")
                r = msg.text.replace("Sunysz change clock to ","")
                if len(n.decode("utf-8")) > 13:
                    random.choice(KAC).sendText(msg.to,"succes a changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
 
                    wait["cName2"] = o
                    kk.sendText(msg.to,"changed to\n\n" + o)
 
                    wait["cName3"] = p
                    ki.sendText(msg.to,"changed to\n\n" + p)
 
                    wait["cName4"] = q
                    kc.sendText(msg.to,"changed to\n\n" + q)
 
                    wait["cName5"] = r
                    kg.sendText(msg.to,"changed to\n\n" + r)
            elif msg.text in ["Up","up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
 
                    now3 = datetime.now()
                    nowU = datetime.strftime(now3,"(%H:%M)")
                    profile = kk.getProfile()
                    profile.displayName = wait["cName2"] + nowU
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"Jam Update")
 
                    now4 = datetime.now()
                    nowV = datetime.strftime(now4,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName3"] + nowV
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Jam Update")
 
                    now5 = datetime.now()
                    nowW = datetime.strftime(now5,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowW
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Update")
 
                    now6 = datetime.now()
                    nowX = datetime.strftime(now6,"(%H:%M)")
                    profile = kg.getProfile()
                    profile.displayName = wait["cName5"] + nowX
                    kg.updateProfile(profile)
                    kg.sendText(msg.to,"Jam Update")
                else:
                    random.choice(KAC).sendText(msg.to,"Please turn on the name clock")
            elif msg.text in ["Share:on","Share on","Share on"]:
                if msg.from_ in staff:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"error")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Share:off","Share off","Share off"]:
                if msg.from_ in staff:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"error")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Visit on","K on","Contact on","k on"]:
                if msg.from_ in staff:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Visit off","K off","Contact off","k off"]:
                if msg.from_ in staff:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done ")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Leave:on","Leave on","Auto leave:on","leave on"]:
                if msg.from_ in staff:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"error")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Leave:off","Leave off","Auto leave:off","leave off"]:
                if msg.from_ in staff:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"error")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Add:on","Add on","Auto add:on","Add On"]:
                if msg.from_ in staff:
                    if wait["autoAdd"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"Done,add has ben on")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif msg.text in ["Add:off","Add off","Auto add:off","Add On"]:
                if msg.from_ in staff:
                    if wait["autoAdd"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"Done,add has ben off")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff permission required.")
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["C on","Comment on","Comment:on","Comment On"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â‚¬Ã£â‚¬â€š")
            elif msg.text in ["C on","Comment on","Comment off","Comment On"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Comment","Comm"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Message","message"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows\n\n" + wait["message"])
            elif msg.text in ["Status"]:
                md = ""
                if wait["contact"] == True: md+="Status:\n\n 》Contact : on􀜁􀄰no􏿿\n"
                else: md+=" Status:\n\n》Contact : off􀜁􀄯ok􏿿\n"
                if wait["autoJoin"] == True: md+=" 》Auto join : on􀜁􀄰no􏿿\n"
                else: md +=" 》Auto join : off\n"
                if cancelinvite["autoCancel"] == True:md+=" 》Auto Cancel : on􀜁􀇔protect􏿿\n"
                else: md+= " 》Auto Cancel : off􀜁􀄯ok􏿿\n"
                if wait["leaveRoom"] == True: md+=" 》Auto leave : on􀜁􀄰no􏿿\n"
                else: md+=" 》Auto leave : off􀜁􀄯ok􏿿\n"
                if wait["timeline"] == True: md+=" 》Url Share : on􀜁􀄰no􏿿\n"
                else:md+=" 》Url Share : off􀜁􀄯ok􏿿\n"
                if wait["autoAdd"] == True: md+=" 》Auto Add : on􀜁􀄰no􏿿\n"
                else: md+=" 》Auto Add : off􀜁􀄯ok􏿿\n"
                if cancelinvite["autoCancel"] == True: md+=" 》Protect url : on􀜁􀇔protect􏿿\n"
                else:md+=" 》Protect url : off􀜁􀄯ok􏿿\n"
                if wait["protectionAdmin"] == True: md+=" 》Protect(admin) : on􀜁􀇔protect􏿿\n"
                else:md+=" 》Protect(admin) : off􀜁􀄯ok􏿿\n"
                if wait["protectionOn"] == True: md+=" 》Protection : on􀜁􀇔protect􏿿\n"
                else:md+=" 》Protection : off􀜁􀄯ok􏿿\n"
                if wait["backup"] == True: md+=" 》Backup mode : on􀜁􀇔protect􏿿\n"
                else:md+=" 》Backup mode : off􀜁􀄯ok􏿿\n"
                if wait["commentOn"] == True: md+=" 》Comment : on􀜁􀄰no􏿿\n"
                else:md+=" 》Comment : off􀜁􀄯ok􏿿\n"
                cl.sendText(msg.to,md)
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Sp","Speed all","Sunysz sp all","Sunysz speed all"]:
                if msg.from_ in staff:
                    start = time.time()
                    cl.sendText(msg.to, "Bot 1 Processing Request...")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%s seconds" % (elapsed_time))
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Sunysz Sp 1","Sunysz Speed 1","Sunysz sp 1","Sunysz speed 1"]:
                if msg.from_ in staff:
                    start = time.time()                  
                    cl.sendText(msg.to, "Processing Request...")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%s seconds" % (elapsed_time))
                    print "[Command]Speed 1 executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Sunysz Sp 2","Sunysz Speed 2","Sunysz sp 2","Sunysz speed 2"]:
                if msg.from_ in staff:
                    start = time.time()                    
                    kk.sendText(msg.to, "Processing Request...")                    
                    elapsed_time = time.time() - start
                    kk.sendText(msg.to, "%s seconds" % (elapsed_time))
                    print "[Command]Speed 2 executed"
                else:
                    kk.sendText(msg.to,"Command denied.")
                    kk.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Sunysz Sp 3","Sunysz Speed 3","Sunysz sp 3","Sunyszr speed 3"]:
                if msg.from_ in staff:
                    start = time.time()                  
                    ki.sendText(msg.to, "Processing Request...")                    
                    elapsed_time = time.time() - start
                    ki.sendText(msg.to, "%s seconds" % (elapsed_time))
                    print "[Command]Speed 3 executed"
                else:
                    ki.sendText(msg.to,"Command denied.")
                    ki.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Sunysz Sp 4","Sunysz Speed 4","Sunysz sp 4","Sunysz speed 4"]:
                if msg.from_ in staff:
                    start = time.time()                  
                    kc.sendText(msg.to, "Processing Request...")                    
                    elapsed_time = time.time() - start
                    kc.sendText(msg.to, "%s seconds" % (elapsed_time))
                    print "[Command]Speed 4 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Sunysz Sp 5","Sunysz Speed 5","Sunysz sp 5","Sunysz speed 5"]:
                if msg.from_ in staff:    
                    start = time.time()                
                    kg.sendText(msg.to, "Processing Request...")                                      
                    elapsed_time = time.time() - start
                    kg.sendText(msg.to, "%s seconds" % (elapsed_time))
                    print "[Command]Speed 5 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Auto Cancel Section]------------------------
            elif "Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Staff del @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Staff del @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif "Del staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Del staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Sunysz Stafflist","Sunysz stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    mc = ""
                    for mi_d in staff:
                        mc += "👉 " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to, "SUNYSZ BOT(s)\n\nStaff list:\n" + mc)
                    print "[Command]Stafflist executed"
            elif "Admin add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Admin add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]Admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Owner permission required.")
            elif "admin add @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Admin add executing"
                    _name = msg.text.replace("admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]Admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Owner permission required.")
            elif "admin del @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Admin remove executing"
                    _name = msg.text.replace("admin del @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]Admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Owner permission required.")
            elif "Admin del @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Admin remove executing"
                    _name = msg.text.replace("Admin del @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]Admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Adminlist","adminlist"]:
                if admin == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    mc = ""
                    for mi_d in admin:
                        mc += "👉 " +cl.getContact(mi_d).displayName + " 😎\n"
                    cl.sendText(msg.to, "BOT(s)\n\nAdmin list:\n" + mc)
#-----------------------[Check Siders Section]------------------------
            elif msg.text in ["Lurk:on","lurk:on","Setpoint","Set"]:
                cl.sendText(msg.to, "You want know the siders? ~> ♪\n「Setpoint」and I check it ♪...\n" + datetime.datetime.today().strftime('\n\n%H:%M:%S'))
                try:
                    del wait2['readPoint'][msg.to]
                    del wait2['readMember'][msg.to]
                except:
                    pass
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.datetime.today().strftime('\n\n%Y-%m-%d %H:%M:%S')
                wait2['ROM'][msg.to] = {}
                print wait2
            elif msg.text in ["Lurk:result","lurk:result","Viewpoint","Check"]:
                if msg.to in wait2['readPoint']:
                    if wait2["ROM"][msg.to].items() == []:
                        chiya = ""
                    else:
                        chiya = ""
                        for rom in wait2["ROM"][msg.to].items():
                            print rom
                            chiya += rom[1] + "\n"
                               
                    cl.sendText(msg.to, "People who readed %s\nthat's it\ndate and time is:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                else:
                    random.choice(KAC).sendText(msg.to, "An already read point has not been set.\n「Setpoint」you can send ♪ read point will be created")
#-----------------------[Auto cancel Section]------------------------
            elif msg.text in ["Cancel off","cancel off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Cancel on","cancel on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Url off","url off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Url on","url on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned on")
                        print "[Command]Url on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel Url already turned on")
                        print "[Command]Url on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Misc Section]-------------------------------------------
            elif "Random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|+'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(4)
                                group.name = name
                                random.choice(KAC).updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
            elif "random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|+'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(4)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
            elif msg.text == "Time":
                if msg.from_ in staff:
                    cl.sendText(msg.to, "Current time is\n" + datetime.datetime.today().strftime('%Y<~Year %m<~Month %d<~Day %H:%M:%S') + "\n\n^up^")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift":
                if msg.from_ in staff:
                    cl.sendText(msg.to, "You want a gift?\nGift list:\n~>Gift 1\n~>Gift 2\n~>Gift 3\n~>Gift 4\n~>Gift 5\n~>Gift 6\n~>Gift 7\n~>Gift 8")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 2":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 1":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'PRDID': '2df50b22-112d-4f21-b856-f88df2193f9e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 3":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'PRDID': 'dc1e9626-7594-4561-a86e-5891910c96f3',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 4":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'PRDID': '40ed630f-22d2-4ddd-8999-d64cef5e6c7d',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 5":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'STKPKGID': '1066653',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '2'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 6":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'STKPKGID': '8588',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '3'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 7":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'STKPKGID': '5594',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '4'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text == "Gift 8":
                if msg.from_ in staff:
                    msg.contentType = 9
                    msg.contentMetadata = {'STKPKGID': '8228',
                                    'PRDTYPE': 'STICKER',
                                    'MSGTPL': '12'}
                    cl.sendMessage(msg)
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text in ["Ngakak","wkwk","Wkwk"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["Hadeh","hadeh","hadeuh"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["You","you","U"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["Sticker","test","hmm"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "2",
                                     "STKPKGID": "1405437",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["lol","Lol","hzz"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["Sedih","sedih","Nangis"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text in ["Please","please","Help me"]:
                msg.contentType = 7
                msg.contentMetadata = {"STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100"}
                cl.sendMessage(msg)
            elif msg.text == "Author":
                msg.contentType = 13
                msg.contentMetadata={'mid': "u7a5257b4cd2286f1a225fe44e797dd0f"}
                cl.sendMessage(msg)
            elif "Cm:" in msg.text:
                if msg.from_ in staff:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    random.choice(KAC).sendText(msg.to,"mid:"+key1)
            elif msg.text in ["Bot1 cn "]:
                string = msg.text.replace("Bot1 cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name "+string+" done")
            elif msg.text in ["Bot3 rename "]:
                string = msg.text.replace("Bot3 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name "+string+" done")
            elif msg.text in ["Bot2 rename "]:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_C = kk.getProfile()
                    profile_C.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name "+string+" done")
            elif msg.text in ["Bot4 rename "]:
                string = msg.text.replace("Bot4 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_D = kc.getProfile()
                    profile_D.displayName = string
                    kc.updateProfile(profile_B)
                    kc.sendText(msg.to,"name "+string+" done")
            elif msg.text in ["Bot5 rename "]:
                string = msg.text.replace("Bot5 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_E = kg.getProfile()
                    profile_E.displayName = string
                    kg.updateProfile(profile_B)
                    kg.sendText(msg.to,"name "+string+" done")
            elif msg.text in ["Taggg","Mention"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    name = [contact.mid for contact in group.members]
                    cb = ""
                    cb2 = ""
                    strt = int(0)
                    akh = int(0)
                    for md in name:
                        akh = akh + int(5)
                        cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                        strt = strt + int(6)
                        akh = akh + 1
                        cb2 += "@nrik\n"
                    cb = (cb[:int(len(cb)-1)])
                    msg.contentType = 0
                    msg.text = cb2
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
            if "km:" in msg.text:
                    if msg.from_ in admin:
                        key = msg.text[5:]
                        cl.kickoutFromGroup(msg.to, [key])
                        kk.kickoutFromGroup(msg.to, [key])
                        ki.kickoutFromGroup(msg.to, [key])
                        kc.kickoutFromGroup(msg.to, [key])
                        kg.kickoutFromGroup(msg.to, [key])
                        contact = cl.getContact(key)
                        contact = kk.getContact(key)
                        contact = ki.getContact(key)
                        contact = kc.getContact(key)
                        contact = kg.getContact(key)
                        random.choice(KAC).sendText(msg.to, ""+contact.displayName+" i hate you")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text in ["List gc bot1"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = cl.getGroup(i).name
                        h += "》%s\n" % (gn)
                    cl.sendText(msg.to,"~~~~~~=[List Groups]=~~~~~~\n"+ h +"\n\nTotal groups: "+str(len(gn)))
                else:
                    cl.sendText("Admin permission required.")
            elif msg.text in ["List gc bot2"]:
                if msg.from_ in admin:
                    gid = kk.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = kk.getGroup(i).name
                        h += "》%s\n" % (gn)
                    kk.sendText(msg.to,"~~~~~~=[List Groups]=~~~~~~\n"+ h +"\n\nTotal groups: "+str(len(gn)))
                else:
                    kk.sendText("Admin permission required.")
            elif msg.text in ["List gc bot3"]:
                if msg.from_ in admin:
                    gid = ki.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = ki.getGroup(i).name
                        h += "》%s\n" % (gn)
                    ki.sendText(msg.to,"~~~~~~=[List Groups]=~~~~~~\n"+ h +"\n\nTotal groups: "+str(len(gn)))
                else:
                    ki.sendText("Admin permission required.")
            elif msg.text in ["List gc bot4"]:
                if msg.from_ in admin:
                    gid = kc.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = kc.getGroup(i).name
                        h += "》%s\n" % (gn)
                    kc.sendText(msg.to,"~~~~~~=[List Groups]=~~~~~~\n"+ h +"\n\nTotal groups: "+str(len(gn)))
                else:
                    kc.sendText("Admin permission required.")
            elif msg.text in ["List gc bot5"]:
                if msg.from_ in admin:
                    gid = kg.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        gn = kg.getGroup(i).name
                        h += "》%s\n" % (gn)
                    kg.sendText(msg.to,"~~~~~~=[List Groups=~~~~~~\n"+ h +"\n\nTotal groups: "+str(len(gn)))
                else:
                    kg.sendText("Admin permission required.")
            elif msg.text in ["Responsename","Response"]:
                if msg.from_ in staff:
                    cl.sendText(msg.to, "Hai")
                    kk.sendText(msg.to, "Hola")
                    ki.sendText(msg.to, "Hello")
                    kc.sendText(msg.to, "Alohaa")
                    kg.sendText(msg.to, "Aloaloha")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text in ["Status:","""{"cancel":1,"kick":0}"""]:
                random.choice(KAC).kickoutFromGroup
            if "We invite:" in msg.text:
                if msg.from_ in staff:
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
                    cl.sendText(msg.to, ""+contact.displayName+" Done")
                    kk.findAndAddContactsByMid(key)
                    kk.inviteIntoGroup(msg.to, [key])
                    contact = kk.getContact(key)
                    kk.sendText(msg.to, ""+contact.displayName+" Done")
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
            elif msg.text in ["Absen","absen"]:
                if msg.from_ in staff:
                    cl.sendText(msg.to, "Bot1 On...􀜁􀅔􏿿")
                    kk.sendText(msg.to, "Bot2 On...􀜁􀅔􏿿")
                    ki.sendText(msg.to, "Bot3 On...􀜁􀅔􏿿")
                    kc.sendText(msg.to, "Bot4 On...􀜁􀅔􏿿")
                    kg.sendText(msg.to, "Bot5 On...􀜁􀅔􏿿")
                    print "[Command]Absen executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif msg.text in ["Kernel","kernel"]:
                if msg.from_ in admin:
                    botKernel = [subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]]
                    cl.sendText(msg.to, botKernel)
                    print "[Command]Kernel executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif "Stalking" in msg.text:
                print "[Command]Stalk executing"
                stalkID = msg.text.replace("Stalking ","")
                subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])  
                files = glob.glob("tmp/*.jpg")
                for file in files:
                    os.rename(file,"tmp/tmp.jpg")
                    fileTmp = glob.glob("tmp/tmp.jpg")
                if not fileTmp:
                    cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                    print "[Command]Stalk executed - no image found"
                else:
                    image = upload_tempimage(client)
                    cl.sendText(msg.to, format(image['link']))
                    print "[Command]Stalk executed - success"

            elif "Add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executing"
                        _name = msg.text.replace("Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    cl.findAndAddContactsByMid(target)
                                except:
                                    ki.sendText(msg.to,"Error")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "add @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Add executed"
                        _name = msg.text.replace("Add @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                ki.findAndAddContactsByMid(target)
                                kk.findAndAddContactsByMid(target)
                                kc.findAndAddContactsByMid(target)
                                kg.findAndAddContactsByMid(target)
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["friendlist","Friendlist"]:
                if friend == []:
                    cl.sendText(msg.to,"The friendlist is empty")
                else:
                    cl.sendText(msg.to,"Friend list:")
                    mc = ""
                    for mi_d in friend:
                        mc += ">>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
                       
            elif msg.text in ["Sunysz Like", "Sunysz like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass
               
        if op.type == 59:
            print op
 
 
    except Exception as error:
        print error
 
# def nameUpdate_Bot1():
#     while True:
#         try:
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["1"]
#             cl.updateProfile(profile)
#             time.sleep(4)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["2"]
#             cl.updateProfile(profile)
#             time.sleep(4)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["3"]
#             cl.updateProfile(profile)
#             time.sleep(4)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["4"]
#             cl.updateProfile(profile)
#             time.sleep(4)
#             profile = cl.getProfile()
#             profile.displayName = bot1_name["5"]
#             cl.updateProfile(profile)
#             time.sleep(4)
#           except:
#             pass
#thread1 = threading.Thread(target=nameUpdate_Bot1)
#thread1.daemon = True
#thread1.start()
 
#def nameUpdate_Bot2():
#    while True:
#        try:
#            profile = kk.getProfile()
#            profile.displayName = bot2_name["1"]
#            kk.updateProfile(profile)
#            time.sleep(4)
#            profile = kk.getProfile()
#            profile.displayName = bot2_name["2"]
#            kk.updateProfile(profile)
#            time.sleep(4)
#            profile = kk.getProfile()
#            profile.displayName = bot2_name["3"]
#            kk.updateProfile(profile)
#            time.sleep(4)
#            profile = kk.getProfile()
#            profile.displayName = bot2_name["4"]
#            kk.updateProfile(profile)
#            time.sleep(4)
#            profile = kk.getProfile()
#            profile.displayName = bot2_name["5"]
#            kk.updateProfile(profile)
#            time.sleep(4)
#        except:
#            pass
#thread2 = threading.Thread(target=nameUpdate_Bot2)
#thread2.daemon = True
#thread2.start()
 
# def nameUpdate_Bot3():
#     while True:
#         try:
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["1"]
#             ki.updateProfile(profile)
#             time.sleep(4)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["2"]
#             ki.updateProfile(profile)
#             time.sleep(4)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["3"]
#             ki.updateProfile(profile)
#             time.sleep(4)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["4"]
#             ki.updateProfile(profile)
#             time.sleep(4)
#             profile = ki.getProfile()
#             profile.displayName = bot3_name["5"]
#             ki.updateProfile(profile)
#             time.sleep(4)
#        except:
#            pass
#thread3 = threading.Thread(target=nameUpdate_Bot3)
#thread3.daemon = True
#thread3.start()
 
# def nameUpdate_Bot4():
#     while True:
#         try:
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["1"]
#             kc.updateProfile(profile)
#             time.sleep(4)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["2"]
#             kc.updateProfile(profile)
#             time.sleep(4)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["3"]
#             kc.updateProfile(profile)
#             time.sleep(4)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["4"]
#             kc.updateProfile(profile)
#             time.sleep(4)
#             profile = kc.getProfile()
#             profile.displayName = bot4_name["5"]
#             kc.updateProfile(profile)
#             time.sleep(4)
#        except:
#            pass
#thread4 = threading.Thread(target=nameUpdate_Bot4)
#thread4.daemon = True
#thread4.start()
 
# def nameUpdate_Bot5():
#     while True:
#         try:
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["1"]
#             kg.updateProfile(profile)
#             time.sleep(4)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["2"]
#             kg.updateProfile(profile)
#             time.sleep(4)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["3"]
#             kg.updateProfile(profile)
#             time.sleep(4)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["4"]
#             kg.updateProfile(profile)
#             time.sleep(4)
#             profile = kg.getProfile()
#             profile.displayName = bot5_name["5"]
#             kg.updateProfile(profile)
#             time.sleep(4)
#        except:
#            pass
#thread5 = threading.Thread(target=nameUpdate_Bot5)
#thread5.daemon = True
#thread5.start()
 
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
 
    now3 = datetime.now()
    nowU = datetime.strftime(now3,"(%H:%M)")
 
    now4 = datetime.now()
    nowV = datetime.strftime(now4,"(%H:%M)")
 
    now5 = datetime.now()
    nowW = datetime.strftime(now5,"(%H:%M)")
 
    now6 = datetime.now()
    nowX = datetime.strftime(now6,"(%H:%M)")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
        if nowU[14:] in ["10","20","30","40","50","00"]:
            return False
        else:
            return True
            if nowV[14:] in ["10","20","30","40","50","00"]:
                return False
            else:
                return True
                if nowW[14:] in ["10","20","30","40","50","00"]:
                    return False
                else:
                    return True
                    if nowX[14:] in ["10","20","30","40","50","00"]:
                        return False
                    else:
                        return True
   
def nameUpdate():
    while True:
        try:
            while a2():
                pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)
 
                now3 = datetime.now()
                nowU = datetime.strftime(now3,"(%H:%M)")
                profile = kk.getProfile()
                profile.displayName = wait["cName2"]
                kk.updateProfile(profile)
 
                now4 = datetime.now()
                nowV = datetime.strftime(now4,"(%H:%M)")
                profile = ki.getProfile()
                profile.displayName = wait["cName3"]
                ki.updateProfile(profile)
 
                now5 = datetime.now()
                nowW = datetime.strftime(now5,"(%H:%M)")
                profile = kc.getProfile()
                profile.displayName = wait["cName4"]
                kc.updateProfile(profile)
 
                now6 = datetime.now()
                nowX = datetime.strftime(now6,"(%H:%M)")
                profile = kg.getProfile()
                profile.displayName = wait["cName5"]
                kg.updateProfile(profile)
            time.sleep(60)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
 
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in staff:
                try:    
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me.ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                    kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me.ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                    ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me.ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                    kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me.ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                    kg.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by SUNYSZ\n>> line.me.ti/p/~rizal.pratama20\n>> line.me.ti/p/~rizalpratama20")
                    print "Like"
                except:
                    pass
            else:
                print "Not Admin or staff"
        time.sleep(500)
thread2 = threading.Thread(target=likePost)
thread2.daemon = True
thread2.start()
 
# Auto Changing name
# thread1 = threading.Thread(target=nameUpdate_Bot1)
# thread1.daemon = True
# thread1.start()
# thread2 = threading.Thread(target=nameUpdate_Bot2)
# thread2.daemon = True
# thread2.start()
# thread3 = threading.Thread(target=nameUpdate_Bot3)
# thread3.daemon = True
# thread3.start()
# thread4 = threading.Thread(target=nameUpdate_Bot4)
# thread4.daemon = True
# thread4.start()
# thread5 = threading.Thread(target=nameUpdate_Bot5)
# thread5.daemon = True
# thread5.start()
# END
 
 
while True:
    while True:
        try:
            Ops = cl.fetchOps(cl.Poll.rev, 5)
        except EOFError:
            raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))
 
        for Op in Ops:
            if (Op.type != OpType.END_OF_OPERATION):
                cl.Poll.rev = max(cl.Poll.rev, Op.revision)
                bot(Op)

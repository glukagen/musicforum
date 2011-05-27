from datetime import timedelta
from django import VERSION
from django.db import connection, transaction, database
from django.db.utils import DatabaseError
from django.db.models import signals
from django.contrib.auth.models import User
from forum import models

def UserCreated(sender, **kwargs):
    user = kwargs['instance']
    models.UserProfile.objects.get_or_create(user=user, defaults={'About': ''})

syncdb_done = False
def SyncDB(sender, **kwargs):
    global syncdb_done
    if syncdb_done:
        return
    syncdb_done = True
    sql_commands = []
    if models.LinkStatQuanta in kwargs['created_models']:
        sql_commands.append("""
        CREATE INDEX interface_linkstatquanta_Epoch
        ON interface_linkstatquanta ("Epoch" DESC NULLS LAST);
        """)
    if models.LiveLinkStat in kwargs['created_models']:
        sql_commands.append("""
        CREATE INDEX interface_livelinkstat_Score
        ON interface_livelinkstat ("Score" DESC NULLS LAST);
        """)
        sql_commands.append("""
        CREATE INDEX interface_livelinkstat_Score_Trend
        ON interface_livelinkstat ("Score_Trend" DESC NULLS LAST);
        """)
    if models.LiveUserStat in kwargs['created_models']:
        sql_commands.append("""
        CREATE INDEX interface_liveuserstat_Score
        ON interface_liveuserstat ("Score" DESC NULLS LAST);
        """)
        sql_commands.append("""
        CREATE INDEX interface_liveuserstat_Score_Trend
        ON interface_liveuserstat ("Score_Trend" DESC NULLS LAST);
        """)
    if models.LiveCircleStat in kwargs['created_models']:
        sql_commands.append("""
        CREATE INDEX interface_livecirclestat_Score
        ON interface_livecirclestat ("Score" DESC NULLS LAST);
        """)
        sql_commands.append("""
        CREATE INDEX interface_livecirclestat_Score_Trend
        ON interface_livecirclestat ("Score_Trend" DESC NULLS LAST);
        """)

    cursor = connection.cursor()
    for sql in sql_commands:
        cursor.execute(sql)
        transaction.commit_unless_managed()            
        

if VERSION[0] >= 1 and VERSION[1] >= 3:
    from django.dispatch import receiver
    
    @receiver(signals.post_save, sender=User)
    def _UserCreated(sender, **kwargs):
        UserCreated(sender, **kwargs)

    @receiver(signals.post_syncdb, sender=models)
    def _SyncDB(sender, **kwargs):
        SyncDB(sender, **kwargs)

else:
    signals.post_save.connect(UserCreated, sender=User)
    signals.post_syncdb.connect(SyncDB, sender=models)

    
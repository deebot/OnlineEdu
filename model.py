import sqlite3
class Subscriber(object):
    """It's the Observer object. It receives messages from the Observable."""

    def __init__(self):
        self.name = ""
        self.data = ""

    def addSubName(self,name):
        self.name= name

    def receive(self, message):
        """Method assigned in, and called by, the Publisher.
        This method is assigned when the Publisher registers a Subscriber to a
        newsletter, and it's called when the Publisher dispatches a message.
        Parameters
        ----------
        message : str
        """
        print("{} received: {}".format(self.name, message))
        self.data = message

    def get_data(self):
        return self.data


class Publisher(object):
    """It's the Observable object. It dispatches messages to the Observers."""
    newsletters=[]
    def __init__(self):
        self.subscriptions = dict()
       # for newsletter in newsletters:
        #    self.add_newsletter(newsletter)

    def get_subscriptions(self, newsletter):
        return self.subscriptions[newsletter]

    def register(self, newsletter, who, callback=None):
        """Register a Subscriber to this newsletter.
        Parameters
        ----------
        newsletter : str
        who : Subscriber
        callback : method
            callback function bound to the Subscriber object
        """
        if callback is None:
            callback = getattr(who, "receive")
        self.get_subscriptions(newsletter)[who] = callback

    def unregister(self, newsletter, who):
        """Remove a Subscriber object from a subscription to a newsletter.
        Parameters
        ----------
        newsletter : str
        who : Subscriber
        """
        try:
            del self.get_subscriptions(newsletter)[who]
        except KeyError:
            print(
                "{} is not subscribed to the {} newsletter!".format(
                    who.name, newsletter
                )
            )

    def dispatch(self, newsletter, message):
        """Send a message to all subscribers registered to this newsletter.
        Parameters
        ----------
        newsletter : str
        message : str
        """
        if len(self.get_subscriptions(newsletter).items()) == 0:
            print(
                "No subscribers for the {} newsletter. Nothing to send!".format(
                    newsletter
                )
            )
            return

        for subscriber, callback in self.get_subscriptions(newsletter).items():
            callback(message)

    def add_newsletter(self, newsletter):
        """Add a subscription key-value pair for a new newsletter.
        The key is the name of the new subscription, namely the name of the
        newsletter (e.g. 'Tech'). The value is an empty dictionary which will be
        populated by subscriber objects willing to register to this newsletter.
        Parameters
        ----------
        newsletter : str
        """
        self.subscriptions[newsletter] = dict()


class Model(Subscriber,Publisher):

    def __init__(self):
        Subscriber.__init__(self)
        Publisher.__init__(self)
        self.LoginID=""
        self.password=""
        self.ButtonID=""
        self.dataLogger=DataLogger
        self.sub = Subscriber()
        self.pub = Publisher()


    def recogniseButton(self, ButtonID):
        if ButtonID == 'buttonSubmit':
            self.pub.add_newsletter("Tech-")

            print(f' In Model button {ButtonID} registered')
            db = self.dataLogger()
            conn = db.connect()
            db.tableCheck(conn)
            print(db.retriveUser())
            if db.retriveUser() =="found":
                self.pub.dispatch(newsletter="Tech", message="Profile")
            else:
                self.pub.dispatch(newsletter="Tech", message="Login")


class SingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@SingletonDecorator
class DataLogger(object):
    def __init__(self):
        self.connection = None
        self.dbname = r"UserDatabase.db"

    def connect(self):
        print("Connecting to Database")
        if self.connection is None:
            self.connection = sqlite3.connect(self.dbname)
        return self.connection



    def tableCheck(self,conn):
        print("Checking Existance of Table")
        cur = conn.cursor()
        cur.execute(''' SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'qrcodes' ''')
        if cur.fetchone()[0] == 1:
            print("table exists")
        else:
            cur.execute("""CREATE TABLE qrcodes(
                        date text,
                        time text,
                        pefferSerial text,
                        sensotekSerial text,
                        aType text,
                        sType text
                )""")

    def InsertUser(self):
        pass

    def retriveUser(self):
        return "found"


if __name__== '__main__':
    pass

from __future__ import print_function
import pickle
import os.path
import apiclient
import urllib.error
import pprint
import html
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Function : GetMessage
# Does     : Get a Message with given ID.
# Args:    : service : Authorized Gmail API service instance.
#            user_id : User's email address. The special value "me"
#                    can be used to indicate the authenticated user.
#            msg_id  : The ID of the Message required.
# Returns  : A text snippet of the message
def GetMessage(service, user_id, msg_id):
    try:
        message = service.users().messages().get(userId=user_id,
                                                 id=msg_id).execute()

        #print('Message snippet: %s' % text_snippet)
        return message['snippet']
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

# Function : ListMessageMatchingQuery
# Does     : List all Messages of the user's mailbox matching the query.
# Args     : service : Authorized Gmail API service instance.
#            user_id : User's email address. The special value "me"
#                     can be used to indicate the authenticated user.
#            query   : String used to filter messages returned.
#                      Eg.- 'from:user@some_domain.com' for Messages from a
#                      particular sender.
# Returns  : List of Messages that match the criteria of the query. Note that
#            the returned list contains Message IDs, you must use get with the
#            appropriate ID to get the details of a Message.
def ListMessagesMatchingQuery(service, user_id):

    today = date.today()
    yesterday = today - timedelta(1)
    query = "in:anywhere"

    response = service.users().messages().list(userId=user_id,
                                               q=query,
                                               maxResults=511).execute()

    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    pageToken = None
    if 'nextPageToken' in response:
        pageToken = response['nextPageToken']

    while pageToken:
        response = service.users().messages().list(userId=user_id,
                                                   q=query,
                                                   maxResults=511,
                                                   pageToken=pageToken)\
                                                   .execute()
        messages.extend(response['messages'])
        if 'nextPageToken' in response:
            pageToken = response['nextPageToken']
        else:
            break

    return messages


def main():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    mails = ListMessagesMatchingQuery(service, "me")

    fo = open("../training_data/marketing_phrases.txt", "w")

    counter = 0

    for mail in mails:
        id = mail['id']
        message = GetMessage(service, "me", id)
        fo.write(message)
        counter = counter + 1
        print(counter)

    fo.close()

if __name__ == '__main__':
    main()

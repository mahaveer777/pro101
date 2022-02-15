import dropbox
class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfiles(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        with open(filefrom,"rb") as f:
            dbx.files_upload(f.read(),fileto)
def main():            
    accesstoken="N8kMVNwIOlUAAAAAAAAAAXjmvMXZCM8xQuI37zS2wWV4asCiVgkMiZJ7N3GKxzkL"
    passs=TransferData(accesstoken)
    filefrom=input("enter file name")
    fileto="/pro101/"+filefrom
    passs.uploadfiles(filefrom,fileto)
main()
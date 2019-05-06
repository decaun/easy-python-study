var = 235
reminder=var%50
for i in range(0,235,50):
    print(i)

                    for counter in range(0,int(request.args.get('count')),50):
                        print(counter)
                    #spotify.call_songs(request.args.get('user_id'),request.args.get('playlist_id'), current=counter, next=50)#max range for api hardcoded as 50
                '''
                if (int(request.args.get('count'))%50)!=0:
                    print('test')
                    spotify.call_songs(request.args.get('user_id'),request.args.get('playlist_id'), current=50*(int(request.args.get('count'))//50), next=int(request.args.get('count'))%50)
                '''

        for batch in range(0,len(list_of_tracks),100):
            self.features=self.active.audio_features(tracks = list_of_tracks[batch:batch+100])
def audio_down(os,requests,vk_api,vk,user_id,r,formate):
    try:
        os.mkdir('audio')
    except:
        ...
    r = r.json()
    url = r['updates'][0]['object']['attachments'][0]['audio']['url']
    title = r['updates'][0]['object']['attachments'][0]['audio']['title']
    artist = r['updates'][0]['object']['attachments'][0]['audio']['artist']
    full_local_path= os.path.join('audio','{}.{}'.format(user_id,formate))
    with open(full_local_path, 'wb') as f:
        r = requests.get(url)
        if r.status_code == 200:
            for c in r:
                f.write(c)
    upload = vk_api.VkUpload(vk)
    docu = upload.document_message(doc = full_local_path, title = title, peer_id= user_id)
    return docu 
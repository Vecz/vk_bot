
def upload_graph(vk,idi, vk_api, os):
    '''Загрузка графика в личные сообщения в вк '''
    upload = vk_api.VkUpload(vk)
    full_path = os.path.join('png','{}.png'.format(idi))
    photo = upload.photo_messages(full_path)
    return(photo)

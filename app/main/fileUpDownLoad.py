# coding=utf-8
import urllib2, json
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

#文件上传
#file:打开的文件对象，example:open('g:/yum','rb')
#url:请求的地址，这里格式为:http://ip:port/fileUpload/multipartFiles/{单片机SN}
def fileUpload(file,url):
    register_openers()

    # file_upload相当于form表单里input的name
    params = {'file_upload': file}
    datagen, headers = multipart_encode(params)
    request = urllib2.Request(url, datagen, headers)

    try:
        response = urllib2.urlopen(request)
        return response.read()

    except urllib2.URLError, e:
        return e.reason

#获取可下载文件的列表
#url格式为http://ip:port/fileDownload/list/{单片机SN}?page=0&size=10&sort=uploadtime,desc
# page，第几页，从0开始，默认为第0页
# size，每一页的大小，默认为20
# sort，排序相关的信息，以property,property(,ASC|DESC)的方式组织,asc默认,不需要写,例如sort=uploadtime,desc&sort=id表示在按uploadtime倒序排列基础上按id正序排列
#返回一个列表，其中每个元素都是json格式
#格式为[{"id":id,"identification":单片机SN,"uploadTime":上传时间戳,"fileName":文件名,"fileSize":文件大小，"objectId":objectId}]
#调用下载方法，需要用到objectId
def fileDownloadList(url):
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res

#下载文件
#url格式为http://ip:port/fileDownload/{ObjectId}
#file为写入的file对象
def fileDownLoad(url,file):
    f = urllib2.urlopen(url)
    file.write(f.read())

if __name__ == '__main__':
    print 'begin'
    res = fileDownloadList('http://10.2.0.135:8080/fileDownload/list/helloworld')
    if res:
        json_array = json.loads(res)
        json_obj = json_array[0]
        object_id = json_obj['objectId']
        f = open('../static/tmp/text12.ini', 'w')
        fileDownLoad("http://10.2.0.135:8080/fileDownload/%s"%object_id, f)
        f.close()
    print res


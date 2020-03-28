import re
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.

#皮肤助手页面
def lolskin(request):
	context = {}
	return render(request, 'lolskin.html', context)

#取得本地保存的文字识别用的安全令牌access_token
def get_access_token(self):
	f = open("../../baidu_access_token.txt","r")
	access_token = f.read()
	#print(access_token)
	f.close()
	data = {}
	data['access_token'] = access_token
	return JsonResponse(data)

def get_download_url(request):
		#这段代码只要软件首页被访问就运行,获取网页下载网址
	html = requests.get("http://leagueskin.net/p/download-mod-skin-2020-chn")
	content = str(html.content,encoding="utf-8")
	#print(html.content)
	skinbox_url_list = re.findall(r"<a id=\"link_download3\" href=\"(.*)\"> <button style=",content)    #正则获取皮肤盒子下载地址
	skinbox_url = ''.join(skinbox_url_list)            #转化为字符串,只有一个元素也就是下载网址
	#print(skinbox_url)
	#print(skinbox_url_list)
	return redirect(skinbox_url)
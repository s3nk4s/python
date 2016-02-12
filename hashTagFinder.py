from instagram.client import InstagramAPI
import urlparse

access_token = ''
clientid = ''
clientSecret = ''
url = ''

tag_name = '4000tricot'
max_tag_id = '0'

api = InstagramAPI(access_token=access_token)
user = api.user_search('')[0].id

tag_info = api.tag(tag_name)
count = tag_info.media_count
print count

f1 = file(tag_name + '.html','w')
h = '<html><table>'

i = 0

while True:

    recent_media, next_url = api.tag_recent_media(count, max_tag_id, tag_name)

    for media in recent_media:

	if i % 5 == 0:
		h = h + '<tr>'

	i = i + 1
	print str(i) + ',' + media.user.username + ',"' + media.user.full_name + '",' + media.link + ',' + str(media.created_time)
	h = h + '<td>' + str(i) + ': <a href="' + media.link + '">' + media.user.username + '<br>' + str(media.created_time) + '<br><img src="' + media.images['thumbnail'].url + '"</a></p>'

	if i % 5 == 0:
		h = h + '</tr>'

    if next_url is None:
	break

    p = urlparse.urlparse(next_url)
    max_tag_id = urlparse.parse_qs(p.query)['max_tag_id'][0]

h = h + '</table></html>'

f1.write(h)

blog_views = [150,800,2500,600,1200,450,3000]
views = 0
count = 0
for x in blog_views:
    views = views + x
    if x > 1000:
        print('Trending')
        count = count + 1
    elif 500 <= x <= 1000:
        print('Average')
    else:
        print('Low Traffic')
print('Total number of views:',views)
print('Number of Trending posts:',count)

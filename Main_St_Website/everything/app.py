from flask import Flask, render_template, url_for
import os


app = Flask(__name__)


#print(os.getcwd(C:\Users\ag752\Desktop\Main_St_Website\static))
@app.route('/')
def home():
    beer_imgs = [
        url_for('static', filename=f'Featured_Items/Beer/{img}')
        for img in os.listdir(os.path.join(app.static_folder, 'Featured_Items/Beer'))
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    IPAimg =[
        url_for('static', filename=f'Featured_Items/IPAs/{img}')
        for img in os.listdir(os.path.join(app.static_folder, 'Featured_Items/IPAs'))
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    wineimgs =[
        url_for('static', filename=f'Featured_Items/Wine/{img}')
        for img in os.listdir(os.path.join(app.static_folder, 'Featured_Items/Wine'))
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]
    spiritsimgs =[
        url_for('static', filename=f'Featured_Items/Spirits/{img}')
        for img in os.listdir(os.path.join(app.static_folder, 'Featured_Items/Spirits'))
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]    
    doordash_logo = url_for('static', filename="Images/doordash-logo.png")
    return render_template('/index.html', image_file=doordash_logo, imgs = beer_imgs, ipaimgs = IPAimg, wineimgs = wineimgs, spiritsimgs = spiritsimgs)

@app.route('/Blog')
def main():
    blogimgs =[
    url_for('static', filename=f'blog_images/{img}')
    for img in os.listdir(os.path.join(app.static_folder, 'blog_images'))
    if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
    ]  
    return render_template('/blog.html', imgs = blogimgs)
@app.route('/Contact')
def contact():
    return render_template('/Contact.html')


if __name__ == '__main__':
    app.run(debug=True)


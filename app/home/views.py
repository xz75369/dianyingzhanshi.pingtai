# _*_ coding: utf-8 _*_
from . import home
from flask import render_template,url_for,redirect

@home.route("/")
def index():
    return render_template("home/index.html")

#登陆
@home.route("/login/")
def login():
    return render_template("home/login.html")
#退出
@home.route("/logout/")
def logout():
    return redirect(url_for('home.login'))

#重新定位到未登陆的状态

@home.route("/register/")
def register():
    return render_template("home/register.html")
#注册页面

@home.route("/user/")
def user():
    """用户中心"""
    return render_template("home/user.html")


@home.route("/pwd/")
def pwd():
    """修改密码"""
    return render_template("home/pwd.html")

@home.route("/comments/")
def comments():
    """评论记录"""
    return render_template("home/comments.html")


@home.route("/loginlog/")
def loginlog():
    """登录日志"""
    return render_template("home/loginlog.html")


@home.route("/moviecol/")
def moviecol():
    """收藏电影"""
    return render_template("home/moviecol.html")

@home.route("/animation/")
def animation():
    return render_template("home/animation.html")

@home.route("/layout/")
def layout():
    return render_template("home/layout.html")


@home.route("/search/")
def search():
    "搜索电影模块"
    return render_template("home/search.html")

@home.route("/play/")
def play():
    "电影详情"
    return render_template("home/play.html")






##@app.errorhandler(404)
##def page_not_found(error):
 ##   "404"
 ##   return render_template("home/404.html"), 404
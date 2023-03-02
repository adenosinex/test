from flask import current_app,render_template,session,request,redirect,flash,url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/api/add' )
def add( ):
    name=request.args.get('name') 
    t=current_app.login_manager.id_attribute
    if name:
        # 名字添加key
        key='add'
        u=User.query.filter_by(name=name).first()
        if not key in u.name:
            u.name=key+name
        else:
            u.name=u.name.replace(key,'')

        if u:
            db.session.add(u)
            db.session.commit()
            flash('修改成功')
        
    url=url_for('.index')
    return redirect(url)

@main.route('/',methods=['get','post'])
def index( ):
    form=NameForm()
    # post修改名
    if   form.validate_on_submit():
        session['name']=form.name.data
     # get修改名
    elif request.args.get('name'):
        session['name']=request.args.get('name')

    page=1
    name='test'
    # 构造默认名
    if not session.get('name'):
        session['name']=name
    # 页数
    if request.args.get('page'):
        page=request.args.get('page')
        try:
            page=int(page)
        except:
            page=1

    pagination=User.query.order_by(User.id.asc()).paginate(page=page,per_page=20)
    posts=pagination.items
    
    data={'hi':"hi",
    'name':session['name'],
     }
    
    return  render_template('index.html',form=form,data=data,posts=posts,pagination=pagination)

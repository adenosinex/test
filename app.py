from app import create_app
 
app=create_app()
123
# with app.app_context():
#     db.create_all()
    # User().fake_data()

app.run(port=80)
import streamlit as st
st.set_page_config(page_title='MyProject',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Information'))
st.title('Employee Page')
st.text('Go to Information section to know the deatils of an employee')
if(mymenu=='Home'):
    st.markdown('<center><h1><WELCOME></h1></center>',unsafe_allow_html=True)
elif(mymenu=='Information'):
    with st.form('Emp Info'):
        emp_id=st.text_input("Enter Employee ID ")
        name=st.text_input('Enter Employee Name')
        age=st.slider('Enter Employee Age')
        salary=st.slider('Choose Salary')
        k=st.form_submit_button('Submit')
        if k:
            import firebase_admin
            from firebase_admin import credentials
            from firebase_admin import db
            d={"Name":name,"Age":age,"Salary":salary}
            e="/"+emp_id
            ref=db.reference(e)
            ref.update(d)
            if 'k' not in st.session_state:
                st.session_state['k']=True
                cred = credentials.Certificate("streamlitkey.json.json")
                app=firebase_admin.initialize_app(cred,{'databaseURL':'https://streamlit-and-firebase-default-rtdb.europe-west1.firebasedatabase.app/'})
        

from flask import Flask, render_template,request
from completeness_check import*
from completeness_display import*
from subsegmentation import*
from completeness_grouping import*
from missingvalue import*
from test2 import*
app = Flask(__name__)
path_name=''


@app.route('/')
def index():

    return render_template("temptest.html")


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():

    return render_template('temptest2.html')


@app.route('/analysis', methods=['POST','GET'])
def analysis():
    if request.method == 'POST':
        result = request.form
        global path_name
        path_name=result["myFile"]
        print(path_name)
        x=path_name
        df=completeness_check.read(x)
        output=data_report(df)
        def highlight_greaterthan(s,column):
            is_max = pd.Series(data=False, index=s.index)
            is_max[column] = s.loc[column] =="Y"
            return ['background-color:#8A878F' if is_max.any() else '' for v in is_max]


        styled_df=output.style.apply(highlight_greaterthan,column=['Null_Check'], axis=1)

        return render_template('analysis.html',data=styled_df.render())
    else:
        # global path_name
        x=path_name
        df=completeness_check.read(x)
        output=data_report(df)
        def highlight_greaterthan(s,column):
            is_max = pd.Series(data=False, index=s.index)
            is_max[column] = s.loc[column] =="NULL"
            return ['background-color:#8A878F' if is_max.any() else '' for v in is_max]


        styled_df=output.style.apply(highlight_greaterthan,column=['Null_Check'], axis=1)
        return render_template('analysis.html',data=styled_df.render())


@app.route('/completeness', methods=['GET', 'POST'])
def completeness():
    global path_name
    df=completeness_check.read(path_name)
    output=data_report(df)
    a=missing_main_final(path_name)
    return render_template('completeness.html',data=a.to_html())

    if __name__ == '__main__':
       app.run(debug = True)

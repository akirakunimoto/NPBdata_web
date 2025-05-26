import streamlit as st
import pandas as pd

# NPB選手情報を分析するStreamlitアプリケーション
# ローカル実行：py -m streamlit run analize_player.py

def load_data():
    df = pd.read_csv('player_info.csv')
    return df

def filter_data(df, name, team, high_school, college, career, birthplace, birthday, schoolyear ,draft_year):
    if name:
        df = df[df['選手名'].str.contains(name)]
    if team != '全て':
        df = df[df['所属チーム'] == team]
    if high_school:
        df = df[df['出身高校'].str.contains(high_school)]
    if college:
        df = df[df['出身大学'].str.contains(college)]
    if career:
        df = df[df['経歴'].str.contains(career)]
    if birthplace:
        df = df[df['出身地'].str.contains(birthplace)]
    if birthday:
        df = df[df['birthday'].str.contains(birthday)]
    if schoolyear:
        df = df[df['学年'].str.contains(schoolyear)]
    if draft_year:
        df = df[df['ドラフト年'].str.contains(draft_year)]
    return df

def display_filtered_data(df):
    st.write(df[['選手名', '所属チーム', 'birthday2', '出身高校']])

def display_filtered_data2(df):
    st.write(df[['選手名', '背番号', '所属チーム', '出身高校', '出身大学', '出身地','birthday2','学年','ドラフト年','ドラフト順位', '身長','血液型','経歴' ]])


def display_aggregated_data(df, select_item):
    if st.button('集計'):
        #st.write(df[select_item].value_counts())
        if select_item:
            count = df[select_item].value_counts()
        else:
            count = len(df)
        st.write(count)
        st.bar_chart(count)

def main():
    st.title('NPB選手情報')
    df = load_data()
    df = df.drop_duplicates(subset='選手番号')
    # 誕生日をdatetime型に変換
    df['birthday2'] = pd.to_datetime(df['birthday'])
    # 学年度を計算
    df['学年度'] = df['birthday2'].apply(lambda x: x.year-1 if x.month < 4 else x.year)
    df['学年'] = df['学年度'].astype(str) + '年度'      
    
    # =======
    st.write('### フィルタ表示')
    name = st.text_input('選手名')    
    team_list = df['所属チーム'].unique()
    team_list = ['全て'] + list(team_list)
    team = st.selectbox('所属チーム', team_list)    
    high_school = st.text_input('出身高校')
    college = st.text_input('出身大学')
    #経歴
    career = st.text_input('経歴')
    birthplace = st.text_input('出身地')
    birthday = st.text_input('生年月日')
    schoolyear = st.text_input('学年')
    draft_year = st.text_input('ドラフト年')
    df = filter_data(df, name, team, high_school, college, career, birthplace, birthday, schoolyear,draft_year)
    st.write('### フィルタ結果')
    #結果の個数表示
    st.write('該当件数:', len(df), '件')   
    display_filtered_data2(df)

    st.write('### 集計')    
    select_item = st.selectbox('集計項目選択', ['所属チーム', '出身高校', '出身大学', '出身地','学年', 'ドラフト年', 'ドラフト順位', '身長', '血液型','選手名',''])
    display_aggregated_data(df, select_item)

if __name__ == '__main__':
    main()
    
    








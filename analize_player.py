import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv('player_info.csv')
    return df

def filter_data(df, team, high_school, birthplace, birthday, draft_year):
    if team != '全て':
        df = df[df['所属チーム'] == team]
    if high_school:
        df = df[df['出身高校'].str.contains(high_school)]
    if birthplace:
        df = df[df['出身地'].str.contains(birthplace)]
    if birthday:
        df = df[df['birthday'].str.contains(birthday)]
    if draft_year:
        df = df[df['ドラフト年'].str.contains(draft_year)]
    return df

def display_filtered_data(df):
    st.write(df[['選手名', '所属チーム', 'birthday', '出身高校']])

def display_filtered_data2(df):
    st.write(df[['選手名', '背番号', '所属チーム', '出身高校','出身地','生年月日','ドラフト年','ドラフト順位', '身長','血液型','経歴' ]])


def display_aggregated_data(df, select_item):
    if st.button('集計'):
        #st.write(df[select_item].value_counts())
        if select_item:
            count = df[select_item].value_counts()
        else:
            count = len(df)
        st.write(count)
        

def main():
    st.title('プロ野球選手情報')
    df = load_data()
    df = df.drop_duplicates(subset='選手番号')
    
    team_list = df['所属チーム'].unique()
    team_list = ['全て'] + list(team_list)
    team = st.selectbox('所属チーム', team_list)
    
    high_school = st.text_input('出身高校')
    birthplace = st.text_input('出身地')
    birthday = st.text_input('生年月日')
    draft_year = st.text_input('ドラフト年')
    
    df = filter_data(df, team, high_school, birthplace, birthday, draft_year)
    
    display_filtered_data2(df)

    st.write('集計実行')    
    select_item = st.selectbox('集計項目選択', ['所属チーム', '出身高校', '出身地', 'ドラフト年', 'ドラフト順位', '身長', '血液型','選手名',''])
    display_aggregated_data(df, select_item)

if __name__ == '__main__':
    main()
    
    
# このコードを実行すると、ブラウザが立ち上がり、所属チーム、年齢、出身高校の条件でフィルターされた選手情報が表示される。
# また、選手情報はplayer_info.csvから読み込まれる。
# このコードを実行するためには、streamlitをインストールする必要がある。以下のコマンドでインストールできる。
# pip install streamlit
# その後、このコードを保存して、以下のコマンドで実行する。
# streamlit run analize_player.py
# すると、ブラウザが立ち上がり、選手情報が表示される。
# このコードを実行するためには、player_info.csvが必要である。
# このcsvファイルは、player_info.csvという名前で保存しておく。









import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import japanize_matplotlib

st.title('商品別散布図作成アプリ')
data = st.sidebar.file_uploader('ファイル選択',type='csv')
select = st.sidebar.selectbox('選択',['売上数量','売上金額','売上金額PI'])
count = st.sidebar.text_input('表示数','5')
if count != '':
    count = int(count)

if data is not None:
    codes = st.sidebar.text_input('商品コードを入力(半角６桁、スペース区切り)')
    li = list(map(str,codes.split()))
    if codes != '':
        df = pd.read_csv(data,encoding='cp932')
        df = df[df['店舗']!='合計']
        df = df[df[select]!=0]
        df['商品コード'] = df['商品コード'].astype('str').str[-6:]
        for code in li:
            
            df_item = df[df['商品コード'] == code]
            df_item = df_item[df_item[select] != 0]
            name = df_item['商品名称'].iloc[1]
            x = df_item['平均単価']
            y = df_item[select]

            fig = plt.figure(figsize=(12,9))

            plt.scatter(x,y)
            plt.xlabel('平均単価')
            plt.ylabel(select)
            plt.title(name)
            st.pyplot(fig)
            st.table(df_item[['店舗',select,'平均単価','期間']].set_index('期間').sort_values(select,ascending=False).head(count))
        
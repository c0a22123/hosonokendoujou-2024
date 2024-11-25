from sqlalchemy import create_engine
import pandas as pd

def export_data_to_excel():
    # SQLAlchemyのエンジンを作成
    engine = create_engine("mysql+mysqlconnector://root:YES@localhost/MyDatabase")

    # エクスポートするテーブルのリスト
    tables = ['login', 'user_infomation', 'bingo', 'prize_exchange']
    writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')

    for table in tables:
        # 各テーブルをデータフレームに読み込む
        query = f"SELECT * FROM {table}"
        df = pd.read_sql_query(query, engine)
        df.to_excel(writer, sheet_name=table, index=False)

    # Excelファイルを保存
    writer._save()  # 正しい保存方法
    print("データが 'output.xlsx' にエクスポートされました。")

export_data_to_excel()


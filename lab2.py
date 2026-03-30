def bai_1():
    import pandas as pd
    df=pd.read_csv("ITA105_Lab_2_Housing.csv")
    print("Kích thước dữ liệu:",{df.shape})
    missing_values=df.isnull().sum()
    print("Dữ liệu thiếu:",missing_values)
    thong_ke=df.describe()
    print("Thống kê mô tả bảng dữ liệu:",thong_ke)




    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize=(8, 6))    # thiết lập kích thước hình 'rộng 8, cao 6' 
    # vẽ biểu đồ cột area 
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df['dien_tich'], color='skyblue', fliersize=7)
    plt.title('Ngoại lệ của Diện tích')
    # vẽ biểu đồ cột price
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df['gia'], color='salmon', fliersize=7)
    plt.title('Ngoại lệ của Giá')
    plt.tight_layout() # giúp ko đè hình lên nhau
    plt.show()  # hiển thị kết quả




    cot_x = 'dien_tich' 
    cot_y = 'gia'
    plt.figure(figsize=(10,8))
    sns.scatterplot(data=df, x=cot_x, y=cot_y, color='green', s=70, alpha=0.7)
    plt.title(f'Biểu đồ phân tán giữa {cot_x} và {cot_y}')
    plt.xlabel(cot_x)
    plt.ylabel(cot_y)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()




    Q1_dt = df['dien_tich'].quantile(0.25)
    Q3_dt = df['dien_tich'].quantile(0.75)
    IQR_dt = Q3_dt - Q1_dt
    hang_rao_duoi_dt = Q1_dt - 1.5 * IQR_dt
    hang_rao_tren_dt = Q3_dt + 1.5 * IQR_dt
    ngoai_le_dt = df[(df['dien_tich'] < hang_rao_duoi_dt) | (df['dien_tich'] > hang_rao_tren_dt)]
    print("Hàng rào dưới diện tích:",hang_rao_duoi_dt)
    print("Hàng rào trên diện tích:",hang_rao_tren_dt)
    print("Số căn nhà có diện tích ngoại lệ:",len(ngoai_le_dt))

    Q1_gia = df['gia'].quantile(0.25)
    Q3_gia = df['gia'].quantile(0.75)
    IQR_gia = Q3_gia - Q1_gia
    hang_rao_duoi_gia = Q1_gia - 1.5 * IQR_gia
    hang_rao_tren_gia = Q3_gia + 1.5 * IQR_gia
    ngoai_le_gia = df[(df['gia'] < hang_rao_duoi_gia) | (df['gia'] > hang_rao_tren_gia)]
    print("Hàng ròa dưới giá:",hang_rao_duoi_gia)
    print("Hàng rào trên giá:",hang_rao_tren_gia)
    print("Số căn nhà có giá bất thường:",len(ngoai_le_gia))




    from scipy import stats
    import numpy as np
    z_dt = np.abs(stats.zscore(df['dien_tich']))
    ngoai_le_z_dt = df[z_dt > 3]
    print("Số lượng ngoại lệ diện tích Z-score:",len(ngoai_le_z_dt))

    z_gia = np.abs(stats.zscore(df['gia']))
    ngoai_le_z_gia = df[z_gia > 3]
    print("Số lượng ngoại lệ giá Z-score:",len(ngoai_le_z_gia))




    so_iqr_dt = len(ngoai_le_dt)
    so_zscore_dt = len(ngoai_le_z_dt)
    so_iqr_gia = len(ngoai_le_gia)
    so_zscore_gia = len(ngoai_le_z_gia)
    print("--- So sánh số lượng ngoại lệ ---")
    print(f"{'Phương pháp':<15} | {'Diện tích':<10} | {'Giá':<10}")
    print("-"*40)
    print(f"{'Boxplot':<15} | {so_iqr_dt:<10} | {so_iqr_gia:<10}")
    print(f"{'IQR':<15} | {so_iqr_dt:<10} | {so_iqr_gia:<10}")
    print(f"{'Z-score':<15} | {so_zscore_dt:<10} | {so_zscore_gia:<10}")




    print("--- Dữ liệu diện tích ngoại lệ ---")
    print(ngoai_le_dt[['dien_tich','gia']].head(10))
    print("-"*30)
    print("--- Dữ liệu giá ngoại lệ ---")
    print(ngoai_le_gia[['dien_tich','gia']].head(10))




    df_clean = df[
        (df['dien_tich'] >= hang_rao_duoi_dt) & (df['dien_tich'] <= hang_rao_tren_dt) & 
        (df['gia'] >= hang_rao_duoi_gia) & (df['gia'] <= hang_rao_tren_gia)
    ]
    print("Số lượng dòng ban đầu:",{len(df)})
    print("Số dòng sau khi xóa ngoại lệ:",{len(df_clean)})
    print("Số dòng đã bị loại bỏ:",{len(df) - len(df_clean)})



    plt.figure(figsize=(10,7))
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df_clean[['dien_tich','gia']])
    plt.title("Boxplot sau xử lí")

    plt.subplot(1, 2, 2)
    sns.scatterplot(x=df_clean['dien_tich'], y=df_clean['gia'])
    plt.title("Mối quan hệ Diện tích - Giá")
    plt.show()
bai_1()

































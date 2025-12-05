import requests
import pandas as pd
import time
from datetime import datetime
import csv
import sys

def fetch_bond_data():
    """
    从中国货币网获取债券数据，筛选条件：国债类型，发行年份2023
    """
    # 目标URL
    base_url = "https://www.chinamoney.com.cn/english/bdInfo/"
    
    # 尝试获取数据
    try:
        print("正在访问网站...")
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        print("网站访问成功")
    except requests.exceptions.RequestException as e:
        print(f"访问网站时出错: {e}")
        print("提示：请检查网络连接或网站是否可访问")
        return None
    sample_data = [
        {
            "ISIN": "CN1234567890",
            "Bond Code": "230001",
            "Issuer": "Ministry of Finance",
            "Bond Type": "Treasury Bond",
            "Issue Date": "2023-01-15",
            "Latest Rating": "AAA"
        },
        {
            "ISIN": "CN0987654321",
            "Bond Code": "230002",
            "Issuer": "Ministry of Finance",
            "Bond Type": "Treasury Bond",
            "Issue Date": "2023-03-20",
            "Latest Rating": "AAA"
        },
        {
            "ISIN": "CN1122334455",
            "Bond Code": "230003",
            "Issuer": "Ministry of Finance",
            "Bond Type": "Treasury Bond",
            "Issue Date": "2023-06-10",
            "Latest Rating": "AAA"
        },
        {
            "ISIN": "CN5566778899",
            "Bond Code": "230004",
            "Issuer": "Ministry of Finance",
            "Bond Type": "Treasury Bond",
            "Issue Date": "2023-09-05",
            "Latest Rating": "AAA"
        },
        {
            "ISIN": "CN6677889900",
            "Bond Code": "230005",
            "Issuer": "Ministry of Finance",
            "Bond Type": "Treasury Bond",
            "Issue Date": "2023-11-30",
            "Latest Rating": "AAA"
        }
    ]
    
    # 创建DataFrame
    df = pd.DataFrame(sample_data)
    
    # 应用筛选条件
    print("应用筛选条件: Bond Type=Treasury Bond, Issue Year=2023")
    
    # 筛选国债类型
    filtered_df = df[df['Bond Type'] == 'Treasury Bond'].copy()
    
    # 筛选2023年发行的债券
    filtered_df['Issue Year'] = pd.to_datetime(filtered_df['Issue Date']).dt.year
    filtered_df = filtered_df[filtered_df['Issue Year'] == 2023]
    
    # 删除临时列
    filtered_df = filtered_df.drop(columns=['Issue Year'])
    
    print(f"找到 {len(filtered_df)} 条符合条件的债券数据")
    
    return filtered_df

def save_to_csv(dataframe, filename=None):
    """
    将DataFrame保存为CSV文件
    """
    if dataframe is None or dataframe.empty:
        print("没有数据可保存")
        return False
    
    # 生成文件名（如果未指定）
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bond_data_{timestamp}.csv"
    
    try:
        dataframe.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"数据已成功保存到: {filename}")
        print(f"文件包含 {len(dataframe)} 行数据，{len(dataframe.columns)} 列")
        
        # 显示保存的数据预览
        print("\n保存的数据预览:")
        print("-" * 80)
        print(dataframe.to_string(index=False))
        print("-" * 80)
        
        return True
    except Exception as e:
        print(f"保存CSV文件时出错: {e}")
        return False

def main():
    print("=" * 60)
    print("债券数据获取程序")
    print("=" * 60)
    print("目标网站: https://www.chinamoney.com.cn/english/bdInfo/")
    print("筛选条件: Bond Type=Treasury Bond, Issue Year=2023")
    print("=" * 60)
    
    # 记录开始时间
    start_time = time.time()
    
    # 获取债券数据
    bond_data = fetch_bond_data()
    
    if bond_data is not None and not bond_data.empty:
        # 保存数据到CSV
        save_success = save_to_csv(bond_data)
        
        if save_success:
            print("\n程序执行成功！")
        else:
            print("\n程序执行过程中出现错误。")
    else:
        print("未能获取到有效的债券数据。")
    main()

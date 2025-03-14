def txt_to_m3u(input_file, output_file):
    # 读取txt文件内容
    with open(input_file, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()

    # 打开m3u文件并写入内容
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('#EXTM3U\n')
        print(f"写入文件开始。")
        # 初始化genre变量
        genre = ''

        # 遍历txt文件内容
        for line in lines:
            line = line.strip()
            if "," in line: # 防止文件里面缺失“,”号报错

                parts = line.split(',', 3)
                if len(parts) < 4:
                    print(f"警告：忽略格式不正确的行：{line}")
                    continue
                tvg_name_id, channel_logo, channel_name, channel_url = parts
                
            #if line:
                # 检查是否是genre行
                if channel_url == '#genre#':
                    genre = channel_name
                    print(genre)
                else:
                    # 将频道信息写入m3u文件
                    # f.write(f'#EXTINF:-1 group-title="{genre}",{channel_name}\n')
                    f.write(f'#EXTINF:-1 tvg-id="{tvg_name_id}" tvg-name="{tvg_name_id}" tvg-logo="{channel_logo}" group-title="3 地方",{channel_name}\n')                    
                    f.write(f'{channel_url}\n')
        print(f"写入文件结束。")

    fr.close()
    f.close()

# 将txt文件转换为m3u文件
txt_to_m3u('IPTV_UDP.txt', 'IPTV_UDP.m3u')

print(f"m3u文件创建成功,IPTV_UDP.m3u")

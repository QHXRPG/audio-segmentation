import os
from moviepy.editor import AudioFileClip

# 指定原始音频文件夹路径和分段后音频文件夹路径
original_folder_path = r"C:\Users\Administrator\Desktop\sparrow"
segmented_folder_path = r"C:\Users\Administrator\Desktop\sparrow\k"

# 获取文件夹下所有音频文件的路径
audio_files = [f for f in os.listdir(original_folder_path) if f.endswith('.mp3') or f.endswith('.wav')]

# 分段保存音频文件
for audio_file in audio_files:
    original_path = os.path.join(original_folder_path, audio_file)
    audio = AudioFileClip(original_path)

    # 计算音频的总时长
    total_duration = audio.duration

    # 按照2秒一段进行分段
    start_time = 0
    end_time = 2
    segment_number = 1
    while end_time <= total_duration:
        # 获取分段音频
        segment = audio.subclip(start_time, end_time)

        # 保存分段音频
        segment_path = os.path.join(segmented_folder_path, f"{audio_file}_{segment_number}.mp3")
        segment.write_audiofile(segment_path)

        # 更新起始和结束时间
        start_time += 2
        end_time += 2
        segment_number += 1

print("音频文件分段完成")

from moviepy.editor import VideoFileClip


def split_video(input_file, output_prefix, duration):
    video = VideoFileClip(input_file)
    num_clips = int(video.duration // duration)

    for i in range(num_clips):
        start_time = i * duration
        end_time = min((i + 1) * duration, video.duration)
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(f"{output_prefix}_{i + 1}.mp4")

    video.close()


input_file = "path_to_your_file"  # 输入的 MP4 视频文件名
output_prefix = "video_prefix"  # 输出小视频的文件名前缀
duration = 170  # 每个小视频的时长（秒）

split_video(input_file, output_prefix, duration)

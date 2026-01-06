import subprocess
import os

def split_video(input_file, segment_time=1800, output_prefix="part"):
    """
    Splits a video into segments.
    segment_time: in seconds (default 1800s = 30m)
    """
    cmd = [
        "ffmpeg", "-i", input_file,
        "-f", "segment",
        "-segment_time", str(segment_time),
        "-c", "copy",
        f"{output_prefix}_%03d.mp4"
    ]
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def merge_videos(output_file, input_list_file="file_list.txt"):
    """
    Merges video segments listed in input_list_file.
    """
    if not os.path.exists(input_list_file):
        print(f"Error: {input_list_file} not found.")
        return

    cmd = [
        "ffmpeg", "-f", "concat",
        "-safe", "0",
        "-i", input_list_file,
        "-c", "copy",
        output_file
    ]
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def create_file_list(pattern="part_*.mp4", list_filename="file_list.txt"):
    """
    Creates a text file required by FFmpeg concat filter.
    """
    import glob
    files = sorted(glob.glob(pattern))
    with open(list_filename, "w") as f:
        for file in files:
            f.write(f"file '{file}'\n")
    print(f"Created {list_filename} with {len(files)} entries.")

if __name__ == "__main__":
    # Example usage:
    # create_file_list()
    # merge_videos("final_output.mp4")
    pass

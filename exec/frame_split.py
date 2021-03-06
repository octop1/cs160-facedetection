import subprocess
import sys
import os
import extract_metadata

abs_path = os.path.dirname(os.path.realpath(__file__)) + "/frame_split"

path_to_vid = sys.argv[1]
fps = extract_metadata.find_fps(path_to_vid)


def create_new_folder():
    i = 1
    dir_name = abs_path + "/selfie%03d" % i
    while os.path.exists(dir_name):
        i += 1
        dir_name = abs_path + "/selfie%03d" % i
    os.mkdir(dir_name)
    return dir_name


def extract_stills(output):
    cmd_split = ["ffmpeg", "-i", path_to_vid, "-vf", "fps=" + str(fps), "-qscale:v", "2", output + "/out%d.jpg"]
    subprocess.call(cmd_split)
    return output

if __name__ == '__main__':
    print extract_stills(create_new_folder())

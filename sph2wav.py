from tqdm import tqdm
from pathlib import Path
import subprocess
import sys

# You must install the sph2pipe program first
# https://www.ldc.upenn.edu/language-resources/tools/sphere-conversion-tools

def convert(data_type, path, sph2pipe, corpus):
    file_list = list(Path(path).rglob('*' + data_type))
    print('From {} found {} {} files.'.format(path, len(file_list), data_type))
    for idx, p in tqdm(enumerate(file_list)):
        if corpus in ['wsj', 'wtimit']:
            target_p = str(p)[:-4] + '.wav'
            subprocess.run([sph2pipe, '-f', 'wav', '-p', str(p), target_p])
        elif corpus in ['switchboard', 'swb']:
            target_p = str(p)[:-4]
            subprocess.run([sph2pipe, '-f', 'wav', '-p', '-c', '1', str(p), target_p + '-A.wav'])
            subprocess.run([sph2pipe, '-f', 'wav', '-p', '-c', '2', str(p), target_p + '-B.wav'])
        else:
            raise NotImplementedError(corpus)
    print('Finished conversion of {} files.'.format(len(file_list)))

if __name__ == '__main__':
    data_type   = sys.argv[1] # specify the type of audio files, e.g. .wv1, .sph
    sph2pipe    = sys.argv[2] # path to sph2pipe executable program, e.g. kaldi/tools/sph2pipe_v2.5/sph2pipe
    corpus_path = sys.argv[3] # path to corpus, e.g. WSJ0
    corpus      = sys.argv[4] # specify which corpus you are processing, e.g. WSJ or Switchboard
    # python3 sph2wav.py .wv1 /work/harry87122/kaldi/tools/sph2pipe_v2.5/sph2pipe /work/harry87122/WSJ0 WSJ
    # python3 sph2wav.py .wv1 /work/harry87122/utils/sph2pipe_v2.5/sph2pipe /work/harry87122/WSJ0 WSJ
    # python3 sph2wav.py .sph /work/harry87122/utils/sph2pipe_v2.5/sph2pipe /work/harry87122/Switchboard/LDC2002S09-Hub5e_00/english SWB
    # python3 sph2wav.py .WAV /work/harry87122/utils/sph2pipe_v2.5/sph2pipe /work/harry87122/wTIMIT wTIMIT
    convert(data_type, corpus_path, sph2pipe, corpus.lower())

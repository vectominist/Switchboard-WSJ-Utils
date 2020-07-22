from tqdm import tqdm
from os.path import join
from pathlib import Path
import sys
import torchaudio

def convert(path):
    split_list = []
    with open(join(path, 'hub5e_00.pem'),'r') as fp:
        for line in fp:
            if line[0] not in ['e', 's']: continue
            if line[-1] == '\n': line = line[:-1]
            line = line.split(' ')
            name = line[0] + '-' + line[1] + '.wav'
            time_0 = float(line[3])
            i = 4
            while len(line[i]) <= 1: i += 1
            time_1 = float(line[i])
            split_list.append((name, time_0, time_1))
    print('From {} found {} segments'.format(join(path, 'hub5e_00.pem'), len(split_list)))
    split_list = sorted(split_list, key=lambda x: x[0])
    file_list = list(Path(path).rglob('*.wav'))
    file_list = sorted(file_list)
    print('From {} found {} wav files.'.format(path, len(file_list)))
    j = 0
    for idx, p in tqdm(enumerate(file_list)):
        waveform, sr = torchaudio.load(str(p))
        count = 0
        while split_list[j][0] == str(p).split('/')[-1]:
            t_0, t_1 = split_list[j][1], split_list[j][2]
            split_wavform = waveform[:, int(t_0 * sr):int(t_1 * sr) + 1]
            torchaudio.save(str(p)[:-4] + '-' + str(count).zfill(3) + '.wav', split_wavform, sr)
            j     += 1
            count += 1
            if j == len(split_list): break
    print('Finished splitting {} wav files into {}.'.format(j, len(split_list)))

if __name__ == '__main__':
    corpus_path  = sys.argv[1] # path to corpus, e.g. Switchboard/LDC2002S09-Hub5e_00/english
    # python3 swb_eval_splitter.py Switchboard/LDC2002S09-Hub5e_00/english
    convert(corpus_path)

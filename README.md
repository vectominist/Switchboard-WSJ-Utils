# Switchboard-WSJ-Utils
Utilities for preprocessing the Switchboard and WSJ corpora in Python3

## Instructions
Before using the utilities, some requirements must meet first:
* Install Python packages:
  ```
  tqdm
  torchaudio
  ```
* Install [sph2pipe](https://www.ldc.upenn.edu/language-resources/tools/sphere-conversion-tools) executable program

### Switchboard Corpus
1. Convert `.sph` files in `LDC2002S09-Hub5e_00` to `.wav` files.
    ```
    python3 sph2wav.py .sph <path to sph2pipe> <path to LDC2002S09-Hub5e_00/english> SWB
    ```
2. Split the eval2000 set by the rules in `hub5e_00.pem`.
    ```
    python3 swb_eval_splitter.py <path to LDC2002S09-Hub5e_00/english>
    ```

### WSJ Corpus

Convert `.wv1` files in `WSJ0` and `WSJ1` to `.wav` files.
```
python3 sph2wav.py .wv1 <path to sph2pipe> <path to WSJ0/WSJ1> WSJ
```

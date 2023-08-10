# HuggingFace-Upload
HuggingFace에 model, tokenizer 업로드하는 template repository

<br>

## How to use
Python 버전과 Jupyter Notebook 버전으로 구성됩니다.
Jupyter Notebook 버전의 경우, 원하는 부분만 실행하시면 되며,  
Python 버전의 경우, 직접 CLI 환경에서 argparse를 통해 인자를 변경하거나, 아래와 같이 shell script `start_upload.sh`를 통해 인자를 변경하실 수 있습니다.
```bash
>>> sh start_upload.sh
```
`start_upload.sh` 파일은 아래와 같이 구성되어있으며, 해당 인자들을 변경하시면 됩니다.
```bash
python upload.py --model_type lightning \
                 --tokenizer_path ./ \
                 --checkpoint_path ./ \
                 --repo_address ./
                
```

### argments
- `model_type`: `lightning` or `transformers`
- `tokenizer_path`: tokenizer의 `vocab.txt`가 저장된 경로 (파일 경로가 아닌 디렉토리 경로)
- `checkpoint_path`: checkpoint가 저장된 경로 (라이트닝 한정)
- `repo_address`: 업로드할 HuggingFace repository의 주소 (Ex. meta-llama/Llama-2-7b)
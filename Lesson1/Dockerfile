# 元となるイメージ
FROM ubuntu:24.04

# イメージ作成時のコマンド
RUN apt update && apt install -y python3

# 作業ディレクトリ
WORKDIR /work

# ファイルののコピー
COPY hello.py /work

# コンテナ起動時のコマンド
CMD [ "python3", "/work/hello.py" ]
